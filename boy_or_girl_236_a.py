class BoyOrGirl:
    pass


if __name__ == "__main__":
    user_name = input()
    name_letters = set(user_name)
    if len(name_letters) % 2 == 0:
        print('CHAT WITH HER!')
    else:
        print('IGNORE HIM!')
