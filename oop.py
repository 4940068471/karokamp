class Dog:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color


    def bark(self):
        print("woofs!")
        print(self.name + ": " + "Woofs!")



# dog_1 = Dog(name="Jessie", age=4, color="Black")
# dog_1.bark() 
# # print(dog_1.name) 
# dog_2= Dog(name="bella",age=2, color="white") 
# dog_2.bark() 
class GermanDog(Dog):
    # def __init__(self, name, age, color):
        # self.name = name
    #     self.age = age
    #     self.color = color
        
    def bark(self):
        print(self.name + ": " + "Woofs!")
        
    def search(self):
        print("I'm searching for humans")
        
    def eat (self,food):
        print(self.name + ": " + "I'm eating " + food)
        self.bark()


gdog = GermanDog(name="Max", age=10, color="Brown")

gdog.search() 
gdog.eat("meat")  