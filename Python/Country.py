class Bangladesh():
    def capital(self):
        print("Capital of Bangladesh is Dhaka")
    def Language(self):
        print("Language of Bangladesh is Bangla")
class India():
    def capital(self):
        print("Capital of India is New Delhi")
    def Language(self):
        print("Language of India is Hindi")
obj_Bangladesh = Bangladesh()
obj_India = India()
for country in (obj_Bangladesh, obj_India):
    country.capital()
    country.Language()
    