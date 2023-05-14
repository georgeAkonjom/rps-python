playerOne = (input("p1 - rps shoot(type the first letter of your pick): "))
playerTwo = (input("p2 - heart of the shot guide me: "))

if playerOne == playerTwo :
    print("Draw, how futile")

if playerOne == 'r':
    if playerTwo == 'p':
        print("p2s paper shrouds the heavens over rock")
    elif playerTwo == 's':
        print("p1s rock grind scissors to dust")

if playerOne == 'p':
    if playerTwo == 'r':
        print("p1s paper blots out the sun, rock suffers")
    elif playerTwo == 's':
        print("p2s scissors make art of paper")

if playerOne == 's':
    if playerTwo == 'r':
        print("p2s rock is doing some crushin'")
    elif playerTwo == 'p':
        print("p1s scissors will need to be sharpened after that paper cutting fest")
    