import tkinter as tk
from start_page import *
import datetime as dt

class registration(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        
        # 캔버스 생성
        self.canvas = tk.Canvas(self, width=979, height=680)    # 캔버스 크기 지정
        self.canvas.pack()
        self.canvas.bind("<Button-1>", lambda event: self.canvas_click(event))
        self.show_image("img\이용권등록.png")
        
        # 이전 프레임에서 전달된 값 가져오기(시작)
        app = self.winfo_toplevel()
        self.previous_value = app.get_entry_value()
        print("Previous Value: " + self.previous_value)
        # 이전 프레임에서 전달된 값 가져오기(끝)
        
        self.username = self.previous_value
    def calc_date(self, day):
        current_time = dt.datetime.now()
        due_date = current_time + dt.timedelta(days=day)
        str_due_date = due_date.strftime("%Y-%m-%d %H:%M:%S")
        self.save_time_info(str_due_date)
        
    def save_time_info(self, due_date):
        try:
            with open("members_time.txt", "a") as file:
                file.write(f"{self.username},{due_date}\n")
        except Exception as e:
            messagebox.showerror("Error", str(e))
    
    def canvas_click(self, event):
        app = self.winfo_toplevel()
        # 뒤로가기
        if 20 <= event.x and event.x <= 101 and 23 <= event.y <= 103:
            from start_page import start_page
            app.start_page = start_page(app)
            app.show_frame("start_page")
        # 상품구매
        if 103 <= event.x and event.x <= 307 and 322 <= event.y <= 385:
            answer = messagebox.askyesno("질문", "1일권을 선택하시겠습니까?")
            if answer:
                self.calc_date(1)
                messagebox.showinfo('이용권등록', '이용권 등록이 완료되었습니다.')
                answer2 = messagebox.askyesno("질문", "자리선택을 하시겠습니까?")
                if answer2:
                    # 자리이동
                    from seat_select import seat_select
                    app.seat_select = seat_select(app)
                    app.show_frame("seat_select")
                else:
                    from start_page import start_page
                    app.start_page = start_page(app)
                    app.show_frame("start_page")
        
        if 386 <= event.x and event.x <= 590 and 322 <= event.y <= 385:
            answer = messagebox.askyesno("질문", "3일권을 선택하시겠습니까?")
            if answer:
                self.calc_date(3)
                messagebox.showinfo('이용권등록', '이용권 등록이 완료되었습니다.')
                answer2 = messagebox.askyesno("질문", "자리선택을 하시겠습니까?")
                if answer2:
                    from seat_select import seat_select
                    app.seat_select = seat_select(app)
                    app.show_frame("seat_select")
                else:
                    from start_page import start_page
                    app.start_page = start_page(app)
                    app.show_frame("start_page")
                
        if 665 <= event.x and event.x <= 870 and 322 <= event.y <= 385:
            answer = messagebox.askyesno("질문", "7이리권을 선택하시겠습니까?")
            if answer:
                self.calc_date(7)
                messagebox.showinfo('이용권등록','이용권 등록이 완료되었습니다.')
                answer2 = messagebox.askyesno("질문", "자리선택을 하시겠습니까?")
                if answer2:
                    from seat_select import seat_select
                    app.seat_select = seat_select(app)
                    app.show_frame("seat_select")
                else:
                    from start_page import start_page
                    app.start_page = start_page(app)
                    app.show_frame("start_page")
        
        if 103 <= event.x and event.x <= 307 and 495 <= event.y <= 558:
            answer = messagebox.askyesno("질문", "한달권을 선택하시겠습니까?")
            if answer:
                self.calc_date(30)
                messagebox.showinfo("이용권등록", "이용권 등록이 완료되었습니다.")
                answer2 = messagebox.askyesno("질문", "자리선택을 하시겠습니까?")
                if answer2:
                    from seat_select import seat_select
                    app.seat_select = seat_select(app)
                    app.show_frame("seat_select")
                else:
                    from start_page import start_page
                    app.start_page = start_page(app)
                    app.show_frame("start_page")
        
        if 386 <= event.x and event.x <= 590 and 495 <= event.y <= 558:
            answer = messagebox.askyesno("질문", "분기권을 선택하시겠습니까?")
            if answer:
                self.calc_date(90)
                messagebox.showinfo('이용권등록', '이용권 등록이 완료되었다.')
                answer2 = messagebox.askyesno("질문","자리선택을 하시겠습니까?")
                if answer2:
                    from seat_select import seat_select
                    app.seat_select = seat_select(app)
                    app.show_frame("seat_select")
                else:
                    from start_page import start_page
                    app.start_page = start_page(app)
                    app.show_frame("start_page")
        
        if 665 <= event.x and event.x <= 870 and 495 <= event.y <= 558:
            answer = messagebox.askyesno("질문", "반기권을 선택하시겠습니까?")
            if answer:
                self.calc_date(180)
                messagebox.showinfo('이용권등록', '이용권 등록이 완료되었습니다.')
                answer2 = messagebox.askyesno("질문","자리선택을 하시겠습니까?")
                if answer2:
                    from seat_select import seat_select
                    app.seat_select = seat_select(app)
                    app.show_frame("seat_select")
                else:
                    from start_page import start_page
                    app.start_page = start_page(app)
                    app.show_frame("start_page")
        
    def show_image(self, image_path):
        image = Image.open(image_path)
        resized_image = image.resize((979,680), Image.Resampling.LANCZOS)
        self.img = ImageTk.PhotoImage(resized_image)
        self.canvas.create_image(0,0,anchor="nw", image=self.img)
        