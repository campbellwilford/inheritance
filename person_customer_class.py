class Person:
    def __init__(self,name,address,number):
        self.__name = name
        self.__address = address
        self.__number = number 

    def get_name(self):
        return self.__name
    
    def get_address(self):
        return self.__address
    
    def get_number(self):
        return self.__number
    
    def print_person(self):
        print('METHOD 1')
        print('Name:',Person.get_name(self))
        print('Addr:',Person.get_address(self))
        print('Phone:',Person.get_number(self))

        print()
        print()


#method 2


