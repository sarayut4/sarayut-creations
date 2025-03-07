"""Choose your own adventure: Survive Your Creations."""
__author__ = "730557387"
from random import randint

player: str = ""
genre: str = "fantasy"
status: str = "well-known"
weapon_of_choice: str = "knives"
points: int = 0
play_thru: bool = False
attempt: int = 1
NARRATOR_AVATAR: str = "\U0001F9D1"


def main() -> None:
    """The entrypoint of the program and the main game loop."""
    global points
    global attempt
    points = 0
    if play_thru is False:
        greet()
    while attempt >= 1: 
        game_path: str = input(f"{NARRATOR_AVATAR}- Would you like to enter the story [story], customize your story [customize], or end the experience [end]? ")
        if game_path == "end":
            print(f"{points} points accumulated. Thanks for playing! ")
            attempt = 0
        if game_path == "story":
            points = 100
            points = chapter(points)
        if game_path == "customize":
            points = 100
            customize()
    if points <= 0 and play_thru is True: 
        print(f"{NARRATOR_AVATAR}- Better luck next time, {player}. Try again another day!")
        print(f"** TOTAL POINTS ACCUMULATED: {points} **")


def greet() -> None:
    """Informs player regarding the substance of the game and asks for name that will continue to be used throughout code."""
    print(f"{NARRATOR_AVATAR}- ==== Welcome to Survive Your Creations, an interactive game where the choices you make will always come back to haunt you. You will be playing the role of a famous author whose characters came to life and are seeking revenge. Your main objective is to survive, survive, survive. ====")
    global player
    player = input("Enter player name: ") 


def chapter(points: int) -> int:
    """Beginning of interactive game."""
    global play_thru
    if points > 0: 
        print(f"==== {NARRATOR_AVATAR}- Welcome, {player}. The first trial is a game of chance. Roll the dice for your outcome. ====")
        dice: int = randint(1, 6)
        print(f"{dice} is the outcome.")
        if dice % 2 == 0: 
            points += 30
            print(f"{NARRATOR_AVATAR}- You were able to gain the upper hand on your MC from your first {genre} novel, momentarily subduing them with your {weapon_of_choice}.")
            print(f" ** {points} points accumulated. ** ")
            direction: str = input(f"{NARRATOR_AVATAR}- After subduing your main character, you reach a fork in the road. The cobblestone road on the left is more well-lit albeit covered by trees. The road on the right is covered in debris and so dark that you aren't able to make out what could linger there. PICK RIGHT or LEFT. ")
            if direction == "RIGHT":
                print(f"{NARRATOR_AVATAR}- While venturing through the right fork, you find a crowbar.")
                crow_bar: str = input(f"{NARRATOR_AVATAR}- Would you like to take [A] or leave [B] the crowbar?")
                if crow_bar == "A":
                    points += 5
                    print(f"{NARRATOR_AVATAR}- The more the merrier! You're going to need all the luck you can get.")
                    print(f" ** {points} points accumulated. ** ")
                    car: str = input(f"{NARRATOR_AVATAR}- Once you take the crowbar, you hear the sound of an engine coming to life. You turn around and see your MC driving a car straight out you. Are you going to run [A] or use your {weapon_of_choice} [B]? ")
                    if car == "A":
                        print(f"{NARRATOR_AVATAR}- You're unable to outrun the car and end up crushed.")
                        points = 0
                    if car == "B":
                        if weapon_of_choice == "knives": 
                            print(f"{NARRATOR_AVATAR}- You're able to slash some tires, but were defenseless when the characters got out of the car.")
                            points = 0
                        if weapon_of_choice == "nunchucks":
                            print(f"{NARRATOR_AVATAR}- Seriously? Why'd you even try? The {weapon_of_choice} did little to help your predicament.")
                            points = 0
                        if weapon_of_choice == "gun":
                            print(f"{NARRATOR_AVATAR}- Guess the exchange paid off. You were able to vanquish your characters easily, putting an end to the nightmare.")
                            points += 500
                            print(f" ** {points} points accumulated. ** ")
                        if weapon_of_choice == "machete":
                            print(f"{NARRATOR_AVATAR}- Through some evasive maneuvers, you were able to cause severe damage to the car and vanquish the characters. Well done.")
                            points += 500
                            print(f" ** {points} points accumulated. ** ")
                else: 
                    print(f"{NARRATOR_AVATAR}- It would be best to carry less. You still have what you need after all.")
                    helping: str = input(f"{NARRATOR_AVATAR}- As you walk farther down, you see someone struggling in the woods. Upon further investigation, you realize it is one of your side characters from your 2nd {genre} novel. Do you want to help them [A] or keep walking [B]? ")
                    if helping == "A": 
                        print(f"{NARRATOR_AVATAR}- When attempting to help them, you realize they have a hidden weapon, a piece of broken shrapnel. They take the broken shrapnel and stab you with it, leaving you fatally wounded.")
                        points = 0
                    if helping == "B": 
                        print(f"{NARRATOR_AVATAR}- You begin walking away from them when they start to shout loudly, drawing attention to your location, causing other characters to arrive to the scene and jump you.")
                        points = 0
            if direction == "LEFT": 
                print(f"{NARRATOR_AVATAR}- You have terrible instincts, {player}. You encounter a side character from your {genre} novel, and unfortunately, suffer an extremely gruesome demise.")
                points = 0
        else: 
            points -= 30
            print(f"{NARRATOR_AVATAR}- You lost your {weapon_of_choice} fighting off a side character from your {genre} novel.")
            print(f" ** {points} points accumulated. ** ")
            shed: str = input(f"{NARRATOR_AVATAR}- While running for dear life from your side character, you encounter a shed. Would you like to seek refuge [A] in the shed or continue running [B]? ")
            if shed == "A":
                points += 20
                print(f"{NARRATOR_AVATAR}- You were able to lose the side character while hiding in the shed, regaining some energy.")
                print(f" ** {points} points accumulated. ** ")
                outside_of_shed: str = input(f"{NARRATOR_AVATAR}- As you walk out of the shed, you notice you are surrounded by your book characters, all closing in on your location. Are you going to run [A] or try to reason with them [B]? ")
                if outside_of_shed == "A":
                    print(f"{NARRATOR_AVATAR}- You fail to run away and end up meeting a swift demise.")
                    points = 0
                else: 
                    if genre == "fantasy":
                        print(f"{NARRATOR_AVATAR}- Your characters listen, but ultimately, refuse to back down, leading to your conclusion.")
                        points = 0
                        print(f" ** {points} points accumulated. ** ")
                    if genre == "horror":
                        print(f"{NARRATOR_AVATAR}- You don't even get a chance to open your mouth before your {genre} character silences you permanently.")
                        points = 0
                        print(f" ** {points} points accumulated. ** ")
                    if genre == "romance":
                        print(f"{NARRATOR_AVATAR}- Your characters end up backing down, because they feel like they overreacted. Anticlimactic, I know.")
                        points += 500
                        print(f" ** {points} points accumulated. ** ")
                    if genre == "sci-fi":
                        print(f"{NARRATOR_AVATAR}- Your characters hear you out and end up leaving you be, thinking your existence is punishment enough, LOL.")
                        points += 500
                        print(f" ** {points} points accumulated. ** ")
            if shed == "B":
                points = 0
                print(f"{NARRATOR_AVATAR}- Overestimating your running, you failed to escape your side character and took a lethal blow.")
    if points <= 0:
        play_thru = True
        return points
    play_thru = True
    return points
    
    
def customize() -> None:
    """Customize your experience, but player will have to experience point changes."""
    print(f"====Welcome, {player}. Here, you will be able to change your genre, status, and weapon of choice. Please be advised: changes to the settings can affect your total adventure points (for better or worse).====")
    global genre
    global points
    genre = input(f"{NARRATOR_AVATAR}- Would you like to keep the same genre [keep], or switch the genres to the following [romance, horror, or sci-fi]? ")
    if genre == "keep": 
        print(f"{NARRATOR_AVATAR}- Playing it safe, {player}. We admire your caution. No point change.")
        points = points
        print(f" ** {points} points accumulated. ** ")
    if genre == "romance": 
        print(f"{NARRATOR_AVATAR}- Pretty tame choice, {player}. It's a disappointment, so it's going to cost you. DEDUCTION 60 POINTS.")
        points -= 60
        print(f" ** {points} points accumulated. ** ")
    if genre == "horror":
        print(f"{NARRATOR_AVATAR}- Wow, a choice that will bring entertainment. We like your style, so points will be added. Word of advice: Don't rejoice too soon. BONUS 100 POINTS.")
        points += 100
        print(f" ** {points} points accumulated. ** ")
    if genre == "sci-fi":
        print(f"{NARRATOR_AVATAR}- Meh, it's kind of entertaining. Would have preferred it if you picked horror.")
        points -= 40
    global status
    status = input(f"{NARRATOR_AVATAR}- Would you like to be a well-known [A] or lesser-known author [B]? ")
    if status == "A":
        points = points
        print(f"{NARRATOR_AVATAR}- Very well, but fame always has its price. Fortunately you won't be paying anything today, {player}.")
        print(f" ** {points} points accumulated. ** ")
    if status == "B": 
        points += 20
        print(f"{NARRATOR_AVATAR}- Bold choice, {player}. We truly hope it doesn't backfire. BONUS 20 POINTS.")
        print(f" ** {points} points accumulated. ** ")
    global weapon_of_choice
    weapon_of_choice = input(f"{NARRATOR_AVATAR}- Would you like to keep your current choice [keep], or change your weapon to the following [nunchucks, gun, machete]? ")
    if weapon_of_choice == "keep" or "machete":
        points == points
        if weapon_of_choice == "machete":
            print(f"{NARRATOR_AVATAR}- We'll keep your point level the same. Consider it a show of good will. You're going to need it. NO CHANGE.")
            print(f" ** {points} points accumulated. ** ")
        if weapon_of_choice == "keep":
            print(f"{NARRATOR_AVATAR}- Knives it is. No point change.")
            print(f" ** {points} points accumulated. ** ")
    if weapon_of_choice == "nunchucks": 
        print(f"{NARRATOR_AVATAR}- It's definitely a unique choice, albeit a bit weak, but we will offer some points. BONUS 5 POINTS.")
        points += 5
        print(f" ** {points} points accumulated. ** ")
    if weapon_of_choice == "gun":
        print(f"{NARRATOR_AVATAR}- A high damage choice, but it's going to cost you. DEDUCTION 15 POINTS.")
        points -= 15
        print(f" ** {points} accumulated. ** ")


if __name__ == "__main__": 
    main()