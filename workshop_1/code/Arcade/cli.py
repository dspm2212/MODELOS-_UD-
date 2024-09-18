"""
This module contains the simple cli for catologe Arcade Machine.

Author: Daniel Santiago Perez Madera <dsperezm@udistrital.edu.co>

This file is part of workshop_1.

workshop_1 is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

workshop_1 is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with workshop_1. If not, see <https://www.gnu.org/licenses/>.
"""
from Arcade import ArcadeMachine
from game import Game
from purchase import Purchase
from payment import FullPayment, FinancingPayment

def main_menu():
    """
    Displays the main menu and manages user interaction for different options.
    """
    
    machines = []  

    while True:
        print("\n--- Main Menu ---")
        print("1. Buy")
        print("2. View Existing Machines")
        print("3. Add Machine")
        print("4. View Available Games")
        print("5. Add Game")
        print("6. Exit")
        choice = input("Enter your choice: ")

        try:
            if choice == '1':
                if machines:
                    print("Choose a machine to purchase:")
                    for i, machine in enumerate(machines):
                        print(f"{i + 1}. Machine with {machine.material} material")
                    machine_choice = int(input("Enter the machine number: ")) - 1
                    if 0 <= machine_choice < len(machines):
                        payment_method = choose_payment_method()
                        purchase = Purchase(machines[machine_choice], payment_method)
                        purchase.gather_customer_info()
                        purchase.finalize_purchase()
                    else:
                        print("Invalid machine selection.")
                else:
                    print("No machines available for purchase.")
            elif choice == '2':
                if machines:
                    for i, machine in enumerate(machines):
                        print(f"Machine {i + 1}:")
                        machine.show_machine_details()
                else:
                    print("No machines created yet.")
            elif choice == '3':
                new_machine = ArcadeMachine()
                new_machine.choose_material()
                while True:
                    add_game = input("Do you want to add a game to this machine? (y/n): ")
                    if add_game.lower() == 'y':
                        new_machine.add_game()
                    else:
                        break
                machines.append(new_machine)
            elif choice == '4':
                Game.show_games()
            elif choice == '5':
                code = input("Enter the game code: ")
                title = input("Enter the game title: ")
                category = input("Enter the game category: ")
                Game.add_game(code, title, category)
                print("Game added successfully.")
            elif choice == '6':
                print("Exiting...")
                break
            else:
                print("Invalid option. Please select again.")
        except ValueError as e:
            print(f"Error: {e}")

def choose_payment_method():
    print("Choose your payment method:")
    print("1. Full Payment\n2. Financing")
    choice = input("Enter your choice: ")

    if choice == '1':
        return FullPayment()
    elif choice == '2':
        installments = int(input("Enter number of installments: "))
        interest_rate = float(input("Enter the interest rate (%): "))
        return FinancingPayment(installments, interest_rate)
    else:
        raise ValueError("Invalid payment method choice")

if __name__ == "__main__":
    main_menu()
