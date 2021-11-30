text = input("Введите исходный текст: ")
gamma = input("Введите текст гамма-текст: ")
enc_list = []
j = 0
for i in range(0,len(text),1):
    if (j == len(gamma)):
        j = 0
    enc_list.append(gamma[j].upper())
    if(j != len(gamma)):
        j += 1
"""
for i in range(len(text)):
    text[i].replace(" ","")

print("deleting spaces:",text)
"""
sum_of_chars = []
for i in range(len(text)):
    sum_of_chars.append((ord(enc_list[i])-64) + (ord(text[i].upper())-64))

alph_ln = 37
final_text = []
for i in range(len(sum_of_chars)):
    final_text.append(sum_of_chars[i]%alph_ln)
encd_list = []
for i in range(len(final_text)):
    encd_list.append((chr(final_text[i]+64)))

output = ""
for s in encd_list:
    output += s

def decode(encd_list,enc_list):
    min_of_chars = []
    for i in range(len(encd_list)):
        min_of_chars.append(chr(((((ord(encd_list[i])-64) - (ord(enc_list[i])-64))+37)%37)+64))

    funcout = ""
    for s in min_of_chars:
        funcout += s

    print("decoded string: ",funcout)

#print(len(text))
#print(enc_list)
#print("Len list: ",len(enc_list))
#print(sum_of_chars)
#print(encd_list)
print("encoded string: ",output)
decode(encd_list,enc_list)