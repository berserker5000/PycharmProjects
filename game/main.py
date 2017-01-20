__author__ = 'kud'

import random

from kivy.uix.gridlayout import GridLayout
from kivy.app import App

import con_to_db

used_questions_id = []


def monkey_q():
    question = con_to_db.print_from_db("Questions")
    return (question)


def monkey_a():
    answer = {1: "Give a banana to monkey.", 2: "Shut her down with pistol.", 3: "Kiss monkey.",
              4: "Sing a sleeping song for monkey."}
    return answer.values()


class Application(GridLayout):
    pass


class MyApp(App):


    def questions(self):
        q = con_to_db.build_dicts("Questions")
        question_id = []
        self.q_id = random.randint(1, len(q))
        question_id.append(self.q_id)
        question_q = q.get(self.q_id)
        for el in question_id:
            if el in used_questions_id:
                print(used_questions_id)
                print "id in list already"
            else:
                used_questions_id.append(question_id)
        # print("q_id:" + self.q_id)
        return question_q

    def loadtobtn1(self):
        self.Label_text = str(self.questions())
        return self.Label_text

    def btn1(self):
        a1 = con_to_db.build_dicts("Correct1")
        self.Button_text1 = str(monkey_a()[random.randrange(len(monkey_a()))])
        return self.Button_text1

    def btn2(self):
        a2 = con_to_db.build_dicts("Correct2")
        #get_answer = a2.get(self.q_id)
        self.Button_text2 = str()#get_answer)
        return self.Button_text2

    def btn3(self):
        a3 = con_to_db.build_dicts("Correct3")
        self.Button_text3 = str(monkey_a()[random.randrange(len(monkey_a()))])
        return self.Button_text3

    def btn4(self):
        a4 = con_to_db.build_dicts("inCorrect")
        self.Button_text4 = str(monkey_a()[random.randrange(len(monkey_a()))])
        return self.Button_text4

    def build(self):
        return Application()


MyApp().run()
