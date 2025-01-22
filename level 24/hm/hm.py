Create a 10-element List and number it as a comment (write indexes).
my_list =  
'Apple',  # 0
'Banana', # 1
'Cherry', # 2
'Date',   # 3
'Elderberry', # 4
'Fig',    # 5
'Grape',  # 6
'Honeydew', # 7
'Ivy',    # 8
'Jackfruit' # 9]'Apple',  # 0




ეკრანზე გამოყვანა
print("Full list:", my_list)

გამოიტანეთ პირველი სამი, ბოლო სამი და შუა 4 დადებითი ინდექსებით
first_three_positive = my_list[:3]
last_three_positive = my_list[-3:]
middle_four_positive = my_list[3:7]

print("First three (positive indices):", first_three_positive)
print("Last three (positive indices):", last_three_positive)
print("Middle four (positive indices):", middle_four_positive)

გამოიტანეთ პირველი სამი, ბოლო სამი და შუა 4 უარყოფითი ინდექსებით
first_three_negative = my_list[-10:-7]  # Negative indices for first three
last_three_negative = my_list[-3:]  # Negative indices for last three
middle_four_negative = my_list[-7:-3]  # Negative indices for middle four

print("First three (negative indices):", first_three_negative)
print("Last three (negative indices):", last_three_negative)
print("Middle four (negative indices):", middle_four_negative)