months   =  [
         "January",
         "February",
         "March",
         "April",
         "May",
         "June",
         "July",
         "August",
         "September",
         "October",
         "November",
         "December"
       ]
while True:
         date=input("date:")
         try:
            month,day,year=date.split("/")
            month=month.replace('"','')
            year=year.replace('"','')
            if (int(month)>=1 and int(month)<=12) and (int(day)>=1  and int(day)<=31):
               break
         except:
            try:
               old_month, old_day,year=  date.split(" ")
               for i in range(len(months)):
                  if old_month == months[i]:
                     month = i+1
                     break
               day= old_day.replace(",","")
               if (int(month)>=1 and int(month)<=12) and (int(day)>=1 and int(day)<=31):
                  break
            except:
                  pass


print(f"{int(year)}-{int(month):02}-{int(day):02}")

