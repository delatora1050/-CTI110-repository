current_price = int(input())
last_months_price = int(input())

change_price = current_price - last_months_price

monthly_mortgage = (current_price * 0.051) / 12

print('This house is',f'${current_price}.','The change is',f'${change_price}','since last month.')
print('The estimated monthly mortgage is', f'${monthly_mortgage:.2f}.')
   