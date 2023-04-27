
while True:



    start = input("Mata in ett tal")

    start = int(start)



    end = input("Mata in ett till tal")

    end = int(end)



    sum = start + end

    print("The sum of {} and {} is {}.".format(start, end, sum))

    question = input("Do you want to calculate another sum? Y/n> ")

    if question.lower() != "y":

        print("skit gubbe")

        exit()

    print("Restarting calculator.")