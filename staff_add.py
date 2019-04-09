import tkinter as tk


class StaffView(tk.Frame):
    """Staff"""

    def __init__(self, parent, _add_callback):
        """Initialize Player"""
        tk.Frame.__init__(self, parent, width=800, height=800)
        self.grid(rowspan=2, columnspan=2)
        self._parent = parent
        self._add_callback = _add_callback
        self._create_widgets()

    def _create_widgets(self):
        """creates widgets for Staff"""

        self._label = tk.Label(self, text="First Name:")
        self._label.grid(row=1, column=0, padx=20)

        self._label = tk.Label(self, text="Last Name:")
        self._label.grid(row=2, column=0, padx=20)

        self._label = tk.Label(self, text="Date of Birth:")
        self._label.grid(row=3, column=0, padx=20)

        self._label = tk.Label(self, text="Position:")
        self._label.grid(row=4, column=0, padx=20)

        self._label = tk.Label(self, text="Date Hired:")
        self._label.grid(row=5, column=0, padx=20)

        self._label = tk.Label(self, text="Previous Teams:")
        self._label.grid(row=6, column=0, padx=20)

        self.first_name = tk.Entry(self)
        self.first_name.grid(row=1, column=1)

        self.last_name = tk.Entry(self)
        self.last_name.grid(row=2, column=1)

        self.date_of_birth = tk.Entry(self)
        self.date_of_birth.grid(row=3, column=1)

        self.position = tk.Entry(self)
        self.position.grid(row=4, column=1)

        self.hire_date = tk.Entry(self)
        self.hire_date.grid(row=5, column=1)

        self.previous_team = tk.Entry(self)
        self.previous_team.grid(row=6, column=1)

        self._button = tk.Button(self,
                                 text="Submit",
                                 command=self._add_callback)
        self._button.grid(row=1, column=2, padx=20)
