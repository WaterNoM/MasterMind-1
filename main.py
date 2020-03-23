

password = []
guess = []
close = 0

def create_password():
    password.append(1)
    password.append(2)
    password.append(3)
    password.append(4)

def get_guess():
    temp = []
    for i in range(4): # [0, 1, 2, 3]
        word = input("Give me a number fool!") # "12"
        num = int(word)
        temp.append(num)
    return temp

def is_correct(guess):
    global close
    
    flag = True
    close = 0
    
    for i in range(4):
        if guess[i] != password[i]:
            flag = False
            
            if guess[i] in password:
                close += 1
            
            print("_")
            
        else:
            print(guess[i])
            
    return flag

def main():
    # Create the password first
    create_password()
    
    guess = get_guess()
    while is_correct(guess) == False:
        print("You got it wrong buster!")
        guess = get_guess()
    
    print("Correct!!!!")

main()


