"""
Copyright (c) 2019  Luis Michaelis, Philip Laskowicz
Licensed under MIT (https://opensource.org/licenses/mit-license.php).
"""

inp = [ord(i) for i in input('Decrypt > ')]
offset = int(input('Offset > '))

out = ''.join([chr((i - offset) % 128) for i in inp])
print(out)
