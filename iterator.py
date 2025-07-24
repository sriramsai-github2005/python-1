class SquareIterator:
    def __init__(self, limit):
        self.limit = limit
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.limit:
            result = self.current ** 2
            self.current += 1
            return result
        else:
            raise StopIteration

# Using the custom iterator
squares = SquareIterator(5)

print("Squares up to 5:")
for num in squares:
    print(num)
