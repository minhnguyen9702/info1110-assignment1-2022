# In this section of my code I am using loops to get inputs for the required variables
# This is because I want users to be able to fail 
# and create errors as many times as they want

import math
# I will need the math library later in order to use
# the math.ceil() function to round numbers

get_name = False
while get_name == False:
    name = input('Please enter your name: ')
    if all(x.isspace() for x in name):
        print('Error: Only accept alphabetical characters and spaces for name\n')
    elif all(x.isalpha() or x.isspace() for x in name):
        get_name = True
        print('')
    else:
        print('Error: Only accept alphabetical characters and spaces for name\n')

get_age = False
while get_age == False:
    try: 
        age = int(input('Please enter your age: '))
        if 0 < int(age) <= 110:
            get_age = True
            print('')
        else:
            print("Error: The age is a number between 0 to 110\n")
    except:
        print("Error: The age is a number between 0 to 110\n")

get_sex = False
while get_sex == False:
    sex = input('Please enter your biological sex (female/male): ')
    if sex == 'female':
        get_sex = True
        print('')
    elif sex == 'male':
        get_sex = True
        print('')
    else:
        print('Error: Please enter valid input\n')

get_goal = False
while get_goal == False:
    try:
        goal = int(input(
            'What do you want to get out of your training? \n'
            '    1. Your goal is losing weight\n'
            '    2. Your goal is to staying calm and relax\n'
            '    3. Your goal is increasing your heart rate\n'
            '    4. Your goal is having stronger legs\n'
            '    5. Your goal is having stronger ABS\n'
            '    6. Your goal is having stronger shoulders and arms\n'
            'Choose a number between 1 to 6: '))
        if 1 <= int(goal) <= 6:
            get_goal = True
            print('')
        else:
            print('Error - It can only be a number between 1 to 6\n')
    except:
        print('Error - It can only be a number between 1 to 6\n')

get_days = False
while get_days == False:
    try: 
        days = int(input('How many days per week you can train: '))
        if 1 <= int(days) <= 7:
            get_days = True
            print('')
        else:
            print("Error: It can only be a number between 1 to 7\n")
    except:
        print("Error: It can only be a number between 1 to 7\n")

#I'm calculating the variable modifer here which adjusts 
#the intensity of the workout based upon age

if age <= 60:
    intensity = 0
if 60 <= age <= 65:
    intensity = (60 - age) * 0.01 
if 65 <= age <= 75:
    intensity = -0.05 + (65 - age) * 0.02
if 75 <= age <= 80:
    intensity = -0.25 + (75 - age) * 0.03
if 80 <= age <= 90:
    intensity = -0.40 + (80 - age) * 0.04
if 90 <= age <= 110:
    intensity = -0.80

modifier = 1 + intensity

#workout_a is based upon the goal given by the variable (goal)
#and what the user wants out of their workout
#1------------------------------------------------------
if goal == 1:
    workout_a = f"""
Gym workout for fat loss

Plate thrusters ({math.ceil(15 * modifier)} reps x 3 sets)
Mountain climbers ({math.ceil(20 * modifier)} reps x 3 sets)
Box jumps ({math.ceil(10 * modifier)} reps x 3 sets)
Lunges ({math.ceil(10 * modifier)} reps x 3 sets)
Renegade rows ({math.ceil(10 * modifier)} reps x 3 sets)
Press ups ({math.ceil(15 * modifier)} reps x 3 sets)
Treadmill ({math.ceil(10 * modifier)} mins x 3 sets)
Supermans ({math.ceil(10 * modifier)} reps x 3 sets)
Crunches ({math.ceil(10 * modifier)} reps x 3 sets)
"""
#2------------------------------------------------------
if goal == 2:
    workout_a = f"""
Gym workout for stretch and relax

Quad stretchs ({math.ceil(2 * modifier)} mins x 3 sets)
Hamstring stretchs ({math.ceil(2 * modifier)} mins x 3 sets)
Chest and shoulder stretchs ({math.ceil(2 * modifier)} mins x 2 sets)
Upper back stretchs ({math.ceil(3 * modifier)} mins x 2 sets)
Biceps stretchs ({math.ceil(2 * modifier)} mins x 2 sets)
Triceps stretchs ({math.ceil(2 * modifier)} mins x 3 sets)
Hip flexors ({math.ceil(2 * modifier)} mins x 3 sets)
Calf stretchs ({math.ceil(2 * modifier)} mins x 3 sets)
Lower back stretchs ({math.ceil(2 * modifier)} mins x 3 sets)
"""
#3------------------------------------------------------
if goal == 3:
    workout_a = f"""
Gym workout for high-intensity exercises

Jumping jacks ({math.ceil(20 * modifier)} reps x 4 sets)
Sprints ({math.ceil(20 * modifier)} reps x 3 sets)
Mountain climbers ({math.ceil(20 * modifier)} reps x 4 sets)
Squat jumps ({math.ceil(20 * modifier)} reps x 4 sets)
Lunges ({math.ceil(20 * modifier)} reps x 3 sets)
Crunches ({math.ceil(20 * modifier)} reps x 3 sets)
Treadmill ({math.ceil(15 * modifier)} mins x 2 sets)
Side planks ({math.ceil(15 * modifier)} reps x 3 sets)
Burpees ({math.ceil(15 * modifier)} reps x 3 sets)
"""
#4------------------------------------------------------
if goal == 4:
    workout_a = f"""
Gym workout for strong legs

Back squats ({math.ceil(10 * modifier)} reps x 5 sets)
Hip thrusts ({math.ceil(12 * modifier)} reps x 3 sets)
Overhead presses ({math.ceil(10 * modifier)} reps x 5 sets)
Rack pulls ({math.ceil(10 * modifier)} reps x 5 sets)
Squats ({math.ceil(10 * modifier)} reps x 4 sets)
Dumbbell lunges ({math.ceil(10 * modifier)} reps x 3 sets)
Leg curls ({math.ceil(15 * modifier)} reps x 3 sets)
Standing calf raises ({math.ceil(20 * modifier)} reps x 2 sets)
"""
#5------------------------------------------------------
if goal == 5:
    workout_a = f"""
Gym workout for strong ABS

Cross crunchs ({math.ceil(12 * modifier)} reps x 3 sets)
Knee ups ({math.ceil(15 * modifier)} reps x 5 sets)
Hip thrusts ({math.ceil(15 * modifier)} reps x 3 sets)
Mountain climbers ({math.ceil(15 * modifier)} reps x 3 sets)
Vertical hip thrusts ({math.ceil(12 * modifier)} reps x 3 sets)
Bicycles ({math.ceil(15 * modifier)} mins x 2 sets)
Front planks ({math.ceil(15 * modifier)} mins x 3 sets)
Dragon flags ({math.ceil(12 * modifier)} reps x 4 sets)
Reverse crunches ({math.ceil(10 * modifier)} reps x 3 sets)
"""
#6------------------------------------------------------
if goal == 6:
    workout_a = f"""
Gym workout for strong shoulder and arms

Bench presses ({math.ceil(10 * modifier)} reps x 5 sets)
Triceps dips ({math.ceil(10 * modifier)} reps x 5 sets)
Incline dumbbell presses (12 reps x 3 sets)
dumbbell flyes ({math.ceil(15 * modifier)} reps x 3 sets)
Triceps extensions ({math.ceil(15 * modifier)} reps x 3 sets)
Pull ups ({math.ceil(10 * modifier)} reps x 5 sets)
Treadmill ({math.ceil(15 * modifier)} mins x 2 sets)
Bent over rows ({math.ceil(10 * modifier)} reps x 5 sets)
Chin ups ({math.ceil(10 * modifier)} reps x 3 sets)
"""
#workout b is based on the user's age and sex
#7------------------------------------------------------
if sex == 'male' and age < 18:
    workout_b = f"""
Gym workout for a male younger than 18 years old

High knees (20 reps x 3 sets)
Squats (10 reps x 3 sets)
Calf raises (10 reps x 3 sets)
Scissor jumps (12 reps x 3 sets)
Burpees (10 reps x 3 sets)
Treadmill (10 mins x 2 sets)
"""
#8------------------------------------------------------
if sex == 'female' and age < 18:
    workout_b = f"""
Gym workout for a female younger than 18 years old

Squats (10 reps x 3 sets)
Crunches (10 reps x 2 sets)
Jumping jacks (10 reps x 3 sets)
Push ups (10 reps x 2 sets)
Burpees (10 reps x 3 sets)
Treadmill (10 mins x 2 sets)
"""
#9------------------------------------------------------
if sex == 'male' and age >= 18:
    workout_b = f"""
Gym workout for a male at least 18 years old

Standing biceps curls ({math.ceil(20 * modifier)} reps x 3 sets)
Seated incline curls ({math.ceil(18 * modifier)} reps x 3 sets)
Seated dumbbell presses ({math.ceil(12 * modifier)} reps x 3 sets)
Leg presses ({math.ceil(15 * modifier)} reps x 3 sets)
Bench presses ({math.ceil(10 * modifier)} reps x 4 sets)
Tricep kickbacks ({math.ceil(15 * modifier)} reps x 3 sets)
Hip thrusts ({math.ceil(12 * modifier)} reps x 3 sets)
Seated rows ({math.ceil(10 * modifier)} reps x 4 sets)
"""
#10------------------------------------------------------
if sex == 'female' and age >= 18:
    workout_b = f"""
Gym workout for a female at least 18 years old

Lateral raises ({math.ceil(15 * modifier)} reps x 3 sets)
Reverse flyes ({math.ceil(12 * modifier)} reps x 3 sets)
Hip thrusts ({math.ceil(12 * modifier)} reps x 3 sets)
Incline dumbbell presses ({math.ceil(15 * modifier)} reps x 3 sets)
Squats ({math.ceil(10 * modifier)} reps x 4 sets)
Dumbbell lunges ({math.ceil(10 * modifier)} reps x 3 sets)
Leg presses ({math.ceil(12 * modifier)} reps x 3 sets)
Dumbbell presses ({math.ceil(10 * modifier)} reps x 4 sets)
"""

print(f'Hello {name}! Here is your training:')

workout_day = 1
while days > 0:
    if not (workout_day % 2) == 0:
        print("------------------------------------------"
        "-------------------------------------------")
        print(f'Day {workout_day}{workout_a}', end='')
        workout_day += 1
        days -= 1
    else:
        print("------------------------------------------"
        "-------------------------------------------")
        print(f'Day {workout_day}{workout_b}', end='')
        workout_day += 1
        days -= 1

print("------------------------------------------"
"-------------------------------------------\n")
print(f"Bye {name}.")


