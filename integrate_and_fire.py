import matplotlib.pyplot as plt
import math

# INTEGRATE AND FIRE MODEL CONSTANTS

El = -70;
Vr = -70;
Tm = 10;
Rm = 10;
Vt = -40;
Ie = 2.9;

# 

def df(v,t):
	return (El - v + Rm * Ie)/Tm

def apply_euler(dt, clr):
	t = 0
	v = Vr

	ts = [t]
	vs = [v]
	while t <= 1:
		t = t + dt
		v = v + df(v,t)
		if(v >= Vt):
			v = Vr
		ts.append(t)
		vs.append(v)
	plt.plot(ts,vs,color=clr)
	
clr = 'b'
apply_euler(0.01, clr)

plt.xlabel("t (seconds)")
plt.ylabel("v(t)")
plt.title("Simulation of the integrate and fire model with Ie smaller than the minimum value.")
plt.show()