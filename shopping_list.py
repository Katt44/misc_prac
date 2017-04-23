#shopping_list




#make a list to hold items
# print out instructions how to use app
#ask for new items
#add new items to our list
#be able to quit the app
#print out list


shopping_list = []
print("What should we buy at the store?")
print("Enter 'DONE' to stop adding items")


while True:
	new_item = raw_input("> ")
	if new_item == 'DONE':
		break
	shopping_list.append(new_item)




print ("Here's your list:")
for item in shopping_list:
	print (item)