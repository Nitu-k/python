#epoch()- dta eand time from which a comp measures system time
import time
# print(time.ctime(100000))#convert a time expressed in seconds since epoch to a readable string
# print(time.time())#return current seconds since epoch

# time_object=time.localtime()
# time_object=time.gmtime()
# print(time_object)
# local_time=time.strftime("%B %d %Y %H:%M:%S", time_object)
# print(local_time)

#strp time function
# time_string="20 April, 2025" 
# time_object=time.strptime(time_string,"%D %B,%Y")
# print(time_object)

#tuple time asctime()
time_tuple=(2025,4,20,4,20,4,20,0,0,0,0)
time_string=time.mktime(time_tuple)
print(time_string)



