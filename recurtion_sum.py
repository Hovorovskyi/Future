def recurtion_sum(n):
    if len(str(n)) <= 1:
        return
    else:
        n = str(n)
        f, s = n[-1], n[-2]
        return int(f) + int(recurtion_sum((s)))


numbers = 123
recurtion_sum(numbers)
