from tkinter import *
def miles_to_kilometer():
    miles=float(miles_input.get())
    km = (miles*1.609)
    Kilometer_result_Label.config(text=f"{km}")

window = Tk()
window.title("Mile To Kilometer Converter")
window.config(padx=40,pady=40)

miles_input = Entry(width=20)
miles_input.grid(column=1, row=0)


miles_label= Label(text="Miles")
miles_label.grid(column=2, row=0)

is_equal_label = Label(text="is_equal")
is_equal_label.grid(column=0, row=1)

Kilometer_result_Label = Label(text="0")
Kilometer_result_Label.grid(column=1, row=1)


Kilo_meter_label = Label(text="KM")
Kilo_meter_label.grid(column=2, row=1)

Calculate_button = Button(text="Calculate", command=miles_to_kilometer)
Calculate_button.grid(column=1, row=2)































window.mainloop()