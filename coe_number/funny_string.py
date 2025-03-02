def funnyString(s):
    n = len(s)

    for i in range(1, n // 2):
        if abs(ord(s[i]) - ord(s[i - 1])) != abs(ord(s[n - i - 1]) - ord(s[n - i])):
            return "Not Funny"

    return "Funny"
