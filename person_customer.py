import person_customer_class as p

def main():
    name = "John"
    address = '1234 Main St'
    number = '123-456-7890'
    cust_number = 1234
    on_list_flag = False

    person1 = p.Person(name,address,number)

    customer1 = p.Customer(name,address,number,cust_number,on_list_flag)

    person1.print_person()

    print()
    print()
    print()

    customer1.print_person()

main()
