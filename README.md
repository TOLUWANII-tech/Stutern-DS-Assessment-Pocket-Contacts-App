# Stutern-DS-Assessment-Pocket-Contacts-App
This is a python Script to store and view contact names and phone numbers, like a mini digital diary.

The script first prompts the user, asking whether he/she wants to add a contact to the list. If the user replies 'yes,' it prompts the user for the name of the contact and the contact's phone number. It validates the name and phone number, ensuring that the name is not left empty and the number is an 11-digit number. If either of these conditions are not met it re-prompts the user for a proper input for the name and phone number. After validating the user's response, a dictionary with the name and number as key and value respectively is appended to the contact list.

The process above is repeated in a loop, until the user has added all the contacts he/she wishes to. At this point, the user replies 'no' when prompted for a new contact. The code then displays the current list of the names and phone numbers present within each dictionary in the contact list. After this, the script ends.
