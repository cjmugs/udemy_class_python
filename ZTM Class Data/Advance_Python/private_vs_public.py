# Test code for Kayak Trips Data
class Crew_Member:
    def __init__(self, name, paddleyear):
       self.name = name
       self.paddleyear = paddleyear

    def member(self):
        print(f'Crew Member name {self.name} and years paddling {self.paddleyear}')

#Instanced the class 
crew1 = Crew_Member('Chris' , 10)
crew2 = Crew_Member('Steve' , 7)
crew3 = Crew_Member('Scott' , 7)
crew4 = Crew_Member('Ben' , 5)
crew5 = Crew_Member('Robbie' , 4)

# Call the instance and method
crew1.member()
crew2.member()
crew3.member()
crew4.member()
crew5.member()