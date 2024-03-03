def letter_to_num(letter: str):
    if 'a' <= letter <= 'z':
        return ord(letter) - ord('a')
    elif 'A' <= letter <= 'Z':
        return ord(letter) - ord('A')
    else:
        return -1

def num_to_letter(num: int):
    if 0 <= num <= 25:
        return chr(num + ord('a'))
    else:
        return ''

def shift(num: int, amount: int, direction: bool):
    if direction:
        return (num + amount) % 26
    else:
        return (num - amount + 26) % 26
    
def encrypt(plaintext: str, key: int):
    cipher = list(plaintext)
    for i in range(len(cipher)):
        letter = plaintext[i]
        case = False
        if letter.isupper():
            case = True
        letter = letter_to_num(letter)
        if letter != -1:
            if case:
                letter = num_to_letter(shift(letter, key, True)).upper()
            else:
                letter = num_to_letter(shift(letter, key, True))
            cipher[i] = letter
    return ''.join(cipher)


key = int(input("Enter key: "))
message = str(input("Enter message: "))

print("Result: " + encrypt(message, key))