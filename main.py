# Dog Walker Program

# Define cost structure
# This dictionary stores the cost details for each walk duration.
# Includes the base cost for one dog. The additional cost per extra dog. The maximum number of dogs allowed for each duration.

walk_details = {
    20: {"cost": 16.00, "extra_cost": 5.00, "max_dogs": 5},
    30: {"cost": 21.00, "extra_cost": 6.00, "max_dogs": 4},
    45: {"cost": 32.50, "extra_cost": 8.50, "max_dogs": 3}
}


def get_walk_duration():
    # Get the walk duration from the user
    # Check if the entered duration is valid (20, 30, or 45minutes)
    walk_duration = int(input("Enter walk duration (20, 30, or 45 minutes): "))
    if walk_duration not in walk_details:
        print("Invalid duration")
        return None
    return walk_duration


def get_num_dogs(walk_duration):
    # Get the number of dogs from the user
    # Ensure the number of dogs does not exceed the maximum allowed for the chosen duration
    num_dogs = int(input("Enter number of dogs: "))
    if num_dogs > walk_details[walk_duration]["max_dogs"]:
        print(f"Too many dogs for a {walk_duration}-minute walk")
        return None
    return num_dogs


def calculate_total_cost(walk_duration, num_dogs):
    # Calculate the total cost based on the walk duration and the number of dogs
    # Cost for the first dog is fixed, additional dogs have an extra cost
    cost_for_one_dog = walk_details[walk_duration]["cost"]
    extra_cost = (num_dogs - 1) * walk_details[walk_duration]["extra_cost"] if num_dogs > 1 else 0
    total_cost = cost_for_one_dog + extra_cost
    return cost_for_one_dog, extra_cost, total_cost


def print_receipt(walk_duration, num_dogs, cost_for_one_dog, extra_cost, total_cost):
    # Print the receipt with all relevant details: walk duration, number of dogs, costs, and total cost
    print("\nRECEIPT")
    print(f"Walk duration: {walk_duration} minutes")
    print(f"Number of dogs: {num_dogs}")
    print(f"Cost for first dog: ${cost_for_one_dog:.2f}")
    if num_dogs > 1:
        print(f"Cost for additional dogs: ${extra_cost:.2f}")
    print(f"Total cost: ${total_cost:.2f}")


def main():
    # Main function to run the program
    # It handles user input, calculates costs, and prints the receipt
    try:
        walk_duration = get_walk_duration()
        if walk_duration is None:
            return

        num_dogs = get_num_dogs(walk_duration)
        if num_dogs is None:
            return

        cost_for_one_dog, extra_cost, total_cost = calculate_total_cost(walk_duration, num_dogs)
        print_receipt(walk_duration, num_dogs, cost_for_one_dog, extra_cost, total_cost)

    except ValueError:
        # Handle invalid input (non-numeric values)
        print("Invalid input. Please enter numeric values only.")


if __name__ == "__main__":
    main()

