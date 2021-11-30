alphabet=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z",",",".","-"," "]
indexes=["11","12","12","14","15","16","21","22","23","24","25","26","31","32","33","34","35","36","41","42","43","44","45","46","51","52","53","54","55","56"]
input_text = input()
res = []
check_text = input_text.upper()
for i in range(len(check_text)):
    for j in range(len(alphabet)):
        if(check_text[i] == alphabet[j]):
            res.append(j)

for i in range(len(res)):
    print(indexes[res[i]],end="")
print()