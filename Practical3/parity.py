def add_parity_bit(data):
    # Count the number of ones in the data
    ones_count = data.count('1')

    # Append a parity bit (even parity)
    parity_bit = '1' if ones_count % 2 != 0 else '0'

    # Return the original data with the added parity bit
    return data + parity_bit

def check_parity(data):
    # Count the number of ones in the data
    ones_count = data.count('1')

    # Check parity (even parity)
    return ones_count % 2 == 0

# Example
original_data = "1100101"
data_with_parity = add_parity_bit(original_data)
print(f"Original Data: {original_data}")
print(f"Data with Parity: {data_with_parity}")

# Simulate an error by flipping one bit
error_data = list(data_with_parity)
error_data[3] = '0' if error_data[3] == '1' else '1'
error_data = ''.join(error_data)

# Check parity to detect errors
if check_parity(error_data):
    print("No error detected.")
else:
    print("Error detected.")
