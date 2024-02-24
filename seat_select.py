import tkinter as tk
from PIL import ImageTk, Image
from start_page import *
from tkinter import messagebox

class seat_select(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        
        # 캔버스 생성
        self.canvas = tk.Canvas(self, width=979, height=680)    # 캔버스 크기 지정
        