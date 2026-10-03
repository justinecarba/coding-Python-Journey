
import pandas as pd

matriculation = {
    "Monday" : [],
    "Tuesday" : [],
    "Wednesday" : [],
    "Thursday" : [],
    "Friday" : [],
    "Saturday" : [],
    "Sunday" : [],
    "Time" : []
}



def add_subject():
    add_sub = input("Enter subject : ")
    add_day = input("Enter the day : ")
    add_time = input("Enter the time : ")

    if add_sub == "" and add_day == "" and add_time == "":
        print("Missing some items!")

    elif add_sub.isdigit():
        print("Subject should be word!!")

    elif add_day.isdigit():
        print("Day should be follow the day week")

    elif not add_time.isdigit():
        print("Time should be number!!")

    else:
        subject = ""
        
        if add_day == "Monday":
            matriculation['Monday'].append(add_sub)
            matriculation['Tuesday'].append(subject)
            matriculation['Wednesday'].append(subject)
            matriculation['Thursday'].append(subject)
            matriculation['Friday'].append(subject)
            matriculation['Saturday'].append(subject)
            matriculation['Sunday'].append(subject)
            matriculation['Time'].append(add_time)
            print("ADDED SUCCESSFULLY!!")

        elif add_day == "Tuesday":
            matriculation['Tuesday'].append(add_sub)
            matriculation['Monday'].append(subject)
            matriculation['Wednesday'].append(subject)
            matriculation['Thursday'].append(subject)
            matriculation['Friday'].append(subject)
            matriculation['Saturday'].append(subject)
            matriculation['Sunday'].append(subject)
            matriculation['Time'].append(add_time)
            print("ADDED SUCCESSFULLY!!")

        elif add_day == "Wednesday":
            matriculation['Wednesday'].append(add_sub)
            matriculation['Monday'].append(subject)
            matriculation['Tuesday'].append(subject)
            matriculation['Thursday'].append(subject)
            matriculation['Friday'].append(subject)
            matriculation['Saturday'].append(subject)
            matriculation['Sunday'].append(subject)
            matriculation['Time'].append(add_time)
            print("ADDED SUCCESSFULLY!!")

        elif add_day == "Thursday":
            matriculation['Thursday'].append(add_sub)
            matriculation['Monday'].append(subject)
            matriculation['Tuesday'].append(subject)
            matriculation['Wednesday'].append(subject)
            matriculation['Friday'].append(subject)
            matriculation['Saturday'].append(subject)
            matriculation['Friday'].append(subject)
            matriculation['Time'].append(add_time)
            print("ADDED SUCCESSFULLY!!")

        elif add_day == "Friday":
            matriculation['Friday'].append(add_sub)
            matriculation['Monday'].append(subject)
            matriculation['Tuesday'].append(subject)
            matriculation['Wednesday'].append(subject)
            matriculation['Thursday'].append(subject)
            matriculation['Saturday'].append(subject)
            matriculation['Sunday'].append(subject)
            matriculation['Time'].append(add_time)
            print("ADDED SUCCESSFULLY!!")

        elif add_day == "Saturday":
            matriculation['Saturday'].append(add_sub)
            matriculation['Monday'].append(subject)
            matriculation['Tuesday'].append(subject)
            matriculation['Wednesday'].append(subject)
            matriculation['Thursday'].append(subject)
            matriculation['Friday'].append(subject)
            matriculation['Sunday'].append(subject)
            matriculation['Time'].append(add_time)
            print("ADDED SUCCESSFULLY!!")

        else:
            matriculation['Sunday'].append(add_sub)
            matriculation['Monday'].append(subject)
            matriculation['Tuesday'].append(subject)
            matriculation['Wednesday'].append(subject)
            matriculation['Thursday'].append(subject)
            matriculation['Friday'].append(subject)
            matriculation['Saturday'].append(subject)
            matriculation['Time'].append(add_time)
            print("ADDED SUCCESSFULLY!!")


def view_matriculation():
    print("\n******************************************")
    print("              YOUR MATRICULATION          ")
    print("******************************************")
    df = pd.DataFrame(matriculation)
    print(df)
    print("******************************************")


def exit():

    exiting = input("Add Again? y/n : ").lower() .strip()

    if exiting == "y" and exiting != "n":
        print("Exiting the program.....")
        running = False


running = True

while running:
    print("\n*****************************************************")
    print("                    MATRICULATION DATA               ")
    print("*****************************************************")
    print("1. Add Subject")
    print("2. View Matriculation")
    print("3. Exit")
    print("*****************************************************")

    choice = input("Enter your choice (1-3) : ")

    if choice == "1":
        add_subject()

    elif choice == "2":
        view_matriculation()

    elif choice == "3":
        exit()
        running = False

    else:
        print("Invalid Choice!!")