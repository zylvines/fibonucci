class FibonacciIterator:
    def __init__(self, max_count):
        self.max_count = max_count
        self.current = 0
        self.next = 1
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= self.max_count:
            raise StopIteration
        result = self.current
        self.current, self.next = self.next, self.current + self.next
        self.index += 1
        return result


if __name__ == "__main__":
    max_count = int(input("Fibonacci ketma-ketligidagi nechta sonni chiqarishni istaysiz? "))
    fibonacci = FibonacciIterator(max_count)
    for num in fibonacci:
        print(num)
