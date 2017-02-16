permissions = 'rw'
print('w' in permissions)
print('x' in permissions)
database = [
        ['A koch', '1234'],
        ['Kim', '2134'],
        ['Apha', '3455'],
        ['Phong', '1234567']
]
user_name = input("User name: ")
pin = input('PIN code: ')
if [user_name, pin] in database: print("You are in")
