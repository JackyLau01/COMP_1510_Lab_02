def format_name(first, last):
    stripped_first = first.strip().title()
    stripped_last = last.strip().title()
    full_name = stripped_first + " " + stripped_last
    return full_name


#print(format_name())


def tripler():
    tripled = input("Please enter anything to be tripled") * 3
    return tripled


#print(tripler())


def this_year():
    return int(((((19+4)*3+4)*3+4)*3+4)*3)


#print(this_year())


# if __name__ == "__main__":
    print(format_name())
    print(tripler())
    print(this_year())


def base_conversion():
    b = int(input("Please enter a base from 2-9."))
    max_n = str(b**4-1)
    number = int(input("Please enter a number to convert, up to " + max_n))
    fourth_digit = str(number % b)
    third_digit = str(number // b % b)
    second_digit = str(number // b // b % b)
    first_digit = str(number // b // b // b % b)
    converted_number = first_digit + second_digit + third_digit + fourth_digit
    return converted_number


#print(base_conversion())


if __name__ == "__main__":
    print(base_conversion())
