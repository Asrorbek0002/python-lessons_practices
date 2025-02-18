import time
data={
    'bel1':123,
    'bel2':345,
    'bel3':567,
    'bel4':789,
}

print('Please, enter your check')
while True:
    user_id=int(input("Enter a number>>>"))
    found=False
    for key,val in data.items():
        if user_id==val:
            gar_da=data.pop(key)
            print(f"we removed this {gar_da}")
            print("You may inter")
            found=True
            break

    if not found:
        print("Number not found in this dict")
        remove_item=data.pop(key)

    if len(data)==0:
        print("List empety, System shutting down in 5 minutes")
        time.sleep(5)
        break

# import time
#
# data = {
#     'bel1': 123,
#     'bel2': 345,
#     'bel3': 567,
#     'bel4': 789,
# }
#
# print("Please, enter your check")
#
# while data:  # Continue as long as there are items in the dictionary
#     try:
#         user_id = int(input("Enter a number >>> "))
#
#         # Check if the number exists in the dictionary
#         found = False
#         for key, val in list(data.items()):  # Iterate over a copy of the dictionary
#             if val == user_id:
#                 removed_item = data.pop(key)
#                 print(f"We removed this {removed_item}")
#                 print("You may enter")
#                 found = True
#                 break  # Stop searching once a match is found
#
#         if not found:
#             print("Number not found in the list.")
#             removed_item = data.popitem()
#
#         # If the dictionary becomes empty, shut down the program
#         if len(data) == 0:
#             print("List is empty. System shutting down in 5 seconds...")
#             time.sleep(5)
#             break
#     except ValueError:
#         print("Please enter a valid number.")
