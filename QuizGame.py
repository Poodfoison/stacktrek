correct = 0

answer_list = ["Software Engineering", "Computer Science", "Information Technology", "Architecture", "Softwarea is developed or engineered", "Software doesn't wear out", "Software can be custom built", "All of the above", "A set of programs, documentation & configuration of data", "A set of programs", "Documentation and configuration of data", "None of the mentioned", "Simplicity", "Accessibilitys", "Application of engineering principles to the design a software","All of the above", "Designing a software", "Testing a software", "Modularity", "None of the above"]

print(f"Multiple Choice")
print(f"\nThe following answers are in multiple choice.")

print(f"\nWhat is a systematic engineering approach to software development?.")
print(f"a. {answer_list[0]} \nb. {answer_list[1]} \nc. {answer_list[2]} \nd. {answer_list[3]}")
choice = input("Enter your answer:")
if choice == 'a' or choice == 'A':
  correct += 1
else:
  correct += 0

print(f"\nWhat are the characteristics of software?")
print(f"a. {answer_list[4]} \nb. {answer_list[5]} \nc. {answer_list[6]} \nd. {answer_list[7]}")
choice = input("Enter your answer:")
if choice == 'd' or choice == 'D':
  correct += 1
else:
  correct += 0

print(f"\nSoftware is defined as ___________")
print(f"a. {answer_list[8]} \nb. {answer_list[9]} \nc. {answer_list[10]} \nd. {answer_list[11]}")
choice = input("Enter your answer:")
if choice == 'a' or choice == 'A':
  correct += 1
else:
  correct += 0

print(f"\nWhat are the features of Software Code?")
print(f"a. {answer_list[12]} \nb. {answer_list[13]} \nc. {answer_list[14]} \nd. {answer_list[15]}")
choice = input("Enter your answer:")
if choice == 'c' or choice == 'C':
  correct += 1
else:
  correct += 0

print(f"\nWhat is Software Engineering?")
print(f"a. {answer_list[16]} \nb. {answer_list[17]} \nc. {answer_list[18]} \nd. {answer_list[19]}")
choice = input("Enter your answer:")
if choice == 'c' or choice == 'C':
  correct += 1
else:
  correct += 0

print(f"\nYou're finished. You got {correct} out of the 5 questions.")