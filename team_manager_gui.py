import tkinter as tk
from top_navbar_view import TopNavbarView


class TeamManager(tk.Frame):
    """Main Application for Team Manager"""

    def __init__(self, parent):
        """Initializes Main Application"""

        tk.Frame.__init__(self, parent)

        self._top_navbar_view = TopNavbarView(self, self._page_callback, self._page_popup_callback)
        # self._player = PlayerView(self, self._player_submit_callback)
        # self._staff = StaffView(self, self_staff_submit_callback)
        # self._bottom_navbar = BottomNavbarView(self, self.)

