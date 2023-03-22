def encoder(password):
    new_password = ''
    for i in password:
        new_password += str(int(i)+3)
    return new_password

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
            pass
        if menu_option == 3:
            break

main()