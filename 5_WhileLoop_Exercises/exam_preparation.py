max_bad_grades = int(input())
sum_of_grades = 0
bad_grades_counter = 0
total_problems_solved = 0
last_problem_solved = ""
is_failed = False
current_problem = input()
while current_problem != "Enough":
    current_grade = int(input())
    if current_grade <= 4:
        bad_grades_counter += 1
        if bad_grades_counter == max_bad_grades:
                is_failed = True
                break
    sum_of_grades += current_grade
    total_problems_solved += 1
    last_problem_solved = current_problem
    current_problem = input()
if is_failed:
    print(f"You need a break, {bad_grades_counter} poor grades.")
else:
    sum_of_grades /= total_problems_solved
    print(f"Average score: {sum_of_grades:.2f}")
    print(f"Number of problems: {total_problems_solved}")
    print(f"Last problem: {last_problem_solved}")