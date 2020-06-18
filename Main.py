from numpy import *
import numpy as np
import cmath
import math
from tkinter import *
from tkinter import ttk
import pylab
import os

colour1 = '#8cc8e9'
colour2 = '#b2daf0'

window = Tk()

window.title("Symmetrical Component Calculator")
window.geometry('350x205')
window.configure(bg=colour1)

VaMag, VbMag, VcMag, VaAng, VbAng, VcAng = 0, 0, 0, 0, 0, 0
V1 = 0
V2 = 0
V0 = 0

VaMagLabel = Label(window, text="Phase A Voltage", bg=colour1).grid(column=0, row=0)
VbMagLabel = Label(window, text="Phase B Voltage", bg=colour1).grid(column=0, row=1)
VcMagLabel = Label(window, text="Phase C Voltage", bg=colour1).grid(column=0, row=2)
VaAngLabel = Label(window, text="Angle", bg=colour1).grid(column=2, row=0)
VbAngLabel = Label(window, text="Angle", bg=colour1).grid(column=2, row=1)
VcAngLabel = Label(window, text="Angle", bg=colour1).grid(column=2, row=2)

V1MagLabel = Label(window, text="Pos. Seq. Voltage:", bg=colour1).grid(column=0, row=3)
V2MagLabel = Label(window, text="Neg. Seq. Voltage:", bg=colour1).grid(column=0, row=5)
V0MagLabel = Label(window, text="Zero Seq. Voltage:", bg=colour1).grid(column=0, row=7)
V1AngLabel = Label(window, text="Pos. Seq. Angle:", bg=colour1).grid(column=0, row=4)
V2AngLabel = Label(window, text="Neg. Seq. Angle:", bg=colour1).grid(column=0, row=6)
V0AngLabel = Label(window, text="Zero Seq. Angle:", bg=colour1).grid(column=0, row=8)

V1MagLabel1 = Label(window, text="V", bg=colour1).grid(column=3, row=3)
V2MagLabel1 = Label(window, text="V", bg=colour1).grid(column=3, row=5)
V0MagLabel1 = Label(window, text="V", bg=colour1).grid(column=3, row=7)
V1AngLabel1 = Label(window, text="Deg.", bg=colour1).grid(column=3, row=4)
V2AngLabel1 = Label(window, text="Deg.", bg=colour1).grid(column=3, row=6)
V0AngLabel1 = Label(window, text="Deg.", bg=colour1).grid(column=3, row=8)

VaMagEntry = Entry(window, width=10, justify=CENTER)
VaMagEntry.grid(column = 1, row = 0)
VbMagEntry = Entry(window, width=10, justify=CENTER)
VbMagEntry.grid(column = 1, row = 1)
VcMagEntry = Entry(window, width=10, justify=CENTER)
VcMagEntry.grid(column = 1, row = 2)
VaAngEntry = Entry(window, width=5, justify=CENTER)
VaAngEntry.grid(column = 3, row = 0)
VbAngEntry = Entry(window, width=5, justify=CENTER)
VbAngEntry.grid(column = 3, row = 1)
VcAngEntry = Entry(window, width=5, justify=CENTER)
VcAngEntry.grid(column = 3, row = 2)
	
def plotphase():	
	VaMag = int(VaMagEntry.get()) # 240
	VbMag = int(VbMagEntry.get()) # 240
	VcMag = int(VcMagEntry.get()) # 240
	VaAng = int(VaAngEntry.get()) # 0 deg
	VbAng = int(VbAngEntry.get()) # 120 deg
	VcAng = int(VcAngEntry.get()) # 240 deg
	VaAngRad = (VaAng * pi) / 180
	VbAngRad = (VbAng * pi) / 180
	VcAngRad = (VcAng * pi) / 180

	VaMagplot = [0, VaMag]
	VaAngplot = [VaAngRad, VaAngRad]
	VbMagplot = [0, VbMag]
	VbAngplot = [VbAngRad, VbAngRad]
	VcMagplot = [0, VcMag]
	VcAngplot = [VcAngRad, VcAngRad]
	
	fig = pylab.figure()
	axarr = fig.add_subplot(111, polar = True)
	axarr.plot(VaAngplot,VaMagplot, label = 'Va')
	axarr.plot(VbAngplot,VbMagplot, label = 'Vb')
	axarr.plot(VcAngplot,VcMagplot, label = 'Vc')
	axarr.legend()
	axarr.set_title("Va, Vb, Vc, Magnitude and Phase", va='bottom')
	pylab.show()
	
	
def plotseq():
	VaMag = int(VaMagEntry.get()) # 240
	VbMag = int(VbMagEntry.get()) # 240
	VcMag = int(VcMagEntry.get()) # 240
	VaAng = int(VaAngEntry.get()) # 0 deg
	VbAng = int(VbAngEntry.get()) # 120 deg
	VcAng = int(VcAngEntry.get()) # 240 deg
	
	a = cmath.rect(1,(120*pi)/180) 
	Va = cmath.rect(VaMag, (VaAng*pi)/180)
	Vb = cmath.rect(VbMag, (VbAng*pi)/180)
	Vc = cmath.rect(VcMag, (VcAng*pi)/180)
	V1 = (Va + (Vb * a) + (Vc * a**2))/3
	V2 = (Va + (Vb * a**2) + (Vc * a))/3
	V0 = (Va + Vb + Vc)/3
	
	V1Mag = abs(V1)
	V2Mag = abs(V2)
	V0Mag = abs(V0)
	V1AngRad = cmath.phase(V1)
	V2AngRad = cmath.phase(V2)
	V0AngRad = cmath.phase(V0)
	V1AngDeg = (V1AngRad * 180) / pi
	V2AngDeg = (V2AngRad * 180) / pi
	V0AngDeg = (V0AngRad * 180) / pi
	print(" ")
	print("Positive Sequence = : " + str(V1Mag) + "V" + " at " + str(V1AngDeg) + " degrees." )
	print("Negative Sequence = : " + str(V2Mag) + "V" + " at " + str(V2AngDeg) + " degrees." )
	print("Zero Sequence = : " + str(V0Mag) + "V" + " at " + str(V0AngDeg) + " degrees." )
	print(" ")
	
	V1MagValue = Label(window, text=V1Mag, bg=colour2).grid(column=1, row=3)
	V2MagValue = Label(window, text=V2Mag, bg=colour2).grid(column=1, row=5)
	V0MagValue = Label(window, text=V0Mag, bg=colour2).grid(column=1, row=7)
	V1AngValue = Label(window, text=V1AngDeg, bg=colour2).grid(column=1, row=4)
	V2AngValue = Label(window, text=V2AngDeg, bg=colour2).grid(column=1, row=6)
	V0AngValue = Label(window, text=V0AngDeg, bg=colour2).grid(column=1, row=8)

	V1Magplot = [0, V1Mag]
	V1Angplot = [V1AngRad, V1AngRad]
	V2Magplot = [0, V2Mag]
	V2Angplot = [V2AngRad, V2AngRad]
	V0Magplot = [0, V0Mag]
	V0Angplot = [V0AngRad, V0AngRad]
	
	fig = pylab.figure()
	axarr = fig.add_subplot(111, polar = True)
	axarr.plot(V1Angplot,V1Magplot, label = 'Positive Sequence')
	axarr.plot(V2Angplot,V2Magplot, label = 'Negative Sequence')
	axarr.plot(V0Angplot,V0Magplot, label = 'Zero Sequence')
	axarr.legend()

	axarr.set_title("Symmetrical Component Magnitude and Phase", va='bottom')
	pylab.show()

	
def reset():
	python = sys.executable
	os.execl(python, python, *sys.argv)
	

plotSeqButton = Button(window, text="Plot Seq", command=plotseq, bg="#f6b360").grid(column=4, row = 0)
plotPhaseButton = Button(window, text="Plot Phase", command=plotphase, bg="#f6b360").grid(column=4, row = 1)
resetButton = Button(window, text="Reset", command=lambda: reset(), bg="#f6b360").grid(column=4, row = 2)
window.mainloop()

