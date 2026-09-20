scores = [3,7,2,9,4,1,8,5,6]

input("List: " + str(scores)+" n=9 Linear search - checks left to right. Press Enter to run")

target = int(input("enter a number to search for:"))

input("searching for " + str(target)+ ". Press Enter to run")
steps = 0
for score in scores:
    steps += 1
    if score == target:
        break
print(" target=", target, " found at position", steps, " checks=", steps)

input("Conpare with best and worst cases. Press Enter")
mid = len(scores) //2
print(" Best: 1 check -> 0(1) Average:", mid,"checks -> 0(n) Worst:9 , Yours",steps)
input("All three cases. Press Enter")
print(" Best 0(1) Average 0(n) Worst 0(n) -> Big-0 = worst case = 0(n)")
