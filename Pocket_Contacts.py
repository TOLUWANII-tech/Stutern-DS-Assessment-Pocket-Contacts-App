contact_list = []


def add_contact():
    # This function asks the user for the name and phone number of the contact and returns both string values
    '''
    Adds a new contact to the contact list at the request of the user.
    '''
    def contact_details():
        '''
        Asks a user for the name and phone number of a new contact and returns the respective strings.

        Args:
        None

        Returns:
        name: (str) the name of the contact to be added.
        number: (str) 11-digit phone number of the contact.
        '''
        name = input("What's the name of the contact you're adding?\n")
        number = input("What's the contact's (11-digit) mobile number\n")
        return name, number

    def update_contact_list(name, number, list_of_contacts):
        '''
        Appends the deatils of the contact (name and phone number) to the contact list.

        Args:
        name: (positional, string) The name of the person whose contact is to be added.
        number: (positional, string) 11-digit number of the contact represented as a string.
        lisr_of_contacts: (positional, iterable) list containing dictionaries of each contact name mapped to a number.

        Returns:
        None
        '''
        contact_dict = {}
        contact_dict[name] = number
        list_of_contacts.append(contact_dict)
        return None

    name, number = contact_details()
    right_length = len(number) == 11

    if name and right_length:
        update_contact_list(name, number, contact_list)
    else:
        while not (name and right_length):
            print('Make sure you have entered a valid name and phone number\n')
            name, number = contact_details()
            right_length = len(number) == 11
        update_contact_list(name, number, contact_list)


def show_contacts(list_of_contacts):
    '''
    Displays each contact name and phone number.

    Args:
    None

    Returns:
    None
    '''
    for dictionary in list_of_contacts:
        for key in dictionary:
            print(
                f"Contact Name: {key}\nPhone number: {dictionary[key]}", end='\n')


new_contact = True

while new_contact:
    # Asks the user if he/she wants to add a new contact.
    ask_user = input(
        "Do you want to add a contact? 'yes' or 'no' \n").lower()
    if ask_user == 'no':
        print('Okay, so far you have the following contacts: ')
        show_contacts(contact_list)
        break
    else:
        add_contact()
