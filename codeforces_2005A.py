for _ in range(int(input())):
    n = int(input())

    letters = "aeiou"
    result = ""
    for i in range(5):
        if i < n%5:
            result += letters[i]*(n//5+1)
        else:
            result += letters[i]*(n//5)

    print(result)
