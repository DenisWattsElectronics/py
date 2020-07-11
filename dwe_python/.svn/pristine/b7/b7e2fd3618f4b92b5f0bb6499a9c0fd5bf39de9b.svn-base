import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integrate
import scipy.special as special
from numpy import sqrt, sin, cos, pi
from scipy import stats
from scipy.stats import norm



Bits = np.zeros((2, 3))
UI = 320*10**(-12)
clk_ui_pos = 160e-12
det_Jitter = 40e-12
ran_Jitter = 10e-12
clk_Pos = np.array([0, 20e-12, 40e-12, 60e-12, 80e-12, 100e-12, 120e-12, 140e-12, 160e-12, 180e-12, 200e-12, 220e-12, 240e-12, 260e-12, 280e-12, 300e-12, 320e-12])

def cdf_jitter_ca
def cdf_jitter_calc_l(UI, clk_ui_pos, det_Jitter, ran_Jitter):
    distr1 = norm.cdf(det_Jitter, clk_ui_pos, ran_Jitter)
    return distr1

a = cdf_jitter_calc_l(UI, 40*10**-12, det_Jitter, ran_Jitter)

def ber_array_calc(UI, det_Jitter, ran_Jitter):
    plot = np.zeros(int(UI*10**12))
    for i in range(int(UI*10**12)):
        plot[i] = cdf_jitter_calc_r(UI, i*10**(-12), det_Jitter, ran_Jitter)
        plot[i] = plot[i] + cdf_jitter_calc_l(UI, i*10**(-12), det_Jitter, ran_Jitter)
    return plot

ber_array=np.zeros(int(UI*10**12))
ber_array = ber_array_calc(UI, det_Jitter, ran_Jitter)

# print(ber_array)

plt.plot(ber_array)
plt.yscale('log')
plt.grid(True)
plt.xlabel('clk_pos')
plt.ylabel('BER')
plt.ylim([10**-12,1])


plt.show()


# def ber_array_calc(UI, det_Jitter, ran_Jitter):
#     plot = np.zeros(int(UI*10**12))
#     for i in range(int(UI*10**12)):
#         plot[i] = cdf_jitter_calc(UI, i*10**(-12), det_Jitter, ran_Jitter)
#     return plot























