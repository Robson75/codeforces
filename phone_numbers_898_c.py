class PhoneNumbers:

    pass


if __name__ == "__main__":
    entries = int(input())
    contacts_dict = {}
    for entry in range(entries):
        contact = list(input().split())
        if contact[0] not in contacts_dict:
            contacts_dict[contact[0]] = []
        for nr in contact[2:]:
            contacts_dict[contact[0]].append(nr)
    # print(contacts_dict)

    for key in contacts_dict:
        numbers = []
        new_numbers = []

        for value in contacts_dict[key]:
            numbers.append(value)
            numbers.sort(key=len)


        for number in range(len(numbers) - 1):
            add_new = True
            number1 = numbers[number]
            nr_length = len(number1)
            for number2 in numbers[number + 1:]:
                if str(number2)[-nr_length:] == number1:
                    add_new = False
                    break
            if add_new:
                new_numbers.append(number1)
        new_numbers.append(numbers[-1])
        contacts_dict[key] = new_numbers
    print(len(contacts_dict))
    for key in contacts_dict:
        out_string = key
        out_string += " "
        out_string += str(len(contacts_dict[key]))
        for value in contacts_dict[key]:
            out_string += " "
            out_string += str(value)
        print(out_string)
