def addwithprint(n):
    countdown = 1
    inter_result = 0

    while countdown <= 5:
        inter_result += countdown
        countdown += 1
        print(inter_result)

    return inter_result


addwithprint(5)


def rocket_launch(n):
    countdown = n
    while countdown > 0:
        print(countdown)
        countdown -= 1
    print("Lift off!")
