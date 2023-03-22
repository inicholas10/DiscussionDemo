def encoder(password):
    new_password = ''
    for i in password:
        new_password += str((int(i)+3) % 10)
    return new_password

def decoder(string):
    new_string = ''
    for i in string:
        new_string += str((int(i)-3) % 10)

    return new_string

def main():

    while True:
        print("Menu\n"
              "-------------\n"
              "1. Encode\n"
              "2. Decode\n"
              "3. Quit\n")
        menu_option = int(input("Please enter an option: "))

        if menu_option == 1:
            password = str(input("Please enter your password to encode: "))
            new_password = encoder(password)
            print("Your password has been encoded and stored!\n")
        if menu_option == 2:
            print(f'The encoded password is {new_password}, and the original password is {decoder(new_password)}.\n')
        if menu_option == 3:
            break

if __name__ == "__main__":
    main()
