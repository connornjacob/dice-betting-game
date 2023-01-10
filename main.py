import random

print('Hello!')
usd = 10
print(f'You have {usd} USD')

def rolldice(usd):
    if usd <= 0:
        print("You do not have enough money to bet")
        return usd
    dice = random.randrange(1,7)
    o = input('Would you like to bet high or low this time? L/H: ').lower().strip()
    number = 50 * usd / 100
    print(f'You bet {number}')
    print(dice)
    if o == 'h':
        if dice >= 4:
            usd += number
            print(f'You won! Your new balance is {usd} USD')
        else:
            usd -= number
            print(f'You lost! Your new balance is {usd} USD')
    elif o == 'l':
        if dice <= 4:
            usd += number
            print(f'You won! Your new balance is {usd} USD')
        else:
            usd -= number
            print(f'You lost! Your new balance is {usd} USD')
    else:
        print("Invalid input. Please enter either 'L' or 'H'")
    return usd

usd = rolldice(usd)
while usd > 0:
    play_again = input("Would you like to play again? Y/N ").lower().strip()
    if play_again == "y":
        usd = rolldice(usd)
    elif play_again == "n":
        print("Thanks for playing! Come back soon.")
        break
    else:
        print("Invalid input. Please enter either 'Y' or 'N'")
else:
    print("Sorry, You do not have enough money to play again.")

