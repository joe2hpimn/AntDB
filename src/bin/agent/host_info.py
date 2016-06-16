#!/usr/bin/python
# -*- coding: UTF-8 -*-

import psutil
import time
import sys

# set timeformat. (e.g. 2016-06-16 16:49:51 HKT)
ISOTIMEFORMAT = '%Y-%m-%d %H:%M:%S %Z'

def get_cpu_info():
	time_stamp = time.strftime(ISOTIMEFORMAT, time.localtime())
	cpu_usage = psutil.cpu_percent(interval=1)
	#print "%s %.2f" % (time_stamp, cpu_usage)
	return (time_stamp, cpu_usage)

def get_mem_info():
	memTotal = psutil.virtual_memory().total
	memUsed = psutil.virtual_memory().used
	memUsage = psutil.virtual_memory().percent
	time_stamp = time.strftime(ISOTIMEFORMAT, time.localtime())
	#print "%s %d %d %.2f" % (time_stamp, memTotal, memUsed, memUsage)
	return (time_stamp, memTotal, memUsed, memUsage)


def get_disk_info():
	time_stamp = time.strftime(ISOTIMEFORMAT, time.localtime())
	disk_read_bytes = psutil.disk_io_counters().read_bytes
	disk_read_time = psutil.disk_io_counters().read_time
	disk_write_bytes = psutil.disk_io_counters().write_bytes
	disk_write_time = psutil.disk_io_counters().write_time
	disk_total = psutil.disk_usage('/').total
	disk_used = psutil.disk_usage('/').used
	#print "%s %d %d %d %d %d %d" %(time_stamp, disk_read_bytes, disk_read_time, disk_write_bytes, disk_write_time, disk_total, disk_used)
	return (time_stamp, disk_read_bytes, disk_read_time, disk_write_bytes, disk_write_time, disk_total, disk_used)


def get_net_info():
	net_bytes_sent1 = psutil.net_io_counters().bytes_sent
	net_bytes_recv1 = psutil.net_io_counters().bytes_recv
	time.sleep(3)
	time_stamp = time.strftime(ISOTIMEFORMAT, time.localtime())
	net_bytes_sent2 = psutil.net_io_counters().bytes_sent
	net_bytes_recv2 = psutil.net_io_counters().bytes_recv
	sent = (net_bytes_sent2 - net_bytes_sent1)/3
	recv = (net_bytes_recv2 - net_bytes_recv1)/3
	#print "%s %d %d" % (time_stamp, sent, recv)
	return (time_stamp, sent, recv)


if __name__ == "__main__":
	get_cpu_info()
	get_mem_info()
	get_disk_info()
	get_net_info()