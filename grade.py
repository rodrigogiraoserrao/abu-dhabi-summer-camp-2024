def grade():
    percentage = int(input("Type your test score: "))
    if percentage <= 59:  # percentage < 60
        print("F")
    elif percentage <= 69:
        print("D")
    elif percentage <= 79:
        print("C")
    elif percentage <= 89:
        print("B")
    elif percentage <= 100:
        print("A")
    else:
        print("I don't recognise this score.")


grade()
