import tkinter as tk


class BottomNavbarView(tk.Frame):
    """bottom nav bar"""

    def __init__(self, parent, add_popup_callback):
        """initialize bottom nav bar"""
        tk.Frame.__init__(self, parent)
        self._parent = parent

        self._add_popup_callback = add_popup_callback
        self._create_widgets()

    def _create_widgets(self):
        self._button = tk.Button(self,
                                 text="ADD",
                                 command=self._add_popup_callback)
        self._button.grid(column=1)
