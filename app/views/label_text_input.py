import tkinter as tk

class LabelTextInput():
    def __init__(self, label_text:str, row:int, frame:tk.Frame) -> None:

        self.label = tk.Label(frame, width=20, text=label_text)
        self.label.grid(row=row, column=0, padx=5, pady=5, sticky='nsew')

        self.input = tk.Entry(frame, width=20)
        self.input.grid(row=row, column=1, padx=5, pady=5, sticky='nsew')
    
    def getResult(self):
        return self.input.get()
    
    def deleteResult(self):
        self.input.delete(0, tk.END)