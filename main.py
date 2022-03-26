import random

class Student:
    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.status = True

    def to_study(self):
        print("Time to study")
        self.progress += 0.12
        self.gladness -= 3 # self.gladness = self.gladness - 3

    def to_sleep(self):
        print("time to sleep")
        self.gladness += 3

    def to_chill(self):
        print("Time to chill")
        self.gladness += 5
        self.progress -= 0.1


    def check(self):
        if self.progress < -0.3:
            print("Тебе вигнали з універу")
            self.status = False
        elif self.gladness <= 0:
            print("я покидаю, гг, команда раків")
            self.status = False
        elif self.progress >= 5:
            print("Ти занадто розумний для цього універу")
            self.status = False

    def end_of_day(self):
        print(f"Gladness = {self.gladness}")
        print(f"Progress = {round(self.progress, 2)}")

    def live(self, day):
        day = "Day " + str(day) + " of " + self.name + " life"
        print(day)
        rand = random.randint(1, 3)
        if rand == 1:
            self.to_study()
        elif rand == 2:
            self.to_sleep()
        elif rand == 3:
            self.to_chill()
        self.end_of_day()
        self.check()

student = Student("Taras")

for day in range(365):
    if student.status == False:
        break
    student.live(day)