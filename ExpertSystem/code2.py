from experta import *

class patient(Fact):
    pass


class GoToDoctor(KnowledgeEngine):
    @Rule(patient(Headache="yes",Fatigue="yes",Increased_thirst="yes",Urinate_a_lot="yes"))
    def urinate_a_lot(self):
        print("You have symptoms of diabetes,You must do tests and see a specialist doctor")

    @Rule(patient(Headache="yes",Fatigue="yes",Increased_thirst="no",Feeling_dryness="yes"))
    def feeling_dryness(self):
        print("You have symptoms of diabetes, you must see a doctor ")

    @Rule(patient(Headache="yes",Fatigue="no",Tachycardia="yes",Blurred_vision="yes"))
    def Blurred_vision(self):
        print("You must do tests and see a specialist doctor")

    @Rule(patient(Headache="yes",Fatigue="no",Tachycardia="no",Shortness_of_breath="yes"))
    def Shortness_of_breath(self):
        print("You have symptoms of diabetes,You should check with the hospital to be sure")

    @Rule(patient(Headache="no",Dizzy="yes",Stressed_or_anxious="yes"))
    def stressed_or_anxious(self):
        print("You must make comprehensive checks to make sure")

    @Rule(patient(Headache="no",Dizzy="no",Sweating="yes"))
    def sweating(self):
        print("You should make sure that you get the necessary examinations from a specialist doctor")

def declare():
    headache= input("Do you have a headache: ").lower()
    if headache=="yes":
        fatigue=input("Do you feel Fatigue: ").lower()
        if fatigue=="yes":
            increased_thirst=input("Do you have increased thirst: ").lower()
            if increased_thirst=="yes":
                urinate_a_lot=input("Do you urinate a lot: ").lower()
                if urinate_a_lot=="yes": 
                 return patient(Headache="yes",Fatigue="yes",Increased_thirst="yes",Urinate_a_lot="yes")
            else:
                feeling_dryness=input("Do you feeling dryness in the tongue and throat: ").lower()
                return patient(Headache="yes",Fatigue="yes",Increased_thirst="no",Feeling_dryness="yes")
        else:
            tachycardia=input("Do you fell a Tachycardia: ").lower()
            if tachycardia=="yes":
                blurred_vision=input("Do you have Blurred vision: ").lower()
                return patient(Headache="yes",Fatigue="no",Tachycardia="no",Shortness_of_breath="yes")
            else:
                shortness_of_breath=input("Do you have Shortness of breath: ").lower()
                return patient(Headache="yes",Fatigue="no",Tachycardia="no",Shortness_of_breath="yes")
    else:
        dizzy=input("Do you feel Dizzy: ").lower()
        if dizzy=="yes":
            stressed_or_anxious=input("Do you feel stressed or anxious: ").lower()
            return patient(Headache="no",Dizzy="yes",Stressed_or_anxious="yes")
        else:
            sweating=input("Do you feel sweating: ").lower()
            return patient(Headache="no",Dizzy="no",Sweating="yes")


engine = GoToDoctor()
engine.reset()
engine.declare(declare())
engine.run()

