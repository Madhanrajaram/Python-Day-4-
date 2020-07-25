s =input("Enter the word:")
print(s)
if s.islower():
  print(s.upper())
elif s.isupper():
  print(s.lower())
elif s.isalpha():
  print(s.swapcase())
else:
  print("Invalid input")

  