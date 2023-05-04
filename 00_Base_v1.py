import pandas
from pandas import DataFrame


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


# Number checking function goes here
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


def costs_check(exit_code, cost_type):
    items_list = []
    quantities_list = []
    costs_list = []

    variable_dict = {
        "Item": items_list,
        "Quantity": quantities_list,
        "Price": costs_list

    }

    print(f"|>=+---  Please enter your {cost_type} costs below  ---+=|")
    print("|>=+---  Enter 'xxx' for the item name when done ---+=|")

    while True:
        get_item_name = choice_checker("Item name:", "no", None, None, None)

        if get_item_name == exit_code:
            break

        if cost_type == "variable":
            get_quantity = num_check("Quantity:", "int", 0, None, None)

        else:
            get_quantity = 1

        get_cost_each = num_check("Cost:", "float", 0, None, None)
        print()

        items_list.append(get_item_name)
        quantities_list.append(get_quantity)
        costs_list.append(get_cost_each)

    # creates pandas dict and sets index
    costs_frame: DataFrame = pandas.DataFrame(variable_dict)
    costs_frame = costs_frame.set_index("Item")

    costs_frame['Cost'] = costs_frame['Quantity'] * costs_frame['Price']

    sub_total = costs_frame['Cost'].sum()

    add_dollars = ["Price", "Cost"]
    for item in add_dollars:
        costs_frame[item] = costs_frame[item].apply(currency)

    return [costs_frame, sub_total]


def instructions():
    print()


yes_no_answers = ["yes", "no"]

print("|>=+--- Welcome to the Fundraising Calculator ---+=<| \n")

used_before = choice_checker("|>=+--- Have you used this program before ---+=<| \n", "no",
                             yes_no_answers, "|>=+--- Please Respond With Either a Yes or No Answer "
                                             "(y/n will work) ---+=<|", "yes")
if used_before == "no":
    instructions()

product_name = choice_checker("|>=+--- Name of Product: ---+=<\n", "no", None, "|>=+--- Cannot be Blank ---+=<|", None)

variable_costs = costs_check("xxx", "variable")
variable_frame = variable_costs[0]
variable_sub = variable_costs[1]

fixed_costs = costs_check("xxx", "Fixed")
fixed_frame = fixed_costs[0]
fixed_sub = fixed_costs[1]

# Printing Area #

print()
print(variable_frame)
print("$", variable_sub)
print()
print(fixed_frame)
print("$", fixed_sub)
print()

# Vid:
# Timestamp:
