# RTC_Data_Retrieval

## Description

The purpose of this module is to set, retrieve and format data of a GPS sensor using a Pyboard. It was created to name the data logging files and thus the primary function returns a formatted string. The data sheet used to parse the datafeed is:

https://datasheets.maximintegrated.com/en/ds/DS3231.pdf

## Functions

`get_timestring(bus)` - This is the primary function which calls all other functions and returns a formatted string. The returned value is `"<year><month><date><hours><minutes><seconds>"`.

The following functions are used to set the time on the RTC:

`set_second(bus, data), set_minute(bus, data), set_hour(bus, data), set_weekday(bus, data), set_date(bus, data), set_month(bus, data), set_year(bus, data)`

The following functions are used to get the time from the RTC:

`get_second(bus, data), get_minute(bus, data), get_hour(bus, data), get_weekday(bus, data), get_date(bus, data), get_month(bus, data), get_year(bus, data)`

