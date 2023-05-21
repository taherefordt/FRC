def bound_age_check(minimum_age, maximum_age):

    age = int(input("how many years old are you?"))

    if minimum_age <= age <= maximum_age:

        if age > 18:
            price = 21.50

        elif age > 65:
            price = 12

        else:
            price = 15

    elif age > maximum_age:
        print("either you're dead, or that was a typo. Please answer reasonably")

    else:
        print("please come back in {} years".format(minimum_age - age))

    return price