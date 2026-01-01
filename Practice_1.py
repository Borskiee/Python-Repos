# Input
def num_func():
    while True:
        try:
            num_input = [int(x) for x in input("Enter numbers separated by spaces: ").split()]
            return num_input
            break
        except ValueError:
            print("Please enter a number.")

numbers = num_func()

# Logic
def compute_sum(n):
    return sum(n)

def compute_avg(a):
    return sum(a) / len(a)

def compute_max(n):
    return max(n)

def compute_min(n):
    return min(n)


# Output
print(f"Sum: {compute_sum(numbers)}")
print(f"Average: {compute_avg(numbers):.2f}")
print(f"Highest: {compute_max(numbers)}")
print(f"Lowest: {compute_min(numbers)}")
