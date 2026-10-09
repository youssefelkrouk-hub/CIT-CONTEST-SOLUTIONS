N = int(input())
strings = input().split()
# write your code here

if len(strings) != N:
    print("500 0")
else:
    count = {}
    for s in strings:
        if s in count:
            count[s] = count[s] + 1
        else:
            count[s] = 1

    pairs = 0
    odd_palindrome = False

    for s in count:
        r = s[::-1]
        if s == r:
            pairs = pairs + count[s] // 2
            if count[s] % 2 == 1:
                odd_palindrome = True
        elif s < r and r in count:
            pairs = pairs + min(count[s], count[r])

    if odd_palindrome:
        print(412, pairs)
    elif pairs == 0:
        print(404, pairs)
    elif 2 * pairs == N:
        print(200, pairs)
    else:
        print(202, pairs)