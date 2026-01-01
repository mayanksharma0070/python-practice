# A python program that reverse an array

import array as arr

# 1. We create an array of Unicode characters ('u').
#    We provide a single string 'abcd' as the input sequence.
#    The variable is correctly named 'name'.
name = arr.array('u', 'abcd')

# 2. We use slicing to reverse the 'name' array.
#    The result is stored in 'reversed_names'.
reversed_names = name[::-1]

print(f"Reversed array (new object): {reversed_names}")
# 3. We use the correct variable 'name' to print the original array.
print(f"Original array (unchanged): {name}")

rev_array=name.reverse()
print(rev_array)