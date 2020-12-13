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

guards_mins = {guard: sum([s for (m, s) in sleep.items()]) for (guard, sleep) in guards.items()}

print(guards_mins)

max_mins = max([mins for (guard, mins) in guards_mins.items()])
print(max_mins)
guard_most_min = [guard for (guard, mins) in guards_mins.items() if mins == max_mins][0]
print(guard_most_min)
guard_sleep_max = guards[guard_most_min]
print(guard_sleep_max)

max_times = max([times for (minute, times) in guard_sleep_max.items()])
print(max_times)
min_most_times = [minute for (minute, times) in guard_sleep_max.items() if times == max_times][0]
print(min_most_times)

print(guard_most_min * min_most_times)
