def print_longer_string(s1, s2):
    if len(s1) > len(s2):
        print(s1)
    elif len(s1) < len(s2):
        print(s2)
    else:
        print(s1)
        print(s2)

# Test hàm
print_longer_string("hello", "world!")
