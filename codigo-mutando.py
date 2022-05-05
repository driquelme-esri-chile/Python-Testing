"""Codigo no funcional, falta que mute"""


from asyncore import write
import datetime
import pandas as pd
import locale

##########################################

import tkinter
from tkinter import messagebox
from tkinter import *
from tkinter import ttk

##########################################

from docxtpl import DocxTemplate
from itertools import groupby
from operator import itemgetter
from asyncore import write
import datetime
import pandas as pd
import locale
from openpyxl import load_workbook
import pandas.io.formats.excel
from openpyxl.styles.alignment import Alignment
from openpyxl.styles.colors import Color
from openpyxl.styles import PatternFill,Border,Side



# This code is to hide the main tkinter window
#win= Tk()

#win.geometry("750x200")
root = tkinter.Tk()
root.withdraw()

# Message Box
#messagebox.showinfo("Title", "Message")
root = Tk()
root.geometry('400x500')
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
root.mainloop()

#addin .net c# 











