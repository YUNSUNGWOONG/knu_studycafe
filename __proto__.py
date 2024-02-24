import tkinter as tk
from start_page import *

class __proto__(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.label = tk.Label(self, text="__proto__")
        self.label.pack()
        self.entry = tk.Entry(self)
        self.entry.pack()
        
        next_button = tk.Button(self, text="Next", command=self.next_frame)
        next_button.pack()
        
    def next_frame(self):
        app = self.winfo_toplevel()
        app.set_entry_value(self.entry.get())   # Entry에서 입력한 값을 저장
        app.__parent__=__parent__(app)          # frame2를 생성하여 app에 할당
        