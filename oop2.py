import cryptocode

class Person:
    total_persons=0
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        Person.total_persons+=1


    def signup(self, email, password):
        self.email = email
        self.password = cryptocode.encrypt(password, "!@#$")  
        
    def __decrypt_password(self) ->str: 
        return cryptocode.decrypt(self.password, "!@#$")   
    
    
    def change_password(self,old_password, new_password):  
        if old_password==self.__decrypt_password() :
            self.password = cryptocode.encrypt(new_password,"!@#$")
        else:
            print("wrong password")
    @staticmethod
    def get_total_persons():
        print(f"Total number of persons is: {Person.total_persons}")
    
    def __str__(self):
        return f"{self.first_name} {self.last_name} is {self.age} years old."

p1= Person("ahmad","ghafari",32)
# print(p1)
# p1.signup("ahmad.ghafari@gmail.com", "123456")
# print(p1.email)
# print(p1.password)
# print("----------------")
# # p1.change_password("123455","123456789")
# p1.change_password("123456","123456789")
# print(p1.password)



# print(p1.decrypt_password())
p2= Person("eli","ghafari",34)
# print(Person.total_persons)
p3= Person("ali" ,"ahmadi",45) 
Person.get_total_persons()
