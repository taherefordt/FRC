
amount = int(input("how many?"))
cost = float(input("how much each"))

total_cost = amount * cost

print(total_cost)

while True:
    profit_num = input("how much profit do you want?")

    if str(profit_num)[-1] == "%":
        profit_type = "%"
        profit_goal = profit_num[:-1]

    else:
        profit_type = "$"

    if profit_type == "%":
        profit_needed = total_cost + (total_cost * (int(profit_goal)/100))

    elif profit_type == "$":
        profit_needed = total_cost + profit_goal

    print(profit_needed)
