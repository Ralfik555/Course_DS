from ipywidgets import widgets
from IPython.display import display

text = widgets.Text()
display(text)

def obsluga(nadawca):
    print(text.value)

text.on_submit(obsluga)

# ====================================================

button = widgets.Button(description="klik klik")
display(button)

def przycisk_obsluga(przycisk):
    print("klik klik")

button.on_click(przycisk_obsluga)

# ====================================================

from ipywidgets import interact
def fun1(x):
    print(x)
interact(fun1, x=10)

def fun2(x, y):
    print(x + y)
interact(fun2, x=1, y=2)

drop_down = [('opcja1', 'wybrano1'), ('opcja2', 'wybrano2')]
interact(fun1, x=drop_down)

# ====================================================

from ipywidgets.widgets import *
from numpy import arange, sin, pi
import matplotlib.pyplot as plt

x = arange(0, 2, 0.02)
czas = arange(0, 1, 0.01)

def sinus(f):
    plt.ylim(-10, 10)
    plt.plot(x, sin(2*pi*czas*f))
    plt.show()

interact(sinus, f=(1, 10, 0.1))
