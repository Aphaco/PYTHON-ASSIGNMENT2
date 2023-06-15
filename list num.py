numbers = []

# Prompt the user to enter a list of numbers
while True:
    num = input("Enter a number (or 'done' to finish): ")
    if num == "done":
        break
    numbers.append(int(num))

# Calculate the sum of the positive numbers
total = 0
for num in numbers:
    if num < 0:
        continue
    total += num

# Print the sum of the positive numbers
print("Sum of positive numbers:", total)