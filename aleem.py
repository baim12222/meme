import tkinter as tk
from PIL import Image, ImageTk
import tkinter.messagebox
from tkinter.constants import SUNKEN
# Membuat window utama
window = tk.Tk()
window.title('Aleem ahmad')

# Aktifkan mode fullscreen
window.attributes('-fullscreen', True)

# Membaca gambar background menggunakan PIL
bg_image = Image.open("ROCKSTAR.jpg")
bg_image = bg_image.resize((window.winfo_screenwidth(), window.winfo_screenheight()), Image.Resampling.LANCZOS)
bg_photo = ImageTk.PhotoImage(bg_image)

# Membuat Canvas untuk background image
canvas = tk.Canvas(window, width=window.winfo_screenwidth(), height=window.winfo_screenheight())
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, image=bg_photo, anchor="nw")

# Frame di atas canvas
frame = tk.Frame(master=window, bg="grey", padx=10)
frame.place(relx=0.5, rely=0.5, anchor='center')  # Tempatkan frame di tengah layar

# Entry field
entry = tk.Entry(master=frame, relief=SUNKEN, borderwidth=10, font=(500), width=30)
entry.grid(row=0, column=0, columnspan=3, ipady=2, pady=2, sticky="nsew")

# Fungsi untuk memasukkan angka ke dalam entry
def myclick(number):
    entry.insert(tk.END, number)

def equal():
    try:
        result = eval(entry.get().replace(',', '.'))
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

def comma():
    current = entry.get()
    if ',' not in current:
        entry.insert(tk.END, ',')
        
def percentage():
    current = entry.get()
    try:
        result = float(current) / 100
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except ValueError:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

def square_root():
    current = entry.get()
    try:
        result = float(current) ** 0.5
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except ValueError:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

def clear():
    entry.delete(0, tk.END)
# Pembuatan tombol angka dan operasi

button_1 = tk.Button(master=frame, text='1', padx=15,
            pady=5, width=3, bg='black', fg='white', command=lambda:
myclick(1))
button_1.grid(row=1, column=0, pady=2, sticky="nsew")
button_2 = tk.Button(master=frame,text='2', padx=15,
            pady=5, width=3, bg='black', fg='white', command=lambda: 
myclick(2))       
button_2.grid(row=1, column=1, pady=2, sticky="nsew")
button_3 = tk.Button(master=frame,text='3', padx=15, 
            pady=5, width=3, bg='black', fg='white', command=lambda: 
myclick(3))       
button_3.grid(row=1, column=2, pady=2, sticky="nsew")
button_4 = tk.Button(master=frame,text='4', padx=15, 
            pady=5, width=3, bg='black', fg='white', command=lambda: 
myclick(4))       
button_4.grid(row=2, column=0, pady=2, sticky="nsew")
button_5 = tk.Button(master=frame,text='5', padx=15, 
            pady=5, width=3, bg='black', fg='white', command=lambda: 
myclick(5))       
button_5.grid(row=2, column=1, pady=2, sticky="nsew")
button_6 = tk.Button(master=frame,text='6', padx=15, 
            pady=5, width=3, bg='black', fg='white', command=lambda: 
myclick(6))       
button_6.grid(row=2, column=2, pady=2, sticky="nsew")
button_7 = tk.Button(master=frame,text='7', padx=15, 
            pady=5, width=3, bg='black', fg='white', command=lambda: 
myclick(7))       
button_7.grid(row=3, column=0, pady=2, sticky="nsew")
button_8 = tk.Button(master=frame,text='8', padx=15, 
            pady=5, width=3, bg='black', fg='white', command=lambda: 
myclick(8))       
button_8.grid(row=3, column=1, pady=2, sticky="nsew")
button_9 = tk.Button(master=frame,text='9', padx=15, 
            pady=5, width=3, bg='black', fg='white', command=lambda: 
myclick(9))       
button_9.grid(row=3, column=2, pady=2, sticky="nsew")
button_0 = tk.Button(master=frame,text='0', padx=15, 
            pady=5, width=3, bg='black', fg='white', command=lambda: 
myclick(0))       
button_0.grid(row=4, column=1, pady=2, sticky="nsew")

button_add = tk.Button(master=frame, text="+", padx=15,
                        pady=5,width=3, bg='black', fg='white', command=lambda:
myclick('+'))
button_add.grid(row=5, column=0, pady=2, sticky="nsew")

button_subtract = tk.Button(master=frame, text="-", padx=15,
                        pady=5,width=3, bg='black', fg='white', command=lambda:
myclick('-'))
button_subtract.grid(row=4, column=0, pady=2, sticky="nsew")

button_multiply = tk.Button(master=frame, text="*", padx=15,
                        pady=5,width=3, bg='black', fg='white', command=lambda:
myclick('*'))
button_multiply.grid(row=4, column=2, pady=2, sticky="nsew")

button_div = tk.Button(master=frame, text="/", padx=15,
                        pady=5,width=3, bg='black', fg='white', command=lambda:
myclick('/'))
button_div.grid(row=6, column=0, pady=2, sticky="nsew")

button_square = tk.Button(master=frame, text="√", padx=15,
                        pady=5, width=3, bg='black', fg='white', command=square_root)
button_square.grid(row=7, column=0, pady=2, sticky="nsew")

button_comma = tk.Button(master=frame, text=",", padx=15,
                        pady=5,width=3, bg='black', fg='white', command=comma)

button_comma.grid(row=7, column=1, pady=2, sticky="nsew")

button_percentage = tk.Button(master=frame, text="%", padx=15,
                        pady=5,width=3, bg='black', fg='white', command=percentage)

button_percentage.grid(row=7, column=2, pady=2, sticky="nsew")

button_clear = tk.Button(master=frame, text="clear", padx=15,
                        pady=5,width=12, bg='black', fg='white', 
command=clear)
button_clear.grid(row=6, column=1, columnspan=2, pady=2, sticky="nsew")

button_equal = tk.Button(master=frame, text="=", padx=15,
                        pady=5, width=12, bg='black', fg='white', 
command=equal)
button_equal.grid(row=5, column=1, columnspan=2, pady=2, sticky="nsew")

for i in range(8):
    frame.grid_rowconfigure(i, weight=1)
for j in range(4):
    frame.grid_columnconfigure(j, weight=1)

def toggle_fullscreen(event=None):
    is_fullscreen = window.attributes('-fullscreen')
    window.attributes('-fullscreen', not is_fullscreen)

def end_fullscreen(event=None):
    window.attributes('-fullscreen', False)

window.bind('<F11>', toggle_fullscreen)
window.bind('<Escape>', end_fullscreen)

window.mainloop()