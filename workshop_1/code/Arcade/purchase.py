"""
This module defines the Purchase class, which manages the arcade machine purchase process, including customer information and payment method.

Author: Daniel Santiago Perez Madera <dsperezm@udistrital.edu.co>

This file is part of workshop_1.

workshop_1 is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

workshop_1 is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with workshop_1. If not, see <https://www.gnu.org/licenses/>.
"""

class Purchase:
    """
    This class handles the purchase of an arcade machine, including customer information and payment processing.
    """

    def __init__(self, arcade_machine, payment_method):
        self.arcade_machine = arcade_machine
        self.payment_method = payment_method
        self.customer_name = ""
        self.address = ""
        self.phone_number = ""

    def gather_customer_info(self)-> None:
        """
        Gathers customer information for the purchase.

        Raises:
            ValueError: If any required customer information is missing.
        """
         
        self.customer_name = input("Enter your name: ")
        self.address = input("Enter your address: ")
        self.phone_number = input("Enter your phone number: ")
        if not self.customer_name or not self.address or not self.phone_number:
            raise ValueError("All customer information must be filled")

    def finalize_purchase(self)-> None:
        """
        Finalizes the purchase by displaying customer and arcade machine details, and calculating the total price.

        Returns:
            None: Displays the purchase summary.
        """
        print(f"Customer Name: {self.customer_name}")
        print(f"Address: {self.address}")
        print(f"Phone Number: {self.phone_number}")
        self.arcade_machine.show_machine_details()

        total_price = self.payment_method.calculate_total(self.arcade_machine.price)
        print(f"Total Price: ${total_price}")
        print("Purchase completed successfully!")
