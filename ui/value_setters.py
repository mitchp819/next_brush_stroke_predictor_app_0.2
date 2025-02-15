import tkinter as tk
from typing import Literal

class Variable:
    def __init__(self, default):
        self.default = default
        self.type = type(default)
        self._value = default
        self._observers = []
    
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
        self._value = new_value
    
    def increment(self, step):
        self._value += step
        print(self._value)

class ValueWidgetInterface:
    def __init__(self, variable, ):
        pass

class IncrementButton:
    def __init__(self, container:tk.Widget, variable:Variable, orientation: Literal["horizontal","vertical"] = "vertical", step = 1):
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
            down_btn.config(text = "<")
            down_btn.pack(side="right")
        if orientation == "vertical":
            up_btn.config(text="^")
            up_btn.pack()
            down_btn.config(text="v")
            down_btn.pack()

class NumberEntry:
    def __init__(self, container:tk.Widget, variable:Variable, max = 255, min = 0):
        vcmd = (container.register(self.validate_input), '%P')
        self._variable = variable
        self._value = variable.value
        self.entry_box = tk.Entry(
            container, 
            textvariable=self._value,  
            validate='key',
            validatecommand=vcmd
        )
        self.entry_box.pack()
        self.entry_box.insert(0,str(self._variable.value))

    @property 
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        self.entry_box.delete(0,tk.END)
        self._variable.value - new_value
        self.entry_box.insert(0, new_value)
        
    
    def validate_input(self, new_value):
        if new_value != "":
            self._variable.value = new_value
            print(type(new_value))
        return new_value.isdigit() or new_value == ""
    



