import tkinter as tk
from start_page import *
from PIL import ImageTk, Image
import tkinter.messagebox as messagebox
class exit_room(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.option_add('*Font', '나눔스퀘어 19 bold')
        # 캔버스 생성
        self.canvas = tk.Canvas(self, width=979, height=680)    # 캔버스 크기 지정
        self.canvas.pack()
        self.canvas.bind("<Button-1>", lambda event: self.canvas_click(event))
        self.show_image("img\퇴실.png")
        
        def ref_username_entry_click(event):
            if self.ref_username.get() == "전화번호를 입력하세요(-제외)":
                self.ref_username.delete(0, tk.END)
                
        # 전화번호 입력
        self.ref_username = tk.Entry(self)
        self.ref_username.place(x=307, y=358, width=364, height=41)
        self.ref_username.insert(0, "전화번호를 입력하세요(-제외)")
        self.ref_username.bind('<Button-1>', ref_username_entry_click)
        
    def canvas_click(self, event):
        app = self.winfo_toplevel()
        if 20 <= event.x and event.x <= 101 and 23 <= event.y <= 103:
            from start_page import start_page
            app.start_page = start_page(app)
            app.show_frame("start_page")
        if 303<=event.x and event.x <=674 and 417 <= event.y <= 480:
            self.username = self.ref_username.get()
            
            if self.check_username():
                answer = messagebox.askyesno("질문", f"{self.username}님 {delete_seat}번 좌석 퇴실 하시겠습니까?")
                if answer:
                    self.cancel_seat(self.username)
                else:
                    return
            else:
                messagebox.showerror("오류", f"{self.username}님 사용중인 좌석이 없습니다.")
                
    def check_username(self):
        try:
            with open("selected_seats.txt","r") as file:
                for line in file:
                    global delete_seat
                    stored_username, delete_seat = line.strip().split(",")
                    if self.username == stored_username:
                        return True
        except Exception as e:
            messagebox.showerror("Error", str(e))
        return False
    
    
    def show_image(self, image_path):
        image = Image.open(image_path)
        resized_image = image.resize((979, 680), Image.Resampling.LANCZOS)
        self.img = ImageTk.PhotoImage(resized_image)
        self.canvas.create_image(0,0,anchor="nw", image=self.img)
        
    def cancel_seat(self, username):
        selected_seat_info = self.get_selected_seat_info()
        seat = selected_seat_info[username]
        del selected_seat_info[username]
        self.save_selected_seat_info(selected_seat_info)
        messagebox.showinfo("퇴실완료", f"{username}님 {seat}번 좌석 퇴실처리 되었습니다.")
        # self.update_seat_buttons(selected_seat_info)
        
    def get_selected_seat_info(self):
        selected_seat_info = {}
        try:
            with open("selected_seats.txt", "r") as file:
                for line in file:
                    username, seat = line.strip().split(",")
                    selected_seat_info[username] = seat
        except Exception as e:
            messagebox.showerror("Error", str(e))
        
        return selected_seat_info
    
    def save_selected_seat_infO(self, selected_seat_info):
        try:
            with open("selected_seats.txt", "w") as file:
                for username, seat in selected_seat_info.items():
                    file.write(f"{username},{seat}\n")
        except Exception as e:
            messagebox.showerror("Error", str(e))
            