"""	
	Primary Function:  get_timestring(bus)
	Returned value: "<year><month><date><hours><minutes><seconds>"
	
	Note: RTC pins depend on the I2C bus created in the calling function.
	Reference: https://datasheets.maximintegrated.com/en/ds/DS3231.pdf
"""

from pyb import I2C
import re

DEVICE_ADDRESS = 0x68

SECOND_ADDRESS = 0x00
MINUTE_ADDRESS = 0x01
HOUR_ADDRESS = 0x02
WEEKDAY_ADDRESS = 0x03
DATE_ADDRESS = 0x04
MONTH_ADDRESS = 0x05
YEAR_ADDRESS = 0x06

def get_second(bus):
	data = bytearray(1)
	data[:] = bus.mem_read(1,DEVICE_ADDRESS,SECOND_ADDRESS)
	return int(str(hex(data[0]))[2:])

def set_second(bus, data):
	bus.mem_write(data, DEVICE_ADDRESS, SECOND_ADDRESS, timeout=1000)


def get_minute(bus):
	data = bytearray(1)
	data[:] = bus.mem_read(1,DEVICE_ADDRESS,MINUTE_ADDRESS)
	return int(str(hex(data[0]))[2:])

def set_minute(bus, data):
	bus.mem_write(data, DEVICE_ADDRESS, MINUTE_ADDRESS, timeout=1000)

def get_hour(bus):
	data = bytearray(1)
	data[:] = bus.mem_read(1,DEVICE_ADDRESS,HOUR_ADDRESS)
	return int(str(hex(data[0]))[2:])

def set_hour(bus, data):
	bus.mem_write(data, DEVICE_ADDRESS, HOUR_ADDRESS, timeout=1000)

def get_weekday(bus):
	data = bytearray(1)
	data[:] = bus.mem_read(1,DEVICE_ADDRESS,WEEKDAY_ADDRESS)
	return int(str(hex(data[0]))[2:])

def set_weekday(bus, data):
	bus.mem_write(data, DEVICE_ADDRESS, WEEKDAY_ADDRESS, timeout=1000)

def get_date(bus):
	data = bytearray(1)
	data[:] = bus.mem_read(1,DEVICE_ADDRESS,DATE_ADDRESS)
	return int(str(hex(data[0]))[2:])

def set_date(bus, data):
	bus.mem_write(data, DEVICE_ADDRESS, DATE_ADDRESS, timeout=1000)

def get_month(bus):
	data = bytearray(1)
	data[:] = bus.mem_read(1,DEVICE_ADDRESS,MONTH_ADDRESS)
	return int(str(hex(data[0]))[2:])

def set_month(bus, data):
	bus.mem_write(data, DEVICE_ADDRESS, MONTH_ADDRESS, timeout=1000)

def get_year(bus):
	data = bytearray(1)
	data[:] = bus.mem_read(1,DEVICE_ADDRESS,YEAR_ADDRESS)
	return int(str(hex(data[0]))[2:])

def set_year(bus, data):
	bus.mem_write(data, DEVICE_ADDRESS, YEAR_ADDRESS, timeout=1000)

def get_timestring(bus):
	"""This function calls all other functions and returns a formatted time string."""
	times = [get_year(bus), get_month(bus), get_date(bus), get_hour(bus), get_minute(bus), get_second(bus)]
	#print(times)

	#formating time string (adding necessary zeros)
	# NOTE: use format instead
	# time_str=str(get_year(bus))
	# month=get_month(bus)
	# time_str+="0"+str(month) if month < 10 else str(month)
	# date=get_date(bus)
	# time_str+="0"+str(date) if date < 10 else str(date)
	# hour=get_hour(bus)
	# time_str+="0"+str(hour) if hour < 10 else str(hour)
	# minute=get_minute(bus)
	# time_str+="0"+str(minute) if minute < 10 else str(minute)
	# second=get_second(bus)
	# time_str+="0"+str(second) if second < 10 else str(second)
	
	time_str = "{:04d}{:02d}{:02d}{:02d}{:02d}{v}".format(times[0],times[1],times[2],times[3],times[4]times[5])
	
	return time_str
	#return str(get_year(bus)) + str(get_month(bus)) + str(get_date(bus)) + str(get_hour(bus)) + str(get_minute(bus)) + str(get_second(bus))