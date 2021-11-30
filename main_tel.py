from tel_class import *
tel_owner_info = []
n = int(input("Enter how much addresses you want to add:"))
for i in range(n):
    first_name = input("Fist name:")
    last_name = input("Last name:")
    patronymic = input("Patronymic:")
    post_index = input("Post index:")
    country = input("Country:")
    area = input("Area:")
    city = input("City:")
    street = input("Street:")
    building_number = input("Building number:")
    flat_number = input("Flat number:")
    tel_number = input("Tel number:")

    tel_owner_info.append(account(first_name,last_name,patronymic,post_index,country,area,city,street,building_number,flat_number,tel_number))

for i in range(len(tel_owner_info)):
    temp_tel = ""
    temp_tel = tel_owner_info[i].get_tel_numb()
    check_tel = "720"
    # print(temp_tel)
    if (temp_tel[0] == '7' and temp_tel[1] == '2' and temp_tel[2] == '0'):
        # print('works')
        print(tel_owner_info[i].get_full_info())
