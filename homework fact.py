# x=int(input("enter x:"))
# y=1
# for i in range (1,x+1):
#     y*=i
#     print(f"fact={y}")
# number= int(input("enter number:"))
# sum=0
# for i in range (1, number//2+1):
#     if number % i == 0:
#         sum += i
# if sum == number:
#     print("it is a compelet number")
# else:
#     print("it is not compelet")

number=int(input("enter number:"))
a=2
for i in range(1, number+1):
    if(number % i==0):
        a +=1
        if a ==2:
            print("it is prime")
else:
    print("it is not prime")