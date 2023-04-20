word_txt = ['разработка', 'администрирование', 'protocol', 'standard']
index = 0
while index < len(word_txt):
    try:
        ENC_STR_BYTES = str.encode(word_txt[index], encoding='utf-8', errors='backslashreplace')
        BYTES_DEC = bytes.decode(ENC_STR_BYTES, encoding='utf-8')

        print(f'encode: {ENC_STR_BYTES} - decode: {BYTES_DEC}')
    except Exception as e:
        print(f'Слово : {e.args[1]} - невозможно записать в байтовом типе в кодировке ASCII')
    finally:
        index += 1
