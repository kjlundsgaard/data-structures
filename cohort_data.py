def unique_houses(filename):
    """TODO: Create a set of student houses.

    Iterates over the cohort_data.txt file to look for all of the included house names
    and creates a set called 'houses' that holds those names.

        ex. houses = set([ "Hufflepuff",
                    "Slytherin",
                    "Ravenclaw",
                    "Gryffindor",
                    "Dumbledore's Army",
                    "Order of the Phoenix"
            ])

    """

    houses = set()

    # Code goes here
    house_file = open(filename)
    for line in house_file:
        data = line.split("|")
        house = data[2]
        if house != "":
            houses.add(house)

    house_file.close()

    return houses

print unique_houses("cohort_data.txt")


def sort_by_cohort(filename):
    """TODO: Sort students by cohort.

    Iterates over the data to create a list for each cohort, ordering students
    alphabetically by first name and tas separately. Returns list of lists.

        ex. winter_15 = ["alice tsao", "amanda gilmore", "anne vetto", "..." ]
        ex. all_students = [winter_15, spring_15, summer_15, tas]

    """

    all_students = []
    winter_15 = []
    spring_15 = []
    summer_15 = []
    tas = []

    # Code goes here
    house_file = open(filename)
    for line in house_file:
        line = line.rstrip()
        data = line.split("|")
        cohort = data[4]
        student = data[0] + " " + data[1]
        if cohort == "I":
            pass
        elif cohort == "TA":
            tas.append(student)
        else:
            if cohort == "Winter 2015":
                winter_15.append(student)
            elif cohort == "Spring 2015":
                spring_15.append(student)
            else:
                summer_15.append(student)

    all_students = [winter_15, spring_15, summer_15, tas]
        

    house_file.close()

    return all_students

print sort_by_cohort("cohort_data.txt")

def students_by_house(filename):
    """TODO: Sort students by house.

    Iterate over the data to create a list for each house, and sort students
    into their appropriate houses by last name. Sort TAs into a list called "tas"
    and instructors in to a list called "instructors".
    Return all lists in one list of lists.
        ex. hufflepuff = ["Gaikwad", "Le", "..." ]
        ex. tas = ["Bryant", "Lefevre", "..."]
        ex. all_students = [ hufflepuff,
                        gryffindor,
                        ravenclaw,
                        slytherin,
                        dumbledores_army,
                        order_of_the_phoenix,
                        tas,
                        instructors
            ]
    """

    all_students = []
    gryffindor = []
    hufflepuff = []
    slytherin = []
    dumbledores_army = []
    order_of_the_phoenix = []
    ravenclaw = []
    tas = []
    instructors = []

    # Code goes here
    house_file = open(filename)
    for line in house_file:
        line = line.rstrip()
        data = line.split("|")
        house = data[2]
        cohort = data[4]
        student = data[0] + " " + data[1]
        if cohort == "I":
            instructors.append(student)
        elif cohort == "TA":
            tas.append(student)
        else:
            if house == "Gryffindor":
                gryffindor.append(student)
            elif house == "Slytherin":
                slytherin.append(student)
            elif house == "Order of the Phoenix":
                order_of_the_phoenix.append(student)
            elif house == "Hufflepuff":
                hufflepuff.append(student)
            elif house == "Ravenclaw":
                ravenclaw.append(student)
            else:
                dumbledores_army.append(student)

    all_students = [hufflepuff, gryffindor, ravenclaw, slytherin, dumbledores_army, order_of_the_phoenix, tas, instructors]
        

    house_file.close()

    return all_students

print students_by_house("cohort_data.txt")


def all_students_tuple_list(filename):
    """TODO: Create a list of tuples of student data.

    Iterates over the data to create a big list of tuples that individually
    hold all the data for each person. (full_name, house, advisor, cohort)
        ex. all_people = [
                ("Alice Tsao", "Slytherin", "Kristen", "Winter 2015"),
                ("Amanda Gilmore", "Hufflepuff", "Meggie", "Winter 2015"),
                # ...
            ]
    """

    student_list = []

    # Code goes here

    house_file = open(filename)
    for line in house_file:
        line = line.rstrip()
        data = line.split("|")
        house = data[2]
        cohort = data[4]
        student = data[0] + " " + data[1]
        advisor = data[3]
        student_list.append((student, house, advisor, cohort))

    house_file.close()

    return student_list

print all_students_tuple_list("cohort_data.txt")



def find_cohort_by_student_name(student_list):
    """TODO: Given full name, return student's cohort.

    Use the above list of tuples generated by the preceding function to make a small
    function that, given a first and last name, returns that student's cohort, or returns
    'Student not found.' when appropriate. """

    # Code goes here
    student_name = raw_input("Student name: ")
    for student in student_list:
        if (student[3] == "I" or student[3] == "TA") and student_name == student[0]:
            return "Student not found"
        else:
            if student_name == student[0]:
                return student[3]



print find_cohort_by_student_name(all_students_tuple_list("cohort_data.txt"))


##########################################################################################
# Further Study Questions


def find_name_duplicates(filename):
    """TODO: Using set operations, make a set of student first names that have duplicates.

    Iterates over the data to find any first names that exist across multiple cohorts.
    Uses set operations (set math) to create a set of these names.
    NOTE: Do not include staff -- or do, if you want a greater challenge.

       ex. duplicate_names = set(["Sarah"])

    """

    duplicate_names = set()

    # Code goes here
    all_students = []
    gryffindor = []
    hufflepuff = []
    slytherin = []
    dumbledores_army = []
    order_of_the_phoenix = []
    ravenclaw = []
    tas = []
    instructors = []

    # Code goes here
    house_file = open(filename)
    for line in house_file:
        line = line.rstrip()
        data = line.split("|")
        house = data[2]
        cohort = data[4]
        student = data[0]
        if cohort == "I":
            instructors.append(student)
        elif cohort == "TA":
            tas.append(student)
        else:
            if house == "Gryffindor":
                gryffindor.append(student)
            elif house == "Slytherin":
                slytherin.append(student)
            elif house == "Order of the Phoenix":
                order_of_the_phoenix.append(student)
            elif house == "Hufflepuff":
                hufflepuff.append(student)
            elif house == "Ravenclaw":
                ravenclaw.append(student)
            else:
                dumbledores_army.append(student)

    all_students = [hufflepuff, gryffindor, ravenclaw, slytherin, dumbledores_army, order_of_the_phoenix, tas, instructors]
        

    house_file.close()

    for student_house in all_students:
        house_names_set = set()
        for item in student_house:
            house_names_set.add(item)

            # trying to put names of individual houses into indiv sets

    for group in house_names_set:



    return duplicate_names


def find_house_members_by_student_name(student_list):
    """TODO: Create a function that prompts the user for a name via the command line
    and when given a name, print a statement of everyone in their house in their cohort.

    Use the list of tuples generated by all_students_tuple_list to make a small function
    that, when given a student's first and last name, print students that are in both
    that student's cohort and that student's house."""

    # Code goes here

    return


#########################################################################################

# Here is some useful code to run these functions!

# print unique_houses("cohort_data.txt")
# print sort_by_cohort("cohort_data.txt")
# print students_by_house("cohort_data.txt")
# all_students_data = all_students_tuple_list("cohort_data.txt")
# print all_students_data
# find_cohort_by_student_name(all_students_data)
# print find_name_duplicates("cohort_data.txt")
# find_house_members_by_student_name(all_students_data)
