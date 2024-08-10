import tkinter as tk

class CurrencyConverter:

    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Currency Converter")
        self.window.geometry("300x200")

        self.input_label = tk.Label(self.window, text="Enter a value:")
        self.input_label.grid(column=0,row=0)
        self.input_entry = tk.Entry(self.window)
        self.input_entry.grid(column=1, row=0)
        self.from_label = tk.Label(self.window, text="From:")
        self.from_label.grid(column=0,row=1)

        self.from_var = tk.StringVar(self.window)
        self.from_var.set("USD")

        self.from_menu = tk.OptionMenu(self.window, self.from_var, "USD", "Pounds", "HKD")
        self.from_menu.grid(column=1, row=1)

        self.to_label = tk.Label(self.window, text="To")
        self.to_label.grid(column=0, row=2)

        self.to_var = tk.StringVar(self.window)
        self.to_var.set("Pounds")

        self.to_menu = tk.OptionMenu(self.window, self.to_var, "USD", "Pounds", "HKD")
        self.to_menu.grid(column=1, row=2)

        #Button

        self.convert_button = tk.Button(self.window, text="Convert", command=self.convert)
        self.convert_button.grid(column=0, row=3)

        #Label

        self.output_label = tk.Label(self.window, text="")
        self.output_label.grid(column=1, row=3)



        self.window.mainloop()


    def convert(self):

        input_value = float(self.input_entry.get())

        if self.from_var.get() == "Pounds":
            usd_value = input_value * 1.28

        elif self.from_var.get() == "HKD":
            usd_value = input_value * 0.13

        else:
            usd_value = input_value


        if self.to_var.get() == "Pounds":
            output_value = usd_value / 1.28

        elif self.to_var.get() == "HKD":
            output_value = usd_value / 0.13

        else:
            output_value = usd_value

        #Disiaplying the code

        self.output_label.config(text=str(output_value), fg="red")

converter = CurrencyConverter()