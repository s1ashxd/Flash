f = open('17.txt')
arr = [int(x, 16) for x in f]
divider = int('1E', 16)
max_sum = 0
cnt = 0
for i in range(len(arr) - 1):
    for j in range(i + 3, len(arr), 3):
        if arr[i] % divider == 0 and arr[j] % divider == 0:
            s = arr[i] + arr[j]
            if len(str(s)) > 4:
                cnt += 1
                if s > max_sum:
                    max_sum = s
print(cnt, max_sum)
