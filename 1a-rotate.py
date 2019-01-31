from datetime import datetime
d = input('Enter a date(dd/mm/yyy) : ')
d = datetime.strptime(d, "%d/%m/%Y")
print(d.strftime("%B %d, %Y"))
year=d.strftime("%Y")
day=d.strftime("%d")
print(day)
month=d.strftime("%B")
if(day==1|21|31):
    print(month+" "+day+"st"+" ,"+year)
elif(day==4|5|6|7|8|9|10|11|12|13|14|15|16|17|18|19|20|24|25|26|27|28|29|30):
    print(month+" "+day+"th"+" ,"+year)
else:
    print(month+" "+day+"rd"+" ,"+year)
