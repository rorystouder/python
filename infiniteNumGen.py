def frame():
    yield 2
    a = 2
    b = 1
    while True:
        yield b
        a, b = b, a + b

for x in frame():
    print(x)
