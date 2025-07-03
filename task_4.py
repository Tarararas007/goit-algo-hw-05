
def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Contact not found."
        except ValueError:
            return "Give me name and phone please."
        except IndexError:
            return "Enter the argument for the command"
    return inner

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    name, phone = args
    name = name.lower()
    contacts[name] = phone
    return 'Contact added.'

def change_contact(args, contacts):
    name, phone = args
    name = name.lower()
    contacts[name] = phone
    return 'Contact updated.'
    
def show_phone(args, contacts):
    name = args[0].lower()
    return contacts[name]
    
def show_all(contacts):
    if not contacts:
        return 'No contacts found.'
    result = []
    for name, phone in contacts.items():
        result.append(f'{name}: {phone}')
    return '\n'.join(result)

def main():
    contacts = {}
    print("Welcome to assistant bot!")
    while True:
        user_input = input('Enter a command: ')
        if not user_input:
            print('Enter a valid command.')
            continue

        try:
            command, *args = parse_input(user_input)
        except ValueError:
            print('Enter a valid command.')
            continue

        if command in ['close', 'exit']:
            print('Good bay!')
            break
        elif command == 'hello':
            print('How can i halp you?')
        elif command == 'add':
            print(add_contact(args, contacts))
        elif command == 'change':
            print(change_contact(args, contacts))
        elif command == 'phone':
            print(show_phone(args, contacts))
        elif command == 'all':
            print(show_all(contacts))
        else:
            print('Invalid command.')

if __name__ == "__main__":
    main()