for a in range(1, 151):
    for b in range(a, 151):
        for c in range(b, 151):
            for d in range(c, 151):
                total = a ** 5 + b ** 5 + c ** 5 + d ** 5
                e = int(total ** 0.2)
                if total == e ** 5:
                    print(f'a = {a}, b = {b}, c = {c}, d = {d}, e = {e}, n = {a + b + c + d + e}')
                    break

