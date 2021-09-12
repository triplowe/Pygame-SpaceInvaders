def main():
    courses = {"CS101": ["3004", "Haynes", "8:00 a.m."],
              "CS102": ["4501", "Alvarado", "9:00 a.m."],
              "CS103": ["6755", "Rich", "10:00 a.m."],
              "NT110": ["1244", "Burke", "11:00 a.m."],
              "CM241": ["1411", "Lee", "1:00 p.m."]}   

    list_of_keys = list(courses)
    courseNumber = input("What course would you like to select?")

    for key in list_of_keys:
        if key == courseNumber:
            print("Room Number: ", courses[key][0])
            print("Instructor: ", courses[key][1])
            print("Meeting Time: ", courses[key][2])

main()