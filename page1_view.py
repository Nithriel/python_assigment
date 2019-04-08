import tkinter as tk


class Page1View(tk.Frame):
    """ Page 1 """

    def __init__(self, parent, submit_callback):
        """ Initialize Page 1 """
        tk.Frame.__init__(self, parent, width=800, height=800)
        self._parent = parent

        self._submit_callback = submit_callback

        self._create_widgets()

    def _create_widgets(self):
        """ Creates the widgets for Page 1 """
        self._scrollbar = tk.Scrollbar(self, orient=tk.VERTICAL)
        self._label = tk.Label(self, text="Staff:")
        self._label.grid(row=1,column=0,padx=20)

        self._list_box = tk.Listbox(self)
        self._list_box.grid(row=2)

        self._scrollbar.config(command=self._list_box.yview)
        self._scrollbar.grid(row=2, column=3, sticky=tk.N + tk.S + tk.W + tk.E)

        self._button = tk.Button(self,
                                 text="Refresh",
                                 command=self._submit_callback)
        self._button.grid(row=3,padx=20)


    # def get_form_data(self):
    #     self.set_form_data()

    def set_form_data(self, data):
        self._list_box.delete(0, tk.END)
        for item in data:
            self._list_box.insert(tk.END, item['first_name'])



