print("I'll recommend you some manga to read")
print("Tell me what type of manga you want to read?")
genre = input("What type of genre do you want? (action / romcom / isekai) " ).lower()
year = input("What type of genre do you want? (2000s / 2010s / 2020s) " )
duration = input("Are you looking for a short read or long read? (short / medium / long) " ).lower()

if genre == 'action':
    if year == '2000s':
        if duration == 'short':
            print("This is what I recommend you, Buso Renkin")
        elif duration == 'medium':
            print("This is what I recommend you, Black Lagoon")
        else:
            print("This is what I recommend you, One Piece")
    elif year == '2010s':
        if duration == 'short':
            print("This is what I recommend you, The Disastrous Life of Saiki K")
        elif duration == 'medium':
            print("This is what I recommend you, One Punch Man")
        else:
            print("This is what I recommend you, Attack on Titan")
    elif year == '2020s':
        if duration == 'short':
            print("This is what I recommend you, Kaiju No. 8")
        elif duration == 'medium':
            print("This is what I recommend you, Tokyo Ghoul")
        else:
            print("This is what I recommend you, Chainsaw Man")

elif genre == 'romcom':
    if year == '2000s':
        if duration == 'short':
            print("This is what I recommend you, Lovely Complex")
        elif duration == 'medium':
            print("This is what I recommend you, Kimi ni Todoke")
        else:
            print("This is what I recommend you, Toradora!")
    elif year == '2010s':
        if duration == 'short':
            print("This is what I recommend you, Oregairu")
        elif duration == 'medium':
            print("This is what I recommend you, The Pet Girl of Sakurasou")
        else:
            print("This is what I recommend you, My Love Story!!!")
    elif year == '2020s':
        if duration == 'short':
            print("This is what I recommend you, My Love Story with Yamada-kun at Lv999")
        elif duration == 'medium':
            print("This is what I recommend you, Komi-San Can't Communicate")
        else:
            print("This is what I recommend you, Ancient Magnus Bride")

elif genre == 'isekai':
    if year == '2000s':
        if duration == 'short':
            print("This is what I recommend you, Legend of Twillight")
        elif duration == 'medium':
            print("This is what I recommend you, Digimon Adventures")
        else:
            print("This is what I recommend you, Mushishi")
    elif year == '2010s':
        if duration == 'short':
            print("This is what I recommend you, Konosuba")
        elif duration == 'medium':
            print("This is what I recommend you, Cautious Hero: The Hero is Overpowered but Overly Cautious")
        else:
            print("This is what I recommend you, Re:Zero")
    elif year == '2020s':
        if duration == 'short':
            print("This is what I recommend you, The Worlds Finest Assassin")
        elif duration == 'medium':
            print("This is what I recommend you, The Greatest Demon Lord is Reborn As a Typical Nobody")
        else:
            print("This is what I recommend you, Mushoku Tensei Jobless Reincarnation")