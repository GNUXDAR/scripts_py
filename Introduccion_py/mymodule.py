# mymodule.py file
def generate_full_name(firstname, lastname):
    return firstname + ' ' + lastname


def sum_two_nums(num1, num2):
    result = num1 + num2
    return result


def person(firstname, lastname, age, rol):
    person = {
        'firstname': firstname,
        'lastname': lastname,
        'age': age,
        'rol': rol
    }
    return person


def gravity():
    g = 9.8
    return g