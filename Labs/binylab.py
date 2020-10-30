#Perform these in Python shell prior  to using biny.py

#Clear screen
print(u"\u001B[2J", u"\u001B[0;0H")

#ordinal value of letter
print(ord("A"))
print(ord("B"))
print(ord("M"))
#store in binary or ordinal
phrase = b"ABM"
print(phrase[0])

#show number base 2, 16
print(bin(phrase[0]))
print(hex(phrase[0]))
print(hex(phrase[2]))

#non-ascii
apple = "🍏"
print(ord(apple))
# apple = b"🍏" #fails
apple = u"🍏" #unicode
print(apple.encode("utf-8"))

# ascii character encoded
a = u"A"
print(a.encode("utf-8"))

# unicode is system that is bigger than ascii
apple_encode = apple.encode("utf-8")
print(apple_encode[0])
print(bin(apple_encode[0]))
#apple is several number together
print(hex(apple_encode[0]))
print(hex(apple_encode[1]))
print(hex(apple_encode[2]))