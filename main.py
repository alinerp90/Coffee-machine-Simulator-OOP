from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

machine = "on"
while machine == "on":
    drink = input("What hot drink do you like? latte/espresso/cappuccino: ").lower()
    choice = menu.find_drink(drink)
    if drink == "report":
        coffee_maker.report()
        money_machine.report()
    elif drink == "off":
        machine = "off"
    else:
        print(choice.cost)
        coffee_maker.is_resource_sufficient(choice)
        money_machine.make_payment(choice.cost)
        coffee_maker.make_coffee(choice)
        restart = input("Do you want to make another drink? (yes/no): ").lower()
        if restart == "no" :
            machine = "off"
    






# #list of drinks
# drink_list = menu.get_items().split("/")
# for i in drink_list:
#     print(i)

# class Animal:
#     def __init__(self, word):
#         self.word = word

#     def speak(self):
#         print(self.word)


# # class Dog(Animal):
# #     def __init__(self):
# #         super.__init__(self, "bark")

# dog = Animal("auau")
# cat = Animal("miau")

# dog.speak()
# cat.speak()
