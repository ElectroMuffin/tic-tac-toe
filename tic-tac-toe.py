turn = "X"
empty_space = "█"
x_space = "X"
o_space = "O"

a1 = empty_space
a2 = empty_space
a3 = empty_space
b1 = empty_space
b2 = empty_space
b3 = empty_space
c1 = empty_space
c2 = empty_space
c3 = empty_space


def check_winner():
    if a1 == x_space and a2 == x_space and a3 == x_space:
        return "X"
    if b1 == x_space and b2 == x_space and b3 == x_space:
        return "X"
    if c1 == x_space and c2 == x_space and c3 == x_space:
        return "X"
    if a1 == x_space and b1 == x_space and c1 == x_space:
        return "X"
    if a2 == x_space and b2 == x_space and c2 == x_space:
        return "X"
    if a3 == x_space and b3 == x_space and c3 == x_space:
        return "X"
    if a1 == x_space and b2 == x_space and c3 == x_space:
        return "X"
    if a3 == x_space and b2 == x_space and c1 == x_space:
        return "X"
    
    if a1 == o_space and a2 == o_space and a3 == o_space:
        return "O"
    if b1 == o_space and b2 == o_space and b3 == o_space:
        return "O"
    if c1 == o_space and c2 == o_space and c3 == o_space:
        return "O"
    if a1 == o_space and b1 == o_space and c1 == o_space:
        return "O"
    if a2 == o_space and b2 == o_space and c2 == o_space:
        return "O"
    if a3 == o_space and b3 == o_space and c3 == o_space:
        return "O"
    if a1 == o_space and b2 == o_space and c3 == o_space:
        return "O"
    if a3 == o_space and b2 == o_space and c1 == o_space:
        return "O"
    
    return None


while True:
    board_state = f"  1 2 3\na {a1} {a2} {a3}\nb {b1} {b2} {b3}\nc {c1} {c2} {c3}"
    print(board_state)
    move = input(f"{turn} - Enter a coordinate (x0 format):\n")

    if turn == "X":
        if move == "a1":
            if a1 == empty_space:
                a1 = x_space
            else:
                print("That spot is taken!")
                continue
        elif move == "a2":
            if a2 == empty_space:
                a2 = x_space
            else:
                print("That spot is taken!")
                continue
        elif move == "a3":
            if a3 == empty_space:
                a3 = x_space
            else:
                print("That spot is taken!")
                continue
        elif move == "b1":
            if b1 == empty_space:
                b1 = x_space
            else:
                print("That spot is taken!")
                continue
        elif move == "b2":
            if b2 == empty_space:
                b2 = x_space
            else:
                print("That spot is taken!")
                continue
        elif move == "b3":
            if b3 == empty_space:
                b3 = x_space
            else:
                print("That spot is taken!")
                continue
        elif move == "c1":
            if c1 == empty_space:
                c1 = x_space
            else:
                print("That spot is taken!")
                continue
        elif move == "c2":
            if c2 == empty_space:
                c2 = x_space
            else:
                print("That spot is taken!")
                continue
        elif move == "c3":
            if c3 == empty_space:
                c3 = x_space
            else:
                print("That spot is taken!")
                continue
        else:
            print("This coordinate does not exist!")
            continue
    elif turn == "O":
        if move == "a1":
            if a1 == empty_space:
                a1 = o_space
            else:
                print("That spot is taken!")
                continue
        elif move == "a2":
            if a2 == empty_space:
                a2 = o_space
            else:
                print("That spot is taken!")
                continue
        elif move == "a3":
            if a3 == empty_space:
                a3 = o_space
            else:
                print("That spot is taken!")
                continue
        elif move == "b1":
            if b1 == empty_space:
                b1 = o_space
            else:
                print("That spot is taken!")
                continue
        elif move == "b2":
            if b2 == empty_space:
                b2 = o_space
            else:
                print("That spot is taken!")
                continue
        elif move == "b3":
            if b3 == empty_space:
                b3 = o_space
            else:
                print("That spot is taken!")
                continue
        elif move == "c1":
            if c1 == empty_space:
                c1 = o_space
            else:
                print("That spot is taken!")
                continue
        elif move == "c2":
            if c2 == empty_space:
                c2 = o_space
            else:
                print("That spot is taken!")
                continue
        elif move == "c3":
            if c3 == empty_space:
                c3 = o_space
            else:
                print("That spot is taken!")
                continue
        else:
            print("This coordinate does not exist!")
            continue

    winner = check_winner()
    if winner:
        print(f"{winner} wins!")
        play_again = input("Do you want to play again? (y/n)")
        if play_again == "y" or play_again == "Y":
            a1 = empty_space
            a2 = empty_space
            a3 = empty_space
            b1 = empty_space
            b2 = empty_space
            b3 = empty_space
            c1 = empty_space
            c2 = empty_space
            c3 = empty_space
            continue
        elif play_again == "n" or play_again == "N":
            print("Exiting...")
            exit()
        else:
            print("Not a valid answer\nExiting...")
            exit()

    if turn == "X":
        turn = "O"
    elif turn == "O":
        turn = "X"
    else:
        print("ERROR 1 - unknown turn")
        exit()
