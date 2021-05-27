#add file for test
def main(symbol):
    for symbol_count in range(symbol):
        for symbol_count_2 in range(symbol):
            print(symbol_count_2, end='')
    print()

input_number = int(input('Input number:'))

main(input_number)