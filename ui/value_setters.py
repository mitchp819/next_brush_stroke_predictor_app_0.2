import tkinter as tk
from tkinter import ttk
from typing import Literal

class Variable:
    """
    A class to represent a variable with observers and bounds checking.

    Attributes:
        default: The default value of the variable.
        max: The maximum allowed value of the variable.
        min: The minimum allowed value of the variable.
        type: The type of the variable.
        _value: The current value of the variable.
        _observers: A list of observers to notify on value changes.
    """

    def __init__(self, default, min=None, max=None):
        """
        Initialize the Variable with a default value, and optional min and max bounds.

        Args:
            default: The default value of the variable.
            min: The minimum allowed value of the variable (optional).
            max: The maximum allowed value of the variable (optional).
        """
        self.default = default
        self.max = max
        self.min = min
        self.type = type(default)
        self._value = default
        self._observers = []

    def register_observer(self, observer):
        """
        Register an observer to be notified on value changes.

        Args:
            observer: The observer to register.
        """
        self._observers.append(observer)

    def notify_observers(self, signal: Literal["any", "setter", "increment"] = "any"):
        for observer in self._observers:
            observer.update(self._value, signal)

    @property
    def value(self):
        if self._value == "":
            self._value = self.default
        return self._value

    @value.setter
    def value(self, new_value):
        if new_value == "":
            return
        if type(new_value) != self.type:
            new_value = int(new_value)
        if not self.in_bounds(new_value):
            return
        self._value = new_value
        self.notify_observers("setter")

    def increment(self, step):
        print(self._value)
        new_value = self._value + step
        if not self.in_bounds(new_value):
            return
        self._value = new_value
        self.notify_observers("increment")

    def in_bounds(self, new_value):
        if self.max is not None and new_value > self.max:
            return False
        if self.min is not None and new_value < self.min:
            return False
        return True

class IncrementButton:
    def __init__(self, container: tk.Widget, variable: Variable, orientation: Literal["horizontal", "vertical"] = "vertical", step=1):
        """
        Initialize the IncrementButton with a container, variable, orientation, and step.

        Args:
            container: The container to place the buttons in.
            variable: The variable to increment or decrement.
            orientation: The orientation of the buttons ("horizontal" or "vertical").
            step: The step to increment or decrement the variable by (default is 1).
        """
        up_btn = tk.Button(
            container,
            command=lambda: variable.increment(step)
        )
        down_btn = tk.Button(
            container,
            command=lambda: variable.increment(-step)
        )
        if orientation == "horizontal":
            up_btn.config(text=">")
            up_btn.pack(side="right")
            down_btn.config(text="<")
            down_btn.pack(side="right")
        if orientation == "vertical":
            up_btn.config(text="^")
            up_btn.pack()
            down_btn.config(text="v")
            down_btn.pack()

class NumberEntry:
    def __init__(self, container: tk.Frame, variable: Variable):
        vcmd = (container.register(self.validate_input), '%P')
        self.variable = variable
        self.variable.register_observer(self)
        self._value = variable.value
        self.entry_box = tk.Entry(
            container,
            textvariable=self.variable.value,
            validate='key',
            validatecommand=vcmd
        )
        self.entry_box.pack()
        self.entry_box.insert(0, str(self.variable.value))

    def validate_input(self, new_value):
        print(new_value)
        if new_value != "":
            self.variable.value = new_value
            self.variable.notify_observers("any")
        return new_value.isdigit() or new_value == ""

    def update(self, new_value, signal: Literal["any", "setter", "increment"]):
        """
        Updates are called when the Variable Class notifys observers.
        """
        if signal != "increment":
            return
        self.entry_box.delete(0, tk.END)
        self.entry_box.insert(0, new_value)

class SimpleSlider:
    def __init__(self, container: tk.Frame, variable: Variable, min: int = None, max: int = None):
        """
        Initialize the SimpleSlider with a container, variable, min, and max values.

        Args:
            container: The container to place the slider widget in.
            variable: The variable to bind to the slider widget.
            min: The minimum value of the slider (optional).
            max: The maximum value of the slider (optional).
        """
        self.set_min_max(variable, min, max)
        self.variable = variable
        self.variable.register_observer(self)
        self.int_var = tk.IntVar()
        self.int_var.set(variable.value)
        self.slider = ttk.Scale(
            container,
            variable=self.int_var,
            command= self.update_variable,
            from_=self.min,
            to=self.max
        )
        self.slider.pack()

    def update_variable(self, value):
        self.variable.value = self.int_var.get()
        self.variable.notify_observers('increment')

    def update(self, new_value, signal):
        self.int_var.set(new_value)
        #self.slider.update()

    def set_min_max(self, variable: Variable, min , max):
        if variable.max != None:
            self.max = int(variable.max)
        elif max:
            self.max = max
        else:
            raise ValueError("Simple Slider needs a max value")

        if variable.min != None:
            self.min = int(variable.min)
        elif min:
            self.min = min
        else:
            raise ValueError("Simple Slider needs a min value")


