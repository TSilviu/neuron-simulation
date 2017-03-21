import matplotlib.pyplot as plt
import math
import random 


# INTEGRATE AND FIRE MODEL CONSTANTS

El = -70e-3;
Vr = -80e-3;
Tm = 20;
RmIe = 18e-3;
Vt = -54e-3;

# 

# Synapse parameters

Rmgs = 0.15
P = 0.5
Ts = 0.01
Es = 0

#

def dfv(v,t,RmIs):
	return (El - v + RmIe + RmIs)/Tm

# def dfs(s,t):
# 	return -s/Ts;

def apply_euler(dt):
	RmIs1 = 0
	RmIs2 = 0

	t = 0

	v1 = random.uniform(-80e-3, -54e-3)
	v2 = random.uniform(-80e-3, -54e-3)

	s1 = 0
	s2 = 0

	ts = [t]
	vs1 = [v1]
	vs2 = [v2]
	while t <= 1:
		t = t + dt

		v1 = v1 + dfv(v1,t,RmIs2)
		if(v1 >= Vt):
			s2 = s2 + P
			Is1 = Rmgs * s1 * (Es - v1)
			RmIs2 = Is1
			v1 = Vr
		else:
			s2 = s2 + (-s2/Ts) * dt
			Is1 = Rmgs * s1 * (Es - v1)
			RmIs2 = Is1


		v2 = v2 + dfv(v2,t,RmIs1)
		if(v2 >= Vt):
			s1 = s1 + P
			Is2 = Rmgs * s2 * (Es - v2)
			RmIs1 = Is2
			v2 = Vr
		else:
			s1 = s1 + (-s1/Ts) * dt
			Is2 = Rmgs * s2 * (Es - v2)
			RmIs1 = Is2

		ts.append(t)
		vs1.append(v1)
		vs2.append(v2)
	plt.plot(ts,vs1,color='b')
	plt.plot(ts,vs2,color='r')
	
apply_euler(0.001)
plt.xlabel("Current(nA)")
plt.ylabel("Firing rate - f(Current)")
plt.title("Increasing the amplitude while counting the number of spikes produced.")
plt.show()