from read_csv import read


def match():
    chances = 1
    while chances <= 2:
        name = input("Please enter the Name: ")
        email = input("Please enter the Email: ")
        data2 = [name, email]
        # print(data2)
        csv_data = read()
        # print(csv_data)
        if chances <= 2:
            for i in csv_data:
                if (i[0] == data2[0]) and (i[1] == data2[1]):
                    print("Welcome to the brain game of River and Land : Just Remember what you give")
                    return True
                    # return "Welcome to the brain game of River and Land : Just Remember what you give"

                else:
                    continue

        chances += 1


match()
