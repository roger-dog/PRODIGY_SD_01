import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import messagebox

# --- Temperature Conversion Functions ---

def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def celsius_to_kelvin(c):
    return c + 273.15

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def fahrenheit_to_kelvin(f):
    return (f - 32) * 5/9 + 273.15

def kelvin_to_celsius(k):
    return k - 273.15

def kelvin_to_fahrenheit(k):
    return (k - 273.15) * 9/5 + 32

# --- Conversion Logic ---

def convert_temperature():
    user_input = entry.get().strip().upper()

    if not user_input or len(user_input) < 2:
        messagebox.showerror("Invalid Input", "Please enter like 25C, 77F, 298K.")
        return

    try:
        value = float(user_input[:-1])
        unit = user_input[-1]

        if unit == 'C':
            f = celsius_to_fahrenheit(value)
            k = celsius_to_kelvin(value)
            result.set(f"{value}°C = {f:.2f}°F  |  {k:.2f}K")
        elif unit == 'F':
            c = fahrenheit_to_celsius(value)
            k = fahrenheit_to_kelvin(value)
            result.set(f"{value}°F = {c:.2f}°C  |  {k:.2f}K")
        elif unit == 'K':
            c = kelvin_to_celsius(value)
            f = kelvin_to_fahrenheit(value)
            result.set(f"{value}K = {c:.2f}°C  |  {f:.2f}°F")
        else:
            messagebox.showerror("Invalid Unit", "Please use C, F, or K.")
    except ValueError:
        messagebox.showerror("Invalid Value", "Use correct number and unit (e.g., 100C).")
    except Exception as e:
        messagebox.showerror("Error", f"Something went wrong: {e}")

# --- GUI Setup ---

app = ttk.Window(themename="darkly")  # darkly, cyborg, solar, morph, minty, etc.
app.title("🌡️ Temperature Converter")
app.geometry("450x250")
app.resizable(False, False)

ttk.Label(app, text="Enter Temperature (e.g., 100C, 32F, 300K):", font=("Segoe UI", 11)).pack(pady=10)

entry = ttk.Entry(app, font=("Segoe UI", 14), width=20, justify="center")
entry.pack(pady=5)

ttk.Button(app, text="Convert", bootstyle="primary", command=convert_temperature).pack(pady=10)

result = ttk.StringVar()
ttk.Label(app, textvariable=result, font=("Segoe UI", 12, "bold"), foreground="cyan").pack(pady=10)

ttk.Label(app, text="Supported Units: C = Celsius, F = Fahrenheit, K = Kelvin", font=("Segoe UI", 9), foreground="gray").pack(pady=5)

app.mainloop()
