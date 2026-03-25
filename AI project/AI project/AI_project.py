import random  
  
forms = []  
  
filename = 'Saiyan_power_levels.txt'  
  
with open(filename, 'r',) as file:  
    for line in file:  
        if '|' in line and 'Power Level' not in line and '---' not in line:  
            parts = [p.strip() for p in line.strip().split('|') if p.strip()]  
            if len(parts) == 2:  
                form = parts[0]  
                power = parts[1].replace(',', '').replace('~', '')  
                try:  
                    power = int(power)  
                except ValueError:  
                    pass  
                forms.append([form, power])  
  
print("Available forms:")  
for form in forms:  
    print(f"- {form[0]}")  
chosen_form = input("Choose a form: ")  
  
user_power = None  
for item in forms:  
    if item[0].lower() == chosen_form.lower():  
        user_power = item[1]  
        print(f"Your power level as {item[0]} is {item[1]}")  
        break  
if user_power is None:  
    print("Form not found.")  
    exit()  
  
opponent_choices = [f for f in forms if f[0].lower() != chosen_form.lower()]  
opponent = random.choice(opponent_choices)  
print(f"Your opponent is: {opponent[0]} (Power: {opponent[1]})")  
  
if user_power > opponent[1]:  
    print("You win!")  
elif user_power < opponent[1]:  
    print("You lose!")  
else:  
    print("It's a tie!")  
