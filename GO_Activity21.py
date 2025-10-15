Di_Pa_Ligo_Si_Denver = True

while Di_Pa_Ligo_Si_Denver:
    tugon = input("\n Naliligo paba si Denver? (y / n) " ).lower()
    if tugon == "y":
        print("\n Toothbrush, Sabon, Shampoo")
        anu = input("Ano gagawin nya? " ).lower()
        if anu == "toothbrush":
            print("\t brush brush brush")
        elif anu == "sabon":
            print("\t wash wash wash")
        elif anu == "shampoo":
            print("\t woosh woosh woosh")
        continue
    if tugon == "n":
        print("\n bango naman ni Denver")
        break