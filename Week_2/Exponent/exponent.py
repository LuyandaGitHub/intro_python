number_1 = int(input('enter a base number'))
number_2 = int(input('enter the power number'))


def get_exponent(base_number, power_number) :
    result = 1

    # HOW MANY TIMES WE LOOP IIS GONNA DEPEND ON THE POWER WE GET IN FROM THE USER
    for index in range(power_number) :
        result = result * base_number

    return result


print(get_exponent(number_1, number_2))
