import tkinter as tk


class Page2View(tk.Frame):
    """ Page 2 """

    def __init__(self, parent, submit_callback):
        """ Initialize Page 2 """
        tk.Frame.__init__(self, parent)
        self._parent = parent

        self._submit_callback = submit_callback

        self._create_widgets()

    def _create_widgets(self):
        """ Creates the widgets for Page 2 """
        self._scrollbar = tk.Scrollbar(self, orient=tk.VERTICAL)
        self._label = tk.Label(self, text="Player:")
        self._label.grid(row=1, column=0, padx=20)

        self._list_box = tk.Listbox(self)
        self._list_box.grid(row=2)

        self._scrollbar.config(command=self._list_box.yview)
        self._scrollbar.grid(row=2, column=3, sticky=tk.N + tk.S + tk.W + tk.E)

        self._button = tk.Button(self,
                                 text="Refresh",
                                 command=self._submit_callback)
        self._button.grid(row=3, padx=20)

    # def get_form_data(self):
    #     return { "birthdate": self._entry_birthdate.get() }
    def set_form_data(self, data):
        self._list_box.delete(0, tk.END)
        for item in data:
            self._list_box.insert(tk.END, item['first_name'])




