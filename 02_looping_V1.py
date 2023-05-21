
# no. of tickets to sell
MAX_TICKETS = 3

# loop for selling the tickets

tickets_sold = 0
while tickets_sold < MAX_TICKETS:
    name = input("please enter your name or type 'xxx' to quit")

    if name == 'xxx':
        break

    tickets_sold += 1

# outputs no. of tickets sold

if tickets_sold == MAX_TICKETS:
    print("Congrats, you have sold all the tickets!")

else:
    print("you have sold {} ticket/s, with {} ticket/s remaining".format(tickets_sold, MAX_TICKETS - tickets_sold))
