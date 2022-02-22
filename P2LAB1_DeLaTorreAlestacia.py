user_int = int(input('Enter integer (32 - 126):\n'))

float_input = float(input('Enter float:\n'))

char_input = input('Enter character:\n')

string_input = str(input('Enter string:\n'))

print(user_int, float_input, char_input, string_input)
print(string_input, char_input, float_input, user_int )

char_value = chr(user_int)

print(str(user_int) + ' converted to a character is ' + str(char_value))
# FIXME (2): Output the four values in reverse
   
# FIXME (3): Convert the integer to a characer, and output that character