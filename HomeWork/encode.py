alphabet = {
    'a': 0, 'b': 1, 'c': 2,
    'd': 3, 'e': 4, 'f': 5,
    'g': 6, 'h': 7, 'i': 8,
    'j': 9, 'k': 10, 'l': 11,
    'm': 12, 'n': 13, 'o': 14,
    'p': 15, 'q': 16, 'r': 17,
    's': 18, 't': 19, 'u': 20,
    'v': 21, 'w': 22, 'x': 23,
    'y': 24, 'z': 25
}


def encode(message, key):
    encode_list = []
    alphabet_index = list(alphabet.keys())
    for i in message:
        try:
            char_index = alphabet[i]
            encode_char = (char_index+key) % 26
            encode_list.append(alphabet_index[encode_char])
        except KeyError:
            encode_list.append(i)
    return ''.join(encode_list)


def decode(encoded_message, key):
    decode_list = []
    alphabet_index = list(alphabet.keys())
    for e in encoded_message:
        try:
            char_index = alphabet[e]
            decoded_char = (char_index-key) % 26
            decode_list.append(alphabet_index[decoded_char])
        except KeyError:
            decode_list.append(e)
    return ''.join(decode_list)


if __name__ == "__main__":
    encode_message = encode('hello world!', 2)
    print(f'encode message is : {encode_message}')
    decode_message = decode(encode_message, 2)
    print(f'decode message is : {decode_message}')
