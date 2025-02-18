# iterator and generator  __iter__() and __next__()

# Iterable (oddiy ro‘yxat)
numbers = [1, 2, 3, 4, 5]

# Ro‘yxatni iteratorga aylantiramiz
num_iter = iter(numbers)

# print(next(num_iter))  # 1
# print(next(num_iter))  # 2
# print(next(num_iter))  # 3
# print(next(num_iter))  # 4
# print(next(num_iter))  # 5
# print(next(num_iter))  # StopIteration xatosi chiqaradi

class Counter:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self  # O‘zi iterator bo‘lishi kerak

    def __next__(self):
        if self.current > self.end:
            raise StopIteration  # Agar chegaradan oshsa, to‘xtatamiz
        val = self.current
        self.current += 1
        return val

# Iterator yaratamiz
count = Counter(1, 5)

# for num in count:
#     print(num)  # 1, 2, 3, 4, 5 chiqadi


def my_generator():
    yield 1
    yield 2
    yield 3

gen = my_generator()

# print(next(gen))  # 1
# print(next(gen))  # 2
# print(next(gen))  # 3

def my_generator():
    yield "A"
    yield "B"
    yield "C"

# for letter in my_generator():
#     print(letter)
#

class SquareIterable:
    def __init__(self,stop:int):
        self.stop=stop
        self.current=0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current>self.stop:
            raise StopIteration

        result=self.current**2
        self.current += 1
        return result

my_custum_iterator=SquareIterable(7)

# new_iterator=iter(my_custum_iterator)
# print('first',next(new_iterator))
# print('second',next(new_iterator))
# print('third',next(new_iterator))
# print('fouth',next(new_iterator))
#
# for i in my_custum_iterator:
#     print(i)

# Generator

def my_range(limit):
    i=0
    while i < limit:
        yield i
        i+=1

lst=my_range(10)




























