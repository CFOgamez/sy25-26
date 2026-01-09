# The initial lineup
lineup = [
    ("Code Play", "Indie", 30),
    ("The Pythonistas", "Rock", 45),
    ("Syntax Error", "Metal", 60)
]

# 1. Add the headliner
headliner = ("The Byte Beats", "Synthwave", 90)
lineup.append(headliner)

#2. remove the dudes and put it to the end
rb = lineup.pop(0)
lineup.append(rb)
# 3. Remove pythonistas
lineup.remove(("The Pythonistas", "Rock", 45))

# 4. Calculate total duration
total_duration = sum(band[2] for band in lineup)
print(f"Total duration of performances: {total_duration} minutes")

print(lineup)