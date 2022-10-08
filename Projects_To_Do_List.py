def Projects_To_Do_List():
    Running = True
    while Running:
        import pickle
        try:
            Projects = pickle.load(open("Projects.dat","rb"))
        
        except:
            new_file = open("Projects.dat", "wb")
            new_file.close()
            Projects = ""
        print("Welcome to projects to do list!")
        while True:
            choice = input("Enter 'a' for adding a project, 'r' for removing a project, 'v' for vewing all the stored projects and 'e' for exiting: ").lower()
            if choice == 'a':
                print(f"The projects present are: {Projects}")
                while True:
                    amount = input("How many Projects do you want to add? ")
                    if amount.isdigit():
                        amount = int(amount)
                        break
                    else:
                        print("Invalid input! Please try again!")
                for i in range(amount):
                    add = input("Enter the name of the project you want to add: ")
                    Projects.append(add)
                print(f"Now the projects present are: {Projects}")
                break
            elif choice == 'r':
                print(f"The avalable projects are: {Projects}")
                while True:
                    amount = input("How many Projects do you want to remove? ")
                    if amount.isdigit():
                        amount = int(amount)
                        break
                    else:
                        print("Invalid input! Please try again!")
                for i in range(amount):
                    remove = input("Enter the name of the project you want to remove: ")
                    Projects.remove(remove)
                print(f"Now the projects present are: {Projects}")
                break
            elif choice == 'v':
                print(f"The projects are: {Projects}")
                break
            elif choice == 'e':
                print("Thank you for using!.")
                pickle.dump(Projects,open("Projects_To_Do_List/Projects.dat","wb"))
                break
            else:
                print("Invalid input! Please try again!")
        if choice == 'e':
            break
        pickle.dump(Projects,open("Projects.dat","wb"))
        while True:
            Again=input("Do you want to edit again? (y/n)").lower()
            if Again == 'y':
                break
            elif Again == 'n':
                Running = False
                print("Thank you for using!.")
                break
            else:
                print("Invalid input! Please try again!")
Projects_To_Do_List()