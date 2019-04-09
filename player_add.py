import tkinter as tk


class PlayerView(tk.Frame):
    """Player"""

    def __init__(self, parent, _add_callback):
        """Initialize Player"""
        tk.Frame.__init__(self, parent, width=800, height=800)
        self.grid(rowspan=2, columnspan=2)
        self._parent = parent
        self._add_callback = _add_callback
        self._create_widgets()

    def _create_widgets(self):
        """creates widgets for Player"""

        self._label = tk.Label(self, text="First Name:")
        self._label.grid(row=1, column=0, padx=20)

        self._label = tk.Label(self, text="Last Name:")
        self._label.grid(row=2, column=0, padx=20)

        self._label = tk.Label(self, text="Date of Birth:")
        self._label.grid(row=3, column=0, padx=20)

        self._label = tk.Label(self, text="Position:")
        self._label.grid(row=4, column=0, padx=20)

        self._label = tk.Label(self, text="Height:")
        self._label.grid(row=5, column=0, padx=20)

        self._label = tk.Label(self, text="Weight:")
        self._label.grid(row=6, column=0, padx=20)

        self._label = tk.Label(self, text="Player Number:")
        self._label.grid(row=7, column=0, padx=20)

        self._label = tk.Label(self, text="Shoots:")
        self._label.grid(row=8, column=0, padx=20)

        self.first_name = tk.Entry(self)
        self.first_name.grid(row=1, column=1)

        self.last_name = tk.Entry(self)
        self.last_name.grid(row=2, column=1)

        self.date_of_birth = tk.Entry(self)
        self.date_of_birth.grid(row=3, column=1)

        self.position = tk.Entry(self)
        self.position.grid(row=4, column=1)

        self.height = tk.Entry(self)
        self.height.grid(row=5, column=1)

        self.weight = tk.Entry(self)
        self.weight.grid(row=6, column=1)

        self.player_number = tk.Entry(self)
        self.player_number.grid(row=7, column=1)

        self.shoot = tk.Entry(self)
        self.shoot.grid(row=8, column=1)

        self._button = tk.Button(self,
                                 text="Submit",
                                 command=self._add_callback)
        self._button.grid(row=1, column=2, padx=20)
