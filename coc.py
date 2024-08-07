print("Clash of Clans Experience Calculator")

level = int(input("Type your level: "))
print("You need this xp to level up:")

if level == 1:
    print(30)
elif level <= 200:
    print((level - 1) * 50)
elif level <= 299:
    print((level - 200) * 500 + 9500)
else:
    print((level - 300) * 1000 + 60000)
