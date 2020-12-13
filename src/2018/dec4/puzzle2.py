input = open("input1", "r")
lines = input.readlines()
lines.sort()

import re


# [1518-11-01 00:00] Guard #10 begins shift
# [1518-11-01 00:05] falls asleep
# [1518-11-01 00:25] wakes up
guard = 0
asleep = 0
guards = {}
guard_sleep = {}
for i in range(0, 60):
    guard_sleep[i] = 0
for line in lines:
    line = line.rstrip()
    match = re.match("\[1518-..-.. ..:([0-9][0-9])\] (.+)", line)
    # print(match.groups())
    minute = int(match.groups()[0])
    text = match.groups()[1]
    if text == "falls asleep":
        asleep = minute
    elif text == "wakes up":
        for m in range(asleep, minute):
            guards[guard][m] += 1
    else:
        match2 = re.match("Guard #([0-9]+) begins shift", text)
        guard = int(match2.groups()[0])
        if guard not in guards:
            guards[guard] = guard_sleep.copy()

print(guards)


max_times = max([max([times for (minute, times) in guard_sleep.items()]) for (guard, guard_sleep) in guards.items()])
print(max_times)
max_guard = [[guard for (minute, times) in guard_sleep.items() if times == max_times] for (guard, guard_sleep) in guards.items()]
max_guard = [item for sublist in max_guard for item in sublist][0]
print(max_guard)
max_minute = [[minute for (minute, times) in guard_sleep.items() if times == max_times] for (guard, guard_sleep) in guards.items()]
max_minute = [item for sublist in max_minute for item in sublist][0]
print(max_minute)

print(max_guard * max_minute)
