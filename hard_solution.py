f = open('17h.txt')
arr = []
for line in f:
    d = line.split()
    arr.append([int(d[0], 16), int(d[1], 16)])
divider = int('1E', 16)
max_sum = 0
cnt = 0
for i in range(len(arr) - 1):
    for j in range(i + 1, len(arr)):
        cond = ((arr[i][0] % divider == 0) +
                (arr[i][1] % divider == 0) +
                (arr[j][0] % divider == 0) +
                (arr[j][1] % divider == 0))
        if cond >= 3:
            s = sum(arr[i]) + sum(arr[j])
            converted = oct(s)[2:]
            if len(converted) < 6:
                cnt += 1
                if s > max_sum:
                    max_sum = s
print(cnt, max_sum)