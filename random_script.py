import random
print("Random number:", random.randint(1, 100))
print("Random choice:", random.choice(['apple', 'banana', 'cherry', 'date']))
numbers = [random.randint(1, 50) for _ in range(5)]
print("Random list:", numbers)