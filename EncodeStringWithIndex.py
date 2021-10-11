
def decode_string(string):
    encoded_string=""
    for i in range(0,len(string),2):
        encoded_string += (string[i] * int(string[i+1]))
    
    return encoded_string

print("Enter the index")
input_index=int(input())

try:
    print(decode_string('a4b2c1d1e1f3')[input_index])
except IndexError:
    print("*")
except Exception as exception:
    # Output unexpected Exceptions.
    print(exception)
