import tkinter as tk
import math

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("계산기")
        self.root.geometry("320x470")

        self.expression = ""

        # 버튼 배열 (sin, cos, tan, 괄호, 백스페이스 포함)
        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', 'C', '+'],
            ['sin', 'cos', 'tan', '='],
            ['(', ')', '←']
        ]

        # 입력창
        self.entry = tk.Entry(root, font=("Arial", 24), justify="right")
        self.entry.pack(fill="both", ipadx=8, ipady=15, padx=10, pady=10)

        for row in buttons:
            frame = tk.Frame(root)
            frame.pack(expand=True, fill="both")
            for char in row:
                btn = tk.Button(
                    frame,
                    text=char,
                    font=("Arial", 18),
                    command=lambda ch=char: self.on_click(ch)
                )
                btn.pack(side="left", expand=True, fill="both")

    # 각도를 라디안으로 변환해서 계산해주는 함수
    def sin_deg(self, x):
        return math.sin(math.radians(x))
    def cos_deg(self, x):
        return math.cos(math.radians(x))
    def tan_deg(self, x):
        return math.tan(math.radians(x))

    def on_click(self, char):
        if char == 'C':
            self.expression = ""
        elif char == '←':
            self.expression = self.expression[:-1]
        elif char == '=':
            try:
                self.expression = str(eval(
                    self.expression,
                    {"__builtins__": None,
                     "sin": self.sin_deg, "cos": self.cos_deg, "tan": self.tan_deg}
                ))
            except Exception:
                self.expression = "에러"
        elif char in ('sin', 'cos', 'tan'):
            self.expression += char + '('
        else:
            self.expression += str(char)

        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, self.expression)
