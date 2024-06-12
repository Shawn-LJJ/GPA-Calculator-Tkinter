import json
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox, filedialog
from .views.label_text_input import LabelTextInput
from .functions.gpa_calculator import GPA_Calculator
from .functions.data_verifier import Data_Verifier

COLS = ['Module Name', 'Module Credit', 'Module Grade']

class App():
    def __init__(self, master: tk.Tk) -> None:

        # structure to store data:
        # module name : [credit, grade]
        self.data = {}

        self.master = master
        self.master.title = 'GPA Calculator App'
        self.master.resizable(False, False)

        # frames: one for home page, another for editing module details
        self.homePage = tk.Frame(master)
        self.homePage.grid_columnconfigure(0, weight=1, pad=1)

        self.editPage = tk.Frame(master)
        self.editPage.grid_columnconfigure(0, weight=1)
        self.editPage.grid_rowconfigure(0, weight=1)

        # home page frame
        self.homeLabel = tk.Label(self.homePage, text='GPA Calculator App')
        self.homeLabel.grid(row=0, column=0, padx=20, pady=10)

        self.editPageButton = tk.Button(self.homePage, text="Enter Grades", command=lambda : self.show_page(self.editPage))
        self.editPageButton.grid(row=1, column=0, padx=20, pady=5)

        self.loadButton = tk.Button(self.homePage, text="Load Grades", command=self.load_json)
        self.loadButton.grid(row=2, column=0, padx=20, pady=5)

        self.saveButton = tk.Button(self.homePage, text="Save Grades", command=self.save_json)
        self.saveButton.grid(row=3, column=0, padx=20, pady=5)

        self.calcGPAButton = tk.Button(self.homePage, text="Calculate GPA", command=self.calcGPA)
        self.calcGPAButton.grid(row=4, column=0, padx=20, pady=5)

        # edit grades page frame
        self.mod = LabelTextInput('Module Name', 0, self.editPage)                                      # module input field
        self.credit = LabelTextInput('Module Credit', 1, self.editPage)                                 # credit input field
        self.grade = LabelTextInput('Module Grade', 2, self.editPage)                                   # grade input field

        self.add_button = tk.Button(self.editPage, text="Add/Edit Module", command=self.add_mod)        # add module button
        self.add_button.grid(row=3, column=0, padx=5, pady=5, columnspan=2)

        self.mod_tree = ttk.Treeview(columns=COLS, show="headings")                                     # tree view for all the module details       
        vsb = ttk.Scrollbar(orient="vertical", command=self.mod_tree.yview)                             # vertical scroll bar
        hsb = ttk.Scrollbar(orient="horizontal", command=self.mod_tree.xview)                           # horizontal scroll bar
        self.mod_tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
        self.mod_tree.grid(column=0, row=4, columnspan=2, sticky='nsew', in_=self.editPage)
        vsb.grid(column=2, row=4, sticky='ns', in_=self.editPage)
        hsb.grid(column=0, row=5, columnspan=2, sticky='ew', in_=self.editPage)
        self.editPage.grid_columnconfigure(0, weight=1)

        for col in COLS:
            self.mod_tree.heading(col, text=col.title())

        self.delete_button = tk.Button(self.editPage, text="Delete Module", command=self.delete_mod)    # remove a module button
        self.delete_button.grid(row=6, column=0, columnspan=3, padx=5, pady=5)

        self.return_button = tk.Button(self.editPage, text="Back", command=lambda : self.show_page(self.homePage)) # button to go back to main menu
        self.return_button.grid(row=7, column=0, columnspan=3, padx=5, pady=5)

        # start showing home page
        self.current_page = None        # the current frame that the user is currently seeing
        self.show_page(self.homePage)
    
    # switch to the requested frame
    def show_page(self, page: tk.Frame):
        if self.current_page:
            self.current_page.pack_forget()
        self.current_page = page
        self.current_page.pack(fill="both", expand=True)
        self.update_mod_list()
    
    # pass through some validators and then add or edit the module
    def add_mod(self):

        results = {self.mod.getResult() : [self.credit.getResult(), self.grade.getResult().upper()]}
        verifier = Data_Verifier(results, 'ui')

        if verifier.verify():
            self.data.update(results)
            self.update_mod_list()

            self.mod.deleteResult()
            self.credit.deleteResult()
            self.grade.deleteResult()

    # delete the selected module
    def delete_mod(self):
        try:
            selected_mod = self.mod_tree.item(self.mod_tree.focus())['values'][0]
            self.data.pop(selected_mod)
            self.update_mod_list()
        except IndexError:
            messagebox.showwarning("Warning", "Please select a module to delete.")

    # update the treeview list
    def update_mod_list(self):
        self.mod_tree.delete(*self.mod_tree.get_children())

        for mod in self.data.keys():
            items = [mod, *self.data[mod]]
            self.mod_tree.insert('', 'end', values=items)
    
    # calculate gpa
    def calcGPA(self):
        if not len(self.data):
            return messagebox.showwarning('Warning', 'No data in memory to calculate GPA')
        calculator = GPA_Calculator(list(self.data.values()))
        messagebox.showinfo('GPA Calculation', f'Your GPA is {round(calculator.calculateGPA(), 3)}')
    
    # load json data file into memory
    def load_json(self):
        file_path = filedialog.askopenfilename(filetypes=[('JSON file', '.json')])
        if file_path:
            with open(file_path, 'r') as f:
                try:
                    data = json.load(f)
                    verifier = Data_Verifier(data, 'import')
                    if verifier.verify(): self.data = data
                except:
                    messagebox.showerror('Error reading data', 'Please check your data to ensure the format is correct.')
    
    # save the data to the specified destination
    def save_json(self):
        if not len(self.data):
            return messagebox.showwarning('Warning', 'No data in memory to save')
        
        file_path = filedialog.asksaveasfilename(filetypes=[('JSON file', '.json')])
        if file_path:
            with open(file_path, 'w') as f:
                json.dump(self.data, f, indent=4)