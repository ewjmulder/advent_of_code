from src.util import *

test = False

card_pub_key = 5764801
door_pub_key = 17807724

if not test:
    card_pub_key = 9232416
    door_pub_key = 14144084

subject_nr = 7
found = False
card_loop_size = 1
result = 1
while not found:
    result *= subject_nr
    result = result % 20201227
    if result == card_pub_key:
        break
    card_loop_size += 1

print(card_loop_size)

found = False
door_loop_size = 1
result = 1
while not found:
    result *= subject_nr
    result = result % 20201227
    if result == door_pub_key:
        break
    door_loop_size += 1

print(door_loop_size)

subject_nr = card_pub_key
result = 1
for i in range(0, door_loop_size):
    result *= subject_nr
    result = result % 20201227

print(result)
