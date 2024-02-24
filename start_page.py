import tkinter as tk
from PIL import ImageTk, Image
from enter_room import *
from exit_room import *
from delay import *
from purchase import *

class start_page(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        
        # 캔버스 생성
        self.canvas = tk.Canvas(self, width=979, height=680) # 캔버스 크기 지정
        self.canvas.pack()
        self.canvas.bind("<Button-1>", lambda event: self.canvas_click(event))
        self.show_image("img\초기화면.png")
        
        
    def canvas_click(self, event):
        app = self.winfo_toplevel()
        if 134 <= event.x and event.x <= 230 and 227 <= event.y <= 347:
            app.enter_room = enter_room(app)    # enter_room을 생성하여 app에 할당
            app.show_frame("enter_room")
        if 256 <= event.x and event.x <= 352 and 227 <= event.y <= 347:
            app.exit_room = exit_room(app)
            app.show_frame("exit_room")
        if 369 <= event.x and event.x <= 465 and 227 <= event.y <= 347:
            app.delay = delay(app)
            app.show_frame("delay")
        if 134 <= event.x and event.x <= 465 and 410 <= event.y <= 507:
            app.purchase = purchase(app)
            app.show_frame("purchase")
            
    def show_image(self, image_path):
        image = Image.open(image_path)
        resized_image = image.resize((979, 680), Image.Resampling.LANCZOS)
        self.img = ImageTk.PhotoImage(resized_image)
        self.canvas.create_image(0,0,anchor="nw", image=self.img)
        