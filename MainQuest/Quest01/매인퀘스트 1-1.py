import random
import json
import os

class Account():
    count = 0
    interest_count = 0
    customer_info = {}

    def __init__(self):
        self.load_db()
        self.login()

    def login(self):
        self.bank = "SC은행"
        self.name = input("고객의 이름을 입력하십시오. ")
        while True:
            try:
                raw = input("계좌번호 11자리를 입력하십시오. 0을 입력하시면 새 계좌번호를 발급합니다.")
                self.process_account_number(raw)
                self.account_number = self.process_account_number(raw)
                self.customer = self.bank + " " + self.account_number + " " + self.name
                if self.account_number_raw == "0" :
                    raise KeyError("새 계좌번호를 발급합니다.")
                elif int(self.account_number_raw) < 0 or int(self.account_number_raw) > 99999999999 or len(self.account_number_raw) != 11 :
                    raise ValueError("유효하지 않은 계좌번호입니다.")
                elif self.account_number_raw.isdigit() is False :
                    raise ValueError("유효하지 않은 계좌번호입니다.")
                elif self.customer not in Account.customer_info :
                    print("등록되지 않은 계좌번호를 입력하셨습니다.")
                else:
                    break
            except(ValueError):
                print("유효하지 않은 계좌번호를 입력하셨습니다.")
            except(KeyError):
                print("새 계좌번호를 발급합니다.")
                Account.count += 1
                self.account_number_raw = str(random.randint(0, 999999999999))
                self.process_account_number(self.account_number_raw)
                self.account_number = self.process_account_number(self.account_number_raw)
                break
        print(f"{self.bank}를 찾아주신 {self.name}님의 계좌번호는 {self.account_number}입니다.")
        if self.customer not in Account.customer_info.keys():
            self.history = []
            while True:
                try:
                    self.balance = float(input("계좌 잔고를 입력하십시오. "))
                    if self.balance < 0:
                        raise ValueError("계좌 잔고는 음수가 될 수 없습니다.")
                    elif type(self.balance) != float:
                        raise ValueError("계좌 잔고는 숫자로 입력해야 합니다.")
                    else:
                        break
                except(ValueError):
                    print("계좌 잔고는 양의 숫자여야 합니다.")
        else:
            self.balance = Account.customer_info[self.customer]["잔고"]
            print(f"{self.customer} 고객의 계좌 잔고는 {self.balance}원입니다.")
            try:
                self.history = Account.customer_info[self.customer]["거래내역"]
            except KeyError:
                Account.customer_info[self.customer]["거래내역"] = []
        self.record_info(Account)
        self.get_account_num(Account)

    def save_db(self):
        with open("csbank.json", 'w', encoding='utf-8') as f:
            json.dump(Account.customer_info, f, indent=4, ensure_ascii=False)

    def load_db(self):
        if os.path.isfile("csbank.json"):
            try:
                with open("csbank.json", 'r', encoding='utf-8') as f:
                    Account.customer_info = json.load(f)
                    Account.customer_info = dict(sorted(Account.customer_info.items()))
                    Account.count += len(Account.customer_info)
            except json.JSONDecodeError as e:
                print("JSON 파일 읽기 오류:", e)
                Account.customer_info = {}
        else:
            Account.customer_info = {}

    def process_account_number(self, raw):
        self.account_number_raw = raw
        self.account_number_1st = self.account_number_raw[0:3]
        self.account_number_2nd = self.account_number_raw[3:5]
        self.account_number_3rd = self.account_number_raw[5:11]
        self.account_number = self.account_number_1st + "-" + self.account_number_2nd + "-" + self.account_number_3rd
        return self.account_number

    def get_customer_id(self):
        while True:
            self.bank = "SC은행"
            self.name = input("고객의 이름을 입력하십시오. ")
            while True:
                raw = input("고객의 계좌번호 11자리를 입력하십시오. ")
                self.process_account_number(raw)
                try:
                    if int(raw) < 0 or int(raw) > 99999999999 or len(raw) != 11 :
                        raise ValueError("유효하지 않은 계좌번호입니다.")
                    elif raw.isdigit() is False :
                        raise ValueError("유효하지 않은 계좌번호입니다.")
                except ValueError:
                    print("유효하지 않은 계좌번호를 입력하셨습니다.")
                else:
                    break
            self.account_number = self.process_account_number(raw)
            self.customer = self.bank + " " + self.account_number + " " + self.name
            if self.customer not in Account.customer_info :
                print("등록되지 않은 고객 정보를 입력하셨습니다.")
            else:
                return self.customer

    def record_info(self, Account):
        self.customer = self.bank + " " + self.account_number + " " + self.name
        Account.customer_info[self.customer] = {"잔고":self.balance, "거래내역":self.history}
        Account.customer_info = dict(sorted(Account.customer_info.items()))
        self.save_db()

    def get_account_num(self, Account):
        print(f"현재 {self.bank}에 개설된 계좌는 총 {Account.count}개입니다.")

    def deposit(self):
        self.customer = self.get_customer_id()
        self.interest_rate = 0.01
        try:
            self.to_deposit = float(input("입금할 금액을 입력하십시오."))
            if self.to_deposit <= 0 :
                raise ValueError("출금할 금액을 0 또는 음수로 입력하셨습니다.")
        except(ValueError):
            print("0원 또는 음수의 금액을 입금할 수는 없습니다.")
        else:
            self.balance += self.to_deposit
            self.history.append(f"예금입금 : {self.to_deposit}")
            Account.customer_info[self.customer]["거래내역"] = self.history
            print(str(self.to_deposit) + "원 입금하였습니다.")
            self.interest_count = self.interest_counter()
            if self.interest_count == 5:
                self.interest_count -= 5
                print(f"{self.balance*self.interest_rate}원의 이자가 지급되었습니다.")
                self.history.append(f"이자수익 : {self.to_deposit}")
                Account.customer_info[self.customer]["거래내역"] = self.history  # 수정된 부분
                self.balance *= 1 + self.interest_rate
            print("계좌 잔고는 " + str(self.balance) + "원입니다.")
            self.record_info(Account)

    def interest_counter(self):
        for_counting = []
        i = len(Account.customer_info[self.customer]["거래내역"]) - 1
        while i >= 0:
            transaction_raw = Account.customer_info[self.customer]["거래내역"][i].split(" ")
            transaction = float(transaction_raw[2])
            if transaction > 0 :
                for_counting.append(Account.customer_info[self.customer]["거래내역"][i])
            i -= 1
        return len(for_counting)

    def deposit_history(self):
        self.customer = self.get_customer_id()
        self.deposit_list = []
        i = len(Account.customer_info[self.customer]["거래내역"]) - 1
        while i >= 0:
            self.transaction_raw = Account.customer_info[self.customer]["거래내역"][i].split(" ")
            self.transaction = float(self.transaction_raw[2])
            if self.transaction > 0 :
                self.deposit_list.append(Account.customer_info[self.customer]["거래내역"][i])
            i -= 1
        print("입금내역은 다음과 같습니다.")
        print(self.deposit_list)

    def withdraw(self):
        self.customer = self.get_customer_id()
        try:
            self.to_withdraw = float(input("출금할 금액을 입력하십시오."))
            if self.to_withdraw > self.balance :
                raise ValueError("출금할 금액이 계좌 잔고보다 더 많습니다.")
        except(ValueError):
            print("계좌 잔고보다 더 많은 금액을 출금할 수는 없습니다.")
        else:
            self.balance -= self.to_withdraw
            self.history.append(f"예금출금 : {0 - self.to_withdraw}")
            Account.customer_info[self.customer]["거래내역"] = self.history
            print(str(self.to_withdraw) + "원 출금하였습니다.")
            print("계좌 잔고는 " + str(self.balance) + "원입니다.")
            self.record_info(Account)

    def withdraw_history(self):
        self.customer = self.get_customer_id()
        self.withdraw_list = []
        i = len(Account.customer_info[self.customer]["거래내역"]) - 1
        while i >= 0:
            self.transaction_raw = Account.customer_info[self.customer]["거래내역"][i].split(" ")
            self.transaction = float(self.transaction_raw[2])
            if self.transaction < 0 :
                self.withdraw_list.append(Account.customer_info[self.customer]["거래내역"][i])
            i -= 1
        print("출금내역은 다음과 같습니다.")
        print(self.withdraw_list)

    def display_info(self):
        self.customer = self.get_customer_id()
        if self.customer in Account.customer_info.keys() :
            if Account.customer_info[self.customer]["잔고"] < 1000000 :
                print("잔고가 1,000,000원 미만인 계좌는 조회할 수 없습니다.")
            else:
                print(f"{self.customer} 고객의 계좌 잔고는 다음과 같습니다.")
                print("계좌 잔액 : " + str(f"{Account.customer_info[self.customer]["잔고"]:,}"))
                print(f"고객의 거래 내역은 다음과 같습니다.")
                print(Account.customer_info[self.customer]["거래내역"])
        else:
            print("등록되지 않은 계좌정보입니다.")

    def start(self):
        start = ""
        while start == "":
            print(f"{self.bank} 은행에 오신 것을 환영합니다. 본 ATM기에 명령을 내려주십시오.")
            print('계좌 개설은 "로그인" 작업에서 할 수 있습니다.')
            start = input('"로그인", "입금", "출금", "입금내역", "출금내역", "정보", "종료" 로 입력하십시오 : ')
            if start == start == "로그인" :
                self.login()
                start = ""
            elif start == "입금" :
                self.deposit()
                start = ""
            elif start == "출금" :
                self.withdraw()
                start = ""
            elif start == "입금내역" :
                self.deposit_history()
                start = ""
            elif start == "출금내역" :
                self.withdraw_history()
                start = ""
            elif start == "정보" :
                self.display_info()
                start = ""
            elif start == "종료" :
                print("프로그램을 종료합니다.")
            else :
                print("잘못 입력하셨습니다.")
                start = ""

a = Account()
a.start()