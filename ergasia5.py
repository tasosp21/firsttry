date=raw_input("Δώσε την ημερομηνία dd/mm/yyyy:")
date=date.split("/")
day=int(date[0])
month=int(date[1])
year=int(date[2])
   

if (month==4 or month==6):
  codemonth=0
elif (month==1 or month==10):
  codemonth=1
elif (month==5):
  codemonth=2
elif (month==8):
  codemonth=3
elif (month==2 or month==3 or month==11):
  codemonth=4
elif (month==6):
  codemonth=5
elif (month==9 or month==12):
  codemonth=6


century=year/100
if (century==19 or century==23):
  codecentury=0
elif (century==18 or century==22):
  codecentury=2
elif (century==17 or centery==21):
  codecentury=4
elif (century==16 or century==20):
  codecentury=6  
  

if (year==2012):
  codeyear=0
elif  (year==2013):
  codeyear=1
elif (year==2008):
  codeyear=2
elif (year==2009):
  codeyear=3
elif (year==2010):
  codeyear=4
elif (year==2011):
  codeyear=5
else   codeyear=(codecentury+(year%100)+(year%100)%4)/7


codeday=(codeyear+codemonth+day)/7



if ((year/4==0 or year/100!=0) or year/400==0):
  codeday=codeday-1


if (codeday==0):
  print "Σάββατο"
if (codeday==1):
  print "Κυριακή"
if (codeday==2):
  print "Δευτέρα"
if (codeday==3):
  print "Τρίτη"
if (codeday==4):
  print "Τετάρτη"
if (codeday==5):
  print "Πέμπτη"
if (codeday==6):
  print "Παρασκευή"




