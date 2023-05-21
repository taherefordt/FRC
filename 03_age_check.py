
def bound_num_check(name, minimum_age, maximum_age):

        age = int(input("sup {} many years old are you? type 'xxx' to quit".format(name)))

        if 12 <= age <= 120:
            valid = True

        elif age > 120:
            print("either you're dead, or that was a typo. Please answer reasonably")

        else:
            print("please come back in {} years".format(12 - age))