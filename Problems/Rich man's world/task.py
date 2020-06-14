initial_sum = int(input())
counter = 0
interest = 0.071


while initial_sum < 700000:
    initial_sum = initial_sum * (1 + interest)
    counter += 1

print(counter)