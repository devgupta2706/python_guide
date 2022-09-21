check=lambda a, b: a == b


def toString(List):
    return ''.join(List)

 
def permute(a, l, r):
    if check(l, r):
        print(toString(a), end=" ")
    else:
        for i in range(l, r + 1):
            a[l], a[i] = a[i], a[l]
            permute(a, l + 1, r)
            a[l], a[i] = a[i], a[l]


str = input("Enter the string:")
n = len(str)
a = list(str)
permute(a, 0, n-1)
