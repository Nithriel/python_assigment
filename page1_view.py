import tkinter as tk


class Page1View(tk.Frame):
    """ Page 1 """

    def __init__(self, parent, submit_callback, delete_callback, add_callback, details_callback):
        """ Initialize Page 1 """
        tk.Frame.__init__(self, parent, width=800, height=800)
        self._parent = parent

        self._submit_callback = submit_callback
        self._add_callback = add_callback
        self._delete = delete_callback
        self._details_callback = details_callback

        self._create_widgets()

    def _create_widgets(self):
        """ Creates the widgets for Page 1 """
        self._scrollbar = tk.Scrollbar(self, orient=tk.VERTICAL)
        self._label = tk.Label(self)
        self._label.grid(row=1,column=0,padx=20)

        self._list_box = tk.Listbox(self)
        self._list_box.grid(row=2, ipadx=30, columnspan=2)

        self._scrollbar.config(command=self._list_box.yview)
        self._scrollbar.grid(row=2, column=4, sticky=tk.N + tk.S + tk.W + tk.E)

        self._add_button = tk.Button(self,
                                 text="Add",
                                 command=self._add_callback)
        self._add_button.grid(row=4, column=0, columnspan=1, sticky=tk.W + tk.E)

        self._update_button = tk.Button(self,
                                 text="Update",
                                 command=self._submit_callback)
        self._update_button.grid(row=4, column=1, columnspan=1, sticky=tk.W + tk.E)

        self._delete_button = tk.Button(self,
                                 text="Delete",
                                 command=self._delete)
        self._delete_button.grid(row=5, column=0, columnspan=1, sticky=tk.W + tk.E)

        self._details_button = tk.Button(self,
                                        text="Details",
                                        command=self._details_callback)
        self._details_button.grid(row=5, column=1, columnspan=1, sticky=tk.W + tk.E)

        self._refresh_button = tk.Button(self,
                                         text="Refresh",
                                         command=self._submit_callback)
        self._refresh_button.grid(row=7, columnspan=2, sticky=tk.E + tk.W)

    def set_form_data(self, data):
        self._list_box.delete(0, tk.END)
        for item in data:
            self._list_box.insert(tk.END, item['first_name'] + ' ' + item['last_name'] + ', ' + item['position'])



