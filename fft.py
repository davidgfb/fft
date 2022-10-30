from numpy import linspace, sin, pi, abs
from numpy.fft import fft
from matplotlib.pyplot import subplots, show

Fs, f0 = 2000, 100
tstep, N = Fs ** -1, int(10 / f0 * Fs)
fstep, b, a = Fs / N, N - 1, int(N / 2 + 1)
t, f = tuple(linspace(0, a, N) for a in (b * tstep, b * fstep))
y = 1 * sin(2 * pi * f0 * t) #+ 4 * sin(2 * pi * 3 * f0 * t) + 2
X = fft(y)
X_mag = abs(X) / N 
f_plot, X_mag_plot, (fig, (ax1, ax2)) = f[: a], 2 * X_mag[: a],\
                                    subplots(nrows = 2, ncols = 1)
X_mag_plot[0] /= 2

tuple(a.plot(*b) for a, b in ((ax1, (t, y)),\
                              (ax2, (f_plot, X_mag_plot))))
tuple(a.set_xlabel(b) for a, b in ((ax1, 'time (s)'),\
                                   (ax2, 'freq (Hz)')))
tuple(a.grid() for a in (ax1, ax2))
tuple(a.set_xlim(0, b) for a, b in ((ax1, t[-1]),\
                                    (ax2, f_plot[-1])))
show()
