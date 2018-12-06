from datetime import datetime, timedelta 
from collections import Counter

with open('04.txt', 'r') as file:
    lines = [(datetime.strptime(line[line.index('[')+1:line.index(']')], "%Y-%m-%d %H:%M"),  line[line.index(']')+2:]) for line in file.readlines()]
    lines.sort(key=lambda tup: tup[0])
    sleep_by_guard = Counter()
    minutes_by_guard = {}
    for date, line in lines:
        if 'asleep' in line:
            date_asleep = date
        elif 'wakes up' in line:
            date_awake = date
            minutes = (date_awake-date_asleep).seconds // 60
            sleep_by_guard[guard_id] += minutes
            if not guard_id in minutes_by_guard:
                minutes_by_guard[guard_id] = Counter()
            minutes_by_guard[guard_id].update([(date_asleep + timedelta(minutes=minute)).minute for minute in range(0, minutes)])
        elif 'begins' in line:
            guard_id = line[line.index('#')+1:line.index('begins')-1]
    most_asleep_guard = sleep_by_guard.most_common(1)[0][0]
    print(most_asleep_guard)
    print(minutes_by_guard[most_asleep_guard])
    same_minute_guard = max(minutes_by_guard.keys(), key=lambda k: minutes_by_guard[k].most_common(1)[0][1])
    print(int(same_minute_guard) * minutes_by_guard[same_minute_guard].most_common(1)[0][0])

    
    
    
