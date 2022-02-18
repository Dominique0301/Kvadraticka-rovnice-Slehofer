from os.path import basename, splitext
import math
from sqlite3 import Row
import tkinter as tk
from tkinter import IntVar
import random
#from typing_extensions import IntVar
import numpy as np
from matplotlib import pyplot as plt
from tkinter.constants import END
from tkinter import messagebox, filedialog, colorchooser
import sympy as sym
#from typing_extensions import IntVar
#from xml.dom.minidom import Entity

class Application(tk.Tk):
    name = basename(splitext(basename(__file__.capitalize()))[0])
    name = "Kvadartická funkce"
    


    def __init__(self):
        super().__init__(className=self.name)
        self.title(self.name)
        self.bind("<Escape>", self.quit)
        self.lbl = tk.Label(self, text="")
        self.lbl.grid(row=1, column=2)
        
        self.lblx1 = tk.Label(self, text="")
        self.lblx1.grid(row=3,column=2)
        self.lblx2 = tk.Label(self, text="")
        self.lblx2.grid(row=5,column=2)

        #vstup a
        self.lbla = tk.Label(self, text="a =")
        self.lbla.grid(row=2, column=1)  
        self.a_vstup = tk.Entry(self,validate="key", validatecommand=(self.register(self.validate), "%P"))
        self.a_vstup.grid(row=2, column=2, padx=10, pady=10)

        #vstup b
        self.lblb = tk.Label(self, text="b =")
        self.lblb.grid(row=4, column=1)  
        self.b_vstup = tk.Entry(self,validate="key", validatecommand=(self.register(self.validate), "%P"))
        self.b_vstup.grid(row=4, column=2, padx=10, pady=10)

        #vstup c
        self.lblc = tk.Label(self, text="c =")
        self.lblc.grid(row=6, column=1)  
        self.c_vstup = tk.Entry(self, validate="key", validatecommand=(self.register(self.validate), "%P"))
        self.c_vstup.grid(row=6, column=2, padx=10, pady=10)


        self.btn=tk.Button(self, text="Diskriminant", command=self.diskriminant)
        self.btn.grid(row=8,column=2)
        self.btn2=tk.Button(self, text="vysledky", command=self.reseni)
        self.btn2.grid(row=9, column=2)
        self.geometry("400x500")

    """def deset(self):
        try:
            float(self.b_vstup.get())
            return True
        except ValueError:
            return False"""

    def validate(self, value):
        if len(value) == 0 or value.isnumeric():
            return True
        else:
            return False

    

    def diskriminant(self):
       self.d = (int(self.b_vstup.get())**2) - (4*int(self.a_vstup.get())*int(self.c_vstup.get()))
       self.lbl.config(text=self.d)


#pokud je diskriminant větší než 0
    def reseni(self):
        self.res1 = (-int(self.b_vstup.get())+math.sqrt(self.d)) / (2*int(self.a_vstup.get()))
        self.res2 = (-int(self.b_vstup.get())-math.sqrt(self.d)) / (2*int(self.a_vstup.get()))
        self.lblx1.config(text=self.res1)
        self.lblx2.config(text=self.res2)
        


        






app = Application()
app.mainloop()