"""dummy system of washing machine---7000kg
invalid input---0 weight in washing machine
0-2000kg ----25 minutes
2001-4000kg---35minutes
4001-7000kg----45 minutes
overloded
"""
weight=int(input("enter weight"))
if(weight<=0):
    print("Invalid input")
elif(weight>0 and weight<=2000):
    print("time Estimated : 25 minutes")
elif(weight>2000 and weight<=4000):
    print("time Estimated : 35 minutes")
elif(weight>4000 and weight<=7000):
    print("time Estimated : 45 minutes")
else:
    print("overloded")