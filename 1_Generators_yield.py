def generator(x):
    for i in range(x):
        yield "Help me"


if __name__ == '__main__':
    for item in generator(5):
        print(item)
