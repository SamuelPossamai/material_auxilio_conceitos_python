

i = 0
while i < 3:
    print('while', i)
    i += 1

print('#--------#')

for i in range(3):
    print('for', i)
    i = 100 # não afeta

print('#--------#')

for i in range(0, 10, 4):
    print('for2', i)

print('#--------#')

for i in [5, 9, 1]:
    print('for3', i)
