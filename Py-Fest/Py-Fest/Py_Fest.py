# The initial lineup
lineup = [
    ("Code Play", "Indie", 30),
    ("The Pythonistas", "Rock", 45),
    ("Syntax Error", "Metal", 60)
]
total_time=0
print("/n---Py-Fest 2026 Stage Manager ---")
print("1. View Lineup & Total Time")
print("2. Add a New Band")
print("3. Move First Band to End (Late Arrival)")
print("4. Remove a Band by Name")
print("5. Move Band to Specific Position") # New Feature!
print("6. Exit")
choice = input("Select an option (1-6): ")

if choice == "1":
    print("\n --- Current Lineup ---")
    for artist in lineup:
        print(f"Band: {artist[0]}, Genre: {artist[1]}, Performance Time: {artist[2]} mins")
        total_time += artist[2]
    print(f"Total Performance Time: {total_time} mins")

elif choice == "2":
    name = input("Enter Band Name: ")
    genre = input("Enter Genre: ")
    duration = int(input("Enter Performance Time (in mins): "))
    lineup.append((name, genre, duration))
    print(f"{name} added to lineup.")
elif choice == "3":
    if lineup:
        late_band=lineup.pop(0)
        lineup.append(late_band)
        print(f"{late_band[0]} moved to the end")
elif choice == "4":
    name_to_remove = input("enter the name of the artist to remove:")
    for artist in lineup:
        if artist[0].lower() == name_to_remove.lower():
            lineup.remove(artist)
            print(f"{artist[0]} removed")
elif choice == "5":
    name_to_move = input("Enter the name of the band to move:")
    new_position = int(input("Enter the new position (0-indexed):"))
    for artist in lineup:
         if artist[0].lower() == name_to_move.lower():
            lineup.remove(artist)
            lineup.insert(new_position, artist)
            print(f"moved artist {artist[0]} to postion {new_position}")
            break
    else:
        print("artist not found")
elif choice == "6":
    print("Exiting Py-Fest Stage Manager. Goodbye!")



