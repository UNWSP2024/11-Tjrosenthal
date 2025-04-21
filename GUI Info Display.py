#Tanner Rosenthal
#4/9/25
#Show Info GUI

import tkinter

class MyGUI:
     def __init__(self):
         self.main_window = tkinter.Tk()

         self.info_label = tkinter.Label(self.main_window, text="")
         self.info_label.pack()

         self.quit_gui = tkinter.Button(self.main_window, text="Quit", command=self.main_window.quit)
         self.quit_gui.pack()

         def show_info():
           self.info_label.config(text="Tanner Rosenthal, 20174 Explorer Ct. N, Forest Lake, MN")

         button = tkinter.Button(self.main_window, text="Click Here!", command=show_info)
         button.pack()

         tkinter.mainloop()
my_gui = MyGUI()
