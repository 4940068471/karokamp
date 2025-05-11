students=[]
first_name= input("enter first-name:")
last_name=input("enter last_name:")
birth_year= int(input("enter birth_year:"))
student1= {"first_name":first_name, "last_name":last_name, "birth_year":birth_year}
students.append(student1)
first_name= input("enter first-name:")
last_name=input("enter last_name:")
birth_year= int(input("enter birth_year:"))
student2= {"first_name":first_name, "last_name":last_name, "birth_year":birth_year}
students.append(student2)
print(students)
full_name_student1=students[0]["first_name"]+""+students[0]["last_name"]
full_name_student1= full_name_student1.upper()
age_student1=2025-students[0]["birth_year"]
full_name_student2= students[1]["first_name"]+""+students[1]["last_name"]
full_name_student2= full_name_student2.upper()
age_student2= 2025- students[1]["birth_year"]
print(full_name_student1)
print(age_student1)
print(full_name_student2)
print(age_student2)
ages=[age_student1,age_student2]
age_avg=sum(ages)/len(ages)
print(age_avg)