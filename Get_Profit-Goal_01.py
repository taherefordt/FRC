def num_check(question, flint, low=None, high=None, exit_code=None):
    while True:

        # sets up error messages
        if low is not None and high is not None:
            error = "Please enter an integer between {} and {} (inclusive)".format(low, high)
        elif low is not None:
            error = "Please enter an integer that is more than or equal to {}".format(low)
        elif high is not None:
            error = "Please enter an integer that is less than or equal to {}".format(high)
        else:
            error = "|+=- Please enter a number -=+|"

        try:
            response = input(question)

            # check to see if response is the exit code and return it
            if response == exit_code:
                return response

            # change the response into an integer or float depending on flint

            if flint == "int":
                response = int(response)

            elif flint == "float":
                response = float(response)

            # Checks response is not too low, not use of 'is not' keywords
            if low is not None and response < low:
                print(error)
                continue

            # Checks response is not too high
            if high is not None and response > high:
                print(error)
                continue

            return response

        # checks input is a integer
        except ValueError:
            print(error)
            continue


def currency(x):
    return "${:.2f}".format(x)


def choice_checker(question, empty_valid, valid_answer=None, error=None, multichoice=None):
    # Loop to keep the question going till answered properly

    if multichoice is not None:

        valid = False
        while not valid:

            response = input(question).lower()

            for word in valid_answer:
                if response == word[:1] or response == word:
                    return word

            print(error)
            print()

    elif multichoice is None and empty_valid == "no":

        while True:

            response = input(question)

            if response == "":
                print("|>=+--- Your response to this cannot be blank ---+=<|")

            else:
                return response

    elif multichoice is None and empty_valid == "yes":

        response = input(question)
        return response


def not_empty(question):

    response = ""

    while response == "":
        response = input(question)

    else:
        return response


def get_profit_goal(question):
    amount = int(input("how many?"))
    cost = float(input("how much each"))

    total_cost = amount * cost

    print(total_cost)

    while True:
        profit_num = input(question)

        if str(profit_num)[-1] == "%":
            profit_type = "%"
            profit_goal = profit_num[:-1]

        else:
            profit_type = "$"

        if profit_type == "%":
            profit_needed = total_cost + (total_cost * (int(profit_goal) / 100))

        elif profit_type == "$":
            profit_needed = total_cost + profit_goal

        print(profit_needed)
