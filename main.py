from encrypt import encrypt_file
from decrypt import decrypt_file

def main():
    while True:
        choice = input("Would you like to (e)ncrypt or (d)ecrypt a file? (q to quit): ")
        if choice == 'q':
            break
        elif choice == 'e':
            encrypt_file()
        elif choice == 'd':
            decrypt_file()
        else:
            print("Invalid choice, please try again.")

if __name__ == '__main__':
    main()
