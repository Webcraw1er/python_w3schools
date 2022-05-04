"""
you can avoid printing spaces(" ") or crlf automatically in print() methods
    with sep='' and end=''

Very good for you, the \n and spaces you wrote yourself will not be neglected.
"""

print(" hello,")
print(" my name\n is Jus", "tin.")
print(" glad to meet you\n")

print(" Hello,", end='')
print(" my name\n is Jus", "tin.", sep='', end='')
print(" glad to meet you\n")