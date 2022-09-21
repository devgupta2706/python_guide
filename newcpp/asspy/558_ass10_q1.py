import datetime
year=lambda a: a.year
date=lambda a: a.date()
time=lambda a: a.time()
month=lambda a: a.month

desh_kaal=datetime.datetime.now()
print(desh_kaal)
print("Date:",date(desh_kaal))
print("Month:",month(desh_kaal))
print("Year:",year(desh_kaal))
print("Time:",time(desh_kaal))