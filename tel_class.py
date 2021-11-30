class account:
    def __init__(self,first_name,last_name,patronymic,post_index,country,area,city,street,building_numb,flat_numb,tel_numb):
        self.first_name = first_name
        self.last_name = last_name
        self.patronymic = patronymic
        self.post_index = post_index
        self.country = country
        self.area = area
        self.city = city
        self.street = street
        self.building_numb = building_numb
        self.flat_numb = flat_numb
        self.tel_numb = tel_numb

    def get_pass(self):
        return self.password
    def get_login(self):
        return self.login
    def get_email(self):
        return self.email
    def get_tel_numb(self):
        return self.tel_numb
    def get_full_info(self):
        return self.first_name,self.last_name,self.patronymic,self.post_index,self.country,self.area,self.city,self.street,self.building_numb,self.flat_numb,self.tel_numb
