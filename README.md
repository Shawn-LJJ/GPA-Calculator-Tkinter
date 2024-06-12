# GPA Calculator Tkinter app

This GPA calculator app is built with Python using Tkinter to allow anyone to enter their school subjects/modules and their respective credit and grades. 
This is a refresh of my GPA calculator app that I made few years back that only works in command line. 
This is just a random hobby project I made during my free time. 

This calculator utilise the 4.0 GPA scale to calculate the GPA, and this is the formula used to calculate the GPA:

$$(\sum_{i=1}^n C_i G_i)/(\sum_{i=1}^n C_i)$$

where $C_i$ is the module's credit and $G_i$ is the grade point obtained for the said module, and $n$ being the number of modules to calculate.

This is the grade mapping which determines which grade correspond to which grade point and is currently being used in this program:

| Grade | A+ | A | B+ | B | C+ | C | D+ | D | P |
|-------|----|---|----|---|----|---|----|---|---|
| **Grade Point** | 4 | 4 | 3.5 | 3 | 2.5 | 2 | 1.5 | 1 | 0.5 |

This app not only allows you to enter the details, but to also save the data in a json file. Also, and you can load the json file into the program so you don't have to enter the details again when you close and run the program. When you have the data entered or loaded, you can click on "Calculate GPA" button to calculate and return the result in a pop up message. 

These are the options available in the program:
1. Enter grades (another page that allows you to enter, edit, and remove data)
2. Load grades (opens up the field dialog to choose which json file to load)
3. Save grades (opens up the field dialog to determine where to save the json file)
4. Calculate GPA

## Instructions

Python has to be installed to run the program. And install Tkinter if need to. Run ```main.py``` located in this directory to get the program up and running. 

When entering the grades, ensure that all fields are filled up, and the module name must be in alphanumeric, credit must be a positive integer, and grades must be any of the grades listed above in the table. To edit a grade in the treeview, simply type the module name you want to edit and type a new credit and grade values. 
To delete a module, select the module in the treeview and click on delete.

## Improvements that can be done

1. Support more file format for "storing" the data, such as csv, xlsx, instead of just only json.
2. Ability to allow users to insert their own mapping of module grade to grade point since every education institution can have different grading system.