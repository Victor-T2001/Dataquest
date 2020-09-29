## 1. The ASCII Encoding ##

data = "QUEST"
for character in data:
    print(bin(ord(character)))

## 2. ASCII Limitations ##

text = "The Swedish word for quest is sökande"
encoded = text.encode(encoding='ascii', errors='replace')
print(encoded)
print(type(encoded))

## 3. Bytes ##

bytes1 = bytes.fromhex('02')
print(bytes1)
bytes2 = bytes.fromhex('5a')
print(bytes2)
bytes3 = bytes.fromhex('ff')
print(bytes3)

## 4. Printable Characters ##

# provided inputs
string_1 = 'lowercase'
string_2 = 'UPPERCASE'

def check_uppercase(string):
    answer = True
    for c in string:
        # print(ord(c))
        if 65 > ord(c) or ord(c) > 90:
            answer = False
    return answer

print(check_uppercase(string_1))
print(check_uppercase(string_2))



## 5. Multi-byte encodings ##

trad_chinese = "你好嗎?"
encoded = trad_chinese.encode(encoding = 'BIG5')
print(len(encoded))


## 7. Unicode ##

sentence = "ASCII cannot represent these: 你好嗎"
encoded_utf8 = sentence.encode(encoding = 'utf-8')
print(encoded_utf8)
encoded_ascii = sentence.encode(encoding = 'ascii', errors='replace')
print(encoded_ascii)

## 8. Decoding Bytes ##

# variable named encoded is accessible
import chardet
decoded_cp1252 = encoded.decode(encoding="cp1252")
print(decoded_cp1252)
encoding = chardet.detect(encoded)['encoding']
decoded = encoded.decode(encoding=encoding) 