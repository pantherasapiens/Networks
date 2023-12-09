def add_hamming_code(data):
    # Calculate the number of parity bits needed
    m = len(data)
    r = 1
    while 2 ** r <= m + r:
        r += 1

    # Create a list to store the data and parity bits
    hamming_data = [0] * (m + r)

    # Fill in the data bits
    for i in range(m):
        hamming_data[2 ** i - 1] = int(data[i])

    # Fill in the parity bits
    for i in range(r):
        parity_index = 2 ** i - 1
        for j in range(1, m + r + 1):
            if (j & (1 << i)) != 0 and j != parity_index + 1:
                hamming_data[parity_index] ^= hamming_data[j - 1]

    # Return the original data with added parity bits
    return ''.join(map(str, hamming_data))

def correct_hamming_code(data):
    # Calculate the number of parity bits needed
    r = 1
    while 2 ** r <= len(data):
        r += 1

    # Create a list to store the data and parity bits
    hamming_data = list(map(int, data))

    # Check for errors and correct if possible
    error_position = 0
    for i in range(r):
        parity_index = 2 ** i - 1
        calculated_parity = 0
        for j in range(1, len(hamming_data) + 1):
            if (j & (1 << i)) != 0 and j != parity_index + 1:
                calculated_parity ^= hamming_data[j - 1]

        if calculated_parity != hamming_data[parity_index]:
            error_position += parity_index + 1

    # Correct the error if found
    if error_position != 0:
        print(f"Error detected at position {error_position}. Correcting...")
        hamming_data[error_position - 1] ^= 1

    # Return the corrected data
    return ''.join(map(str, hamming_data))

# Example
original_data = "1101"
data_with_hamming = add_hamming_code(original_data)
print(f"Original Data: {original_data}")
print(f"Data with Hamming Code: {data_with_hamming}")

# Simulate an error by flipping one bit
error_data = list(data_with_hamming)
error_data[3] = '0' if error_data[3] == '1' else '1'
error_data = ''.join(error_data)

# Correct errors using Hamming Code
corrected_data = correct_hamming_code(error_data)
print(f"Corrected Data: {corrected_data}")
