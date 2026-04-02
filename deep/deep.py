# Starts the program and then start deeptough function
def main():
    deeptough()


# Deeptough function that ask the great question of life, the universe and everything if answer 42 or equivlent it says yes if not it answer no
def deeptough():
    deepguy = input(
        "What is the Answer to the Great Question of Life, the Universe, and Everything? "
    )
    if deepguy == "42" or deepguy == "forty-two" or deepguy == "forty two":
        print("Yes")
    else:
        print("No")


# Runs main program
main()
