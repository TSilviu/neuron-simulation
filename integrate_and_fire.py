import matplotlib.pyplot as plt
import math

# INTEGRATE AND FIRE MODEL CONSTANTS

El = -70e-3;
Vr = -70e-3;
Tm = 10;
Rm = 10e6;
Vt = -40e-3;
Ie = 2.0e-9;

# 

def df(v,t,i):
	return (El - v + Rm * i)/Tm

def apply_euler(dt, clr):
	t = 0
	v = Vr
	i = Ie

	ts = [t]
	vs = [v]
	Is = []
	spikes = []

	while i <= 5.1e-9:	
		spikes_count = 0
		while t <= 1:
			t = t + dt
			v = v + df(v,t,i)
			if(v >= Vt):
				v = Vr
				spikes_count = spikes_count + 1
			ts.append(t)
			vs.append(v)
		Is.append(i)
		spikes.append(spikes_count)
		i = i + 0.1e-9
		t = 0
		v = Vr
	# plt.plot(ts,vs,color=clr)
	plt.plot(Is,spikes,color=clr)
	
clr = 'b'
apply_euler(0.001, clr)

plt.xlabel("Current(nA)")
plt.ylabel("Firing rate - f(Current)")
plt.title("Increasing the amplitude while counting the number of spikes produced.")
plt.show()