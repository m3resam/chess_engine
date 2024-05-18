def main():
    num = int(input())
    if num <= 0:
        return main()
    k = 0
    while num > 0:
        k = k + 2 * num -1
        num -= 1

    print(k)

main()
