def validUTF8(data):
    # Initialize a variable to count the number of continuation bytes expected
    continuation_bytes = 0
    
    # Iterate through the list of integers
    for num in data:
        # Check if the byte is a continuation byte
        if continuation_bytes > 0:
            # If it's a continuation byte, check if it starts with '10'
            if num >> 6 != 0b10:
                return False
            continuation_bytes -= 1
        else:
            # Determine the number of bytes in the UTF-8 character sequence
            if num >> 7 == 0:
                # 1-byte character
                continue
            elif num >> 5 == 0b110:
                # 2-byte character
                continuation_bytes = 1
            elif num >> 4 == 0b1110:
                # 3-byte character
                continuation_bytes = 2
            elif num >> 3 == 0b11110:
                # 4-byte character
                continuation_bytes = 3
            else:
                # Invalid start of a character sequence
                return False
    
    # If there are still continuation bytes left at the end, return False
    return continuation_bytes == 0
