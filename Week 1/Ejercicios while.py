

nombre= input("Write your First name: ")
count=0

while count < 4:
    if nombre == "Danny":
        apellido= input("Write your last Name: ")
        apellido= input("Write your Last name again: ")
        
    elif count != 3:
        print(f"You can only try 3 times, Time: {count + 1} ")
        nombre= input("Write your First name again: ")
        count +=1
    else:
        print("Sorry you have been blocked")
        count +=1
