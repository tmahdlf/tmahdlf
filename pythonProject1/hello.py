import random
import tkinter as tk
from tkinter import messagebox

class GamblingGame:
    def __init__(self, master, update_balance, initial_balance=1000):
        self.master = master
        self.master.title("O/X 도박 게임")
        self.master.geometry("300x300")
        self.master.configure(bg="#f0f0f0")
        self.update_balance = update_balance

        self.balance = initial_balance  # 초기 잔액 설정

        # 잔액 레이블
        self.balance_label = tk.Label(
            master, text=f"현재 잔액: {self.balance}원", font=("Arial", 14, "bold"), bg="#f0f0f0", fg="green"
        )
        self.balance_label.pack(pady=(20, 10))

        # 배팅 레이블과 입력 필드
        self.bet_label = tk.Label(
            master, text="배팅할 금액을 입력하세요:", font=("Arial", 12), bg="#f0f0f0"
        )
        self.bet_label.pack(pady=5)

        self.bet_entry = tk.Entry(master, font=("Arial", 12), justify="center")
        self.bet_entry.pack(pady=5)

        # O/X 선택 라디오 버튼
        self.choice_label = tk.Label(
            master, text="O 또는 X를 선택하세요:", font=("Arial", 12), bg="#f0f0f0"
        )
        self.choice_label.pack(pady=5)

        self.choice_var = tk.StringVar(value="O")
        self.choice_frame = tk.Frame(master, bg="#f0f0f0")
        self.choice_frame.pack(pady=5)

        self.choice_o = tk.Radiobutton(
            self.choice_frame, text="O", variable=self.choice_var, value="O", font=("Arial", 12), bg="#f0f0f0", activebackground="#d0d0d0", fg="blue"
        )
        self.choice_o.pack(side="left", padx=10)

        self.choice_x = tk.Radiobutton(
            self.choice_frame, text="X", variable=self.choice_var, value="X", font=("Arial", 12), bg="#f0f0f0", activebackground="#d0d0d0", fg="red"
        )
        self.choice_x.pack(side="right", padx=10)

        # 플레이 버튼
        self.play_button = tk.Button(
            master, text="Play", command=self.play, bg="#4CAF50", fg="white", font=("Arial", 12, "bold"), activebackground="#45a049"
        )
        self.play_button.pack(pady=(10, 20))

    def play(self):
        try:
            bet = int(self.bet_entry.get())
            choice = self.choice_var.get()
            result = random.choices(["O", "X"], weights=[2, 1])[0]

            if bet <= 0 or bet > self.balance:
                messagebox.showerror("오류", "배팅 금액이 잘못되었습니다.")
                return

            if choice == result:
                self.balance += bet * 2
                messagebox.showinfo("축하합니다!", f"맞췄습니다! 결과는 {result}입니다.")
            else:
                self.balance -= bet
                messagebox.showinfo("오답", f"틀렸습니다. 결과는 {result}였습니다.")

            self.update_balance(self.balance)
            self.balance_label.config(text=f"현재 잔액: {self.balance}원")

            if self.balance <= 0:
                messagebox.showinfo("게임 종료", "잔액이 모두 소진되었습니다. 게임을 종료합니다.")
                self.master.destroy()

        except ValueError:
            messagebox.showerror("오류", "숫자를 입력하세요.")


class DiceGame:
    def __init__(self, master, update_balance, initial_balance=1000):
        self.master = master
        self.master.title("숫자 더하기 도박 게임")
        self.master.geometry("400x400")
        self.master.configure(bg="#f0f0f0")
        self.update_balance = update_balance

        self.balance = initial_balance  # 초기 잔액 설정

        # 잔액 레이블
        self.balance_label = tk.Label(
            master, text=f"현재 잔액: {self.balance}원", font=("Arial", 14, "bold"), bg="#f0f0f0", fg="green"
        )
        self.balance_label.pack(pady=(20, 10))

        # 배팅 레이블과 입력 필드
        self.bet_label = tk.Label(
            master, text="배팅할 금액을 입력하세요:", font=("Arial", 12), bg="#f0f0f0"
        )
        self.bet_label.pack(pady=5)

        self.bet_entry = tk.Entry(master, font=("Arial", 12), justify="center")
        self.bet_entry.pack(pady=5)

        # 주사위 합 선택 라디오 버튼
        self.choice_label = tk.Label(
            master, text="합이 7에서 12 사이인지 선택하세요:", font=("Arial", 12), bg="#f0f0f0"
        )
        self.choice_label.pack(pady=5)

        self.choice_var = tk.StringVar(value="yes")
        self.choice_frame = tk.Frame(master, bg="#f0f0f0")
        self.choice_frame.pack(pady=5)

        self.choice_yes = tk.Radiobutton(
            self.choice_frame, text="네", variable=self.choice_var, value="yes", font=("Arial", 12), bg="#f0f0f0", activebackground="#d0d0d0"
        )
        self.choice_yes.pack(side="left", padx=10)

        self.choice_no = tk.Radiobutton(
            self.choice_frame, text="아니오", variable=self.choice_var, value="no", font=("Arial", 12), bg="#f0f0f0", activebackground="#d0d0d0"
        )
        self.choice_no.pack(side="right", padx=10)

        # 주사위 결과 표시
        self.dice_frame = tk.Frame(master, bg="#f0f0f0")
        self.dice_frame.pack(pady=10)

        self.dice_label1 = tk.Label(self.dice_frame, bg="#f0f0f0")
        self.dice_label1.pack(side="left", padx=10)

        self.dice_label2 = tk.Label(self.dice_frame, bg="#f0f0f0")
        self.dice_label2.pack(side="right", padx=10)

        # 플레이 버튼
        self.play_button = tk.Button(
            master, text="Play", command=self.play, bg="#4CAF50", fg="white", font=("Arial", 12, "bold"), activebackground="#45a049"
        )
        self.play_button.pack(pady=(10, 20))

    def roll_dice(self):
        # 주사위를 굴리는 것처럼 보이게 이미지 빠르게 전환
        for _ in range(10):
            dice1 = random.randint(1, 6)
            dice2 = random.randint(1, 6)
            self.dice_label1.config(text=f"🎲 {dice1}")
            self.dice_label2.config(text=f"🎲 {dice2}")
            self.master.update()
            self.master.after(50)  # 전환 속도

        return dice1, dice2

    def play(self):
        try:
            bet = int(self.bet_entry.get())
            choice = self.choice_var.get()
            dice1, dice2 = self.roll_dice()
            total = dice1 + dice2

            if bet <= 0 or bet > self.balance:
                messagebox.showerror("오류", "배팅 금액이 잘못되었습니다.")
                return

            win = (total >= 7 and total <= 12)

            if (choice == "yes" and win) or (choice == "no" and not win):
                self.balance += bet * 2
                messagebox.showinfo("축하합니다!", f"맞췄습니다! 주사위 합은 {total}입니다.")
            else:
                self.balance -= bet
                messagebox.showinfo("오답", f"틀렸습니다. 주사위 합은 {total}였습니다.")

            self.update_balance(self.balance)
            self.balance_label.config(text=f"현재 잔액: {self.balance}원")

            if self.balance <= 0:
                messagebox.showinfo("게임 종료", "잔액이 모두 소진되었습니다. 게임을 종료합니다.")
                self.master.destroy()

        except ValueError:
            messagebox.showerror("오류", "숫자를 입력하세요.")


class SlotMachineGame:
    def __init__(self, master, update_balance, initial_balance=1000):
        self.master = master
        self.master.title("슬롯 머신 게임")
        self.master.geometry("500x500")
        self.master.configure(bg="#222831")
        self.update_balance = update_balance

        self.balance = initial_balance  # 초기 잔액 설정

        # 잔액 레이블
        self.balance_label = tk.Label(
            master,
            text=f"현재 잔액: {self.balance}원",
            font=("Arial", 16, "bold"),
            bg="#393e46",
            fg="#00adb5",
            pady=10,
            padx=10,
        )
        self.balance_label.pack(pady=(20, 10), fill=tk.X)

        # 배팅 레이블과 입력 필드
        self.bet_label = tk.Label(
            master,
            text="배팅할 금액을 입력하세요:",
            font=("Arial", 12),
            bg="#393e46",
            fg="#eeeeee"
        )
        self.bet_label.pack(pady=5)

        self.bet_entry = tk.Entry(master, font=("Arial", 12), justify="center")
        self.bet_entry.pack(pady=5)

        # 슬롯 릴 레이블
        self.reel_frame = tk.Frame(master, bg="#222831")
        self.reel_frame.pack(pady=20)

        self.reel1 = tk.Label(self.reel_frame, text="🍒", font=("Arial", 48), bg="#393e46", fg="#eeeeee", width=3)
        self.reel1.pack(side="left", padx=20)

        self.reel2 = tk.Label(self.reel_frame, text="🍋", font=("Arial", 48), bg="#393e46", fg="#eeeeee", width=3)
        self.reel2.pack(side="left", padx=20)

        self.reel3 = tk.Label(self.reel_frame, text="🍊", font=("Arial", 48), bg="#393e46", fg="#eeeeee", width=3)
        self.reel3.pack(side="left", padx=20)

        # 플레이 버튼
        self.play_button = tk.Button(
            master,
            text="Play",
            command=self.start_spin,
            bg="#00adb5",
            fg="#eeeeee",
            font=("Arial", 14, "bold"),
            activebackground="#393e46",
            width=10,
        )
        self.play_button.pack(pady=(30, 20))

        # 슬롯 기호
        self.symbols = ["🍒", "🍋", "🍊", "🍉", "⭐", "🍇", "🍓", "🍍", "🥝", "🍎"]

    def start_spin(self):
        try:
            bet = int(self.bet_entry.get())
            if bet <= 0 or bet > self.balance:
                messagebox.showerror("오류", "배팅 금액이 잘못되었습니다. 다시 입력해주세요.")
                return

            # 릴이 돌아가는 동안 버튼 비활성화
            self.play_button.config(state="disabled")
            self.bet_entry.config(state="disabled")
            self.spin_reels(10, bet)  # 릴이 돌아가는 횟수

        except ValueError:
            messagebox.showerror("오류", "유효한 숫자를 입력해주세요.")

    def spin_reels(self, spins, bet):
        if spins > 0:
            # 릴을 돌리는 것처럼 보이게 랜덤으로 이모지 선택
            reel1 = random.choice(self.symbols)
            reel2 = random.choice(self.symbols)
            reel3 = random.choice(self.symbols)

            self.reel1.config(text=reel1)
            self.reel2.config(text=reel2)
            self.reel3.config(text=reel3)

            # 100ms마다 이 함수를 다시 호출하여 애니메이션 효과 생성
            self.master.after(100, self.spin_reels, spins - 1, bet)
        else:
            self.check_result(bet)  # 릴이 멈추면 결과 확인

    def check_result(self, bet):
        reel1 = self.reel1.cget("text")
        reel2 = self.reel2.cget("text")
        reel3 = self.reel3.cget("text")

        # 결과 확인
        jackpot_chance = random.random() < 0.1
        if reel1 == reel2 == reel3 and jackpot_chance:
            winnings = bet * 10
            self.balance += winnings
            messagebox.showinfo("축하합니다!", f"잭팟! {winnings}원을 받았습니다!")
        else:
            self.balance -= bet
            messagebox.showinfo("결과", f"아쉽습니다! {bet}원을 잃었습니다.")

        # 잔액 업데이트
        self.balance_label.config(text=f"현재 잔액: {self.balance}원")

        if self.balance <= 0:
            messagebox.showinfo("게임 종료", "잔액이 모두 소진되었습니다. 게임을 종료합니다.")
            self.master.destroy()
        else:
            # 버튼 다시 활성화
            self.play_button.config(state="normal")
            self.bet_entry.config(state="normal")
            self.update_balance(self.balance)


class IntroScreen:
    def __init__(self, master):
        self.master = master
        self.master.title("도박 게임 선택")
        self.master.geometry("300x300")
        self.master.configure(bg="#f0f0f0")
        self.balance = 100000  # 초기 잔액 설정

        # 인트로 레이블
        self.intro_label = tk.Label(master, text="게임을 선택하세요", font=("Arial", 14, "bold"), bg="#f0f0f0")
        self.intro_label.pack(pady=(20, 10))

        # O/X 게임 버튼
        self.game1_button = tk.Button(
            master,
            text="O/X 게임",
            command=self.start_game1,
            bg="#4CAF50",
            fg="white",
            font=("Arial", 12, "bold"),
            activebackground="#45a049",
        )
        self.game1_button.pack(pady=(10, 10))

        # 주사위 게임 버튼
        self.game2_button = tk.Button(
            master,
            text="주사위 게임",
            command=self.start_game2,
            bg="#4CAF50",
            fg="white",
            font=("Arial", 12, "bold"),
            activebackground="#45a049",
        )
        self.game2_button.pack(pady=(10, 10))

        # 슬롯 머신 게임 버튼
        self.game3_button = tk.Button(
            master,
            text="슬롯 머신 게임",
            command=self.start_game3,
            bg="#4CAF50",
            fg="white",
            font=("Arial", 12, "bold"),
            activebackground="#45a049",
        )
        self.game3_button.pack(pady=(10, 10))

    def start_game1(self):
        game_window = tk.Toplevel(self.master)
        GamblingGame(game_window, self.update_balance, self.balance)

    def start_game2(self):
        game_window = tk.Toplevel(self.master)
        DiceGame(game_window, self.update_balance, self.balance)

    def start_game3(self):
        game_window = tk.Toplevel(self.master)
        SlotMachineGame(game_window, self.update_balance, self.balance)

    def update_balance(self, new_balance):
        self.balance = new_balance


if __name__ == "__main__":
    root = tk.Tk()
    intro_screen = IntroScreen(root)
    root.mainloop()
    print