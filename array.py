scores = [65, 80, 45, 90, 70]

while True:
    print("\n===== STUDENT SCORES ARRAY =====")
    print("1. Display Scores")
    print("2. Search Score")
    print("3. Add New Score")
    print("4. Sort Scores")
    print("5. Delete Score")
    print("6. Calculate Average")
    print("7. Exit")

    choice = int(input("Enter your choice (1-7): "))

    if choice == 1:
        print("Student Scores:", scores)

    elif choice == 2:
        score = int(input("Enter score to search: "))

        if score in scores:
            print("Score found at index:", scores.index(score))
        else:
            print("Score not found!")

    elif choice == 3:
        score = int(input("Enter new score: "))
        scores.append(score)
        print("Score added successfully!")
        print("Updated Scores:", scores)

    elif choice == 4:
        scores.sort()
        print("Sorted Scores:", scores)

    elif choice == 5:
        score = int(input("Enter score to delete: "))

        if score in scores:
            scores.remove(score)
            print("Score deleted successfully!")
            print("Updated Scores:", scores)
        else:
            print("Score not found!")

    elif choice == 6:
        average = sum(scores) / len(scores)
        print("Average Score:", average)

    elif choice == 7:
        print("Program closed successfully!")
        break

    else:
        print("Invalid choice! Please try again.")        
