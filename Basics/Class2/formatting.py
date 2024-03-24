print("Hello Mr. Tarmo, nice to meet you!")

title = "Mr."
name = "Tarmo"

# + method
print("Hello " + title + name + ", Nice to meet you!")

# printf
print("Hello %s %s, nice to meet you!" % (title, name))

# str. format ()
print("Hello {} {}, nice to meet you!".format(title, name))
print("Hello {title} {name}, nice to meet you!".format(title=title, name=name))
print("Hello {0} {1}, nice to meet you!".format(title, name))

# f-string
print(f"Hello {title} {name}, nice to meet you!")

# rounding
number = 109.34569787352728
print(f"{number:.3f}")
print(f"{round(number, 3)}")

