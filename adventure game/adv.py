#advanture game in the jungle


name = input("Please provide your name to start: ")

print(f"\nWelcome, {name}!")
print("Pick your path through the ruins, but choose wisely.\n")

answer = input(
    "You step into the jungle. Ahead, the trail splits:\n"
    "Cross the bridge\n"
    "Pass through vines\n\n"
    "Choose: "
).lower()

if answer == "cross the bridge":

    answer = input(
        "\nHalfway across, the bridge creaks. Below, a river rushes.\n"
        "Do you sprint the rest of the way, or crawl slowly to spread your weight?\n"
        "Sprint\n"
        "Crawl\n\n"
        "Choose: "
    ).lower()

    if answer == "sprint":
        print("\nThe bridge snaps! You plunge into the river and are swept downstream, losing your supplies.")

    elif answer == "crawl":

        answer = input(
            "\nYou reach a sunlit clearing with an old stone altar.\n"
            "A carved riddle asks:\n"
            "'I have no legs but I climb. What am I?'\n"
            "Smoke\n"
            "River\n\n"
            "Choose: "
        ).lower()

        if answer == "smoke":
            print("\nThe altar rumbles open, revealing a golden idol. You've found the jungle's lost treasure!")

        elif answer == "river":
            print("\nA stone guardian awakens and blocks the path back. Your adventure ends here.")

        else:
            print("\nInvalid choice.")

    else:
        print("\nInvalid choice.")

elif answer == "pass through vines":

    answer = input(
        "\nBehind the vines, you find a dim cave with two tunnels.\n"
        "Glowing tunnel\n"
        "Dark tunnel\n\n"
        "Choose: "
    ).lower()

    if answer == "glowing tunnel":
        print("\nThe green glow was swamp gas. You cough and stumble back out, dizzy and defeated.")

    elif answer == "dark tunnel":

        answer = input(
            "\nYou discover another stone altar with the same riddle.\n"
            "'I have no legs but I climb. What am I?'\n"
            "Smoke\n"
            "River\n\n"
            "Choose: "
        ).lower()

        if answer == "smoke":
            print("\nThe altar rumbles open, revealing a golden idol. You've found the jungle's lost treasure!")

        elif answer == "river":
            print("\nA stone guardian awakens and blocks the path back. Your adventure ends here.")

        else:
            print("\nInvalid choice.")

    else:
        print("\nInvalid choice.")

else:
    print("\nInvalid choice. Please restart the game.")