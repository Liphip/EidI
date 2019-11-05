"""
Copyright (c) 2019  Luis Michaelis, Philip Laskowicz
Licensed under MIT (https://opensource.org/licenses/mit-license.php).
"""

inp = input('Encrypt > ')
offset = int(input('Offset > '))

out = ''.join([chr((ord(i) + offset) % 128) for i in inp])
print(out)
