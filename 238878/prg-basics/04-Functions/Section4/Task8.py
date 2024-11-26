def  time_string(hours, minutes, format = '24'):
    if format == '24':
        time = str(hours) + ":" + str(minutes)
        return time
    if format == '12':
        if hours > 12:
            hours -= 12
            time = str(hours) + ":" + str(minutes) + ' pm'
            return time
        elif hours <= 12:
            time = str(hours) + ":" + str(minutes) + ' am'
            return time

print(time_string(int(input('Hours: ')), int(input('Minutes: ')), input('Format: ')))