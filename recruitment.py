def main():
    skills = ["programming", "teamwork", "swimming", "running", "boxing", "hiking"]
    cv = {}
    uname = input("Enter your name: ")
    cv["name"] = uname
    uage = input("Enter your age: ")
    cv["age"] = int(uage)
    uexperience = input("Enter years of experience: ")
    cv["experience"] = int(uexperience)
    cv["skills"] = []
    print("1."+skills[0]+" 2."+skills[1]+"  3."+skills[2]+"  4."+skills[3]+"  5."+skills[4]+"  6."+skills[5])
    choice1 = input("Choose a skill from above by entering its number: ")
    if choice1 == "1":
        cv["skills"]= "programming"
    elif choice1 == "2":
        cv["skills"]= "teamwork"
    elif choice1 == "3":
        cv["skills"]= "swimming"
    elif choice1 == "4":
        cv["skills"]= "running"
    elif choice1 == "5":
        cv["skills"]= "boxing"
    elif choice1 == "6":
        cv["skills"]= "hiking"

    choice2 = input("Choose another skill from above by entering its number: ")
    if choice2 == "1":
        cv["skills"]= "programming"
    elif choice2 == "2":
        cv["skills"]= "teamwork"
    elif choice2 == "3":
        cv["skills"]= "swimming"
    elif choice2 == "4":
        cv["skills"]= "running"
    elif choice2 == "5":
        cv["skills"]= "boxing"
    elif choice2 == "6":
        cv["skills"]= "hiking"

    if cv["age"] > 24 and cv["age"] < 41:
        if cv["experience"] > 4:
            if "hiking" in cv["skills"]:
                print("Congratulations "+uname+ " you were Accepted!")
            else:
                print("Sorry "+uname+ " you were Rejected")

        else:
            print("Sorry "+uname+ " you were Rejected")

    else:
        print("Sorry "+uname+ " you were Rejected")







if __name__ == '__main__':
    main()
