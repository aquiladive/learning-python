#making use of dictionaries for a simple student attendance register

data_dict={"1":"Akash","2":"Ava","3":"Dinesh","4":"Dhruv","5":"Esha"}
record_dict={"1":[21,9],"2":[29,1],"3":[26,4],"4":[22,8],"5":[13,17]}
invalid=1

while True:
    print("Actions:")
    print("1) Mark attendance\t2) View attendance\t3) Exit\t")
    
    choice = int(input())

    if choice == 1:
        print("Give roll number of student.")
        rolln = input()
        for x in record_dict:
            if rolln == x:
                invalid=0
                print("Mark attendance with 'x' for present and 'o' for absent.")
                mark = input()
                if mark == "x":
                    record_dict[rolln][0]+=1
                elif mark == "o":
                    record_dict[rolln][1]+=1
                else:
                    print("Invalid. Try again.\n")
                present=record_dict[rolln][0]
                absent=record_dict[rolln][1]
                name=data_dict[rolln]
                print(name + " (Roll no: " + rolln + ")")
                print("Days present = ",present)
                print("Days absent = ",absent,"\n")
        if invalid == 1:
            print("Invalid roll number. Try again.")
    
    elif choice == 2:
        print("1) View particular\t2) View all")
        view_choice = int(input())
        if view_choice == 1:
            print("Give roll number of student.")
            rolln = input()
            for x in record_dict:
                if rolln==x:
                    invalid=0
                    present=record_dict[rolln][0]
                    absent=record_dict[rolln][1]
                    name=data_dict[rolln]
                    print(name + " (Roll no: " + rolln + ")")
                    print("Days present = ",present)
                    print("Days absent = ",absent,"\n")
            if invalid == 1:
                print("Invalid roll number. Try again.\n")
        elif view_choice == 2:
            for x in record_dict:
                present=record_dict[x][0]
                absent=record_dict[x][1]
                name=data_dict[x]
                print(name + " (Roll no: " + x + ")")
                print("Days present = ",present)
                print("Days absent = ",absent,"\n")
        else:
            print("Invalid choice. Try again.\n")
    
    elif choice == 3:
        break
    
    else:
        print("Error.\n")
