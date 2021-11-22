# Variant 1
print('# Variant 1')
print('Openning data.txt for reading...')
f = open('data.txt')

try:
    print('Reading data.txt...')
    for line in f:
        print(line, end='')
        1 / 0
    print('')
except:
    print('Something went wrong...')
finally:
    f.close()

print('Done')

# Variant 2
print('# Variant 2')
print('Openning data.txt for reading...\n')
try:
    with open('data.txt') as f:
        print('Reading data.txt...')
        for line in f:
            print(line, end='')
            1 / 0
        print('')
except:
    print('Something went wrong...')

print('Done')
