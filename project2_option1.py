import random
import numpy as np
import matplotlib.pyplot as plt
import math
from matplotlib import *

def my_range(start, end, step):
	while start <= end:
        	yield start
        	start += step
def rand_delay():
	return float(random.randrange(0,N,1)/N)
def count(x, start_times):
	y = 0
	i = 0
	while i!=len(start_times)-1:
		#if start_times[i-1]+propag_delay+packet_dur < start_times[i]:
		if start_times[i]+(x/N)+propag_delay < start_times[i+1]:
			y = y+1
			i = i+1
			#print i
		else:
			start_times[i+1] = start_times[i+1]+rand_delay()
			if start_times[i+1] <= 1:
				start_times = sorted(start_times)
			else:
				start_times.remove(start_times[i+1])
	return y

def non_persistent(start_times):
	for x in my_range(0, 20.1, 0.1):
	    	G.append(x)
		safe_packet = count(x, start_times)
		throughput.append((safe_packet*x)/N)

def is_busy():
	return True

# Start
# Non-persistent

N = 1000.0
propag_delay = 0.000001 #ms
packet_dur = 0.001 #ms
start_times = []
G = []
throughput = []

for i in range(0, int(N)):
	r = random.randint(0, 1000000)/1000000.0
	start_times.append(r)
	#print r

start_times = sorted(start_times)
print start_times

non_persistent(start_times)
transmission_time = propag_delay+packet_dur
a = propag_delay/transmission_time
#lower prop higher trans
print G
print throughput

plt.figure()
plt.plot(G, throughput)
plt.xlabel('G - avg no of packets per packet duration')
plt.ylabel('S - Throughput')
plt.title('Non Persistent CSMA')
plt.show()



	
