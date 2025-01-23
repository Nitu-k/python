#like list comp.. but dictionary 
# create dictionaries using an expression
# #replace for loop and certian lambda function
# dict={key: expression for (key,value) in iterable}

cities_in_F={'New York':32,'Boston':75,'Los Angles':100}
cities_in_C={key:round((value -32)*(5/9)) for (key,value) in cities_in_F.items()}
print(cities_in_C)
#-------------------------------------------------------------------------
#dict with dict comp..
weather={'New York':"snowing",'Boston':"sunny",'Los Angeles':"sunny",'Chicago':"cloudy"}
sunny_weather={key:value for (key,value) in weather.items() if value=="sunny"}
print(sunny_weather)



