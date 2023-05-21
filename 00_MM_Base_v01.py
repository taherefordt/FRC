import pandas
import random
from datetime import date


def word_input_checker(question, num_letter, valid_answer):
    error = f"please choose {valid_answer[0]} or {valid_answer[1]}"

    # Loop to keep the question going till answered properly
    while True:

        response = input(question).lower()

        for word in valid_answer:
            if response == word[:num_letter] or response == word:
                return word

        print(error)
        print()


def currency(x):
    return "${:.2f}".format(x)


def instructions():
    print('''\n
|>=+--- instructions ---=+<|

* For each ticket, one must enter... *
- Their name (this cannot be blank)
- Their age (between 12 and 120)
- Payment method (cash / credit)

When you have entered all the users, press 'xxx' to quit

The program will then display the ticket details\n''')


# no. of tickets to sell
MAX_TICKETS = 7

# no. of tickets user has sold
tickets_sold = 0

# the total amount of profit
profit = 0

# price of a ticket
price = 0

# variables to be used later
age = 0
name = ""
payment_method = ["cash", "credit"]
yes_no_answer = ["yes", "no"]

# data lists for table of results
all_names = []
all_ticket_costs = []
all_surcharge = []

# dictionary used when formatting table
mini_movie_dict = {
    "Name": all_names,
    "Ticket Price": all_ticket_costs,
    "Surcharge": all_surcharge
}

show_instructions = word_input_checker("Do you want to see the instructions "
                                       "on how to use this program?", 1, yes_no_answer)

if show_instructions == "yes":
    instructions()


# main here
while tickets_sold < MAX_TICKETS:

    # asks the user for their name
    while name == "":
        name = input("please enter your name or type 'xxx' to quit \n")

        if name == "":
            print("this cannot be blank, try again \n")

    # early exit code
    if name == 'xxx' and len(all_names) > 0:
        break

    elif name == 'xxx':
        print("You must sell at least ONE ticket before quitting")
        continue

    while True:

        try:

            # asks user for their age
            age = int(input("so {} how many years old are you? \n".format(name)))

            if 12 <= age <= 120:
                ticket_valid = "yes"
                break

            else:
                ticket_valid = "no"
                name = ""
                break

        except ValueError:
            print("please enter a whole number")

    # compares age with the ticket prices
    if ticket_valid == "yes":
        if age <= 15:
            price = 7.50

        elif age <= 64:
            price = 10.50

        else:
            price = 6.50

        tickets_sold += 1

    # if you're too old, or too young this bit prints a
    elif ticket_valid == "no":

        if age > 120:

            print("that looks to be a typo, try again")

        else:
            print("you're too young for this movie")
            name = ""

        continue

    cash_cred = word_input_checker("will you pay with cash or credit? (ca/cr is acceptable) \n",
                                   2, payment_method, )

    if cash_cred == "credit":
        surcharge = price * 0.05
    else:
        surcharge = 0

    profit += price

    # this chunk prints a ticket price
    if ticket_valid == "yes":
        print(f"your ticket will cost ${price + surcharge:.2f}")

    else:
        print("you dont get a ticket")

    # appends variables to their lists
    all_names.append(name)
    all_ticket_costs.append(price)
    all_surcharge.append(surcharge)

    # resets name for next loop
    name = ""

mini_movie_frame = pandas.DataFrame(mini_movie_dict)
# mini_movie_frame = mini_movie_frame.set_index('Name')

# Calculate the total ticket cost (ticket + surcharge)
mini_movie_frame['Total'] = mini_movie_frame['Surcharge'] \
                            + mini_movie_frame['Ticket Price']

# calculate the ticket and profit totals
mini_movie_frame['Profit'] = mini_movie_frame['Ticket Price'] - 5
total = mini_movie_frame['Total'].sum()
profit = mini_movie_frame["Profit"].sum()

add_dollars = ['Ticket Price', 'Surcharge', 'Total', 'Profit']
for var_item in add_dollars:
    mini_movie_frame[var_item] = mini_movie_frame[var_item].apply(currency)

# picks a random person to be a winner and calculates total won
winner_name = random.choice(all_names)
winner_index = all_names.index(winner_name)
total_won = mini_movie_frame.at[winner_index, 'Total']

# set index at end (before print)
mini_movie_frame = mini_movie_frame.set_index('Name')


# gets today's date
today = date.today()

# Get day, month, and year as individual strings
day = today.strftime("%d")
month = today.strftime("%m")
year = today.strftime("%Y")

heading = "|>=+--- Mini Movie Fundraiser Data {}/{}/{} ---+=<|".format(day, month, year)
filename = "MMF_{}_{}_{}".format(year, month, day)

# change frame to a string so that we can export it to file
mini_movie_string = pandas.DataFrame.to_string(mini_movie_frame)

# create strings for printing
ticket_cost_heading = "\n|>=+--- Ticket cost / Profit ---+=<|"
total_ticket_sales = "Total Ticket Sales: ${:.2f}".format(total)
total_profit = "Total Profit: ${:.2f}".format(profit)

# edit text below!! must work with unsold tickets
sales_status = "\n *** All Tickets Have Been Sold ***"

winner_heading = "|>=+--- Raffle Winner ---+=<| "
winner_text = "The winner of the raffle is {}." \
              "They have won {}. ie: their ticket is" \
              "free!".format(winner_name, total_won)

# list holding things to write/put in file
to_write = [heading, mini_movie_string, ticket_cost_heading,
            total_ticket_sales, total_profit, sales_status,
            winner_heading, winner_text]

# print output
for item in to_write:
    print(item)

# write to output file
# create file to hold data (add .txt extension)
write_to = "{}.txt".format(filename)
text_file = open(write_to, "w+")

for item in to_write:
    text_file.write(item)
    text_file.write("\n")

# closes file
text_file.close()
