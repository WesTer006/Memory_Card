from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QGroupBox, QButtonGroup, QRadioButton, QPushButton, QLabel, QSpinBox 
from PyQt5.QtCore import Qt 
from random import shuffle 
 
card_width = 600 
card_height = 500 
 
win_card = QWidget() 
win_card.resize(card_width,card_height) 
win_card.setWindowTitle("Memory Card") 
 
btn_menu = QPushButton("Меню") 
btn_sleep = QPushButton("Відпочити") 
btn_minutes = QSpinBox() 
btn_minutes.setValue(30) 
btn_ok = QPushButton("Відповісти") 
lb_question = QLabel("")
lb_question.setStyleSheet("font-size: 25px; font-weight: bold;") 
 
RadioGroupBox = QGroupBox("Варіанти відповідей") 
RadioGroup = QButtonGroup() 
 
rbtn_1 = QRadioButton("")
rbtn_2 = QRadioButton("") 
rbtn_3 = QRadioButton("") 
rbtn_4 = QRadioButton("") 
RadioGroup.addButton(rbtn_1) 
RadioGroup.addButton(rbtn_2) 
RadioGroup.addButton(rbtn_3) 
RadioGroup.addButton(rbtn_4) 
 
AnsGroupBox = QGroupBox("Результат тесту") 
lb_result = QLabel("") 
lb_correct = QLabel("") 
 
layout_ans1 = QHBoxLayout() 
layout_ans2 = QVBoxLayout() 
layout_ans3 = QVBoxLayout() 
 
layout_ans2.addWidget(rbtn_1) 
layout_ans2.addWidget(rbtn_2) 
layout_ans3.addWidget(rbtn_3) 
layout_ans3.addWidget(rbtn_4) 
 
layout_ans1.addLayout(layout_ans2) 
layout_ans1.addLayout(layout_ans3) 
 
RadioGroupBox.setLayout(layout_ans1) 
 
layout_res = QVBoxLayout() 
layout_res.addWidget(lb_result, alignment=(Qt.AlignLeft | Qt.AlignTop)) 
layout_res.addWidget(lb_correct, alignment=Qt.AlignHCenter, stretch=2) 
AnsGroupBox.setLayout(layout_res) 
AnsGroupBox.hide() 
 
layout_line1 = QHBoxLayout() 
layout_line2 = QHBoxLayout() 
layout_line3 = QHBoxLayout() 
layout_line4 = QHBoxLayout() 
 
layout_line1.addWidget(btn_menu) 
layout_line1.addStretch(1) 
layout_line1.addWidget(btn_sleep) 
layout_line1.addWidget(btn_minutes) 
layout_line1.addWidget(QLabel("хвилин")) 
 
layout_line2.addWidget(lb_question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter)) 
 
layout_line3.addWidget(RadioGroupBox) 
layout_line3.addWidget(AnsGroupBox) 
 
layout_line4.addStretch(1) 
layout_line4.addWidget(btn_ok, stretch=2) 
layout_line4.addStretch(1) 
 
layout_card = QVBoxLayout() 
layout_card.addLayout(layout_line1, stretch=1) 
layout_card.addLayout(layout_line2, stretch=2) 
layout_card.addLayout(layout_line3,stretch=8) 
layout_card.addStretch(1) 
layout_card.addLayout(layout_line4, stretch = 1) 
layout_card.addStretch(1) 
layout_card.addSpacing(5) 
 
text_wrong = "Неправильно" 
text_correct = "Правильно" 
 
frm_question = "Яблуко" 
frm_right = "Apple" 
frm_wrong1 = "Application" 
frm_wrong2 = "Building" 
frm_wrong3 = "caterpillar" 
 
radio_list = [rbtn_1, rbtn_2, rbtn_3, rbtn_4] 
shuffle(radio_list) 
answer = radio_list[0] # ми не знаємо, який це з радіобаттонів, але можемо покласти сюди правильну відповідь і запам'ятати це 
wrong_answer1, wrong_answer2, wrong_answer3 = radio_list[1], radio_list[2], radio_list[3] 
 
win_card.setLayout(layout_card) 
win_card.show()