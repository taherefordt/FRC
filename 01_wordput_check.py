yes_no_answer = ["yes", "no"]


def choice_checker(question, valid_answer, error, multichoice=None):
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

    elif multichoice is None:

        response = input(question)
        return response


answer = choice_checker("ye/no?", yes_no_answer, "answer y/n!", "multichoice")

print(f"you said {answer}")
