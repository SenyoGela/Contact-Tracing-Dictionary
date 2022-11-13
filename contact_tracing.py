# display menu
print("")
print("********** MENU **********")
print("(1) Add an item")
print("(2) Search an item")
print("(3) Exit")
print("**************************")
print("")
# ask user to select item from the menu
# if input is 1: add an item
# if input is 2: search an item
# if input is 3: exit
import pprint
# create/add elements to the dictionary
contacts_dictionary = {"LUSI ZHAO": {"Age":"24", "Gender":"Female", "Birthday":"November 9, 1998", "Address":"Chengdu,China", "Contact Number":"2356-890-1299"},
                        "JOSHUA HONG": {"Age":"26", "Gender":"Male", "Birthday":"December 30, 1995", "Address":"Los Angeles, California", "Contact Number":"7833-121-0345"},
                        "ANNE HATHAWAY": {"Age":"40", "Gender":"Female", "Birthday":"November 12, 1982", "Address":"Brooklyn, New York", "Contact Number":"6792-010-3387"},
                        "NAOI REI": {"Age":"18", "Gender":"Female", "Birthday":"February 3, 2004", "Address":"Tokushima, Japan", "Contact Number":"0622-153-6543"},
                        "XU MINGHAO": {"Age":"25",  "Gender":"Male", "Birthday":"November 7, 1997", "Address":"Anshan,China", "Contact Number":"2000-888-0926"}}
while True:                        
	# display menu
	print("")
	print("********** MENU **********")
	print("(1) Add an item")
	print("(2) Search an item")
	print("(3) View all items")
	print("(4) Delete an item")
	print("(5) Exit")
	print("**************************")
	print("")
	# ask user to select item from the menu
	menu_option = int(input("What do you want to do (1-5)? "))
	print("")
	# if input is 1: add an item
	if menu_option == 1:
	    full_name = str(input("Enter full name: ")).upper()
	    age = int(input("Enter age: "))
	    gender = input("Enter gender: ")
	    birthday = input("Enter birthday: ")
	    address = str(input("Enter address: "))
	    contact_number = input("Enter contact number(XXXX-XXX-XXXX): ")
	    new_contacts = {full_name:{"Age":age, "Gender":gender, "Birthday":birthday, "Address":address, "Contact Number":contact_number}}
	    contacts_dictionary.update(new_contacts)
	    print("")
	    print("The person named", full_name, "has been added.")
	    pprint.pprint(new_contacts)
	    print("")
	    
	# if input is 2: search an item
	if menu_option == 2:
	    search_name = str(input("Who do you want to search (Full Name)? ")).upper()
	    if search_name in contacts_dictionary:
	        print("")
	        print("The person named", search_name, "has been found.")
	        print("Here are his/her personal information.")
	        print("")
	        print("Full name:",search_name)
	        pprint.pprint(str(contacts_dictionary[search_name]).replace("{","").replace("}","").replace("'","").replace("(","").replace(")",""))
	    else:
	        print("Person not found!")
	#if input is 3: view dictionary keys  
	if menu_option == 3:
	 	print("")
	 	print("Here are all the people in the contact list:")
	 	pprint.pprint(contacts_dictionary.keys())
	 	print("")                  
	# if input is 4:
	if menu_option == 4:
		delete_contact = str(input("Who do you want to delete (full name)? ")).upper()
		if delete_contact in contacts_dictionary:
			del contacts_dictionary[delete_contact]
			print("The person named", delete_contact, "has been deleted.")
			print("")
			print("Here are the new list of contacts")
			pprint.pprint(contacts_dictionary.keys())
			print("")
		else:
			print("Person not found!")
			print("")
	# if input is 5: exit
	if menu_option == 5:
		exit = str(input("Do you want to exit (Y/N)? ")).upper()
		if exit == "Y":
			break
