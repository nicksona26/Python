sec = int(input("Enter number of seconds "))
years = int(sec / 31536000)
remsec1 = sec % 31536000
days = int(remsec1 / 86400)
remsec2 = remsec1 % 86400
hours = int(remsec2 / 3600)
remsec3 = remsec2 % 3600
minutes = int(remsec3 / 60)
seconds = int(remsec3 % 60)

print("In {0:} seconds there are:\n{1:} years\n{2:} days\n{3:.1f} hours\n{4:.1f} minutes\n{5:.1f} seconds".format(sec, years, days, hours, minutes, seconds))
