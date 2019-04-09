import tkinter as tk


class PlayerDetails(tk.Frame):
    """"Player"""

    def __init__(self, parent, response_json):
        """Initialize Player"""

        tk.Frame.__init__(self, parent, width=800, height=800)
        self.grid(rowspan=2, columnspan=2)
        self.parent = parent
        self.first_name = response_json['first_name']
        self.last_name = response_json['last_name']
        self.date_of_birth = response_json['date_of_birth']
        self.position = response_json['position']
        self.height = str(response_json['height'])
        self.weight = str(response_json['weight'])
        self.player_number = str(response_json['player_number'])
        self.shoot = response_json['shoot']
        self._create_widgets()

    def _create_widgets(self):

        self._label_first_name = tk.Label(self, text="First Name: " + self.first_name)
        self._label_first_name.grid(row=1, column=0, padx=20)

        self._label_last_name = tk.Label(self, text="Last Name: " + self.last_name)
        self._label_last_name.grid(row=2, column=0, padx=20)

        self._label_date_of_birth = tk.Label(self, text="date_of_birth: " + self.date_of_birth)
        self._label_date_of_birth.grid(row=3, column=0, padx=20)

        self._label_position = tk.Label(self, text="Position: " + self.position)
        self._label_position.grid(row=4, column=0, padx=20)

        self._label_height = tk.Label(self, text="Height: " + self.height)
        self._label_height.grid(row=5, column=0, padx=20)

        self._label_weight = tk.Label(self, text="Weight: " + self.weight)
        self._label_weight.grid(row=6, column=0, padx=20)

        self._label_player_number = tk.Label(self, text="Player_Number: " + self.player_number)
        self._label_player_number.grid(row=7, column=0, padx=20)

        self._label_shoot = tk.Label(self, text="Shoot: " + self.shoot)
        self._label_shoot.grid(row=8, column=0, padx=20)
