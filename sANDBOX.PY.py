amount = int(input("how many?"))
cost = float(input("how much each"))

total_cost = amount * cost

print(total_cost)

while True:

    profit_num = not_empty(question)

    # removes the '$' from the response and flags it as a flat not percentage profit
    if str(profit_num)[0] == "$":
        profit_type = "$"
        goal = profit_num[1:]

    elif str(profit_num)[-1] == "%":
        profit_type = "%"
        goal = profit_num[:-1]

    else:
        profit_type = "unknown"
        goal = profit_num
    try:
        goal = float(goal)
        if goal >= 0:
            continue

    except ValueError:
        print(error)
        continue

    if profit_type == "%":
        cost_needed =
        amount_sold =

    elif profit_type == "$":
        cost_needed = goal + total_cost / amount
        amount_sold =

    print(profit_needed)

    return profit_needed



