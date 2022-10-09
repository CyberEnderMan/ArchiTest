import tkinter as tk
from tkinter import *
from core import Core


class Interface(Core):
    '''Класс интерфейса'''

    def clear(self):
        '''Очистка экрана программы'''
        for widget in frame.winfo_children():
            widget.destroy()

    def load_first_question(self):
        '''Загрузка первого вопроса'''
        self.clear()
        self.load_question(1)
        self.test_question()

    def load_next_question(self, answer_number):
        '''Загрузка следующего вопроса'''
        self.clear()

        if answer_number == self.correct_number:
            self.points_add()

        if 0 < self.number < 10:
            self.number += 1
            self.load_question(self.number)
            self.test_question()

        elif self.number == 10:
            self.clear()
            self.test_result()

    def test_start(self):
        '''Запуск теста'''
        global root
        global frame

        root = tk.Tk()
        root.title("Архитектурный тест")

        frame = Frame(root, height="600", width="800")
        frame.pack(side="top", expand=False, fill="both")

        title = tk.Label(frame, text='Архитектурный тест', bg='green', fg="white", font=("Arial", 25))
        start_button = tk.Button(frame, text="Начать", bg="red", fg="white", command=lambda: self.load_first_question(),
                                 font=("Arial", 15))

        title.place(relx=0.5, rely=0.4, width=400, height=100, anchor="center")
        start_button.place(relx=0.5, rely=0.6, width=150, height=50, anchor="center")

        root.mainloop()

    def test_question(self):
        '''Визуализация вопроса'''
        number_frame = tk.Label(frame, text=self.number, bg='cyan', fg="black", font=("Arial", 15))
        question_frame = tk.Label(frame, text=self.question, bg='green', fg="white", font=("Arial", 10))
        answer1_frame = tk.Button(frame, text=self.answer1, bg="yellow", command=lambda: self.load_next_question(1), font=("Arial", 12))
        answer2_frame = tk.Button(frame, text=self.answer2, bg="yellow", command=lambda: self.load_next_question(2), font=("Arial", 12))
        answer3_frame = tk.Button(frame, text=self.answer3, bg="yellow", command=lambda: self.load_next_question(3), font=("Arial", 12))

        number_frame.place(relx=0.0, rely=0.0, width=50, height=50)
        question_frame.place(relx=0.08, rely=0.0, height=50)
        answer1_frame.place(relx=0.02, rely=0.12)
        answer2_frame.place(relx=0.02, rely=0.2)
        answer3_frame.place(relx=0.02, rely=0.28)

    def test_result(self):
        '''Визуализация результата'''
        result_title = tk.Label(frame, text='Результат теста', bg='#FF008B', fg="white", font=("Arial", 25))
        result_points = tk.Label(frame, text='Баллов:' + ' ' + str(self.points_sum), bg='blue', fg="white", font=("Arial", 15))

        if self.points_sum <= 3:
            result_mark = tk.Label(frame, text='Плохо', bg='red', fg="white", font=("Arial", 17))
        elif 6 >= self.points_sum > 3:
            result_mark = tk.Label(frame, text='Удовлетворительно', bg='#414042', fg="white", font=("Arial", 17))
        elif 9 >= self.points_sum > 6:
            result_mark = tk.Label(frame, text='Хорошо', bg='#4D8802', fg="white", font=("Arial", 17))
        elif self.points_sum == 10:
            result_mark = tk.Label(frame, text='Отлично', bg='cyan', fg="white", font=("Arial", 17))

        result_title.place(relx=0.5, rely=0.4, width=400, height=100, anchor="center")
        result_points.place(relx=0.5, rely=0.6, width=150, height=50, anchor="center")
        result_mark.place(relx=0.5, rely=0.75, width=300, height=50, anchor="center")
