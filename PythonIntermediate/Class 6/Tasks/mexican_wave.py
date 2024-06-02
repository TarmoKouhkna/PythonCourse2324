def wave(people):
    result = []
    for i in range(len(people)):
        if people[i].isalpha():
            result.append(people[:i] + people[i].upper() + people[i + 1:])
    return result


# Test cases
print(wave("hello"))  # ["Hello", "hEllo", "heLlo", "helLo", "hellO"]
print(wave(""))  # []
print(wave(
    "two words"))   # ["Two words", "tWo words", "twO words", "two Words", "two wOrds", "two woRds",
                    # "two worDs", "two wordS"]
print(wave("a       b    "))  # ["A       b    ", "a       B    "]
