data = '1h 45m,360s,25m,30m 120s,2h 60s'

new_data = data.replace(',', ' ')

data_list = new_data.split()

hours = []
minutes = []
seconds = []

total_minutes = 0

for i in data_list:
    if 'h' in i:
        hours.append(int(i.replace('h', ' ')))
        for h in hours:
            total_minutes += h * 60
    elif 'm' in i:
        minutes.append(int(i.replace('m', ' ')))
        for m in minutes:
            total_minutes += m
    elif 's' in i:
        seconds.append(int(i.replace('s', ' ')))
        for s in seconds:
            total_minutes += s // 60

print('Общее время' , total_minutes, 'минут')