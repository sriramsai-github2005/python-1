def count_up_to(n):
    count = 1
    while count <= n:
        yield count
        count += 1

# Using the generator
for num in count_up_to(3):
    print(num)


