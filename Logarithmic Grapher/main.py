
'''
Logarithmic Grapher v0.1
1/11/2022
'''

import math
from tkinter import *
import tkinter.messagebox
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from PIL import ImageTk,Image

xAxis = []
yAxis = []

fig = Figure(figsize = (5, 5), dpi = 100)
plot1 = fig.add_subplot(111)
plot1.grid(True)
plot1.axis([-10, 10, -10, 10])

window = Tk()
canvas = FigureCanvasTkAgg(fig, master = window)

LogLabel = Label(window, text=u'log_b (x - h) + k')
LogLabel.config(font=('Helvetica bold',30))
LogLabel.pack()

BLabel = Label(window, text="b:").pack()
logEntry = Entry(window, width=5)
logEntry.pack()

# x translation input
XLabel = Label(window, text="h:").pack()
XTrans = Entry(window, width=5)
XTrans.pack()

# y translation input
YLabel = Label(window, text="k:").pack()
YTrans = Entry(window, width=5)
YTrans.pack()


def getValues(logBase, xTrans, yTrans):
  # getting & clearing data
  decimalXAxis = []
  decimalYValList = []
  valList = [] 
  wholeNumberXAxis = [1,2,3,4,5,6,7,8,9,10,11]

  # this is if they enter something less than 0 or 1
  if logBase <= 0:
    tkinter.messagebox.showinfo("Error", "You cannot enter anything less than or equal to 0 as a BASE")
  elif logBase == 1:
    tkinter.messagebox.showinfo("Error", "You cannot enter 1 as a BASE")

  # this if if they enter a normal base number
  else:
    # values for x < 1, x > 0
    for decimal in range(1,10):
      decimalXAxis.append(decimal/10)
      decimalYValList.append(math.log(decimal/10, logBase))
    valList.append(0) # this is f(1) = 0
    for x in range(2,12):
        valList.append(math.log(x, logBase))
    # graphing data
    xAxis = decimalXAxis + wholeNumberXAxis
    yAxis = decimalYValList + valList

    # adding translations
    xAxis = [x + xTrans for x in xAxis]
    yAxis = [y + yTrans for y in yAxis]

    plot(xAxis, yAxis)

def plot(x, y):
    # creating graph
    plot1.plot(x, y)

    # creating canvas
    canvas.draw()
    canvas.flush_events()
  
    # places the graph on the tkinter window
    canvas.get_tk_widget().pack()

window.title('Logarithmic Grapher')
window.geometry("500x500")

# this checks if the values are actually strings
def valuecheck(base, x, y):
  try:
    getValues(float(base.get()), float(x.get()), float(y.get()))
  except ValueError:
    tkinter.messagebox.showinfo("Error", "One or more of your input boxes have characters that are not integers, or you have an unnecessary space.")
    
plot_button = Button(master=window, text='Plot', command= lambda: valuecheck(logEntry, XTrans, YTrans))

plot_button.pack()

# run the gui
window.mainloop()