"""
This module defines the PaymentMethod class and its subclasses, responsible for handling different payment options.

Author: Daniel Santiago Perez Madera <dsperezm@udistrital.edu.co>

This file is part of workshop_1.

workshop_1 is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

workshop_1 is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with workshop_1. If not, see <https://www.gnu.org/licenses/>.
"""
from abc import ABC, abstractmethod

class PaymentMethod:
    """
    Abstract base class for different payment methods.
    """

    @abstractmethod
    def calculate_total(self, base_price:float)->float:
        """
        Calculates the total cost based on the base price and specific payment conditions.

        Args:
            base_price (float): The base price of the arcade machine.

        Returns:
            float: The total cost after applying payment conditions.
        """



class FullPayment(PaymentMethod):
    """
    Class representing full payment .
    """
    def calculate_total(self, base_price:float)->float:
        """
        This concreted method represent the price of the Arcade Machine 

        Returns the base price as no additional charges are applied for full payment.

        Args:
            base_price (float): The base price of the arcade machine.

        Returns:
            float: The total cost (same as base price).
        """
        return base_price


class FinancingPayment(PaymentMethod):
    """
    Class representing financing payment (with interest applied).

    Args:
        installments (int): Number of installments.
        interest_rate (float): Interest rate to be applied.

    """
    def __init__(self, installments, interest_rate):
        self.installments = installments
        self.interest_rate = interest_rate

    def calculate_total(self, base_price:float)->float:
        """
        Calculates the total cost including interest for financing payment.

        Args:
            base_price (float): The base price of the arcade machine.

        Returns:
            float: The total cost after applying interest.
        """
        return base_price + base_price * (self.interest_rate / 100)
