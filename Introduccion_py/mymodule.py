# mymodule.py file
def generate_full_name(firstname, lastname):
    """ nombre completo """
    return firstname + ' ' + lastname


def sum_two_nums(num1, num2):
    """ suma dos numeros """
    result = num1 + num2
    return result


def person(firstname, lastname, age, rol):
    """ datos personales """
    persona = {
        'firstname': firstname,
        'lastname': lastname,
        'age': age,
        'rol': rol
    }
    return persona


def gravity():
    """ valor de la gravedad """
    g = 9.8
    return g