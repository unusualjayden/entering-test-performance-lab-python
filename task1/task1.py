def itoBase(nb, base):
    nums = []
    res = []
    b = len(base)
    while (nb != 0):
        nums.append(nb % b)
        nb = nb // b
    nums.reverse()
    for l in nums:
        res.append(str(base[l]))
    return "".join(res)

print(itoBase(127482935, "0123456789abcdef"))

