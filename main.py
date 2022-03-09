from calendar import c
from os.path import basename, splitext
import math
from sqlite3 import Row
import tkinter as tk
from tkinter import IntVar, StringVar
import random
from tokenize import String
import numpy as np
from matplotlib import markers, pyplot as plt
from tkinter.constants import END
from tkinter import messagebox, filedialog, colorchooser
from tkinter.messagebox import showerror
from tkinter.colorchooser import askcolor


class Application(tk.Tk):
    name = basename(splitext(basename(__file__.capitalize()))[0])
    name = "Kvadartická funkce"
    


    def __init__(self):
        super().__init__(className=self.name)
        self.title(self.name)
        self.bind("<Escape>", self.quit)

        self.fr = tk.Frame(self, highlightbackground="blue", highlightthickness=2)
        self.fr.grid(row=1, column=1)
        

        #vypsání diskriminantu
        self.d=None
        self.w = 1
        self.lbl = tk.Label(self, text="")
        self.lbl.grid(row=10, column=2)
        self.lbl_d = tk.Label(self, text="D =")
        self.lbl_d.grid(row=10, column=1)

       #vypsání výsledků 
        self.lblx1 = tk.Label(self, text="")
        self.lblx1.grid(row=11,column=2)
        self.lblx2 = tk.Label(self, text="")
        self.lblx2.grid(row=12,column=2)
        self.lbl_x1 = tk.Label(self, text="X1 =")
        self.lbl_x1.grid(row=11, column=1)
        self.lbl_x2 = tk.Label(self, text="X2 =")
        self.lbl_x2.grid(row=12, column=1)

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

        self.lblGraf=tk.Button(self, text="Zobrazit graf",command=self.linew)
        self.lblGraf.grid(row=8,column=3)
        self.btn=tk.Button(self, text="Diskriminant", command=self.validace)
        self.btn.grid(row=8,column=2)
        self.btn2=tk.Button(self, text="Výsledky", command=self.validace_x)
        self.btn2.grid(row=9, column=2)

        #nastavení pro graf
        self.mr = IntVar()
        self.m = tk.Checkbutton(self, text="Mřížka grafu", variable=self.mr)
        self.m.grid(row=2, column=4)
        self.x_label = tk.Entry(self)
        self.x_label.grid(row=3, column=4)
        self.y_label = tk.Entry(self)
        self.y_label.grid(row=4, column=4)
        self.xlbl = tk.Label(self, text="Popis osy X")
        self.xlbl.grid(row=3, column=3)
        self.ylbl = tk.Label(self, text="Popis osy Y")
        self.ylbl.grid(row=4, column=3)
        self.title = tk.Entry(self)
        self.title.grid(row=5,column=4)
        self.title_lbl = tk.Label(self, text="Název grafu")
        self.title_lbl.grid(row=5, column=3)
        self.w = tk.Entry(self, validate="key", validatecommand=(self.register(self.kontrola_tloustky),"%P"))
        self.w.grid(row=6, column=4)
        self.wlbl=tk.Label(self, text="Tloušťka grafu")
        self.wlbl.grid(row=6, column=3)

        self.geometry("600x500")

#možnost zadání desetinných čísel
    def desetinne(self, value):
        try:
            float(value)
        except:
            return False
        return True

#možnost zadání záporných čísel
    def nula(self, value):
        if value == "-":
            return True
        else:
            return False

#validace vstupu
    def validate(self, value):
        if len(value) == 0 or value.isnumeric() or self.desetinne(value) or self.nula(value):
            return True
        else:
            return False

    def kontrola_tloustky(self, value):
        if len(value) == 0 or value.isnumeric():
            return True
        else:
            return False
        
    

   

    def diskriminant(self):
       self.d = (float(self.b_vstup.get())**2) - (4*float(self.a_vstup.get())*float(self.c_vstup.get()))
       self.lbl.config(text=self.d)


#pokud je diskriminant větší než 0
    def reseni(self):
        self.res1 = (-float(self.b_vstup.get())+math.sqrt(self.d)) / (2*float(self.a_vstup.get()))
        self.res2 = (-float(self.b_vstup.get())-math.sqrt(self.d)) / (2*float(self.a_vstup.get()))
        self.lblx1.config(text=self.res1)
        self.lblx2.config(text=self.res2)

#pokud je diskriminant 0
    def reseni_nula(self):
        self.reseni_nul = -float(self.b_vstup.get()) / (2*float(self.a_vstup.get()))
        self.lblx1.config(text=self.reseni_nul)
        self.lblx2.config(text="")

#zvolí se vhodný popstup řešení
    def vysledek(self):
        if self.d == 0:
            self.reseni_nula()
        elif self.d > 0:
            self.reseni()
        else:
            messagebox.showerror("Nelze", "Rovnice nemá reálná řešení. Pravidlo D>=0")


    def change_color(self):
        colors = askcolor(title="Vyberte barvu grafu")
        self.c = colors[1]

    def graf_dve(self):
        self.change_color()
        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)
        self.x = np.linspace(self.res2, self.res1, 100)
       #self.y1 = self.res1**2
        self.y = (float(self.a_vstup.get())*(self.x**2))+(float(self.b_vstup.get())*self.x)+float(self.c_vstup.get())
        plt.plot(self.x, self.y, color=self.c, linewidth=self.w.get())
        plt.xlabel(self.x_label.get(), loc="right")
        plt.ylabel(self.y_label.get(), loc="top")
        plt.title(self.title.get())
        #plt.xlim(-self.res1,self.res2)
        #plt.ylim(-self.y,self.y)
        #plt.annotate("X1",(self.res2,self.y1))
        #plt.annotate("x2", (self.res1, self.y1))
        ax.spines['left'].set_position('center')
        ax.spines['bottom'].set_position('center')
        ax.spines['right'].set_color('none')
        ax.spines['top'].set_color('none')
        ax.xaxis.set_ticks_position('bottom')
        ax.yaxis.set_ticks_position('left')
        if self.mr.get() == 1:
            plt.grid()
        else:
            pass
        plt.show()


    def graf(self):
        if self.d == None:
             messagebox.showerror("Chyba", "Nelze zobrazit graf")
        elif self.d > 0:
            self.graf_dve()
        else:
            pass
        
          

#validace pro počet diskriminantu
    def validace(self):
        if self.a_vstup.get()=="" or self.b_vstup.get()=="" or self.c_vstup.get()=="":
            messagebox.showerror("chyba", "Nezazdali jste vstupní hondoty.")
        else:
            self.diskriminant()
#validace jestli můžu provést výpočet x1 a x2
    def validace_x(self):
        if self.d==None:
            messagebox.showerror("Chyba", "Nemáte vypočítaný diskriminant")
        else:
            self.vysledek()

    def linew(self):
        if self.w.get()=="":
            messagebox.showwarning("Pozor", "Musíte zadat tloušťku čáry grafu.")
        else:
            self.graf()






app = Application()
app.mainloop()