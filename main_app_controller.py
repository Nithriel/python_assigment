import tkinter as tk
from top_navbar_view import TopNavbarView
from page1_view import Page1View
from page2_view import Page2View
from staff_add import StaffView
from player_add import PlayerView
from details_staff import StaffDetails
from details_player import PlayerDetails
from bottom_navbar_view import BottomNavbarView
from tkinter import messagebox as tkMessageBox
from update_player import PlayerUpdate
import requests


class MainAppController(tk.Frame):
    """ Main Application for GUI """

    def __init__(self, parent):
        """ Initialize Main Application """
        tk.Frame.__init__(self, parent)

        self._top_navbar = TopNavbarView(self, self._page_callback)
        self._page1 = Page1View(self, self._page1_refresh_callback, self._page_1_delete_callback,
                                self._page1_add_callback, self._page1_details_callback, self._page1_update_callback)
        self._page2 = Page2View(self, self._page2_refresh_callback, self._page_2_delete_callback,
                                self._page2_add_callback, self._page2_details_callback, self._page2_update_callback)
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
        if self._curr_page != curr_page and self._curr_page == TopNavbarView.PAGE1:
            self._page1.grid_forget()
            self._page2.grid(row=1, columnspan=4)
            self._curr_page = TopNavbarView.PAGE2
        elif self._curr_page != curr_page and self._curr_page == TopNavbarView.PAGE2:
            self._page2.grid_forget()
            self._page1.grid(row=1, columnspan=4)
            self._curr_page = TopNavbarView.PAGE1

    def _page1_refresh_callback(self):
        """refresh page 1"""
        print("Refresh Page Staff")
        self._page1.set_form_data(self._call_requests('staff'))

    def _page2_refresh_callback(self):
        """refresh page 2"""
        print("Refresh Page Player")
        self._page2.set_form_data(self._call_requests('player'))

    def _page_1_delete_callback(self):
        """callback to delete staff member"""
        try:
            index = self._page1._list_box.curselection()[0]
            if tkMessageBox.askyesno('Verify', 'Really delete?'):
                # Delete item
                print("Index: " + str(index))
                staff_list = self._call_requests('staff')
                self._delete_id(staff_list[index]['id'])
                self._page1_refresh_callback()
        except:
            tkMessageBox.showerror("Error", "Invalid Selection")

    def _page_2_delete_callback(self):
        """callback to delete player member"""
        try:
            index = self._page2._list_box.curselection()[0]
            if tkMessageBox.askyesno('Verify', 'Really delete?'):
                # Delete item
                print("Index: " + str(index))
                player_list = self._call_requests('player')
                self._delete_id(player_list[index]['id'])
                self._page2_refresh_callback()
        except:
            tkMessageBox.showerror("Error", "Invalid Selection")

    def _page1_add_callback(self):
        """creates popup window to add staff"""
        self._popup_win = tk.Toplevel()
        self._popup = StaffView(self._popup_win, self._add_1_callback)

    def _page2_add_callback(self):
        """creates popup window to add player"""
        self._popup_win = tk.Toplevel()
        self._popup = PlayerView(self._popup_win, self._add_2_callback)

    def _page1_update_callback(self):
        """creates popup window with staff details to be updated"""
        self._popup_win = tk.Toplevel()
        self._popup = StaffView(self._popup_win, self._update_1_callback)
        try:
            index = self._page1._list_box.curselection()[0]
            print("Index: " + str(index))
            staff_list = self._call_requests('staff')
            response = requests.get("http://127.0.0.1:5000/team_manager/employee/" + str(staff_list[index]['id']))
            response_json = response.json()
            self._popup.first_name.insert(0, response_json['first_name'])
            self._popup.last_name.insert(0, response_json['last_name'])
            self._popup.date_of_birth.insert(0, response_json['date_of_birth'])
            self._popup.position.insert(0, response_json['position'])
            self._popup.hire_date.insert(0, response_json['hire_date'])
            self._popup.previous_team.insert(0, response_json['previous_team'])
            self._popup.id = response_json['id']
        except:
            self._popup_win.destroy()
            tkMessageBox.showerror("Error", "Invalid Selection")

    def _page2_update_callback(self):
        """creates popup window with player details to be updated"""
        self._popup_win = tk.Toplevel()
        self._popup = PlayerUpdate(self._popup_win, self._update_2_callback)
        try:
            index = self._page2._list_box.curselection()[0]
            print("Index: " + str(index))
            player_list = self._call_requests('player')
            response = requests.get("http://127.0.0.1:5000/team_manager/employee/" + str(player_list[index]['id']))
            response_json = response.json()
            self._popup.first_name.insert(0, response_json['first_name'])
            self._popup.last_name.insert(0, response_json['last_name'])
            self._popup.date_of_birth.insert(0, response_json['date_of_birth'])
            self._popup.position.insert(0, response_json['position'])
            self._popup.height.insert(0, response_json['height'])
            self._popup.weight.insert(0, response_json['weight'])
            self._popup.player_number.insert(0, response_json['player_number'])
            self._popup.shoot.insert(0, response_json['shoot'])
            self._popup.id = response_json['id']
        except:
            self._popup_win.destroy()
            tkMessageBox.showerror("Error", "Invalid Selection")


    def _update_1_callback(self):
        """recalls instance of staff details that's already been create from json"""
        first_name = self._popup.first_name.get()
        last_name = self._popup.last_name.get()
        date_of_birth = self._popup.date_of_birth.get()
        position = self._popup.position.get()
        hire_date = self._popup.hire_date.get()
        previous_team = self._popup.previous_team.get()
        staff_dict = {
            "first_name": first_name,
            "last_name": last_name,
            "date_of_birth": date_of_birth,
            "position": position,
            "hire_date": hire_date,
            "previous_team": previous_team,
            "type": "staff"
        }
        response = requests.put(url="http://127.0.0.1:5000/team_manager/employee/" + str(self._popup.id), json=staff_dict)
        if response.status_code == 200:
            self._popup_win.destroy()
        else:
            tkMessageBox.showerror("Error", "Invalid Input")
        self._page1_refresh_callback()

    def _update_2_callback(self):
        """recalls instance of player details that's already been create from json"""
        first_name = self._popup.first_name.get()
        last_name = self._popup.last_name.get()
        date_of_birth = self._popup.date_of_birth.get()
        position = self._popup.position.get()
        height = self._popup.height.get()
        weight = self._popup.weight.get()
        player_number = self._popup.player_number.get()
        shoot = self._popup.shoot.get()
        player_dict = {
            "first_name": first_name,
            "last_name": last_name,
            "date_of_birth": date_of_birth,
            "position": position,
            "height": height,
            "weight": weight,
            "player_number": player_number,
            "shoot": shoot,
            "type": "player"
        }
        response = requests.put(url="http://127.0.0.1:5000/team_manager/employee/" + str(self._popup.id), json=player_dict)
        if response.status_code == 200:
            self._popup_win.destroy()
        else:
            tkMessageBox.showerror("Error", "Invalid Input")
        self._page2_refresh_callback()

    def _close_popup_callback(self):
        """closes and destroys popup"""
        self._popup_win.destroy()

    def _quit_callback(self):
        """quit app"""
        self.quit()

    def _page1_details_callback(self):
        """pulls staff details from json and lists details of staff member"""
        try:
            index = self._page1._list_box.curselection()[0]
            print("Index: " + str(index))
            staff_list = self._call_requests('staff')
            response = requests.get("http://127.0.0.1:5000/team_manager/employee/" + str(staff_list[index]['id']))
            response_json = response.json()
            print(response_json)
            self._popup_win = tk.Toplevel()
            self._popup = StaffDetails(self._popup_win, response_json)
        except:
            tkMessageBox.showerror("Error", "Invalid Selection")

    def _page2_details_callback(self):
        """pulls player details from json and lists details of player member"""
        try:
            index = self._page2._list_box.curselection()[0]
            print("Index: " + str(index))
            player_list = self._call_requests('player')
            response = requests.get("http://127.0.0.1:5000/team_manager/employee/" + str(player_list[index]['id']))
            response_json = response.json()
            print(response_json)
            self._popup_win = tk.Toplevel()
            self._popup = PlayerDetails(self._popup_win, response_json)
        except:
            tkMessageBox.showerror("Error", "Invalid Selection")

    def _add_1_callback(self):
        """creates staff"""
        first_name = self._popup.first_name.get()
        last_name = self._popup.last_name.get()
        date_of_birth = self._popup.date_of_birth.get()
        position = self._popup.position.get()
        hire_date = self._popup.hire_date.get()
        previous_team = self._popup.previous_team.get()
        player_dict = {
            "first_name": first_name,
            "last_name": last_name,
            "date_of_birth": date_of_birth,
            "position": position,
            "hire_date": hire_date,
            "previous_team": previous_team,
            "type": "staff"
        }
        response = requests.post(url="http://127.0.0.1:5000/team_manager/employee", json=player_dict)
        if response.status_code == 200:
            self._popup_win.destroy()
        else:
            tkMessageBox.showerror("Error", "Invalid Input")
        self._page1_refresh_callback()

    def _add_2_callback(self):
        """creates player"""
        first_name = self._popup.first_name.get()
        last_name = self._popup.last_name.get()
        date_of_birth = self._popup.date_of_birth.get()
        position = self._popup.position.get()
        height = self._popup.height.get()
        weight = self._popup.weight.get()
        player_number = self._popup.player_number.get()
        shoot = self._popup.shoot.get()
        player_dict = {
            "first_name": first_name,
            "last_name": last_name,
            "date_of_birth": date_of_birth,
            "position": position,
            "height": height,
            "weight": weight,
            "player_number": player_number,
            "shoot": shoot,
            "type": "player"
        }
        response = requests.post(url="http://127.0.0.1:5000/team_manager/employee", json=player_dict)
        if response.status_code == 200:
            self._popup_win.destroy()
        else:
            tkMessageBox.showerror("Error", "Invalid Input")
        self._page2_refresh_callback()

    def _call_requests(self, entity_type):
        """shows list for each type"""
        response = requests.get("http://127.0.0.1:5000/team_manager/employee/all/" + entity_type)
        if response.status_code == 200:
            return response.json()

    @staticmethod
    def _delete_id(id):
        """deletes instance of entity"""
        requests.delete("http://127.0.0.1:5000/team_manager/employee/" + str(id))

if __name__ == "__main__":
    root = tk.Tk()
    MainAppController(root).pack(side=tk.TOP, fill=tk.BOTH, expand=True)
    root.mainloop()

