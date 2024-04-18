def is_function(ordered_pairs):
    mapping = {}
    
    for x, y in ordered_pairs:
        if x in mapping:
            if mapping[x] != y:
                return False
        else:
            mapping[x] = y
    
    return True

pairs1 = [(1, 2), (3, 4), (5, 6)]
pairs2 = [(1, 2), (3, 4), (1, 6)]
pairs3 = [(1, 2), (3, 4), (5)]

if is_function(pairs1):
    print(f"{pairs1} is Function")
else:
    print(f"{pairs1} is not Function")

if is_function(pairs2):
    print(f"{pairs2} is Function")
else:
    print(f"{pairs2} is not Function")

if is_function(pairs3):
    print(f"{pairs3} is Function")
else:
    print(f"{pairs3} is not Function")
