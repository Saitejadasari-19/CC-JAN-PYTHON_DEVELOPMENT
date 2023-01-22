from tkinter import *
import winsound
import time
import datetime

clock = Tk()
clock.geometry("400x300")


def alarm():
    while True:
        alarm_time = f"{hour.get()}:{min.get()}:{sec.get()}"
        time.sleep(1)
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time,alarm_time)
        if current_time == alarm_time:
            print("It's time to Wake Up!")
            winsound.PlaySound('sound.wav',winsound.SND_ASYNC)
            break

Label(clock,text="Alarm Clock",font=("Arial 20 bold"),fg="green").pack()
Label(clock,text="Set Alarm Time",font=("Arial 15")).pack()

frame = Frame(clock)
frame.pack()

hour = StringVar(clock)
min = StringVar(clock)
sec = StringVar(clock)

hours = ('00', '01', '02', '03', '04', '05', '06', '07',
        '08', '09', '10', '11', '12', '13', '14', '15',
        '16', '17', '18', '19', '20', '21', '22', '23', '24')
hour.set(hours[0])
hourTime = OptionMenu(clock,hour,*hours)
hourTime.pack()
Label(clock,text="Hours",font=("Arial 8")).pack()


minutes = ('00', '01', '02', '03', '04', '05', '06', '07',
            '08', '09', '10', '11', '12', '13', '14', '15',
            '16', '17', '18', '19', '20', '21', '22', '23',
            '24', '25', '26', '27', '28', '29', '30', '31',
            '32', '33', '34', '35', '36', '37', '38', '39',
            '40', '41', '42', '43', '44', '45', '46', '47',
            '48', '49', '50', '51', '52', '53', '54', '55',
            '56', '57', '58', '59', '60')
min.set(minutes[0])
minTime = OptionMenu(clock,min,*minutes)
minTime.pack()
Label(clock,text="Minutes",font=("Arial 8")).pack()



seconds = ('00', '01', '02', '03', '04', '05', '06', '07',
            '08', '09', '10', '11', '12', '13', '14', '15',
            '16', '17', '18', '19', '20', '21', '22', '23',
            '24', '25', '26', '27', '28', '29', '30', '31',
            '32', '33', '34', '35', '36', '37', '38', '39',
            '40', '41', '42', '43', '44', '45', '46', '47',
            '48', '49', '50', '51', '52', '53', '54', '55',
            '56', '57', '58', '59', '60')
sec.set(seconds[0])
secTime = OptionMenu(clock,sec,*seconds)
secTime.pack()
Label(clock,text="Seconds",font=("Arial 8")).pack()

Button(clock,text='Set Alarm',font='Arial 15',command=alarm).pack()

clock.mainloop()