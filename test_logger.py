from logger import log_time

@log_time
def hello():
    print("Python is fun!")

@log_time
def add(a, b):
    return a + b

hello()

result = add(2, 3)
print("Result:", result)
