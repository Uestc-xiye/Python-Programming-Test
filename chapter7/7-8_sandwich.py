sandwich_orders = ['beef', 'fish', 'pepperoni']
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print("I made your " + current_sandwich + " sandwich")
    finished_sandwiches.append(current_sandwich)

print("\nThe following sandwich have been finished:")
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich)