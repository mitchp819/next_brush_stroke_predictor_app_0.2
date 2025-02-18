import tkinter as tk
from drawing_app import GreyScalePicker
from ui import Variable, ValueSetterPack
if __name__ == "__main__":
    test_root = tk.Tk()
    test_root.geometry("800x600")
    test_root.config(bg = 'blue')
    test_frame = tk.Frame(test_root)
    var = Variable(10, 0 ,255)


    ValueSetterPack(test_frame)
    
    
    test_frame.pack()
    test_root.mainloop()