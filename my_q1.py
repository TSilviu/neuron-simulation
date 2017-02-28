import matplotlib.pyplot as plt
import math

def df(f,t):
	return math.pow(f,2) - 3*f + math.exp(-t)

def apply_euler(dt,clr):
	t0 = 0
	f0 = 0

	ts = [t0]
	fs = [f0]
	while t0 <= 3:
		t0 = t0 + dt
		f0 = f0 + df(f0,t0) * dt

		ts.append(t0)
		fs.append(f0)
	
	plt.plot(ts,fs,color = clr)

clr = 'r'
apply_euler(0.01,clr)
clr = 'b'
apply_euler(0.1,clr)
clr = 'g'
apply_euler(0.5,clr)

plt.xlabel("t (seconds)")
plt.ylabel("f(t)")
plt.title("Euler solution with dt=0.01")
plt.show()