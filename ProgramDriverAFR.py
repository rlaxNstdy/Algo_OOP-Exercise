from ProgramExerciseAFR import Food

class PurchasedItem:
    def __init__(self, foodname, pounds, price_per_pound):
        self.name = foodname
        self.pounds = pounds
        self.price_per_pound = price_per_pound

    def calculate_cost(self):
        return self.pounds * self.price_per_pound

def create_item_list():
    item_list = []
    num_items = int(input("How many items will you order today? "))

    while num_items < 1:
        print("Number of items must be at least 1!!!!")
        num_items = int(input("How many items will you order today? "))

    for _ in range(num_items):
        name = input("Enter the name of the item: ")
        pounds = float(input("Enter the amount of the item in pounds: "))
        
        while pounds <= 0:
            print("Amount of pounds must be greater than 0. Please try again.")
            pounds = float(input("Enter the amount of the item in pounds: "))
        
        item = PurchasedItem(name, pounds)
        item_list.append(item)

    return item_list

def display_item_list(item_list):
    for item in item_list:
        print(f"Item: {item.name}, Pounds: {item.pounds}, Price per Pound: ${item.price_per_pound:.2f}, Cost: ${item.calculate_cost():.2f}")


def main():
    items = create_item_list()
    print("\nItems Purchased:")
    display_item_list(items)
    
    total_cost = calculate_total_cost(items)
    print(f"\nTotal Cost of Items: ${total_cost:.2f}")

if __name__ == "__main__":
    main()
