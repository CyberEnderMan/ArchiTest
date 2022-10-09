import csv


class Core:
    '''Основной класс'''

    def __init__(self, number, question, answer1, answer2, answer3, correct_number, points_sum):
        '''Инициализация класса'''
        self.points_sum = points_sum
        self.number = number
        self.question = question
        self.answer1 = answer1
        self.answer2 = answer2
        self.answer3 = answer3
        self.correct_number = correct_number

    def load_question(self, no):
        '''Загрузка вопроса из CSV'''
        with open("test_data.csv", "r", encoding="utf-8") as csv_file:
            reader = csv.DictReader(csv_file, delimiter=';')
            for row in reader:
                if int(row["Номер"]) == no:
                    self.number = no
                    self.question = row["Вопрос"]
                    self.answer1 = row["Ответ1"]
                    self.answer2 = row["Ответ2"]
                    self.answer3 = row["Ответ3"]
                    self.correct_number = int(row["Верный ответ"])
                    break

    def points_add(self):
        '''Добавление баллов'''
        self.points_sum = self.points_sum + 1


