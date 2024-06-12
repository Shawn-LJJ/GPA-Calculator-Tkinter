from tkinter import messagebox

GRADES = ('A+', 'A', 'B+', 'B', 'C+', 'C', 'D+', 'D', 'P')

class Data_Verifier():
    def __init__(self, data: dict, input_type: str) -> None:
        # (mod name, credit, grade)
        self.data: tuple = tuple((item[0], item[1][0], item[1][1]) for item in data.items())
        self.input_type = input_type
    
    def verify(self) -> bool:
        for i, mod in enumerate(self.data):
            if any(not bool(result) for result in mod):
                if self.input_type == 'ui':
                    messagebox.showwarning("Warning", "Please ensure all text inputs are filled up.")
                else:
                    messagebox.showwarning('Warning', f'Empty value(s) located at row {i + 1}')
                return False
            
            if not mod[0].isalnum():
                if self.input_type == 'ui':
                    messagebox.showwarning("Warning", "Module name must be in alphanumeric only.")
                else:
                    messagebox.showwarning('Warning', f'Module name {mod[0]} located at row {i + 1} is invalid. Must be alphanumeric.')
                return False
            
            if mod[2] not in GRADES:
                if self.input_type == 'ui':
                    messagebox.showwarning("Warning", f"Invalid grade inputted. Grade must be one of the following: {GRADES}")
                else:
                    messagebox.showwarning('Warning', f'The grade at row {i + 1} or under the module {mod[0]} is invalid. Grades must be one of the following: {GRADES}')
                return False
            
            if not mod[1].isnumeric() or mod[1] == '0':
                if self.input_type == 'ui':
                    messagebox.showwarning("Warning", "Credit must be a positive integer.")
                else:
                    messagebox.showwarning('Warning', f'The credit at row {i + 1} or under the module {mod[0]} is invalid. Must be a positive integer.')
                return False
        
        return True