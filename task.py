def average(scores):
    return sum(scores) / 3

def grade(average):
    if average >= 90:
        return 'A'
    elif 80 <= average < 90:
        return 'B'
    elif 70 <= average < 80:
        return 'C'
    elif 60 <= average < 70:
        return 'D'
    else:
        return 'F'

def getScores():
    return [
        float(input("Enter score 1: ")),
        float(input("Enter score 2: ")),
        float(input("Enter score 3: "))
    ]

def display(name, average, grade):
    print(f"\nStudent: {name}")
    print(f"Average Score: {average:.2f}")
    print(f"Grade: {grade}\n")

# main fun
students = int(input("Enter the number of students: "))
for x in range(students):
    name = input("Enter student name: ")
    scores = getScores()
    av = average(scores)
    g=grade(av)
    display(name, av, g)