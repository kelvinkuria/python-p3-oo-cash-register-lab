class Item:
  """
  A class representing an item with a name and price.
  """

  def __init__(self, name, price):
    """
    Initializes an Item object with a name and price.

    Args:
      name: The name of the item (str).
      price: The price of the item (float).
    """
    self.name = name
    self.price = price

  def __str__(self):
    """
    Returns a string representation of the item in the format "name: $price".

    Returns:
      A string representation of the item.
    """
    return f"{self.name}: ${self.price}"


class CashRegister:
  """
  A class representing a cash register system.
  """

  def __init__(self):
    """
    Initializes the cash register with an empty list of transactions and a total of 0.
    """
    self.transactions = []
    self.total = 0.0  # Use float for accurate decimal calculations

  def purchase_item(self, item):
    """
    Adds a purchased item (represented by an object) to the list of transactions
    and updates the total amount.

    Args:
      item: An object representing the purchased item.
    """
    self.transactions.append(item)
    self.total += item.price

  def get_total(self):
    """
    Returns the current total price of all purchased items.

    Returns:
      The current total price (float).
    """
    return self.total

  def show_items(self):
    """
    Prints a list of all purchased items and their details.
    """
    for item in self.transactions:
      print(item)  # Assume the item object has a __str__ method

  def apply_discount(self, discount_percent):
    """
    Applies a discount to the total price based on the provided percentage.

    Args:
      discount_percent: An integer representing the discount percentage.

    Returns:
      The final total price after applying the discount (float).
    """
    discount = self.total * (discount_percent / 100.0)  # Convert percentage to decimal
    self.total -= discount
    return self.total

  def void_last_transaction(self):
    """
    Removes the last purchased item from the transactions list and subtracts its
    price from the total.

    Raises:
      IndexError: If there are no transactions to void.
    """
    if not self.transactions:
      raise IndexError("No transactions to void")
    last_item = self.transactions.pop()
    self.total -= last_item.price


# Example usage
apple = Item("Apple", 1.50)
banana = Item("Banana", 0.75)

cash_register = CashRegister()
cash_register.purchase_item(apple)
cash_register.purchase_item(banana)

print("Items purchased:")
cash_register.show_items()

total_price = cash_register.get_total()
print(f"Total before discount: ${total_price:.2f}")

discount = 10  # Apply a 10% discount
final_price = cash_register.apply_discount(discount)
print(f"Total after {discount}% discount: ${final_price:.2f}")





