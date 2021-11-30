initial_text = input("Enter text you want to encrypt:")
print("your initial text is: ",initial_text," and it's length is :",len(initial_text))
key = int(input("Enter key of shift:"))
print("your shift key is: ",key)
result = ""
for i in range(len(initial_text)):
    if ((ord(initial_text[i]) + key) >= 90):
        result += chr(ord(initial_text[i])+key -25)
        '''print(initial_text[i])
        print(result)'''
    elif ((ord(initial_text[i])) == 32):
        result += chr((ord(initial_text[i]) + 33 + key))
    else:
        result += chr(ord(initial_text[i]) + key)

print("Encrypted text: ",result)
print("it's length is :",len(result))