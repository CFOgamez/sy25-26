A4 = [
    "A4",
    "Suzuki Ignis",
    180,
    (153,206),
    7250,
    8.0,
    1597,
    4
    ]
G3 = [
    "G3",
    "Mitsubishi Pajero",
    185,
    (153,208),
    7000,
    9.6,
    3497,
    6
    ]
D2 = [
    "D2",
    "Toyota Celia GT-Four",
    245,
    (220,299),
    5600,
    5.3,
    1998,
    4
    ]
C3 = [
    "C3",
    "VW-Polo GTI",
    185,
    (96,103),
    7600,
    8.0,
    1600,
    4
    ]
B3 = [
    "B3",
    "Toyota Corolla WRC",
    210,
    (220,299),
    5700,
    5.4,
    1972,
    4
    ]
E2 = [
    "E2",
    "Ford Escort WRC",
    220,
    (220,299),
    6250,
    5.6,
    1993,
    4
]
C1 = [
    "C1",
    "Subaru Impreza WRC",
    220,
    (221,300),
    5500,
    5.4,
    1994,
    4
    ]
B1 = [
    "B1",
    "Seat Cordoba WRC",
    230,
    (221,300),
    6000,
    5.0,
    1998,
    4
]
C2 = [
    "C2",
    "Opel Astra GSi",
    235,
    (235,320),
    6200,
    5.6,
    2962,
    6
    ]
A2 = [
    "A2",
    "Ford Focus WRC",
    224,
    (221,300),
    5400,
    5.5,
    1995,
    4
    ]

def print_car(c):
    lines = [
        f"{c[0]}",
        f"Car Model: {c[1]}",
        f"Top Speed (km/h): {c[2]}",
        f"Power (HP): {c[3][1]}",
        f"Weight (kg): {c[4]}",
        f"0-100 km/h (s): {c[5]}",
        f"Engine Capacity (cc): {c[6]}",
        f"Number of Cylinders: {c[7]}"
    ]
    
    # Split into two columns
    col1 = lines[:len(lines)//2 + len(lines) % 2]  # First half
    col2 = lines[len(lines)//2 + len(lines) % 2:]  # Second half
    
    # Calculate column widths for alignment
    col1_width = max(len(line) for line in col1)
    col2_width = max(len(line) for line in col2)
    total_width = col1_width + col2_width + 3  # Add spacing between columns
    
    border = "+" + "_" * total_width + "+"
    
    # Print header border
    print(border)
    
    # Print rows without a line between columns
    for i in range(max(len(col1), len(col2))):
        col1_text = col1[i] if i < len(col1) else ""
        col2_text = col2[i] if i < len(col2) else ""
        print(f"| {col1_text.ljust(col1_width)} {col2_text.ljust(col2_width)} |")
    
    # Print footer border
    print(border)
    
cars = [A4, G3, D2, C3, B3, E2, C1, B1, C2, A2] 
i = 1
for c in cars:
    print(i,c[1])
    i += 1

while True:
    try:
        choice = int(input("Enter a car number (1-10), or 0 to exit: "))
        if choice == 0:
            print("Goodbye!")
            break
        if 1 <= choice <= len(cars):
            print_car(cars[choice - 1])
        else:
            print("Invalid number. Please enter a number between 1 and 10.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")