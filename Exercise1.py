def exercise_1_basics():
    course = "CMP 269"
    students = 30
    print(f"The course {course} has {students} students.")

def exercise_2_collections():
    colors = ["red", "orange", "yellow", "green", "blue"]
    colors.append("purple")

    student = {"name" : "Max", "gpa" : 4.0}

    print(colors)
    print(student)

def exercise_3_logic():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    evens = []

    for number in numbers:
        if number % 2 == 0:
            evens.append(number)

    print(evens)

if __name__ == "__main__":
    print("--- Exercise 1 ---")
    exercise_1_basics()
    print("\n--- Exercise 2 ---")
    exercise_2_collections()
    print("\n--- Exercise 3 ---")
    exercise_3_logic()
