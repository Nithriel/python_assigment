import tkinter as tk


class PlayerView(tk.Frame):
    """Player"""

    def __init__(self, parent, submit_callback):
        """Initialize Player"""
        tk.Frame.__init__(self, parent, width=800, height=800)
        self.grid(rowspan=2, columnspan=2)
        self._parent = parent
        self._submit_callback = submit_callback
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

        self._first_name = tk.Entry(self)
        self._first_name.grid(row=1, column=1)

        self._last_name = tk.Entry(self)
        self._last_name.grid(row=2, column=1)

        self._date_of_birth = tk.Entry(self)
        self._date_of_birth.grid(row=3, column=1)

        self._position = tk.Entry(self)
        self._position.grid(row=4, column=1)

        self._height = tk.Entry(self)
        self._height.grid(row=5, column=1)

        self._weight = tk.Entry(self)
        self._weight.grid(row=6, column=1)

        self._player_number = tk.Entry(self)
        self._player_number.grid(row=7, column=1)

        self._shoots = tk.Entry(self)
        self._shoots.grid(row=8, column=1)

        self._button = tk.Button(self,
                                 text="Submit",
                                 command=self._submit_callback)
        self._button.grid(row=1, column=2, padx=20)
