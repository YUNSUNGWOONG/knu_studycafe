import tkinter as tk
from tkinter import messagebox
from seat_select import *
from start_page import *
from seat_select import *


class enter_room(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.option_add('*Font', '나눔스퀘어 19 bold')
        # 캔버스 생성
        self.canvas = tk.Canvas(self, width=979, height=680)    # 캔버스 크기 지정
        self.canvas.pack()
        self.canvas.bind("<Button-1>", lambda event: self.canvas_click(event))
        self.show_image("img\입실.png")
        
        
        def ref_username_entry_click(event):
            if self.ref_username.get() == "전화번호를 입력하세요(-제외)":
                self.ref_username.delete(0, tk.END)
        
        def ref_password_entry_click(event):
            if self.ref_password.get() == "비밀번호를 입력하세요.":
                self.ref_password.delete(0, tk.END)
                
        # 전화번호 입력
        self.ref_username = tk.Entry(self)
        self.ref_username.place(x=307, y=358, width=364, height=41)
        self.ref_username.insert(0, "전화번호를 입력하세요(-제외)")
        self.ref_username.bind('<Button-1>', ref_username_entry_click)
        
        # 패스워드 입력
        self.ref_password = tk.Entry(self)
        self.ref_username.place(x=307, y=433, width=364, height=41)
        self.ref_username.insert(0, "비밀번호를 입력하세요.")
        self.ref_username.bind('<Button-1>', ref_password_entry_click)
        
    def canvas_clicK(self, event):
        app = self.winfo_toplevel()
        if 20 <= event.x and event.x <= 101 and 23 <= event.y <= 103:
            from start_page import start_page
            app.start_page = start_page(app)
            app.show_frame("start_page")
        if 303 <= event.x and event.x <= 673 and 498 <= event.y <= 560:
            self.username = self.ref_username.get()
            self.password = self.ref_password.get()
            
            if self.check_membership():
                messagebox.showinfO("조회 성공", f"{self.username}님 환영합니다!")
                from seat_select import seat_select
                app.set_entry_value(self.username)
                app.seat_select = seat_select(app)
                app.show_frame("seat_select")
            else:
                messagebox.showerror("조회 실패", "등록되지 않은 사용자입니다.")
                
    def check_membership(self):
        try:
            with open("members.txt", "r") as file:
                for line in file:
                    stored_username, stored_password = line.strip().split(",")
                    if self.username == stored_username and self.password == stored_password:
                        return True
        except Exception as e:
            messagebox.showerror("Error", str(e))
        return False

    def show_image(self, image_path):
        image = Image.open(image_path)
        resized_image = image.resize((979,680), Image.Resampling.LANCZOS)
        self.img = ImageTk.PhotoImage(resized_image)
        self.canvas.create_image(0,0,anchor="nw", image=self.img)