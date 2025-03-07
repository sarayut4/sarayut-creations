"""Escape the Room."""


play_thru: bool = False # acts as an on and off switch for the game
white_box: str = "\U00002B1C" # used for code cracking games
green_box: str = "\U0001F7E9" # used for code cracking games
yellow_box: str = "\U0001F7E8" # used for code cracking games
list_of_attendees: list[str] = ["Ashwathama", "Sanjana", "Chhaya", "Draupadi", "Saraswati", "Yama", "Arjuna", "Yamuna", "Uma"]
completion: bool = False


def main() -> None: 
    """Main gateway for game."""
    if play_thru is False:
        intro()
    else: 
        print("Better luck next time! Try again! ")
    if play_thru is True: 
        if completion is True:
            print("Thanks for playing!")


def intro() -> None:
    """Introduction to the game."""
    print("Greetings, your Royal Highness of Trion. It is I, your royal advisor, Ashwathama. As you know the royal envoy of Lumos, our neighboring kingdom, shall be arriving on Trion territory soon. It's in our best interest to ensure that the meeting with Lumos goes well. We can no longer afford any conflict with the nation that ends with innocent lives being sacrificed. So, behave. Alright?")
    background_info: str = input("Would you like more info regarding our relations with Lumos? Please answer YES or NO: ")
    if background_info == "YES": # gives information
        print("Go to the following link: ")
        prologue()
    if background_info == "NO":  # no info proceeds straight into prologue
        prologue()

def prologue() -> None:
    """Prologue, implements actual story mode. Gives us the setting."""
    cycle_thru: bool = False # acts as a switch for the little quiz game to make sure user knows information
    while cycle_thru is False:
        print("Here's the list of those attending the conference. Review it carefully: ")
        print("In order to make sure you reviewed the list, we would like to check your memory.")
        advisor_of_trion: str = input("Who is the advisor of Trion? Type in all CAPS. ")
        while advisor_of_trion != "ASHWATHAMA":
            print("Wrong! Review the list once more. ")
            advisor_of_trion = input("Try again: ")
        print("Great, here's another one for good measure.")
        advisor_of_lumos: str = input("Who is the advisor of the Lumos Constituency? Answer in all CAPS: ")
        while advisor_of_lumos != "CHHAYA":
            print("Wrong! Review the list once more. ")
            advisor_of_lumos = input("Try again: ")
        print("Great! Try one more, and we are done. ")
        lady_in_waiting_lumos: str = input("Who is the Lady-in-Waiting of Lumos? Answer in all CAPS:")
        while lady_in_waiting_lumos != "SARASWATI":
            print("Wrong! Review the list once more.")
            lady_in_waiting_lumos = input("Try again: ")
        print("Great! Let's move on.")
        review: str = input("Would you like to go over the previous questions once again? Type YES or NO. ")
        if review == "NO":
            cycle_thru = True
            print("We shall proceed.")
            first_chapter()

def first_chapter() -> None:
    """Introduce the first story chapter and scene."""
    print("The Lumos envoy is arriving. Proceed to the following link:  ")
    next_chapter: str = input("Ready to proceed to the next scene? Type YES or NO. ")
    while next_chapter == "NO":
        print("Review the link once more: ")
        next_chapter = input("Ready to move forward now? Type YES or NO. ")
    if next_chapter == "YES":
        second_third_chapter()

def second_third_chapter() -> None:
    """Second and third chapter."""
    print("Oh, no! It's your sister! What is she doing here?")
    print("Proceed to the following link:")
    check: str = input("When ready to continue, type YES. ") # asks if user is ready to continue, this occurs throughout code. 
    while check != "YES": 
        print("It's a simple question, really. Type YES if you are done.")
        check = input("Are you done, your Highness? Type YES. ")
    print("Proceed to the following link:  ")
    second_check: str = input("Ready to continue? Type CONTINUE ")
    while second_check != "CONTINUE":
        print("It's a simple question, really. Type CONTINUE if you are done.")
        second_check = input("Are you done, your Highness? Type CONTINUE. ")
    eliminator("Yama", list_of_attendees)
    print("Your Highness! Are you alright? I am sorry. I wasn't vigilant enough. As per your orders, the castle is under lockdown, and we are keeping the matter under wraps. There's no need to scare the people. However, we don't have much time. We have to find out who is causing this.")
    print("Take my advice, your Highness. Whatever answers you seek are probably within the castle.")
    inquiry: str = input("Would you like to know about our defenses or where you might be able to find some clues? Type either DEFENSE or CLUE: ")
    if inquiry == "DEFENSE":
        print("If you ever suspect anyone your majesty, I shall place them in the most fortified cell in our prison. If no one dies during that time, then they are most likely our culprit. If not, then that's one less person on your list.")
        print("Regarding places to look, I would check the library.")
    if inquiry == "CLUE": 
        print("I am surprised at you, your Majesty. If I were you, I would head to the tower where the archives are located. Our history will probably tell you more than I can. Quit picking my brain.")
        print("Once you have someone you are wary of, notify me and I will place them in a prison cell. If no one dies, they are likely our culprit. Otherwise, we are one step closer to doom.")
    fourth_fifth_chapter()
    
def fourth_fifth_chapter() -> None:
    """Enter fourth and fifth chapter."""
    print("In order to gain access to the archives, you need to unlock the door which is protected by a numerical code.")
    print("Proceed to the following link to get your hints: ")
    archive_code: str = "645992521"
    attempt_code: str = input("Type in the code needed to unlock the archives: ")
    while len(attempt_code) != len(archive_code): # checks and sees if digits are correct
        print(f"That's not {len(archive_code)} digits.")
        attempt_code = input("Try again: ")
    while archive_code != code_cracker(attempt_code, archive_code): # checks and sees if code matches
        print("Incorrect, attempt again!")
        attempt_code = input("Try again: ")
    print("Correct! The door opens to the archives. As you search through numerous shelves, you notice a piece of parchment paper wedged between miniscule spaces. Almost as if it was meant to be hidden and never touched. ")
    print("Proceed to the following link:  ")
    check: str = input("Ready to continue? Type CONTINUE ")
    while check != "CONTINUE":
        print("It's a simple question, really. Type CONTINUE if you are done.")
        check = input("Are you done, your Highness? Type CONTINUE. ")
    print("Pocketing the ballad, you look through the archives even further. As you exhaust your search of the shelves, your attention turns to the locked chest underneath the window.")
    print("Proceed to the following link: ")
    second_check: str = input("Ready to continue? Type CONTINUE ")
    while second_check != "CONTINUE":
        print("It's a simple question, really. Type CONTINUE if you are done.")
        second_check = input("Are you done, your Highness? Type CONTINUE. ")
    chest_code: str = "lizard"
    chest_attempt: str = input("What's the code to unlock the chest (6 letters, all lowercase)? ")
    while len(chest_attempt) != len(chest_code):
        print("Wrong length!")
        chest_attempt = input("Try again: ")
    while chest_code != code_cracker(chest_attempt, chest_code):
        print("Not quite!")
        chest_attempt = input("Try again: ")
    print("Correct! The chest unlocks revealing treasures you have never seen before. Among everything, a piece of parchment paper a familiar color catches your eye. ")
    print("Proceed to the following link: ")
    first_night: str = input("Who are you placing in the cell tonight? Type normally (Ex: Ashwathama). Don't actually put me in the cell though. It was just for the sake of demonstration. ")
    victim: str = ""
    while not name_checker(first_night, list_of_attendees): 
        print("Name not found in list, try once again. ") 
        first_night = input("Try again: ")
    if first_night == "Yamuna":
        print("The night was peaceful. No one passed. ")
        finale()
    else:
        if first_night == "Ashwathama":
            print("It was just for a demonstration. Luckily, this display of your clear lack of faith barely fazes me. BARELY. We have bigger problems. Another member of the Lumos Constituency died. Lady-in-Waiting Saraswati was killed last night. Not only that, but Uma was the last to see her alive.")
            victim = "Saraswati"
        if first_night == "Saraswati":
            print("Royal Advisor Chhaya of Lumos was killed last night in the Atrium.")
            victim = "Chhaya"
        else:
            print("Lady-in-Waiting Saraswati of Lumos was killed last night in her quarters.")
            victim = "Saraswati"
    eliminator(victim, list_of_attendees) # takes the victim out of list, permanently eliminating
    print(f"REMAINING SURVIVORS: {list_of_attendees} ")
    third_check: str = input("Ready to continue? Type CONTINUE ")
    while third_check != "CONTINUE":
        print("It's a simple question, really. Type CONTINUE if you are done.")
        third_check = input("Are you done, your Highness? Type CONTINUE. ")
    print("If someone of Lumos origin died, it has to be an individual of Trion, right? Proceed to the following link: ")
    sixth_seventh_chapter()
        
def sixth_seventh_chapter() -> None:
    """Enter 2nd night/Sixth and Seventh Chapter."""
    print("Let's see if we get closer to our culprit this night. ")
    print("You return to the library searching once more. You lift the carpet to find a loose floorboard. Underneath the loose floorboard, you find another locked box. Ugh, why do we have so many of these? ")
    print("Proceed to the following link: ")
    box_code: str = "2310622754276"
    attempt_box: str = input("Type in the code needed to unlock the box: ")
    while len(attempt_box) != len(box_code):
        print(f"That's not {len(box_code)} digits.")
        attempt_box = input("Try again: ")
    while attempt_box != code_cracker(attempt_box, box_code): 
        print("Not quite!")
        attempt_box = input("Try again: ")
    print("Correct The box unlocks, revealing yet another piece of paper. ")
    print("Proceed to the following link: ")
    check: str = input("Ready to continue? Type CONTINUE ")
    while check != "CONTINUE":
        print("It's a simple question, really. Type CONTINUE if you are done.")
        check = input("Are you done, your Highness? Type CONTINUE. ")
    second_night: str = input("Who are you placing in the cell tonight? Type normally: ")
    victim: str = ""
    while not name_checker(second_night, list_of_attendees): 
        print("Name not found in list, try once again. ") 
        second_night = input("Try again: ")
    if second_night == "Yamuna":
        print("The night was peaceful. No one passed. ")
        finale()
    else:
        if second_night == "Draupadi":
            print("Knight of Trion Arjuna was killed while defending a kitchen staff member. ")
            victim = "Arjuna"
        else: 
            print("Lady-in-Waiting Draupadi of Trion was killed last night in the Lone Tower.")
            victim = "Draupadi"
    eliminator(victim, list_of_attendees)
    print(f"REMAINING SURVIVORS: {list_of_attendees} ")
    second_check: str = input("Ready to continue? Type CONTINUE ")
    while second_check != "CONTINUE":
        print("It's a simple question, really. Type CONTINUE if you are done.")
        second_check = input("Are you done, your Highness? Type CONTINUE. ")
    eighth_chapter()
    
def eighth_chapter() -> None:
    """Enter final night."""
    global play_thru
    print("This is our last chance. We have to find the culprit. ")
    print("This time, you venture into the Lone Tower. ")
    print("It's a lonesome place, one you never liked going into as a child. However, it's time to face childhood fears. ")
    print("As you walk through, you notice something shiny on the highest shelf. It's another chest. You shrug and try to get it. ")
    print("Proceed to the next link: ")
    shiny_code: str = "21025"
    attempt_shiny: str = input("Type in the code needed to unlock the box: ")
    while len(attempt_shiny) != len(shiny_code):
        print(f"That's not {len(shiny_code)} digits.")
        attempt_shiny = input("Try again: ")
    while attempt_shiny != code_cracker(attempt_shiny, shiny_code):
        print("Not quite!")
        attempt_shiny = input("Try again: ")    
    print("Correct! The chest unlocks, revealing yet another piece of paper. ")
    print("Proceed to the following link: ")
    check: str = input("Ready to continue? Type CONTINUE ")
    while check != "CONTINUE":
        print("It's a simple question, really. Type CONTINUE if you are done.")
        check = input("Are you done, your Highness? Type CONTINUE. ")
    print("You look more through the Lone Tower, pulling out an alamanac. As you go through the alamanac shelf, one book sticks out to you, but it has a padlock. ")
    print("Proceed to the following link:  ")
    padlock: str = "31422"
    attempt_padlock: str = input("Type in the code needed to unlock the box: ")
    while len(attempt_padlock) != len(padlock):
        print(f"That's not {len(padlock)} digits.")
        attempt_padlock = input("Try again: ")
    while attempt_padlock != code_cracker(attempt_padlock, padlock):
        print("Not quite!")
        attempt_padlock = input("Try again: ")  
    print("Correct! The box unlocks, revealing yet another piece of paper. ")
    print("Proceed to the following link: ")
    second_check: str = input("Ready to continue? Type CONTINUE ")
    while second_check != "CONTINUE":
        print("It's a simple question, really. Type CONTINUE if you are done.")
        second_check = input("Are you done, your Highness? Type CONTINUE. ")
    print("I think that's all the clues we got. Do you have a good guess on who it is? ")
    third_night: str = input("Who are you placing in the cell tonight? Type normally: ")
    victim: str = ""
    while not name_checker(third_night, list_of_attendees): 
        print("Name not found in list, try once again. ") 
        third_night = input("Try again: ")
    if third_night == "Yamuna":
        print("The night was peaceful. No one passed. ")
        play_thru = True
        finale()
    else:
        if third_night == "Chhaya":
            print("Lady-in-Waiting Saraswati was killed in her quarters last night. ")
            victim = "Saraswati"
        else: 
            print("Royal Advisor Chhaya of Lumos was killed last night in the Atrium.")
            victim = "Chhaya"
    play_thru = True
    eliminator(victim, list_of_attendees)
    print(f"REMAINING SURVIVORS: {list_of_attendees} ")

def finale() -> None:
    """Last chapter."""
    global completion
    print("Yay, you defeated the murderer! I knew you could do it. As a reward for a job well done, here's your gift:  ")    
    check: str = input("Ready to continue? Type CONTINUE ")
    while check != "CONTINUE":
        print("It's a simple question, really. Type CONTINUE if you are done.")
        check = input("Are you done, your Highness? Type CONTINUE. ")
        completion = True
    main()
    
def code_cracker(inp_code: str, actual_code: str) -> str:
    """Crack numerical and alphabetical codes for mini games."""
    return_code: str = ""
    i: int = 0
    cross_check: str = ""
    track_guess: bool = False
    track_alternate: int = 0
    while i < len(actual_code):
        if inp_code[i] == actual_code[i]:
            return_code += inp_code[i]
            cross_check += green_box
        else: 
            track_alternate = 0
            track_guess = False
            while not track_guess and track_alternate < len(actual_code):
                if actual_code[track_alternate] == inp_code[i]:
                    cross_check += yellow_box
                    track_guess = True
                track_alternate += 1
            if not track_guess:
                cross_check += white_box
        i += 1
    print(cross_check)
    return return_code
                    
    
def eliminator(name: str, inp_list: list[str]) -> list[str]:
    """Eliminate the suspect from the global list."""
    survivors: list[str] = []
    global list_of_attendees
    i: int = 0
    while i < len(inp_list):
        if name != inp_list[i]:
            survivors.append(inp_list[i])
        i += 1
    list_of_attendees = survivors
    return list_of_attendees

def name_checker(name: str, inp_list: list[str]) -> bool:
    """Searches list for the name."""
    i: int = 0
    exist: bool = False
    while i < len(inp_list):
        if name == inp_list[i]:
            exist = True
            return exist
        i += 1
    return exist
    

if __name__ == "__main__":
    main()