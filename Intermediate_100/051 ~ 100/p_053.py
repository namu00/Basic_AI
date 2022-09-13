data = input()
open = data.count("(")
close = data.count(")")

if open != close: print("NO")
else: print("YES")