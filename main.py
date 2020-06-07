from time import strftime
from tkinter import *
import math

window = Tk()
window.title("Clock")
window.resizable(0, 0)

cv = Canvas(window, width=300, height=300, bg="#faf9f9")
cv.pack()

# -- initialization
font_type = ('Raleway', 20)
second = 0
minute = 0
hour = 0

s_hand = []
m_hand = []
h_hand = []
pivot = []
# -- end of initialization


# get current time
def time():

    global minute, hour, second

    # set digital time
    curr_time = strftime('%H:%M:%S %p')
    label.configure(text=curr_time, fg='#2d3142')

    second = int(curr_time[6:8])
    minute = int(curr_time[3:5])
    hour = int(curr_time[0:2])

    label.after(1000, time)


# rotate the hands
def rotate(origin, point, angle):

    ox, oy = origin
    px, py = point

    qx = ox + math.cos(angle) * (px - ox) - math.sin(angle) * (py - oy)
    qy = oy + math.sin(angle) * (px - ox) + math.cos(angle) * (py - oy)

    return qx, qy


# draw the hands
def draw_clock_hands():

    global s_hand, m_hand, h_hand, pivot

    cv.delete(s_hand, m_hand, h_hand, pivot)
    s_hand = cv.create_line(150, 170, rotate((150, 170), (150, 100), math.radians(second * 6)), width=1, fill='#4a4e69')  # second hand
    m_hand = cv.create_line(150, 170, rotate((150, 170), (150, 105), math.radians(minute * 6)), width=2)  # minute hand
    h_hand = cv.create_line(150, 170, rotate((150, 170), (150, 120), math.radians(hour * 30)), width=3)  # hour hand
    pivot = cv.create_oval(146, 166, 154, 174, fill='#2d3142', outline='')

    window.after(1000, draw_clock_hands)


label = Label(window, font=font_type, bg="#faf9f9")
label.pack()
cv.create_window(150, 50, window=label)

time()

# draw clock face
cv.create_oval(70, 90, 230, 250, fill='#dee2ff', outline='black', width=2)
for x in range(0, 12):
    cv.create_line(rotate((150, 170), (150, 95), math.radians(x*30)), rotate((150, 170), (150, 105), math.radians(x*30)), width=4, fill='#2d3142')

draw_clock_hands()

window.mainloop()