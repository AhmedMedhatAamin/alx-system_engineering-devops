def decode(message_file):
    with open(message_file, 'r') as file:
        lines = file.readlines()

    # Mapping of numbers to words
    num_to_word = {}
    for line in lines:
        parts = line.strip().split()
        if len(parts) >= 2:
            num_to_word[int(parts[0])] = parts[1]

    # Find the maximum number to know the size of the pyramid
    max_num = max(num_to_word.keys())

    # Decode the message
    decoded_message = []
    current_line = 1
    while max_num > 0:
        for i in range(current_line, 0, -1):
            if i in num_to_word:
                decoded_message.append(num_to_word[i])
                break
        max_num -= current_line
        current_line += 1

    return ' '.join(decoded_message[::-1])

print(decode("my.txt"))

