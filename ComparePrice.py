#!/usr/bin/env python
#-*- coding:utf-8 -*-

import os, sys
import thread
import time
import btcchina
import bitstamp
import re
import traceback

try:
    from tkinter import *
except ImportError:  #Python 2.x
    PythonVersion = 2
    from Tkinter import *
    from tkFont import Font
    #Usage:showinfo/warning/error,askquestion/okcancel/yesno/retrycancel
    from tkMessageBox import *
    #Usage:f=tkFileDialog.askopenfilename(initialdir='E:/Python')
    #import tkFileDialog
    #import tkSimpleDialog
else:  #Python 3.x
    PythonVersion = 3
    from tkinter.font import Font
    from tkinter.messagebox import *
    #import tkinter.filedialog as tkFileDialog
    #import tkinter.simpledialog as tkSimpleDialog    #askstring()

RATE = 6.1086

def cal(self):
    while True:
        try:
            
            print "========================="
            
            s_str = bitstamp.get_data()
            c_str = btcchina.get_data()

            s_data = eval(s_str)
            s_data = s_data["bids"][:25]

            c_str = c_str[c_str.find("bid")-80*30:c_str.find("bid")]
            regex = re.compile(r'{"price":"(.*?)","totalamount":"(.*?)","type":"ask"}')
            c_data = regex.findall(c_str)
            c_data = c_data[-25:]

            print s_data
            print c_data
            
            s_price = [0,0,0,0,0]
            c_price = [0,0,0,0,0]
            s_totalamount = [0,0,0,0,0]
            c_totalamount = [0,0,0,0,0]
            for i in range(5):
                s_price[i] = float(s_data[i+4][0])
                c_price[i] = float(c_data[i+4][0])
                s_totalamount[i] = sum([float(s_data[i][1]),
                                  float(s_data[i+1][1]),
                                  float(s_data[i+2][1]),
                                  float(s_data[i+3][1]),
                                  float(s_data[i+4][1])])
                c_totalamount[i] = sum([float(c_data[i][1]),
                                  float(c_data[i+1][1]),
                                  float(c_data[i+2][1]),
                                  float(c_data[i+3][1]),
                                  float(c_data[i+4][1])])

                print s_price[i],"|",s_totalamount[i],"    ",c_price[i],"|",c_totalamount[i]
            gap = s_price[0] * 0.995 * RATE - c_price[0]
            gap_percent = gap / c_price[0] * 100
            SUM = min(s_totalamount[0], c_totalamount[0])
            print "GAP%:", gap_percent
            print "SUM:", SUM

            self.s_price_0["text"] = str(s_price[0])
            self.s_price_1["text"] = str(s_price[1])
            self.s_price_2["text"] = str(s_price[2])
            self.s_price_3["text"] = str(s_price[3])
            self.s_price_4["text"] = str(s_price[4])

            self.c_price_0["text"] = str(c_price[0])
            self.c_price_1["text"] = str(c_price[1])
            self.c_price_2["text"] = str(c_price[2])
            self.c_price_3["text"] = str(c_price[3])
            self.c_price_4["text"] = str(c_price[4])

            self.s_totalamount_0["text"] = str(s_totalamount[0])
            self.s_totalamount_1["text"] = str(s_totalamount[1])
            self.s_totalamount_2["text"] = str(s_totalamount[2])
            self.s_totalamount_3["text"] = str(s_totalamount[3])
            self.s_totalamount_4["text"] = str(s_totalamount[4])

            self.c_totalamount_0["text"] = str(c_totalamount[0])
            self.c_totalamount_1["text"] = str(c_totalamount[1])
            self.c_totalamount_2["text"] = str(c_totalamount[2])
            self.c_totalamount_3["text"] = str(c_totalamount[3])
            self.c_totalamount_4["text"] = str(c_totalamount[4])

            self.gap_percent["text"] = "%.5f %%" % gap_percent
            self.SUM["text"] = str(SUM)

            time.sleep(1)
            
        except:
            traceback.print_exc()


    

class Application_ui(Frame):
    #这个类仅实现界面生成功能，具体事件处理代码在子类Application中。
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master.title(u'交易所报价比价器')
        self.master.geometry('675x291')
        self.createWidgets()

    def createWidgets(self):
        self.top = self.winfo_toplevel()

        self.Label1Font = Font(font=(u'宋体',9))
        self.Label1 = Label(self.top, text=u'价差 %', anchor='w', font=self.Label1Font)
        self.Label1.place(relx=0.024, rely=0.11, relwidth=0.108, relheight=0.086)

        self.Label2Font = Font(font=(u'宋体',9))
        self.Label2 = Label(self.top, text='SUM', anchor='w', font=self.Label2Font)
        self.Label2.place(relx=0.178, rely=0.11, relwidth=0.096, relheight=0.086)

        self.Label3Font = Font(font=(u'宋体',9))
        self.Label3 = Label(self.top, text='Bitstamp', anchor='w', font=self.Label3Font)
        self.Label3.place(relx=0.391, rely=0.11, relwidth=0.108, relheight=0.086)

        self.Label4Font = Font(font=(u'宋体',9))
        self.Label4 = Label(self.top, text='Btcchina', anchor='w', font=self.Label4Font)
        self.Label4.place(relx=0.747, rely=0.11, relwidth=0.12, relheight=0.086)

        self.Label5Font = Font(font=(u'宋体',9))
        self.s_price_0 = Label(self.top, text='-', anchor='w', font=self.Label5Font)
        self.s_price_0.place(relx=0.308, rely=0.275, relwidth=0.132, relheight=0.086)

        self.Label6Font = Font(font=(u'宋体',9))
        self.s_price_1 = Label(self.top, text='-', anchor='w', font=self.Label6Font)
        self.s_price_1.place(relx=0.308, rely=0.412, relwidth=0.132, relheight=0.086)

        self.Label7Font = Font(font=(u'宋体',9))
        self.s_price_2 = Label(self.top, text='-', anchor='w', font=self.Label7Font)
        self.s_price_2.place(relx=0.308, rely=0.55, relwidth=0.132, relheight=0.086)

        self.Label8Font = Font(font=(u'宋体',9))
        self.s_price_3 = Label(self.top, text='-', anchor='w', font=self.Label8Font)
        self.s_price_3.place(relx=0.308, rely=0.687, relwidth=0.132, relheight=0.086)

        self.Label9Font = Font(font=(u'宋体',9))
        self.s_price_4 = Label(self.top, text='-', anchor='w', font=self.Label9Font)
        self.s_price_4.place(relx=0.308, rely=0.825, relwidth=0.132, relheight=0.086)

        self.Label10Font = Font(font=(u'宋体',9))
        self.s_totalamount_0 = Label(self.top, text='-', anchor='w', font=self.Label10Font)
        self.s_totalamount_0.place(relx=0.462, rely=0.275, relwidth=0.132, relheight=0.086)

        self.Label11Font = Font(font=(u'宋体',9))
        self.s_totalamount_1 = Label(self.top, text='-', anchor='w', font=self.Label11Font)
        self.s_totalamount_1.place(relx=0.462, rely=0.412, relwidth=0.132, relheight=0.086)

        self.Label12Font = Font(font=(u'宋体',9))
        self.s_totalamount_2 = Label(self.top, text='-', anchor='w', font=self.Label12Font)
        self.s_totalamount_2.place(relx=0.462, rely=0.55, relwidth=0.132, relheight=0.086)

        self.Label13Font = Font(font=(u'宋体',9))
        self.s_totalamount_3 = Label(self.top, text='-', anchor='w', font=self.Label13Font)
        self.s_totalamount_3.place(relx=0.462, rely=0.687, relwidth=0.132, relheight=0.086)

        self.Label14Font = Font(font=(u'宋体',9))
        self.s_totalamount_4 = Label(self.top, text='-', anchor='w', font=self.Label14Font)
        self.s_totalamount_4.place(relx=0.462, rely=0.825, relwidth=0.132, relheight=0.086)

        self.Label15Font = Font(font=(u'宋体',9))
        self.c_price_0 = Label(self.top, text='-', anchor='w', font=self.Label15Font)
        self.c_price_0.place(relx=0.652, rely=0.275, relwidth=0.132, relheight=0.086)

        self.Label16Font = Font(font=(u'宋体',9))
        self.c_price_1 = Label(self.top, text='-', anchor='w', font=self.Label16Font)
        self.c_price_1.place(relx=0.652, rely=0.412, relwidth=0.132, relheight=0.086)

        self.Label17Font = Font(font=(u'宋体',9))
        self.c_price_2 = Label(self.top, text='-', anchor='w', font=self.Label17Font)
        self.c_price_2.place(relx=0.652, rely=0.55, relwidth=0.132, relheight=0.086)

        self.Label18Font = Font(font=(u'宋体',9))
        self.c_price_3 = Label(self.top, text='-', anchor='w', font=self.Label18Font)
        self.c_price_3.place(relx=0.652, rely=0.687, relwidth=0.132, relheight=0.086)

        self.Label19Font = Font(font=(u'宋体',9))
        self.c_price_4 = Label(self.top, text='-', anchor='w', font=self.Label19Font)
        self.c_price_4.place(relx=0.652, rely=0.825, relwidth=0.132, relheight=0.086)

        self.Label20Font = Font(font=(u'宋体',9))
        self.c_totalamount_0 = Label(self.top, text='-', anchor='w', font=self.Label20Font)
        self.c_totalamount_0.place(relx=0.806, rely=0.275, relwidth=0.132, relheight=0.086)

        self.Label21Font = Font(font=(u'宋体',9))
        self.c_totalamount_1 = Label(self.top, text='-', anchor='w', font=self.Label21Font)
        self.c_totalamount_1.place(relx=0.806, rely=0.412, relwidth=0.132, relheight=0.086)

        self.Label22Font = Font(font=(u'宋体',9))
        self.c_totalamount_2 = Label(self.top, text='-', anchor='w', font=self.Label22Font)
        self.c_totalamount_2.place(relx=0.806, rely=0.55, relwidth=0.132, relheight=0.086)

        self.Label23Font = Font(font=(u'宋体',9))
        self.c_totalamount_3 = Label(self.top, text='-', anchor='w', font=self.Label23Font)
        self.c_totalamount_3.place(relx=0.806, rely=0.687, relwidth=0.132, relheight=0.086)

        self.Label24Font = Font(font=(u'宋体',9))
        self.c_totalamount_4 = Label(self.top, text='-', anchor='w', font=self.Label24Font)
        self.c_totalamount_4.place(relx=0.806, rely=0.825, relwidth=0.132, relheight=0.086)

        self.Label25Font = Font(font=(u'宋体',9))
        self.gap_percent = Label(self.top, text='-', anchor='w', font=self.Label25Font)
        self.gap_percent.place(relx=0.024, rely=0.275, relwidth=0.12, relheight=0.086)

        self.Label26Font = Font(font=(u'宋体',9))
        self.SUM = Label(self.top, text='-', anchor='w', font=self.Label26Font)
        self.SUM.place(relx=0.166, rely=0.275, relwidth=0.12, relheight=0.086)


class Application(Application_ui):
    #这个类实现具体的事件处理回调函数。界面生成代码在Application_ui中。
    def __init__(self, master=None):
        Application_ui.__init__(self, master)
        thread.start_new_thread(cal,(self,))


if __name__ == "__main__":
    top = Tk()
    Application(top).mainloop()
    try: top.destroy()
    except: pass


