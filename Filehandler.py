file = open("bucket_list.txt","w")
file.write("1,Visit the Taj Mahal\n")
file.write("2,Learn to play the Piano better\n")
file.write("3,Code my own scratch game\n")
file.close()
print("Bucket list saved to bucket-list.txt!")


file = open("bucket_list.txt","r")
content = file.read()
print("\n=== My Bucket list ===")
print(content)
file.close()

file = open("bucket_list.txt","r")
lines = file.readlines()
print(f"You have {len(lines)} items on your bucket list.")
file.close()

file = open("bucket_list.txt","a")
file.write("4.Travel to Singapore\n")
file.write("5 Run a 4k Marathon\n")
file.close()
print("\n2 more items were added!")

file = open("bucket_list.txt", "r")
print("\n=== Updated Bucket List ===")
print(file.read())
file.close()
            
            
            


           
