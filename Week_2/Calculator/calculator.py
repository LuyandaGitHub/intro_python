number_1 = input('Enter a number: ');
number_2 = input('Enter another number: ');

# when we get an input from a user...the default data type of the input is a string, so we have to change the data type to a float so we support decimal numbers. If we wanna add the two numbers instead of concatinating them.
result = float(number_1) + float(number_2);

print(result);
