from ChineseFont import ChineseFont

print_count = 0

def print_byte(pix_byte):
    global print_count
    for i in range(0, 8):
        if(pix_byte & (1 << (7-i)) != 0):
            print('#', end=' ')
        else:
            print('-', end=' ')
        print_count = print_count + 1
        if(print_count == 32):
            print_count = 0
            print(' ')

font = ChineseFont('font_db.data', 32, True)

print("言 is exist: %s" % font.is_exist(b'言'))

font_map = font.get_bit_map(b'言')
for pix_byte in font_map:
    print_byte(pix_byte)
