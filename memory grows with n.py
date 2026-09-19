n = 4
guess = input(" Predict: How many items in the list for n=4?")
points = list(range(1, n+1))
print(" Your guess:",guess," List:",points, " items:",len(points))

input("Predict: What happens to list size as N grows? Press enter")
for size in [4,10,100,1000]:
    print(f"n = {size:<5} list uses {size:>5} items in memory")
