def recieve_valid_scores (prompt):
    while True : 
        try:
            score = int(input(prompt + "\n"))
            if 0 <= score <= 100 :
                return score
            else :
                print("Please enter a valid scrore in percentage (0-100).")
    
        except ValueError:
            print("Your score should be a number in percentage.")

scores = []
total = 0
highest_num = 0
lowest_num = 100

for i in range (5):
    scores.insert(i, recieve_valid_scores(f"Please enter your score in test {i +1 } in percentage."))
    total += scores[i]

    if scores[i] > highest_num :
        highest_num = scores[i]

    if scores[i] < lowest_num :
        lowest_num = scores[i]
    

average = total / 5

print(f"Your lowest score is {lowest_num} \nYour highest score is {highest_num}" )

if average >= 40 :

    if average >= 70 :
        grade_band = "A"

    elif average >= 60 :
        grade_band = "B"

    elif average >= 50 :
        grade_band = "C"

    else:
        grade_band = "D"
    
    print(f"You passed! Your grade band is {grade_band}")

else :
    print("You failed...")

