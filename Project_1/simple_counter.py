# Simple counter that counts from 0 - 255 then resets back to 0
# Prints each line in binary and decimal

count = 0

for count in range (256):
    Binary_representation = format(count, '08b')
    print((Binary_representation) + " " + str(count))
    count = 0
