#import random
n = int(input("How many sticks (N) in thr pile: "))
print("There are", n, "sticks in the pile.")
name = (input("What is your name:"))
a = n%3
if a == 1 :
    time = 2
elif a == 2 :
    time = 1
else :
    time = 1

while n > 0 :
    if time%2 == 0:
        x = int(input("{},how many sticks you will take (1 or 2): ".format(name)))
        if  1 <= x <= 2 and n >= x :
            n = n-x
            time = time + 1
            if n == 0 :
                print("{},take the last stick.".format(name))
                print("\n\nI,smart computer, win!!!")
            else :
                print("There are", n, "sticks in the pile")
        elif x > 2 :
            print("No you cannot take more than 2 sticks! ")
        elif x > n :
            print("There are no enough sticks to take.") 
        else :
            print("No you cannot take less than 1 stick! ")
    elif time == 1 and a == 2 :
         y=1
         print("\nI,smart computer, take: ", y)
         if  1 <= y <= 2 and n >= y :
             n = n-y
             time = time + 1
             if n == 0 :
                 print("I,smart computer, take the last stick.")
                 print("\n\n{} win (I,smart computer, am sad T_T)".format(name))
             else :
                 print("There are", n, "sticks in the pile")
         elif y > 2 :
             print("No you cannot take more than 2 sticks! ")
         elif y > n :
             print("There are no enough sticks to take.") 
         else :
             print("No you cannot take less than 1 stick! ")
    elif time == 1 and a == 0 :
         y=2
         print("\nI,smart computer, take: ", y)
         if  1 <= y <= 2 and n >= y :
             n = n-y
             time = time + 1
             if n == 0 :
                 print("I,smart computer, take the last stick.")
                 print("\n\n{} win (I,smart computer, am sad T_T)".format(name))
             else :
                 print("There are", n, "sticks in the pile")
         elif y > 2 :
             print("No you cannot take more than 2 sticks! ")
         elif y > n :
             print("There are no enough sticks to take.") 
         else :
             print("No you cannot take less than 1 stick! ")
    else:
        if x == 1:
         y=2
         print("\nI,smart computer, take: ", y)
         if  1 <= y <= 2 and n >= y :
             n = n-y
             time = time + 1
             if n == 0 :
                 print("I,smart computer, take the last stick.")
                 print("\n\n{} win (I,smart computer, am sad T_T)".format(name))
             else :
                 print("There are", n, "sticks in the pile")
         elif y > 2 :
             print("No you cannot take more than 2 sticks! ")
         elif y > n :
             print("There are no enough sticks to take.") 
         else :
             print("No you cannot take less than 1 stick! ")
        else :
         y=1
         print("\nI,smart computer, take: ", y)
         if  1 <= y <= 2 and n >= y :
             n = n-y
             time = time + 1
             if n == 0 :
                 print("I,smart computer, take the last stick.")
                 print("\n\n{} win (I,smart computer, am sad T_T)".format(name))
             else :
                 print("There are", n, "sticks in the pile")
         elif y > 2 :
             print("No you cannot take more than 2 sticks! ")
         elif y > n :
             print("There are no enough sticks to take.") 
         else :
             print("No you cannot take less than 1 stick! ")