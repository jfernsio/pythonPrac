
title = '         Python     test          '

# remove trailing whitespace from title
print(title)
result = title.strip() # strip blanckspace from both sides
result1 = title.lstrip()
result2 = title.rstrip()
print("only strip func",result)
print("only lstrip func",result1)
print("only rstrip func",result2)

# Output: Python Programming 
# -----------------
text = '      Python     is     fun        '

# split the text from space
print(text.split())

# Output: ['Python', 'is', 'fun']