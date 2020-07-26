from random import randint


def update_opions(standart_options):
    combinations = {}
    size = len(standart_options) // 2
    for item in standart_options:
        lose_combine = ""
        index_slice = 0  # to switch to the (0 - i) element
        for i in range(size):
            if standart_options.index(item) + i + 1 >= len(standart_options):
                lose_combine = lose_combine + f"{standart_options[index_slice]} "
                index_slice += 1
            else:
                index = standart_options.index(item)
                lose_combine = lose_combine + f"{standart_options[index + i + 1]} "

        win_combine = ""
        index_slice = -1
        for i in range(size):
            if standart_options.index(item) - i - 1 < 0:
                win_combine = win_combine + f"{standart_options[index_slice]} "
                index_slice -= 1
            else:
                index = standart_options.index(item)
                win_combine = win_combine + f"{standart_options[index - i - 1]} "
        combinations[item] = dict(win=win_combine, lose=lose_combine)
    return combinations


standart_options = ["rock", "scissors", "paper"]
combination = {"rock": {"win": "scissors", "lose": "paper"},
               "scissors": {"win": "paper", "lose": "rock"},
               "paper": {"win": "rock", "lose": "scissors"}}

user_name = input("Enter your name: ")
file = open("rating.txt", "r+")
print("Hello,", user_name)

add_user = True
point = 0
for line in file:
    split_line = line.split()
    if split_line[0] == user_name:
        point = int(split_line[1])
        add_user = False
file.close()

new_options = input()
if new_options != "":
    standart_options = new_options.split(",")
    combination = update_opions(standart_options)

print("Okay, let's start")

while True:
    user_option = input()

    pc_combine = randint(0, 2)
    pc_option = standart_options[pc_combine]

    if user_option == "!exit":
        print("Bye!")
        break
    elif user_option == "!rating":
        print("Your rating:", point)
    elif user_option not in standart_options:
        print("Invalid input")
    elif user_option == pc_option:
        print(f"There is a draw {user_option}")
        point += 50
    elif pc_option in combination[user_option]["win"]:
        point += 100
        print(f"Well done. Computer chose {pc_option} and failed")
    elif pc_option in combination[user_option]["lose"]:
        print(f"Sorry, but computer chose {pc_option}")
