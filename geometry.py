# This program allows the user to choose various
# geometry calculations from a menu. This program
# imports the circle and rectangle modules.

import circle
import rectangle
# The main function.


def main():

    # The choice variable controls the loop
    # and holds the user's menu choice.
    choice = 0

    while not(choice == 5):
        # display the menu.
        display_menu()

        # Get the user's choice.
        choice = int(input('Enter your choice: '))

        # Perform the selected action.
        if choice == 1:
            r = float(input("Enter the circle's radius: "))
            print('The area is {:.3f}.'.format(circle.area(r)))
        elif choice == 2:
            radius = float(input("Enter the circle's radius: "))
            print('The circumference is {:.3f}'.
                  format(circle.circumference(radius)))
        elif choice == 3:
            width = float(input("Enter the rectangle's width: "))
            length = float(input("Enter the rectangle's length: "))
            print('The area is {:.3f}'.format(rectangle.area(width, length)))
        elif choice == 4:
            width = float(input("Enter the rectangle's width: "))
            length = float(input("Enter the rectangle's length: "))
            print('The perimeter is {:.3f}'.
                  format(rectangle.perimeter(width, length)))
        elif choice == 5:
            print("Exiting the program...")
        else:
            print("Error: invalid selection.")


# The display_menu function displays a menu.


def display_menu():
    print("        MENU for ")
    print("1) Area of a circle")
    print("2) Circumference of a circle")
    print("3) Area of a rectangle")
    print("4) Perimeter of a rectangle")
    print("5) Quit")

# Call the main function.


main()
