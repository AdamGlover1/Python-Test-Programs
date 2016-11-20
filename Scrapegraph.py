import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg\
    import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import matplotlib.animation as animation
from matplotlib import style

import tkinter as tk

import bs4 as bs
import urllib.request


style.use("ggplot")

f = Figure(dpi=100)

a = f.add_subplot(111)
a.set_ylim([0,2000])
a.set_autoscaley_on(False)
XLIST = []
YLIST = []

def animate(i):
    sauce = urllib.request.urlopen('http://oldschool.runescape.com/slu?order=WMLPA').read()
    soup = bs.BeautifulSoup(sauce,'lxml')

    contents = []
    for i in soup.find_all('tr', class_='server-list__row server-list__row--members'):
        content = i.text.strip('\n').split('\n')
        content.pop(1)
        contents.append(content)

    for world in contents:
        if world[0] == "Old School 2":
            ystring = world[1].rstrip(' players')
            YLIST.append(int(ystring))
            print(ystring)
            XLIST.append(len(XLIST)*10)
    a.clear()
    a.plot(XLIST,YLIST)
    
    


class Window(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title("Graph")


        canvas = FigureCanvasTkAgg(f, self)
        canvas.show()
        canvas.get_tk_widget().pack()



s = Window()
ani = animation.FuncAnimation(f, animate, interval=10000)
s.mainloop()
