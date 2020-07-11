from tkinter import *
# from tkinter.ttk import *
import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integrate
import scipy.special as special
from numpy import sqrt, sin, cos, pi
from scipy import stats
from scipy.stats import norm

UI_input = 0
det_iitter_input = 0
ran_jitter_input = 0

UI = 320*10**(-12)
clk_ui_pos = 160e-12
det_jitter = 40e-12
ran_jitter = 10e-12
clk_Pos = np.array([0, 20e-12, 40e-12, 60e-12, 80e-12, 100e-12, 120e-12, 140e-12, 160e-12, 180e-12, 200e-12, 220e-12, 240e-12, 260e-12, 280e-12, 300e-12, 320e-12])

# # # BACKEND # # #

def cdf_jitter_calc_r(UI, clk_ui_pos, det_jitter, ran_jitter):
    distr1 = norm.cdf(clk_ui_pos, UI - det_jitter, ran_jitter)
    return distr1

def cdf_jitter_calc_l(UI, clk_ui_pos, det_jitter, ran_jitter):
    distr1 = norm.cdf(det_jitter, clk_ui_pos, ran_jitter)
    return distr1

def ber_array_calc(UI, det_jitter, ran_jitter):
    plot = np.zeros(int(UI*10**12))
    for i in range(int(UI*10**12)):
        plot[i] = cdf_jitter_calc_r(UI, i*10**(-12), det_jitter, ran_jitter)
        plot[i] = plot[i] + cdf_jitter_calc_l(UI, i*10**(-12), det_jitter, ran_jitter)
    return plot

ber_array=np.zeros(int(UI*10**12))

# # #  FRONTEND  # # #

def plot_bath(event):
    UI_input = ent_UI.get()
    det_jitter_input = ent_detj.get()
    ran_jitter_input = ent_ranj.get()
    ber_array = ber_array_calc(int(UI_input)*10**(-12), float(det_jitter_input)*10**(-12), float(ran_jitter_input)*10**(-12))
    plt.plot(ber_array)
    plt.yscale('log')
    plt.grid(True)
    plt.xlabel('clk_pos')
    plt.ylabel('BER')
    plt.ylim([10**-12,1])
    plt.show()

root = Tk()
root.minsize(width = 1280, height = 480)
root.title("Simple Ber Plotter")
butplot = Button(root, text = "Построить график BER")
butplot.bind("<Button-1>", plot_bath)
main_tit = Label(root, text = "Добро пожаловать! Введите параметры для построения графика BER", font=("Helvetica", 14))
main_tit.place(x = 18, y = 0)

# Parameters input

lab_UI = Label(root, text = "Битовый интервал, пс", font=("Helvetica", 12))
lab_UI.place(x = 200, y = 40)
ent_UI = Entry(root, width = 20, bd = 3 )
ent_UI.place(x = 18, y = 40)

lab_detj = Label(root, text = "Детерминированный джиттер, пс", font=("Helvetica", 12))
lab_detj.place(x = 200, y = 80)
ent_detj = Entry(root, width = 20, bd = 3)
ent_detj.place(x = 18, y = 80)

lab_ranj = Label(root, text = "Случайный джиттер, пс", font=("Helvetica", 12))
lab_ranj.place(x = 200, y = 120)
ent_ranj = Entry(root, width = 20, bd = 3)
ent_ranj.place(x = 18, y = 120)




butplot.place(x = 5, y = 360)
root.mainloop()



















