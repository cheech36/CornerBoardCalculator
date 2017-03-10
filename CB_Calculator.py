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
        Calc_btn = Button(frame_1, text="Calculate", width=33, command=lambda: self.back_end.parse(Item_ent.get()))
        self.parent.clipboard_append(Item_ent.get())

        Item_lbl = Label(frame_1, text="Item Code")
        Desc_lbl = Label(frame_1, text="Description")
        Glue_lbl = Label(frame_1, text="Glue")
        Paper_lbl = Label(frame_1, text="Paper")
        Liner_lbl = Label(frame_1, text="Liner")
        Blank_lbl2 = Label('')
        Blank_lbl3 = Label('')
        Warehouse_lbl = Label(text='Warehouse')

        whse = IntVar()
        rb_001 = Radiobutton(frame_1, text="001", padx = 20, variable=whse,
                                         command=lambda:self.switch(whse), value=1)

        rb_LVS = Radiobutton(frame_1, text="LVS", padx = 20, variable=whse,
                                         command=lambda:self.switch(whse), value=2)


        Glue_txt = Text(frame_1, height=1, width = 20)
        Paper_txt = Text(frame_1, height=1, width = 20)
        Liner_txt = Text(frame_1, height=1, width = 20)
        ItemDesc_txt = Text(frame_1, height=1, width= 20)

        Txt_dict = {'Glue':Glue_txt , 'Paper':Paper_txt, 'Liner':Liner_txt, 'Desc':ItemDesc_txt}
        self.back_end.set_text_dict(Txt_dict)


        offset = 3
        pad_x = 20

        Item_lbl.grid(row= 1, column = 0, stick=S+W, padx=pad_x, pady=5)
        Item_ent.grid(row = 1, rowspan=1)
        Item_ent.grid(row = 1, column=1, pady=5, stick=S)
        Calc_btn.grid(row=2, column = 0, columnspan=2, stick=E)
        Blank_lbl2.grid(row= offset)
        Desc_lbl.grid(row=1+offset, column=0, stick=S+W, padx=pad_x)
        ItemDesc_txt.grid(row= 1 + offset, column=1)
        Glue_lbl.grid(row=2 +offset, column = 0, stick=S+W, padx=pad_x)
        Glue_txt.grid(row=2 +offset, column = 1)
        Paper_lbl.grid(row=3 +offset, column=0, stick=W, padx=pad_x)
        Paper_txt.grid(row=3 +offset, column=1)
        Liner_lbl.grid(row=4 +offset, column=0, stick=W, padx=pad_x)
        Liner_txt.grid(row=4 +offset, column=1)
        Blank_lbl3.grid(row=5 + offset)
        Warehouse_lbl.grid(row=6+offset)
        rb_001.grid(row = 7 + offset, sticky=W)
        rb_LVS.grid(row = 8 + offset, sticky=W)


    def switch(self, var):
        self.back_end.switch_warehouse(var.get())


def main():
    root = Tk()
    root.geometry("295x250")
    app = Main_Window(root)
    root.mainloop()


if __name__ == '__main__':
    main()
