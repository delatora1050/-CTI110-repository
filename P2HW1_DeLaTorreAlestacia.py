user_input1 = float(input('Enter the price of item #1: '))
user_input2 = float(input('Enter the price of item #2: '))
user_input3 = float(input('Enter the price of item #3: '))
user_input4 = float(input('Enter the price of item #4: '))
user_input5 = float(input('Enter the price of item #5: '))

sub_total = user_input1 + user_input2 + user_input3 + user_input4 + user_input5

sales_tax = sub_total * 0.07

total_price = sub_total + sales_tax

print('-------Results-------')
print('Subtotal: ', f'{sub_total:.2f}')
print('Sales Tax: ', f'{sales_tax:.2f}')
print('Total: ', f'{total_price:.2f}')
