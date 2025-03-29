def find_cube_pairs(targ):
    solutions = []
    max_num = int(targ ** (1/3))  

    for a in range(1, max_num):
        for b in range(a, max_num):
            if a**3 + b**3 == targ:
                solutions.append((a, b))
    return solutions

pairs = find_cube_pairs(1729)

print("Valid cube pairs for 1729:")
for a, b in pairs:
    print(f" → {a}³ + {b}³ = {a**3} + {b**3} = 1729")
  
