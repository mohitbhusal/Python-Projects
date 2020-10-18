import calendar
cal = calendar.HTMLCalendar(calendar.SUNDAY)
cal2 = calendar.TextCalendar(calendar.SUNDAY)
yo = cal2.formatmonth(2020, 9)
#print(yo)
mnth = [0,'january', 'february', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
for m in range(1, 13):
    k = calendar.monthcalendar(2020, m)
    wk1 = k[0]
    wk2 = k[1]
    if wk1[calendar.SATURDAY] != 0:
        meeting = wk1[calendar.SATURDAY]
    else:
        meeting = wk2[calendar.SATURDAY]
    print(mnth[m], meeting)
















