def swap(A, B):
    A = A + B
    B = A - B
    A = A - B
    return A, B


if __name__ == '__main__':
    print(swap(1, 2))
