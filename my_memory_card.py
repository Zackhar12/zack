#создай приложение для запоминания информации
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout,QGroupBox,QRadioButton,QHBoxLayout
from random import randint

class Question():
    def __init__(
        self,question,right_answer,
        wrong1,wrong2,wrong3):
        self.question = question
        self.right_answer =right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

question_list = []
question_list.append(Question('Как называется еврейский Новый год? ','Ханука','Рош ха-Шана ','Йом Кипур','Кванза'))
question_list.append(Question('Какая самая редкая группа крови?','I группа',' IV группа','II группа','III группа'))
question_list.append(Question('Fe — это символ какого химического элемента?','Водород','Железо','Фтор','Цинк'))
question_list.append(Question('Какая африканская страна раньше называлась Абиссинией?','Зимбабве','Эфиопия ','ЮАР','Того'))

def show_guestion():
    ansGroup.hide()
    RadioGroupBox.show()
    btn_OK.setText('Ответить')
    
def show_result():
    RadioGroupBox.hide()    
    ansGroup.show()
    btn_OK.setText('следующий вопрос')
def show_test():
    if btn_OK.text() == 'Ответить':
        show_result()
    else:
        show_guestion()   

def ask(q:Question):
    
    show_guestion()

app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('mremory card')
text = QLabel('какой национальности не существует?')
main_win.resize(500,300)


lb_Questin = QLabel('Question')
layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()
layout_line5 = QVBoxLayout()
main_layout = QVBoxLayout() 
layout_line1.addWidget(lb_Questin, alignment = (Qt.AlignCenter | Qt.AlignVCenter))
buttons = [btn_answer1,btn_answer2,btn_answer3,btn_answer4]
RadioGroupBox = QGroupBox('Как называется еврейский Новый год?')
btn_answer1 = QRadioButton('Ханука')
btn_answer2 = QRadioButton('Рош ха-Шана')
btn_answer3 = QRadioButton('Йом Кипур')
btn_answer4 = QRadioButton('Кванза')
layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()


layout_ans2.addWidget(btn_answer1)
layout_ans2.addWidget(btn_answer2)
layout_ans3.addWidget(btn_answer3)
layout_ans3.addWidget(btn_answer4)
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)
ansGroup = QGroupBox('Ответ')
is_correct = QLabel('')
lb_ans = QLabel('')
RadioGroupBox.setLayout(layout_ans1)
layout_line2.addWidget(RadioGroupBox,alignment= Qt.AlignCenter)
layout_line2.addWidget(ansGroup,alignment= Qt.AlignCenter)
ansGroup.hide()
btn_OK = QPushButton('Ответить')
layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch=2)
layout_line3.addStretch(1)
layout_line5.addWidget(lb_ans)
layout_line5.addWidget(is_correct)
btn_OK.clicked.connect(show_test)
layout_card = QVBoxLayout()
layout_card.setSpacing(5)
layout_card.addLayout(layout_line1)
layout_card.addLayout(layout_line2)
layout_card.addLayout(layout_line3)
main_win.setLayout(layout_card)














































































main_win.show()
app.exec_()