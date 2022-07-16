

n = 20
prime_list = [2, 3, 4, 5, 6, 7, 8, 9, 10,
              11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
for i in range(2, n+1):
    if i not in range(i*i, n+1, i):
        print(i)
        for j in prime_list:
            if j in prime_list:
                prime_list.remove(j)
