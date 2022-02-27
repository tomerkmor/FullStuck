s = "xy"*50

print(s+"\n")


s = input("Enter some text(at least 100 words): ")
print(s[:5])
print(s[len(s)-5:len(s)])
print(s[::2])
print(s[:len(s)//2])
print(s.upper()) 