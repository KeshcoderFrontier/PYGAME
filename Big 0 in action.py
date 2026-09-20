n = 10

guess = input("Double Loop at n = 10 checks n x n pairs. How many?")

input("Formula: One calculation , done. Press Enter to run")
steps = 1
print(" steps=", steps, " -> 0(1) constant time -> steps never change")

input("Loop: one step per item. Press Enter to run")
steps = 0
for i in range(n):
    steps += 1
print(" steps = ", steps," -> 0(n) linear  time -> steps grow with n")

input("Doube Loop : checks every pair. Press Enter to run")
steps = 0
for i in range(n):
    for j in range(n):
        steps +=1
print(" steps =", steps, "your guess:",guess, " -> 0(n^2) quadratic time")


input("Two more notations. Press Enter")
print(" Big Omega 0 -> best case lower bound")
print(" Big theta 0 _> exact bound (worst = best")

    
