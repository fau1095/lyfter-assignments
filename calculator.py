initial_number = 0.0
calculator_actions = ['1','2','3','4','5','6']

def terminal_menu():
    print("Choose an action to perform: ")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Reset")
    print("6. Exit")
    action = input("Enter a number to perform an action: ")
    return action

def main():
    global initial_number
    while True:
        print(f"Current number: {initial_number}")
        action = terminal_menu()
        if action in calculator_actions:
            if action == '6':
                print("Exiting the calculator...")
                break
            elif action == '5':
                initial_number = 0.0
            elif action == '4':
                num = float(input("Enter a number: "))
                try:
                    if num in {0, 0.0} or initial_number in {0, 0.0}:
                        raise ValueError()
                except ValueError:
                    print("You can't divide by zero")
                    continue
                initial_number /= num
            elif action == '3':
                num = int(input("Enter a number: "))
                initial_number *= num
            elif action == '2':
                num = int(input("Enter a number: "))
                initial_number -= num
            elif action == '1':
                num = int(input("Enter a number: "))
                initial_number += num                
            print(f'The result is: {initial_number}')
        
        if action not in calculator_actions:
            print("Invalid action, please try again")
            continue
        
main()                