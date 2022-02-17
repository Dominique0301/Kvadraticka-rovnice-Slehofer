from os.path import basename, splitext
import math
import tkinter as tk
from tkinter import IntVar
import random
#from typing_extensions import IntVar
import numpy as np
from matplotlib import pyplot as plt
from tkinter.constants import END
from tkinter import messagebox, filedialog, colorchooser
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
        #self.a_vstup = IntVar()
        self.a_vstup = tk.Entry(self)
        self.a_vstup.grid(row=2, column=2, padx=10, pady=10)
        #self.b_vstup = IntVar()
        self.b_vstup = tk.Entry(self)
        self.b_vstup.grid(row=4, column=2, padx=10, pady=10)
       # self.c_vstup = IntVar()
        self.c_vstup = tk.Entry(self)
        self.c_vstup.grid(row=6, column=2, padx=10, pady=10)
        self.btn=tk.Button(self, text="vysledek", command=self.diskriminant)
        self.btn.grid(row=8,column=2)
        self.geometry("400x500")

    

    def diskriminant(self):
       self.d = float((self.b_vstup.get()**2)) - float((4*self.a_vstup.get()*self.c_vstup.get()))
       self.lbl.config(text=self.d)

    def reseni(self):
        self.res1 = (-self.b_vstup.get()+math.sqrt(self.d)) / (2*self.a_vstup.get())
        self.res2 = (-self.b_vstup.get()-math.sqrt(self.d)) / (2*self.a_vstup.get())
        


        






app = Application()
app.mainloop()