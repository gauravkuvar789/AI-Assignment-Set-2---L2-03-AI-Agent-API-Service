from datetime import datetime


def get_current_time():

    return datetime.now().strftime("%d-%m-%Y %H:%M:%S")


def calculator(expression):

    try:

        return str(eval(expression))

    except:

        return "Invalid Expression"
