import tkinter as tk


class StaffDetails(tk.Frame):
    """Staff"""

    def __init__(self, parent, response_json):
        """Initialize Staff"""

        tk.Frame.__init__(self, parent, width=800, height=800)
        self.grid(rowspan=2, columnspan=2)
        self._parent = parent
        self.first_name = response_json['first_name']
        self.last_name = response_json['last_name']
        self.date_of_birth = response_json['date_of_birth']
        self.position = response_json['position']
        self.date_hired = response_json['hire_date']
        self.previous_team = response_json['previous_team']
        self._create_widgets()

    def _create_widgets(self):
        """creates widgets for Staff"""

        self._label_first_name = tk.Label(self, text="First Name: " + self.first_name)
        self._label_first_name.grid(row=1, column=0, padx=20)

        self._label_last_name = tk.Label(self, text="Last Name: " + self.last_name)
        self._label_last_name.grid(row=2, column=0, padx=20)

        self._label_date_of_birth = tk.Label(self, text="Date of Birth: " + self.date_of_birth)
        self._label_date_of_birth.grid(row=3, column=0, padx=20)

        self._label_position = tk.Label(self, text="Position :" + self.position)
        self._label_position.grid(row=4, column=0, padx=20)

        self._label_date_hired = tk.Label(self, text="Date Hired: " + self.date_hired)
        self._label_date_hired.grid(row=5, column=0, padx=20)

        self._label_previous_team = tk.Label(self, text="Previous Teams: " + self.previous_team)
        self._label_previous_team.grid(row=6, column=0, padx=20)


