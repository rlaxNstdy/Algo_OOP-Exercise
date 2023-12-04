from ProgramExerciseAFR import Food 

def create_item_list():
    item_list = []
    num_items = int(input("Enter the number of items to purchase: "))

    while num_items < 1:
        print("Number of items must be at least 1. Please try again.")
        num_items = int(input("Enter the number of items to purchase: "))

    for _ in range(num_items):
        name = input("Enter the name of the food item: ")
        pounds = float(input("Enter the amount of the food item in pounds: "))

        while pounds <= 0:
            print("Amount of pounds must be greater than 0. Please try again.")
            pounds = float(input("Enter the amount of the food item in pounds: "))

        food_item = Food(name, pounds)
        item_list.append(food_item)

    return item_list

def display_item_list(item_list):
    for item in item_list:
        print(item)

def calculate_total_cost(item_list):
    total_cost = sum(item.getcalulated() for item in item_list)
    return total_cost

def main():
    items = create_item_list()
    print("\nItems Purchased:")
    display_item_list(items)

    total_cost = calculate_total_cost(items)
    print(f"\nTotal Cost of Items: ${total_cost:.2f}")

if __name__ == "__main__":
    main()
