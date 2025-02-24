from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QGroupBox, QButtonGroup, QRadioButton, QPushButton, QLabel, QSpinBox, QLineEdit

menu_win =QWidget()

lb_quest = QLabel("Введіть запитання:")
lb_right_ans = QLabel("Введіть вірну відповідь:")
lb_wrong_ans1 = QLabel("Введіть першу хибну відповідь:")
lb_wrong_ans2 = QLabel("Введіть другу хибну відповідь:")
lb_wrong_ans3 = QLabel("Введіть третю хибну відповідь:")

line_quest = QLineEdit()
line_right_ans = QLineEdit()
line_wrong1_ans = QLineEdit()
line_wrong2_ans = QLineEdit()
line_wrong3_ans = QLineEdit()

lb_header_stat = QLabel("Статистика")
lb_header_stat.setStyleSheet("font-size: 19px; font-weight: bold;")

lb_statistic = QLabel()

v1_labels = QVBoxLayout()
v1_labels.addWidget(lb_quest)
v1_labels.addWidget(lb_right_ans)
v1_labels.addWidget(lb_wrong_ans1)
v1_labels.addWidget(lb_wrong_ans2)
v1_labels.addWidget(lb_wrong_ans3)

v1_lineEdits = QVBoxLayout()
v1_lineEdits.addWidget(line_quest)
v1_lineEdits.addWidget(line_right_ans)
v1_lineEdits.addWidget(line_wrong1_ans)
v1_lineEdits.addWidget(line_wrong2_ans)
v1_lineEdits.addWidget(line_wrong3_ans)

h1_question = QHBoxLayout()
h1_question.addLayout(v1_labels)
h1_question.addLayout(v1_lineEdits)

btn_back = QPushButton("Назад")
btn_clear = QPushButton("Очистити")
btn_add_quest = QPushButton("Додати запитання")

h1_buttons = QHBoxLayout()
h1_buttons.addWidget(btn_add_quest)
h1_buttons.addWidget(btn_clear)

v1_res = QVBoxLayout()
v1_res.addLayout(h1_question)
v1_res.addLayout(h1_buttons)
v1_res.addWidget(lb_header_stat)
v1_res.addWidget(lb_statistic)
v1_res.addWidget(btn_back)

menu_win.setLayout(v1_res)
menu_win.resize(600,500)