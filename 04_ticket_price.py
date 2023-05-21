import pandas
from datetime import date
import random


def currency(x):
    return "${:.2f}".format(x)


all_names = ["a", "b", "c", "d", "e"]
all_ticket_costs = [7.50, 7.50, 10.50, 10.50, 6.50]
surcharge = [0, 0, 0.53, 0.53, 0]

mini_movie_dict = {
    "Name": all_names,
    "Ticket Price": all_ticket_costs,
    "Surcharge": surcharge
}

mini_movie_frame = pandas.DataFrame(mini_movie_dict)


# Calculate the total ticket cost (ticket + surcharge)
mini_movie_frame['Total'] = mini_movie_frame['Surcharge'] \
                            + mini_movie_frame['Ticket Price']

# calculate the ticket and profit totals
mini_movie_frame['Profit'] = mini_movie_frame['Ticket Price'] - 5
total = mini_movie_frame['Total'].sum()
profit = mini_movie_frame["Profit"].sum()

# choose winner and find the total won
winner_name = random.choice(all_names)
winner_index = all_names.index(winner_name)
total_won = mini_movie_frame.at[winner_index, 'Total']

# set index at the end
mini_movie_frame = mini_movie_frame.set_index('Name')

# getting the date and time for file name

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
total_ticket_sales = "Total Ticket Sales: ${}".format(total)
total_profit = "Total Profit: ${}".format(profit)

# edit text below!! must work with unsold tickets
sales_status = "\n *** All Tickets Have Been Sold ***"

winner_heading = "|>=+--- Raffle Winner ---+=<| "
winner_text = "The winner of the raffle is {}." \
              "They have won ${}. ie: their ticket is" \
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

# Heading
print(heading)
print("the filename will be {}.txt".format(filename))

# adds '$' to the specified variables
add_dollars = ['Ticket Price', 'Surcharge', 'Total', 'Profit']
for var_item in add_dollars:
    mini_movie_frame[var_item] = mini_movie_frame[var_item].apply(currency)

# prints the table of results
print("|>=+---Ticket Data --+=<|")
print()

print(mini_movie_frame)

print()
print("|>=+--- Ticket cost / Profit ---+=<|")

print("Total Ticket Sales: ${:.2f}".format(total))
print("Total Profit: ${:.2f}".format(profit))

print()
print("|>=+--- Raffle Winner ---+=<|")
print(f"congratulations {winner_name} you have won a free ticket / ${total_won}! ")
