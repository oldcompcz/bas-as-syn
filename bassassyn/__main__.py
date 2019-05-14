import logging
import os
import sys
import tkinter as tk
from tkinter import filedialog
from tkinter import font

from bassassyn import utils


class TkApp(tk.Tk):

    def __init__(self):
        super().__init__()
        self.wm_title('bassassyn')

        self.open_dir = './samples/'
        self.save_dir = None
        self.basename = None

        self.token_mode = tk.StringVar()
        self.token_mode.set('keywords')
        # mode of displaying values after a $C token
        self.token_0c_mode = tk.StringVar()
        self.token_0c_mode.set('number')
        self.raw_bytes = tk.BooleanVar()
        self.raw_bytes.set(False)

        self.font_size = tk.IntVar()
        self.font_size.set(14)
        self.set_font_size()

        # menu bar
        menu = tk.Menu(self)

        # File menu
        self.menu_file = tk.Menu(menu, tearoff=False)
        self.menu_file.add('command', label='Open...', underline=0,
                           accelerator='Ctrl+O', command=self.open_file)
        self.menu_file.add('command', label='Save...', underline=0,
                           accelerator='Ctrl+S', command=self.save_file)
        self.menu_file.add('separator')
        self.menu_file.add('command', label='Quit', underline=0,
                           accelerator='Ctrl+Q', command=self.close)

        menu.add('cascade', label='File', underline=0, menu=self.menu_file)

        # View menu
        self.menu_view = tk.Menu(menu, tearoff=False)
        self.menu_view.add('radiobutton', label='Keywords', underline=0,
                           variable=self.token_mode, value='keywords',
                           accelerator='Ctrl+K', command=self.display)
        self.menu_view.add('radiobutton', label='Tokens Hex', underline=7,
                           variable=self.token_mode, value='tokens_hex',
                           accelerator='Ctrl+H', command=self.display)
        self.menu_view.add('radiobutton', label='Tokens Dec', underline=7,
                           variable=self.token_mode, value='tokens_dec',
                           accelerator='Ctrl+D', command=self.display)
        self.menu_view.add('separator')
        self.menu_view.add('radiobutton', label='Line number', underline=5,
                           variable=self.token_0c_mode, value='number',
                           accelerator='Ctrl+N', command=self.display)
        self.menu_view.add('radiobutton', label='Line address', underline=5,
                           variable=self.token_0c_mode, value='address',
                           accelerator='Ctrl+A', command=self.display)
        self.menu_view.add('separator')
        self.menu_view.add('checkbutton', label='Raw bytes', underline=0,
                           variable=self.raw_bytes, onvalue=True,
                           offvalue=False,
                           accelerator='Ctrl+R', command=self.display)

        menu.add('cascade', label='View', underline=0, menu=self.menu_view)

        # Font menu
        self.menu_font = tk.Menu(menu, tearoff=False)
        self.menu_font.add('radiobutton', label='Small', underline=0,
                           variable=self.font_size, value=11,
                           accelerator='Ctrl+F1', command=self.set_font_size)
        self.menu_font.add('radiobutton', label='Default', underline=0,
                           variable=self.font_size, value=14,
                           accelerator='Ctrl+F2', command=self.set_font_size)
        self.menu_font.add('radiobutton', label='Large', underline=0,
                           variable=self.font_size, value=17,
                           accelerator='Ctrl+F3', command=self.set_font_size)

        menu.add('cascade', label='Font', underline=1, menu=self.menu_font)

        self['menu'] = menu

        # keyboard events
        self.bind('<Control o>', self.open_file)
        self.bind('<Control s>', self.save_file)
        self.bind('<Control q>', self.close)
        self.bind('<Control k>', lambda event: self.menu_view.invoke(0))
        self.bind('<Control h>', lambda event: self.menu_view.invoke(1))
        self.bind('<Control d>', lambda event: self.menu_view.invoke(2))
        self.bind('<Control n>', lambda event: self.menu_view.invoke(4))
        self.bind('<Control a>', lambda event: self.menu_view.invoke(5))
        self.bind('<Control r>', lambda event: self.menu_view.invoke(7))
        self.bind('<Control F1>', lambda event: self.menu_font.invoke(0))
        self.bind('<Control F2>', lambda event: self.menu_font.invoke(1))
        self.bind('<Control F3>', lambda event: self.menu_font.invoke(2))

        # main text widget
        self.listing = tk.Text(self, width=80, height=25,
                               foreground='#eee', background='#111',
                               selectbackground='#242', state='disabled')
        for tag, color in utils.constants.COLORS.items():
            self.listing.tag_configure(tag, foreground=color)
        self.listing.grid()

        # if possible, open a file from a command line argument
        if sys.argv[1:] and os.path.isfile(sys.argv[1]):
            self.open_file(filename=sys.argv[1])
        else:
            logging.debug('No file passed as argument.')

    def open_file(self, event=None, filename=None):
        """Launch an 'Open' dialog. If valid data is detected, display
        the contents."""
        if not filename:
            dialog = filedialog.Open(self, initialdir=self.open_dir,
                                     filetypes=(('MZ* files', '*.mz*'),
                                                ('MZF files', '*.mzf'),
                                                ('All files', '*')))
            filename = dialog.show()

        if filename:
            filename = os.path.abspath(filename)
            self.open_dir, self.basename = os.path.split(filename)
            if not self.save_dir:
                self.save_dir = self.open_dir

            with open(filename, 'rb') as f:
                file_data = f.read()

            if file_data.startswith(b'MZS\x00') and len(file_data) == 98404:
                # MZS file
                params = [(4, 0x6bcf), (4, 0x9f9e), (4, 0xa3fa)]
            else:
                # MZF file
                params = [(128, 0)]

            for offset, start in params:
                try:
                    self.lines = list(utils.grab_data(file_data,
                                                      offset, start))
                except ValueError as err:
                    logging.info('{} Skipping start address {:#x}.'
                                 .format(err, start))
                else:
                    self.wm_title(self.basename + ' - bassassyn')
                    self.adr_to_num = {line['adr']: line['number']
                                       for line in self.lines}
                    self.display()
                    self.listing.focus()
                    break

    def save_file(self, event=None):
        """Launch a 'Save As' dialog."""
        if not self.basename or not self.listing.get('1.0', 'end').strip():
            return

        dialog = filedialog.SaveAs(self, initialdir=self.save_dir,
                                   initialfile='{}.txt'.format(
                                       os.path.splitext(self.basename)[0]),
                                   filetypes=(('Text files', '*.txt'),))
        filename = dialog.show()

        if filename:
            self.save_dir, self.basename = os.path.split(filename)
            with open(filename, 'w', encoding='utf-8', newline='\n') as f:
                f.write(self.listing.get('1.0', 'end'))

    def display(self):
        """Display content in the main text widget."""
        if not hasattr(self, 'lines'):
            return

        self.listing['state'] = 'normal'
        self.listing.delete('1.0', 'end')

        for line in self.lines:
            self.listing.insert('end', line['number'], 'line_number')
            self.listing.insert('end', ' ')

            if self.raw_bytes.get():
                # insert bytes repr without leading b' and trailing '
                self.listing.insert('end', repr(line['contents'])[2:-1])
            else:
                for chunk, tag in utils.text_repr(line['contents'],
                                                  self.adr_to_num,
                                                  token_mode=self.token_mode.get(),
                                                  token_0c_mode=self.token_0c_mode.get()):
                    self.listing.insert('end', chunk, tag)
            self.listing.insert('end', '\n')

        self.listing['state'] = 'disabled'

    def set_font_size(self):
        font.Font(name='TkFixedFont',
                  exists=True)['size'] = self.font_size.get()

    def close(self, event=None):
        """Close the application window."""
        self.destroy()


def main():
    logging.basicConfig(level=logging.INFO, format='%(message)s')
    app = TkApp()
    app.mainloop()


if __name__ == '__main__':
    main()
