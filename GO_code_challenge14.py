print("Welcome to the anime lister.")
insert = ""
anime_list = []

while insert != "done":
    insert = input("Enter the title of an anime (type 'done' to finish): " )
    anime_list.append(insert)
    print("'", insert, "' has been added to the list")
print("You have finished listing your anime.")
print(f"Your anime list includes the following shows:")
for show in anime_list:
    print(f"> {show}")