import matplotlib.pyplot as plt
import math

# INTEGRATE AND FIRE MODEL CONSTANTS

El = -70e-3;
Vr = -70e-3;
Tm = 10;
Rm = 10e6;
Vt = -40e-3;
Ie = 3.1e-9;

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
apply_euler(0.001, clr)

plt.xlabel("t (seconds)")
plt.ylabel("v(t)")
plt.title("Simulation of the integrate and fire model with Ie smaller than the minimum value.")
plt.show()