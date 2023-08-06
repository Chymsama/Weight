#!/usr/bin/env python
# coding: utf-8

# In[1]:


from tkinter import *
from tkinter import ttk


main = Tk()


main.mainloop()


# In[4]:


import tkinter as tk

class WeightConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Weight Converter")

        self.e2_value = tk.StringVar()

        self.label1 = tk.Label(root, text="Enter weight in kg:")
        self.label1.grid(row=0, column=0)

        self.e2 = tk.Entry(root, textvariable=self.e2_value)
        self.e2.grid(row=0, column=1)

        self.b1 = tk.Button(root, text="Convert", command=self.convert_weight)
        self.b1.grid(row=0, column=2)

        self.e3 = tk.Text(root, height=1, width=20)
        self.e3.grid(row=1, column=0)

        self.e4 = tk.Text(root, height=1, width=20)
        self.e4.grid(row=1, column=1)

        self.e5 = tk.Text(root, height=1, width=20)
        self.e5.grid(row=1, column=2)

        self.label2 = tk.Label(root, text="Gram")
        self.label2.grid(row=2, column=0)

        self.label3 = tk.Label(root, text="Pounds")
        self.label3.grid(row=2, column=1)

        self.label4 = tk.Label(root, text="Ounce")
        self.label4.grid(row=2, column=2)

    def convert_weight(self):
        kg = float(self.e2_value.get())
        gram = kg * 1000
        pound = kg * 2.20462
        ounce = kg * 35.274

        self.e3.delete("1.0", tk.END)
        self.e3.insert(tk.END, f"{gram:.2f} g")

        self.e4.delete("1.0", tk.END)
        self.e4.insert(tk.END, f"{pound:.2f} lbs")

        self.e5.delete("1.0", tk.END)
        self.e5.insert(tk.END, f"{ounce:.2f} oz")

if __name__ == "__main__":
    root = tk.Tk()
    app = WeightConverterApp(root)
    root.mainloop()

