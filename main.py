from menu import MENU, resources


def report():
    for k, v in resources.items():
        print(k, ":", v)
    ask_choice()


def check_quantity(menu_copy, choice):
    if choice == 'espresso' and (int(resources.get('water')) < int(menu_copy.get('espresso').get('ingredients').get('water')) or int(resources.get('coffee')) < (menu_copy.get('espresso').get('ingredients').get('coffee'))):
        print('Not enough resources for ', choice)
        ask_choice()
    elif choice == 'latte' and (int(resources.get('water')) < int(menu_copy.get('latte').get('ingredients').get('water')) or int(resources.get('coffee')) < (menu_copy.get('latte').get('ingredients').get('coffee')) or int(resources.get('milk')) < (menu_copy.get('latte').get('ingredients').get('milk'))):
        print('Not enough resources for ', choice)
        ask_choice()
    elif choice == 'cappuccino' and (int(resources.get('water')) < int(menu_copy.get('cappuccino').get('ingredients').get('water')) or int(resources.get('coffee')) < (menu_copy.get('cappuccino').get('ingredients').get('coffee')) or int(resources.get('milk')) < (menu_copy.get('cappuccino').get('ingredients').get('milk'))):
        print('Not enough resources for ', choice)
        ask_choice()


def ask_for_money_check(choice):
    check_quantity(MENU, choice)
    quarters = 0
    dimes = 0
    nickels = 0
    pennies = 0
    while not str(quarters).isdigit() or int(quarters) <= 0:
        quarters = input("How many quarters(enter a positive integer): ")
        if str(quarters).isdigit():
            quarters = int(quarters)
            if quarters > 0:
                break
    while not str(dimes).isdigit() or int(dimes) <= 0:
        dimes = input("How many dimes(enter a positive integer): ")
        if str(dimes).isdigit():
            dimes = int(dimes)
            if dimes > 0:
                break
    while not str(nickels).isdigit() or int(nickels) <= 0:
        nickels = input("How many nickels(enter a positive integer): ")
        if str(nickels).isdigit():
            nickels = int(nickels)
            if nickels > 0:
                break
    while not str(pennies).isdigit() or int(pennies) <= 0:
        pennies = input("How many pennies(enter a positive integer): ")
        if str(pennies).isdigit():
            pennies = int(pennies)
            if pennies > 0:
                break
    while not str(pennies).isdigit() or int(pennies) <= 0:
        pennies = int(input("How many pennies(enter a positive integer): "))
    money_collected = float(((quarters * 25) + (dimes * 10) + (nickels * 5) + (pennies * 1)) / 100.0)
    if money_collected < MENU.get(choice).get('cost'):
        print(f"Money not enough for {choice}")
    elif money_collected == MENU.get(choice).get('cost'):
        print(f"Your change is {money_collected} - {MENU.get(choice).get('cost')}")
        print(f"Enjoy your {choice} coffee")
    else:
        formatted_string = "{:.2f}".format(round(money_collected - MENU.get(choice).get('cost'), 2))
        print(f"Your change is", formatted_string)
        print(f"Enjoy your {choice} coffee")
    return


def espresso(menu_copy, choice):
    ask_for_money_check(choice)
    resources['water'] = int(resources.get('water')) - int(menu_copy.get('espresso').get('ingredients').get('water'))
    # resources['milk'] = int(resources.get('milk')) - int(menu_copy.get('espresso').get('ingredients').get('milk'))
    resources['coffee'] = int(resources.get('coffee')) - int(menu_copy.get('espresso').get('ingredients').get('coffee'))
    ask_choice()


def latte(menu_copy, choice):
    ask_for_money_check(choice)
    resources['water'] = int(resources.get('water')) - int(menu_copy.get('latte').get('ingredients').get('water'))
    resources['milk'] = int(resources.get('milk')) - int(menu_copy.get('latte').get('ingredients').get('milk'))
    resources['coffee'] = int(resources.get('coffee')) - int(menu_copy.get('latte').get('ingredients').get('coffee'))
    ask_choice()


def cappuccino(menu_copy, choice):
    ask_for_money_check(choice)
    resources['water'] = int(resources.get('water')) - int(menu_copy.get('cappuccino').get('ingredients').get('water'))
    resources['milk'] = int(resources.get('milk')) - int(menu_copy.get('cappuccino').get('ingredients').get('milk'))
    resources['coffee'] = int(resources.get('coffee')) - int(
        menu_copy.get('cappuccino').get('ingredients').get('coffee'))
    ask_choice()


def ask_choice():
    choice: str = ''
    while choice.lower() not in ('espresso', 'latte', 'cappuccino', 'report', 'exit'):
        choice = input("What would you like to have(type espresso/latte/cappucino) "
                       "or do you just need a report(type report)? or type exit to quit: ")
        if choice == "report":
            report()
        elif choice == "espresso":
            espresso(MENU, choice)
        elif choice == "latte":
            latte(MENU, choice)
        elif choice == "cappuccino":
            cappuccino(MENU, choice)
        elif choice == "exit":
            break


def main():
    ask_choice()


if __name__ == "__main__":
    main()
