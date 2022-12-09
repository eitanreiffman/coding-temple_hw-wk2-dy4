# Question 1
# Create a program that allows a user to continue to add people
# To an address book until the user quits. Once the user quits,
# break out of the loop and print out the name and address of everyone in the address book:


def create_address_book():
    address_book = {}
    x = ""
    while x != 'no':
        name = input("Enter a name: ")
        address = input("Enter an address: ")
        address_book[name] = address
        x = input("Do you want to continue? Enter yes or no: ")
    
    print("\nHere is your completed address book:\n")
    for name, address in address_book.items():
        print(f"\t{name} lives on {address}")

create_address_book()


# Question 2
#Best Time to Meet
#Billy is trying to figure out if there is a time that he and his team can meet to work on the project.
#His three teammates each give him a list of times they are available ('HH:MM' 24-hour).
# Create a function that will take in an original list plus any number of lists of
# teammate's available times (*remember *args*) and return a list of times where everyone can meet.


person1 = ['09:00', '10:30', '11:30', '12:00', '13:00', '14:30']
person2 = ['09:30', '10:00', '10:30', '12:00', '14:30', '16:00']
person3 = ['09:00', '09:30', '11:00', '11:30', '12:00', '13:30', '14:30', '15:00']
person4 = ['11:00', '11:30', '12:00', '14:00', '14:30', '16:30', '17:00']
person5 = ['9:00', '12:00', '14:30', '16:30']
person6 = ['9:30', '14:30', '16:00']


def common_times(orig_list, *args):
    set1 = set(orig_list)
    for person in args:
        set1 &= set(person)
    return set1

print(common_times(person1, person2, person3, person4, person5, person6))