listy = [420, 67, 69, 41, 21]

for i in listy:
    print(i)

days = ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")

victorDictor = {
    "Title": "Lord of the Rings",
    "Author": "JRR Tolkein",
}

students = ["John James", "John Jacob", "John Backflip", "Jack Frontflip", "Timmy ToughKnuckles"]
students.append("John Backflip")
students = set(students)

studentTracker = dict(zip(students, listy))
for stud in studentTracker:
    if studentTracker[stud] >= 70:
        print(stud)