secret_num = 7
count = 0

while count < 3:

    guess = int(input("Guess the number :"))
    if secret_num == guess:
        print("You won!")
        break
    else:
        count += 1
else:
    print("Sorry! You lose")