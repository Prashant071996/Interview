from datetime import date,time,datetime,tzinfo,timedelta,timezone
#
# #datetime
#
# print(datetime.today())
#
# d = date.today()
# print(d)
#
# a = datetime.now()
# print(a)
#
# print(datetime.utcnow())
#
# #date
# print(date.today())
#
# print(date(2022,2,24))
#
# print(date.fromtimestamp(1236777333))
#
# #Diffn in Date
#
# t1=date(1996,6,7)
# t2=date(2022,5,15)
# print(t2-t1)
#
# #strftime and strptime
#
# #strftime
# now=datetime.now()
# s1=now.strftime('%d-%m-%y')
# print(s1)
# print(type(s1))
#
# #strptime
# P_now='15-06-2022'
# s2=datetime.strptime(P_now,'%d-%m-%Y')
# print(s2)
# print(type(s2))


# a= datetime.today()
# b=a.strftime('%d-%m-%Y')
# print(b)

# a='15-05-2022'
# b=datetime.strptime(a,'%d-%m-%Y')
# print(b)
