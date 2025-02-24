from random import choice, shuffle
from time import sleep
from PyQt5.QtWidgets import QApplication
from style import *

app = QApplication([])
app.setStyleSheet(style)

from main_window import *
from menu_window import *


def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_ok.setText("Наступне питання")

def show_question():
    AnsGroupBox.hide()
    RadioGroupBox.show()
    btn_ok.setText("Відповісти")
    RadioGroup.setExclusive(False)
    for btn in radio_buttons:
        btn.setChecked(False)
    RadioGroup.setExclusive(True)

def check_result():
    RadioGroup.setExclusive(False)
    for btn in radio_buttons:
        if btn.isChecked():
            if btn.text() == lb_correct.text():
                cur_q.got_right()
                lb_result.setText('Вірно!')
                btn.setChecked(False)
                break
    else:
        lb_result.setText('Не вірно!')
        cur_q.got_wrong()

def click_OK():
    if btn_ok.text() == 'Відповісти':
        check_result()
        lb_result.show()
        show_result()
    else:
        new_question()
        show_question()

class Question:
    def __init__(self, question, answer, wrong_answer1, wrong_answer2, wrong_answer3):
        self.question = question
        self.answer = answer
        self.wrong_answer1 = wrong_answer1
        self.wrong_answer2 = wrong_answer2
        self.wrong_answer3 = wrong_answer3
        self.count_ask = 0
        self.count_right = 0

    def got_right(self):
        self.count_ask += 1
        self.count_right += 1

    def got_wrong(self):
        self.count_ask += 1

q1 = Question('Яблуко', 'apple', 'application', 'pineapple', 'apply')
q2 = Question('Дім', 'house', 'horse', 'hurry', 'hour')
q3 = Question('Миша', 'mouse', 'mouth', 'muse', 'museum')
q4 = Question('Число', 'number', 'digit', 'amount', 'summary')

radio_buttons = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]
questions = [q1, q2, q3, q4]

def new_question():
    global cur_q
    cur_q = choice(questions)
    lb_question.setText(cur_q.question)
    lb_correct.setText(cur_q.answer)

    answers = [cur_q.answer, cur_q.wrong_answer1, cur_q.wrong_answer2, cur_q.wrong_answer3]
    shuffle(answers)

    for btn, text in zip(radio_buttons, answers):
        btn.setText(text)

new_question()
show_question()
btn_ok.clicked.connect(click_OK)

def rest():
    win_card.hide()
    n = btn_minutes.value() * 60
    sleep(n)
    win_card.show()

btn_sleep.clicked.connect(rest)

def show_menu():
    win_card.hide()
    menu_win.show()

btn_menu.clicked.connect(show_menu) 

def hide_menu():
    menu_win.hide()
    win_card.show()

btn_back.clicked.connect(hide_menu)

def clear():
    line_quest.clear()
    line_right_ans.clear()
    line_wrong1_ans.clear()
    line_wrong2_ans.clear()
    line_wrong3_ans.clear()

btn_clear.clicked.connect(clear)

def add_question():
    new_q = Question(line_quest.text(),line_right_ans.text(),
                     line_wrong1_ans.text(),line_wrong2_ans.text(),line_wrong3_ans.text())
    
    questions.append(new_q)
    clear()

btn_add_quest.clicked.connect(add_question)

def stat_generator():
    if cur_q.count_ask == 0:
        c = 0
    else:
        c = (cur_q.count_right / cur_q.count_ask) * 100

    text = f'Разів відповіли: {cur_q.count_ask}\n' \
           f'Вірних відповідей: {cur_q.count_right}\n' \
           f'Успішність: {round(c, 2)}%'
    
    lb_statistic.setText(text)
    menu_win.show()
    win_card.hide()

btn_menu.clicked.connect(stat_generator)

app.exec_()
