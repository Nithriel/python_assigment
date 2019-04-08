import tkinter as tk
from top_navbar_view import TopNavbarView
from bottom_navbar_view import BottomNavbarView
from player_add import PlayerView


class TeamManagerController(tk.Frame):
    """Main Application for GUI"""

    def __init__(self, parent):
        """Initializes Main Application"""

        tk.Frame.__init__(self, parent)

        self._top_navbar_view = TopNavbarView(self, self._page_callback, self._page_popup_callback)
        self._player = PlayerView(self, self._player_submit_callback)
        # self._staff = StaffView(self, self_staff_submit_callback)
        self._bottom_navbar_view = BottomNavbarView(self, self.add_popup_callback)

        self._top_navbar_view.grid(row=0, columnspan=4, pady=10)
        self._player.grid(row=1, columnspan=4, pady=10)
        self._bottom_navbar_view.grid(row=2, columnspan=4, pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    TeamManagerController(root).pack(side=tk.TOP, fill=tk.BOTH, expand=True)
    root.mainloop()