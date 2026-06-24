print("Student Average Calculator")

while True:
    name = input("Enter student name: ").strip()

    scores = []
    for i in range(3):
        while True:
            try:
                score = float(input(f"Enter score {i + 1}: "))
                if 0 <= score <= 100:
                    scores.append(score)
                    break
                print("Please enter a value between 0 and 100.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    average = sum(scores) / len(scores)
    print(f"{name}'s average is {average:.2f}")

    if average >= 50:
        print("Result: Pass")
    else:
        print("Result: Fail")

    choice = input("Continue? Select Y/N: ").strip().upper()
    if choice != "Y":
        break

print("Program Ended")
