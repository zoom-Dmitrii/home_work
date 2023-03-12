time_sec = int(input('Введите время в секундах: '))
hours = time_sec // 3600
if hours < 10:
    hours_txt = '0' + str(hours)
else: hours_txt = str(hours)   
time_sec = time_sec - hours * 3600
minutes = time_sec // 60
if minutes < 10:
    minutes_txt = '0' + str(minutes)
else: minutes_txt = str(minutes)
seconds = time_sec - minutes * 60
if seconds < 10:
    seconds_xt = '0' + str(seconds)
else: seconds_xt = str(seconds) 
print(f"Время в формате ч:м:с - {hours_txt}:{minutes_txt}:{seconds_xt}")