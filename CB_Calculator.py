# -*- coding: utf-8 -*-
"""
CornerBoard Calculator
Created on Tue Jan 24 12:24:00 2017

@author: Richard Brosius
"""
import os
from Tkinter import *
from ttk import Frame, Button, Style
from Parser import Backend_Manager




class Main_Window(Frame):
    
    def __init__(self, parent):
        Frame.__init__(self,parent)
        
        self.parent = parent

        path = os.getcwd()
        paper_table = 'Gauge_Data_csv.csv'
        liner_table = 'Liner_Table.csv'

        self.back_end = Backend_Manager(self.parent, paper_table, liner_table, path)
        self.initUI()
        
    def initUI(self):
        self.parent.title("CornerBoard Calculator")
        self.style = Style()
        self.style.theme_use("default")
        frame_1=self.parent

        Item_ent = Entry(frame_1)
        Calc_btn = Button(frame_1, text="Calculate", command=lambda: self.back_end.parse(Item_ent.get()))
        self.parent.clipboard_append(Item_ent.get())

        Glue_lbl = Label(frame_1, text="Glue")
        Paper_lbl = Label(frame_1, text="Paper")
        Liner_lbl = Label(frame_1, text="Liner")

        Warehouses = [("001", 1), ("LVS", 2)]
        whse = IntVar()
        rb_001 = Radiobutton(frame_1, text="001", padx = 20, variable=whse,
                                         command=lambda:self.switch(whse), value=1)

        rb_LVS = Radiobutton(frame_1, text="LVS", padx = 20, variable=whse,
                                         command=lambda:self.switch(whse), value=2)

        rb_001.grid(row = 8, sticky=W)
        rb_LVS.grid(row = 9, sticky=W)

        Glue_txt = Text(frame_1, height=1, width = 20)
        Paper_txt = Text(frame_1, height=1, width = 20)
        Liner_txt = Text(frame_1, height=1, width = 20)
        ItemDesc_txt = Text(frame_1, height=1, width= 30)

        Txt_dict = {'Glue':Glue_txt , 'Paper':Paper_txt, 'Liner':Liner_txt, 'Desc':ItemDesc_txt}
        self.back_end.set_text_dict(Txt_dict)
        Item_ent.grid(row = 0, rowspan=2)
        Calc_btn.grid(row=0, column = 1, rowspan=2)

        x = 1
        ItemDesc_txt.grid(row= 1 + x)
        Glue_lbl.grid(row=2 + x, column = 0, stick=W)
        Glue_txt.grid(row=2 + x, column = 1)
        Paper_lbl.grid(row=3 + x, column=0, stick=W)
        Paper_txt.grid(row=3 + x, column=1)
        Liner_lbl.grid(row=4 + x, column=0, stick=W)
        Liner_txt.grid(row=4 + x, column=1)

    def switch(self, var):
        self.back_end.switch_warehouse(var.get())




def main():
    root = Tk()
    root.geometry("350x250")
    app = Main_Window(root)
    root.mainloop()



    
if __name__ == '__main__':
    main()