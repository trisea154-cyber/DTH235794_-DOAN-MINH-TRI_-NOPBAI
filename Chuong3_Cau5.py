def xu_ly(i, j, k):
    if i < j:
        if j < k:
            i = j
        else:
            j = k
    else:
        if j > k:
            j = i
        else:
            i = k
    print("i =", i, ", j =", j, ", k =", k)

# Test theo đề bài:
print("Trường hợp (a):")
xu_ly(3, 5, 7)

print("Trường hợp (b):")
xu_ly(3, 7, 5)

print("Trường hợp (c):")
xu_ly(5, 3, 7)

print("Trường hợp (d):")
xu_ly(5, 7, 3)

print("Trường hợp (e):")
xu_ly(7, 3, 5)

print("Trường hợp (f):")
xu_ly(7, 5, 3)
