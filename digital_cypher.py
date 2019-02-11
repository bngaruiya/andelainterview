def code_to_message(code, key):
    dict = "abcdefghijklmnopqrstuvwxyz"
    message = ""
    key_str = str(key)
    key_str_index = 0
    for i in code:
        message += dict[i - int(key_str[key_str_index]) - 1]
        key_str_index += 1
        if key_str_index >= len(key_str):
            key_str_index = 0
    return message


print(code_to_message([14, 10, 22, 29, 6, 27, 19, 18, 6, 12, 8], 1939))
