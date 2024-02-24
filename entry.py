import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
from start_page import start_page


class SampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("knu_studycafe")
        self.geometry("970x680+350+140")

        self.entry_value = None # Entry에서 입력한 값을 저장할 변수
        self.current_frame = None # 현재 표시된 프레임을 저장할 변수

        self.start_page = start_page(self)
        self.enter_room = None
        self.seat_select = None #초기에는 frame2를 None으로 설정
        self.exit_room = None
        self.delay = None
        self.user_state = None
        self.purchase = None


        #메뉴바 생성
        menubar = tk.Menu(self)
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="관리자모드", command=self.admin_mode)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.exit)
        menubar.add_cascade(label="설정", menu=file_menu)
        self.config(menu=menubar)

        self.show_frame("start_page")

    def show_frame(self, frame_name):
        if self.current_frame is not None:
            self.current_frame.pack_forget() #현재 표시된 프레임 제거

        if frame_name == "start_page":
            frame = self.start_page
        elif frame_name == "enter_room":
            frame = self.enter_room
        elif frame_name == "seat_select":
            frame = self.seat_select
        elif frame_name == "exit_room":
            frame = self.exit_room
        elif frame_name == "delay":
            frame = self.delay
        elif frame_name == "user_state":
            frame = self.user_state
        elif frame_name == "purchase":
            frame = self.purchase
        elif frame_name == "registration":
            frame = self.registration
            
        frame.pack(fill=tk.BOTH, expand=True)
        self.current_frame = frame
        
    def get_entry_value(self):
        return self.entry_value
    
    def set_entry_value(self, value):
        self.entry_value = value
        
    def admin_mode(self):
        # 비밀번호 먼저 입력
        password = tk.TK()
        
        label = tk.Label(password, text="관리자 비밀번호를 입력하세요:")
        label.pack()
        
        entry = tk.Entry(password, show="*")
        entry.pack()
        
        def check_password():
            password_entry = entry.get()
            if password_entry == "admin":
                password.destory()
                mesaagebox.showinfo("성공", "관리자모드를 실행합니다.")
                
                # 회원정보를 읽어와서 딕셔너리 형태로 저장하는 함수
                def read_members(file_name):
                    members = {}
                    with open(file_name, 'r') as file:
                        for line in file:
                            line = line.strip()
                            if line:
                                member_id, data = line.split(',')
                                members[member_id] = data
                    return members
                
                # 회원정보를 비교하여 mixed_members 딕셔너리에 저장하는 함수
                def compare_members(mebers, members_time):
                    mixed_members = {}
                    for member_id, password in members.items():
                        if member_id in members_time:
                            expiration_date = memebers_time[member_id]
                            mixed_members[member_id] = (password, expiration_date)
                    return mixed_members
                
                # 회원 정보를 파일에 저장하는 함수
                def save_members(file_name, mixed_members):
                    with open(file_name, 'w') as file:
                        for member_id, (password, expiration_date) in mixed_members.items():
                            line = f"{member_id},{password},{expiration_date}\n"
                            file.write(line)

                
                # members.txt와 members_time.txt에서 회원 정보를 읽어옴
                members = read_members('members.txt')
                members_time = read_members('members_time.txt')
                
                # 회원 정보를 비교하여 mixed_members 딕셔너리에 저장
                mixed_members = compare_members(members, members_time)
                
                # mixed_members 딕셔너리의 회원 정보를 members_times_mixed.txt에 저장
                save_members('members_times_mixed.txt', mixed_members)
                
                # 회원정보를 읽어와서 딕셔너리 형태로 저장하는 함수
                def read_members_2(file_name):
                    members = {}
                    with open(file_name, 'r') as file:
                        for line in file:
                            line = line.strip()
                            if line:
                                member_id, password, expiration_date = line.split(',')
                                members[member_id] = (password, expiration_date)
                    return members
                
                # 좌석 정버를 읽어와서 딕셔너리 형태로 저장하는 함수
                def read_seats(file_name):
                    seats = {}
                    with open(file_name, 'r') as file:
                        for line in flie:
                            line = line.strip()
                            if line:
                                memeber_id, seat_number = line.split(',')
                                if memeber_id in seats:
                                    seats[memeber_id].append(seat_number)
                                else:
                                    seats[memeber_id] = [seat_number]
                    return seats
            
                # 회원 정보와 좌석정보를 비교하여 mixed_members 딕셔너리에 저장하는 함수
                def compare_members_2(members, seats):
                    mixed_members = {}
                    for memeber_id, (password, expiration_date) in members.items():
                        if memeber_id in seats:
                            seat_numbers = seats[memeber_id]
                            mixed_members[memeber_id] = (password, expiration_date, seat_numbers)
                    return mixed_members
            
                # 회원 정보를 파일에 저장하는 함수
                def save_members_2(file_name, mixed_members):
                    with open(file_name, 'w') as file:
                        for member_id, (password, expiration_date, seat_numbers) in mixed_members.items():
                            for seat_number in seat_numbers:
                                line = f"{member_id},{seat_number},{password},{expiration_date}\n"
                                file.write(line)
                                
                # members_times_mixed.txt와 selected_seats.txt에서 회원 정보를 읽어옴
                members_2 = read_members_2('members_times_mixed.txt')
                seats = read_seats('selected_seats.txt')
                
                # 회원정보와 좌석 정보를 비교하여 mixed_members 딕셔너리에 저장
                mixed_members_2 = compare_members_2(members_2, seats)
                
                # mixed_members 딕셔너리의 회원 정보를 members_seats.txt에 저장
                save_members_2('members_seats.txt', mixed_members_2)
                
                # members_times_mixed.txt 파일에서 회원정보를 읽어와 리스트로 반환하는 함수
                def read_members_times_mixed(file_name):
                    members_times_mixed = []
                    with open(file_name, 'r') as file:
                        for line in file:
                            line = line.strip()
                            if line:
                                member_id, password, expiration_date = line.split(',')
                                members_times_mixed.append((member_id, password, expiration_date))
                    return members_times_mixed
                
                # members_seats.txt 파일에서 회원 정보를 읽어와 리스트로 반환하는 함수
                def read_members_seats(file_name):
                    members_seats = []
                    with open(file_name, 'r') as file:
                        for line in file:
                            line = line.strip()
                            if line:
                                member_id, seat_number, password, expiration_date = line.split(',')
                                members_seats.append((member_id, seat_number, password, expiration_date))
                    return members_seats
            
                # 좌측 화면에 회원 정보 리스트를 시각화하는 함수
                def display_members(members_list):
                    members_text.delete(1.0, tk.END) # 기존 텍스트 삭제
                    for member in members_list:
                        if len(member) == 3:    # members_times_mixed.txt 정렬시
                            line = f"ID: {member[0]}\n비밀번호: {member[1]}\n만료기한: {member[2]}\n\n"
                        else:   # members_seat.txt 정렬시
                            line = f"ID: {member[0]}\n좌석번호: {member[1]}\n비밀번호: {member[2]}\n만료기한: {member[3]}\n\n"
                        members_text.insert(tk.END, line)
                
                def save_members_final(file_name, members):
                    with open(file_name, 'w') as file:
                        for member_id, password in members.items():
                            file.write(f"{member_id},{password}\n")
                            
                # '정렬' 버튼 클릭시 동작하는 함수
                def search_member():
                    selected_file = file_select.get()   # 선택된 파일명 가져오기
                    if selected_file == 'members_times_mixed.txt':
                        members_times_mixed = read_members_times_mixed('members_times_mixed.txt')
                        display_members(members_times_mixed)
                    elif selected_file == 'members_seats.txt':
                        members_seats = read_members_seats('members_seats.txt')
                        display_members(members_seats)
                    
                # '탈퇴' 버튼 클릭 시 동작하는 함수
                def withdraw_member():
                    messagebox.showinfo('주의', '모든 정보를 삭제할 회원의 ID줄을 드래그 하였는지 확인하십시오.')
                    answer = messagebox.askyesno("주의", "해당 회원의 정보를 정말로 모두 삭제하시겠습니까?")
                    if answer:
                        selected_index = members_text.tag_ranges(tk.SEL)
                        if selected_index:
                            start, end = selected_index
                            selected_id = members_txt.get(start, end).strip()
                            if selected_id:
                                selected_id = selected_id.split(': ')[1] # ID 추출
                                members_times_mixed = read_members_times_mixed('members_times_mixed.txt')
                                members_seats = read_members_seats('members_seats.txt')
                                
                                # members_times_mixed.txt에서 해당 ID 삭제
                                members_times_mixed = [member for member in members_times_mixed if 
                                                    member[0] != selected_id]
                                with open('members_times_mixed.txt', 'w') as file:
                                    for member in members_times_mixed:
                                        file.write(f"{member[0]},{member[1]},{member[2]}\n")
                                        
                                # members_seats.txt에서 해당 ID 삭제
                                members_seats = [member for member in members_seats if member[0] != selected_id]
                                with open('members_seats.txt', 'w') as file:
                                    for member in members_seats:
                                        file.write(f"{member[0]}, {member[1]},{member[2]},{member[3]}\n")
                                
                                # members.txt에서 해당 ID 삭제
                                members = read_members('members.txt')
                                members.pop(selected_id, None)
                                save_members_final('members.txt', members)
                                
                                # members_time.txt에서 해당 ID 삭제
                                members_time = read_members('members_time.txt')
                                members_time.pop(selected_id, None)
                                save_members_final('members_time.txt', members_time)
                                
                                # selected_seats.txt에서 해당 ID 삭제
                                seats = read_seats('selected_seats.txt')
                                if selected_id in seats:
                                    del seats[selected_id]
                                    with open('selected_seats.txt', 'w') as file:
                                        for member_id, seat_numbers in seats.items():
                                            for seat_number in seat_numbers:
                                                file.write(f"{member_id},{seat_number}\n")
                                                
                                messagebox.showinfo('완료', '탈퇴 완료되었습니다.')
                                
                                # 탈퇴 후 새로운 리스트 조회
                                search_member()
                                
                                
                # Tkinter 창 생성
                window = tk.Tk()
                window.title("회원 정보 시스템")
                
                # 좌측 화면
                members_frame = tk.Frame(window)
                members_frame.pack(side=tk.LEFT, padx=20, pady=20)
                
                members_text = tk.Text(members_frame, width=30, height=15)
                members_text.pack()
                
                # 우측 버튼들
                buttons_frame  = tk.Frame(window)
                buttons_frame.pack(side=tk.RIGHT, padx=20, pady=20)
                
                file_select = tk.StringVar()
                file_select.set('members_times_mixed.txt') #초기 선택값
                
                file_option_menu = tk.OptionMenu(buttons_frame, file_select, 'members_times_mixed.txt',
                                                'members_seats.txt')
                file_option_menu.pack(pady=10)
                
                search_button = tk.Button(buttons_frame, text="정렬", command=search_member)
                search_button.pack(pady=10)
                
                withdraw_button = tk.Button(buttons_frame, text="탈퇴", command=withdraw_member)
                withdraw_button.pack(pady=10)
                
                # 초기 회원 정보 리스트를 읽어와서 좌측 화면에 시각화
                members_times_mixed = read_members_times_mixed('members_times_mixed.txt')
                display_members(members_times_mixed)
                
                # Tkinter 창 실행
                window.mainloop()
                
                
            else: # 비밀번호가 일치하지 않은 경우
                messagebox.showerror("오류", "비밀번호가 틀렸습니다. 다시 시도하세요.")
    
    
    
    
        #toplevel = tk.Toplevel()
        #toplevel.geometry("300x200+820+100")
        
        # 확인 버튼 추가
        button = tk.Button(password, text="확인", command=check_password)
        button.pack()
        
        # Tkinter 이벤투 루프 시작
        password.mainloop()
        
    def exit(self):
        self.quit()
        self.destroy()
        
app = SampleApp()
app.mainloop()

