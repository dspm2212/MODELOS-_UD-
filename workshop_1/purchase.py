class Purchase:
    def __init__(self, arcade_machine, payment_method):
        self.arcade_machine = arcade_machine
        self.payment_method = payment_method
        self.customer_name = ""
        self.address = ""
        self.phone_number = ""

    def gather_customer_info(self):
        self.customer_name = input("Enter your name: ")
        self.address = input("Enter your address: ")
        self.phone_number = input("Enter your phone number: ")
        if not self.customer_name or not self.address or not self.phone_number:
            raise ValueError("All customer information must be filled")

    def finalize_purchase(self):
        print(f"Customer Name: {self.customer_name}")
        print(f"Address: {self.address}")
        print(f"Phone Number: {self.phone_number}")
        self.arcade_machine.show_machine_details()

        total_price = self.payment_method.calculate_total(self.arcade_machine.price)
        print(f"Total Price: ${total_price}")
        print("Purchase completed successfully!")