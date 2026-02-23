x = input("Enter any word : ").lower()
count = 0
for ch in x :
    if ch in "aeiou" :
     count += 1
print(count)
