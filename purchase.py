import tkinter as tk
from start_page import *
import tkinter.messagebox as messagebox
class purchase(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.option_add('*Font', '나눔스퀘어 19 bold')
        # 캔버스 생성
        self.canvas = tk.Canvas(self, width=979, height=680)    # 캔버스 크기 지정
        self.canvas.pack()
        self.canvas.bind("<Button-1>", lambda event: self.canvas_click(event))
        self.show_image("img\이용권구매.png")
        
        def ref_username_entry_click(event):
            if self.ref_username.get() == "전화번호를 입력하세요(-제외)":
                self.ref_username.delete(0, tk.END)
        
        def ref_password_entry_click(event):
            if self.ref_password.get() == "비밀번호를 입력하세요.":
                self.ref_password.delete(0, tk.END)
        
        # 전화번호 입력
        self.ref_username = tk.Entry(self)
        self.ref_username.place(x=307, y=336, width=364, height=41)
        self.ref_username.insert(0, "전화번호를 입력하세요(-제외)")
        self.ref_username.bind('<Button-1>', ref_username_entry_click)
        
        # 패스워드 입력
        self.ref_password = tk.Entry(self)
        self.ref_password.place(x=307, y=399, width=364, height=41)
        self.ref_password.insert(0, "비밀번호를 입력하세요.")
        self.ref_password.bind('<Button-1>', ref_password_entry_click)
        
    def canvas_click(self, event):
        app = self.winfo_toplevel()
        
        if 20 <= event.x and event.x <= 101 and 23 <= event.y <= 103:
            from start_page import start_page
            app.start_page = start_page(app)
            app.show_frame("start_page")
            
        if 304 <= event.x and event.x <= 671 and 456 <= event.y <= 516:
            self.username = self.ref_username.get()
            self.password = self.ref_password.get()
            
            if self.check_ticket(self.username):
                messagebox.showerror("오류", "이미 이용권이 등록된 사용자입니다.")
                return
            
            elif self.check_membership():
                messagebox.showinfo("조회 성공", f"{self.username}님 환영합니다!")
                from registration import registration
                app.set_entry_value(self.username)
                app.registration = registration(app)
                app.show_frame("registration")
                
            else:
                messagebox.showerror("조회 실패", "등록되지 않은 사용자입니다.")
        
        if 304<= event.x and event.x <= 671 and 529 <= event.y <= 591:
            def register():
                username = username_entry.get()
                password = password_entry.get()
                
                if len(username) != 11:
                    messagebox.showwarning("전화번호 오류", "올바른 전화번호인지 확인해주세요.")
                    return
                
                if username and password:   # username과 password에 값이 들어있으면
                    with open("members.txt", "r") as file:
                        for line in file:
                            stored_username, _ = line.split(",")
                            if username == stored_username:
                                messagebox.showerror("등록실패", "이미 존재하는 회원입니다.")
                                return
                    with open("members.txt", "a") as file:
                        file.write(f"{username},{password}\n")
                    messagebox.showinfo("등록성공", "회원으로 등록되셨습니다.")
                    register_window.destroy()
                    
                    
            def username_entry_click(event):
                if username_entry.get() == "전화번호를 입력하세요(-제외)":
                    username_entry.delete(0, tk.END)
            
            def password_entry_click(event):
                if password_entry.get() == "비밀번호를 입력하세요.":
                    password_entry.delete(0, tk.END)
            
            register_window = tk.Toplevel()
            register_window.geometry("400x200+820+100")
            
            username_label = tk.Label(register_window, text="사용자 비밀번호")
            username_label.pack()
            
            username_entry = tk.Entry(register_window, width=25)
            username_entry.pack()
            username_entry.insert(0, "전화번호를 입력하세요(-제외)")
            username_entry.bind('<Button-1>', username_entry_click)
            
            password_label = tk.Label(register_window, text="비밀번호")
            password_label.pack()
            
            password_entry = tk.Entry(register_window, width=25)
            password_entry.pack()
            password_entry.insert(0, "비밀번호를 입력하세요.")
            password_entry.bind('<Button-1>', password_entry_click)
            
            register_button = tk.Button(register_window, text="회원가입", command=register)
            register_button.pack()
            
    def check_ticket(self, username):
        try:
            with open("members_time.txt", "r") as file:
                for line in file:
                    member_username, tim = line.strip().split(",")
                    if member_username == username:
                        return True
        except Exception as e:
            messagebox.showerror("Error", str(e))
            
        return False
    
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
        resized_image = image.resize((979, 680), Image.Resampling.LANCZOS)
        self.img = ImageTk.PhotoImage(resized_image)
        self.canvas.create_image(0,0,anchor="nw", image=self.img)
    
    
    def next_frame(self):
        app = self.winfo_toplevel()
        app.set_entry_value(self.entry.get())   # Entry에서 입력한 값을 저장
        app.__parent__ == __parent__(app)       # frame2를 생성하여 app에 할당
        app.show_frame("__parent__")
        