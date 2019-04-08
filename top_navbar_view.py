import tkinter as tk


class TopNavbarView(tk.Frame):
    """create Nav Bar"""

    Player = "player"
    Staff = "staff"
    All = "all"

    def __init__(self, parent, page_callback, page_popup_callback):
        tk.Frame.__init__(self, parent)
        self._parent = parent

        self._page_callback = page_callback
        self._page_popup_callback = page_popup_callback
        self._page = tk.IntVar()
        self._create_widgets()

    def _create_widgets(self):
        """creates widgets for nav bar"""

        tk.Label(self, text="Select Page:").grid(row=0, column=0)

        self.current_page = tk.IntVar()

        tk.Radiobutton(self,
                       text="Player",
                       variable=self.current_page,
                       command=self._page_callback,
                       value=TopNavbarView.Player).grid(row=0, column=1)

        tk.Radiobutton(self,
                       text="Coach",
                       variable=self.current_page,
                       command=self._page_callback,
                       value=TopNavbarView.Staff).grid(row=0, column=2)

        tk.Radiobutton(self,
                       text="All",
                       variable=self.current_page,
                       command=self._page_callback,
                       value=TopNavbarView.All).grid(row=0, column=3)

        self.current_page.set(TopNavbarView.Player)

        self._page.set(1)
