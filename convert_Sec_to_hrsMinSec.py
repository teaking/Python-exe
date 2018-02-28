str_seconds=input("enter the number of seconds to convert")
total_secs=int(str_seconds)

#converting seconds to hrs min and secs
hrs=total_secs//3600
remaining_sec=total_secs%3600
min=remaining_sec//60
sec=remaining_sec%60

print("hrs=%s min=%s sec=%s" % (hrs,min,sec))
