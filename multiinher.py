class Father:
    def skill(self):
        print("garding,programming")
class Mother:
    def skill(self):
        print("cooking,art")
class Child1(Father,Mother):
    def skill(self):
        print("sports")
        Father.skill(self)
        Mother.skill(self)
class Child2(Father,Mother):
    def skill(self):
        print("editing")
        Father.skill(self)
        Mother.skill(self)

c=Child1()
c.skill()
c=Child2()
c.skill()
    