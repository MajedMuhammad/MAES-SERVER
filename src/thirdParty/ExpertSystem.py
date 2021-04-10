from experta import *

class patient(Fact):
    pass


class GoToDoctor(KnowledgeEngine):
    @Rule(patient(Headache="yes",Fatigue="yes",Increased_thirst="yes",Urinate_a_lot="yes"))
    def urinate_a_lot(self):
        print("You have symptoms of diabetes")

    @Rule(patient(Headache="yes",Fatigue="yes",Increased_thirst="no",Feeling_dryness="yes"))
    def feeling_dryness(self):
        print("You have symptoms of diabetes")

    @Rule(patient(Headache="yes",Fatigue="no",Tachycardia="yes",Blurred_vision="yes"))
    def Blurred_vision(self):
        print("You have symptoms of diabetes")

    @Rule(patient(Headache="yes",Fatigue="no",Tachycardia="no",Shortness_of_breath="yes"))
    def Shortness_of_breath(self):
        print("You have symptoms of diabetes")

    @Rule(patient(Headache="no",Dizzy="yes",Stressed_or_anxious="yes"))
    def stressed_or_anxious(self):
        print("You must see a specialist doctor")

    @Rule(patient(Headache="no",Dizzy="no",Sweating="yes"))
    def sweating(self):
        print("You must see a specialist doctor")

def declare():
    headache=input("Do you have a headache: ")
    if headache=="yes":
        fatigue=input("Do you feel Fatigue: ")
        if fatigue=="yes":
            increased_thirst=input("Do you have increased thirst: ")
            if increased_thirst=="yes":
                urinate_a_lot=input("Do you urinate a lot: ")
                if urinate_a_lot=="yes": 

               
                 return patient(Headache="yes",Fatigue="yes",Increased_thirst="yes",Urinate_a_lot="yes")
            else:
                feeling_dryness=input("Do you feeling dryness in the tongue and throat: ")
                return patient(Headache="yes",Fatigue="yes",Increased_thirst="no",Feeling_dryness="yes")
        else:
            tachycardia=input("Do you fell a Tachycardia: ")
            if tachycardia=="yes":
                blurred_vision=input("Do you have Blurred vision: ")
                return patient(Headache="yes",Fatigue="no",Tachycardia="no",Shortness_of_breath="yes")
            else:
                shortness_of_breath=input("Do you have Shortness of breath: ")
                return patient(Headache="yes",Fatigue="no",Tachycardia="no",Shortness_of_breath="yes")
    else:
        dizzy=input("Do you feel Dizzy: ")
        if dizzy=="yes":
            stressed_or_anxious=input("Do you feel stressed or anxious: ")
            return patient(Headache="no",Dizzy="yes",Stressed_or_anxious="yes")
        else:
            sweating=input("Do you feel sweating: ")
            return patient(Headache="no",Dizzy="no",Sweating="yes")


engine = GoToDoctor()
engine.reset()
engine.declare(declare())
engine.run()
