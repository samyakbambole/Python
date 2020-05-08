#List functions Program
#8/5/2020

lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Samyak", "Ayush", "Surabhi", "Jayden", "Ayush.H", "Laptop" ]
friends2 = friends.copy()

friends.extend(lucky_numbers) # This will extend the elements of the list.

friends.append("Sam") # This will add another item / string to the list

friends.insert(2, "Laptop") # This will insert at the given index position.

friends.remove("Jayden")

# friends.clear() This will clear the whole list

friends.pop() # This will remove the last element

print(friends.index("Laptop"))

print(friends.count("Laptop"))

lucky_numbers.sort() # This will sort the numbers in ascending order

lucky_numbers.reverse()

print(friends)

print(lucky_numbers)
