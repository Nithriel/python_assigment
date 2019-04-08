import tkinter as tk
from top_navbar_view import TopNavbarView
from page1_view import Page1View
from page2_view import Page2View
from bottom_navbar_view import BottomNavbarView
from popup_view import PopupView
import requests


class MainAppController(tk.Frame):
    """ Main Application for GUI """

    def __init__(self, parent):
        """ Initialize Main Application """
        tk.Frame.__init__(self, parent)

        self._top_navbar = TopNavbarView(self, self._page_callback, self._page_popup_callback)
        self._page1 = Page1View(self, self._page1_submit_callback)
        self._page2 = Page2View(self, self._page2_submit_callback)
        self._bottom_navbar = BottomNavbarView(self, self._quit_callback)

        self._top_navbar.grid(row=0, columnspan=4, pady=10)
        self._page1.grid(row=1, columnspan=4, pady=10)
        self._curr_page = TopNavbarView.PAGE1
        # Hide Page 2 by default
        self._bottom_navbar.grid(row=2, columnspan=4, pady=10)

        self._staff_list = self._call_requests('staff')
        self._page1.set_form_data(self._staff_list)
        self._player_list = self._call_requests('player')
        self._page2.set_form_data(self._player_list)

    def _page_callback(self):
        """ Handle Switching Between Pages """

        curr_page = self._top_navbar.curr_page.get()
        if (self._curr_page != curr_page and self._curr_page == TopNavbarView.PAGE1):
            self._page1.grid_forget()
            self._page2.grid(row=1, columnspan=4)
            self._curr_page = TopNavbarView.PAGE2
        elif (self._curr_page != curr_page and self._curr_page == TopNavbarView.PAGE2):
            self._page2.grid_forget()
            self._page1.grid(row=1, columnspan=4)
            self._curr_page = TopNavbarView.PAGE1

    def _page_popup_callback(self):
        self._popup_win = tk.Toplevel()
        self._popup = PopupView(self._popup_win, self._close_popup_callback)

    def _close_popup_callback(self):
        self._popup_win.destroy()

    def _page1_submit_callback(self):
        print("Refresh Page Staff")
        print(self._page1.set_form_data(self._call_requests('staff')))

    def _page2_submit_callback(self):
        print("Refresh Page Player")
        print(self._page1.set_form_data(self._call_requests('player')))

    def _quit_callback(self):
        self.quit()

    def _call_requests(self, entity_type):
        response = requests.get("http://127.0.0.1:5000/team_manager/employee/all/" + entity_type)
        if response.status_code == 200:
            return response.json()

if __name__ == "__main__":
    root = tk.Tk()
    MainAppController(root).pack(side=tk.TOP, fill=tk.BOTH, expand=True)
    root.mainloop()
