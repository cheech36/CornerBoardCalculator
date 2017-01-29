# -*- coding: utf-8 -*-
"""
CornerBoard Calculator
Created on Tue Jan 24 12:24:00 2017

@author: Richard Brosius
"""

from Tkinter import *
from ttk import Frame, Button, Style



class Main_Window(Frame):
    
    def __init__(self, parent):
        Frame.__init__(self,parent)
        
        self.parent = parent
        self.initUI()
        
    def initUI(self):
        self.parent.title("CornerBoard Calculator")
        self.style = Style()
        self.style.theme_use("default")
        
        frame_1 = Frame(self, relief=RAISED, borderwidth=1, height=1)
        frame_1.pack(side=TOP, expand=True)

        frame_2 = Frame(self, height=1)
        frame_2.pack(expand=FALSE)
        self.pack(fill=BOTH, expand=TRUE)

        Item_txt = Text(frame_1, height=1, width = 20)
        Item_txt.pack(side=TOP, padx=5, pady=5)
        Calc_btn = Button(frame_1, text="Calculate")
        Calc_btn.pack(side=RIGHT, padx=5, pady=5)


        frame_3 = Frame(self, height=1)
        frame_3.pack(expand=TRUE)
        Glue_lbl = Label(frame_3, text="Glue")
        Glue_lbl.pack(side=TOP)
        Glue_txt = Text(frame_3, height=1, width = 20)
        Glue_txt.pack(side=RIGHT)


        frame_4 = Frame(self, height=1)
        frame_4.pack(expand=FALSE)
        Glue_lbl = Label(frame_4, text="Paper")
        Glue_lbl.pack(side=TOP)

        frame_5 = Frame(self, height=1)
        frame_5.pack(expand=FALSE)
        Glue_lbl = Label(frame_5, text="Liner")
        Glue_lbl.pack(side=LEFT)



def main():
    root = Tk()
    root.geometry("350x250")
    app = Main_Window(root)
    root.mainloop()
    
    
if __name__ == '__main__':
    main()
