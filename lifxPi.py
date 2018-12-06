
from lifxlan import *
from Tkinter import *

lifx = LifxLAN(2)
lights = lifx.get_lights()

window = Tk()
window.title("LIFX")
frame = Frame(window)
frame.pack()

white = False

def info():
    color = lights[0].get_color()
    info = {"HUE": color[0], "SATURATION": color[1], "BRIGHTNESS": color[2], "KELVIN": color[3]}
    return info

def updateElements():
    brightnessSlider.set(info()["BRIGHTNESS"])

def updateBrightness(value):
    lights[0].set_brightness(value)
    lights[1].set_brightness(value)
    print("BRIGHTNESS UPDATED: " + str(info()["BRIGHTNESS"]))

def toggle():
    state = lights[0].get_power()
    if state > 0:
        lights[0].set_power("off")
        lights[1].set_power("off")
        print("STATE UPDATED: OFF")
    else:
        lights[0].set_power("on")
        lights[0].set_brightness(float(brightnessSlider.get()))
        lights[1].set_power("on")
        lights[1].set_brightness(float(brightnessSlider.get()))
        print("STATE UPDATED: ON")

def redColor():
    lights[0].set_color(RED)
    lights[0].set_brightness(float(brightnessSlider.get()))
    lights[1].set_color(RED)
    lights[1].set_brightness(float(brightnessSlider.get()))

def blueColor():
    lights[0].set_color(BLUE)
    lights[0].set_brightness(float(brightnessSlider.get()))
    lights[1].set_color(BLUE)
    lights[1].set_brightness(float(brightnessSlider.get()))

def whiteColor():
    color = lights[0].get_color()
    if color[1] != 0:
        lights[0].set_saturation(0)
        lights[0].set_brightness(float(brightnessSlider.get()))
        lights[1].set_saturation(0)
        lights[1].set_brightness(float(brightnessSlider.get()))
    else:
        lights[0].set_colortemp(2500)
        lights[0].set_brightness(float(brightnessSlider.get()))
        lights[1].set_colortemp(2500)
        lights[1].set_brightness(float(brightnessSlider.get()))


brightnessSlider = Scale(frame, from_=65535, to=0, command=updateBrightness, showvalue=0, width=25)
brightnessSlider.pack(fill=Y, side=LEFT)

toggleButton = Button(frame, text="TOGGLE LIGHTS", command=toggle)
toggleButton.pack(fill=X)

whiteButton = Button(frame, text="WHITE", command=whiteColor)
whiteButton.pack(fill=X)

blueButton = Button(frame, text="BLUE", command=blueColor)
blueButton.pack(fill=X)

redButton = Button(frame, text="RED", command=redColor)
redButton.pack(fill=X)

window.mainloop()
