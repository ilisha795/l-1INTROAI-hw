print("Hello ! I am an AI Bot. What is your name ?: ")

name = input()

print(f"Nice to meet you, {name} !")

print("How are you feeling today ? Good or bad ?: ")
mood = input().lower()

if mood == "good":
    print("I'm glad to hear that !")
elif mood == "bad":
    print("I'm sorry to hear that. I hope things get better soon !")

print("How is the weather today ? Sunny or rainy ?: ")
weather = input().lower()

if weather == "sunny":
    print("I love sunny days !")
elif weather == "rainy":
    print("Rainy days can be gloomy, but they also have their charm.")

print("Do you have any plans for today ? Yes or no ?: ")
plans = input().lower()

if plans == "yes":
    print("That's great ! I hope you have a wonderful time.")   
elif plans == "no":
    print("That's okay. Sometimes it's nice to stay at home and relax.")

print(f"It was nice talking to you, {name}. Bye !")