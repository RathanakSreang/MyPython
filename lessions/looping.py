words = ['rathanak', 'kimly', 'apha', 'akoch']
for w in words:
    print(w, len(w))

for w in words[:]:
    print(w)
    if len(w) > 5:
        words.insert(0, w)
print(words)

for i in range(5):
    print(i)

def fib(n):
    a, b = 0, 1
    while a < n:
        print(a,end='')
        a, b = b, a+b
    print()
fib(2000)
