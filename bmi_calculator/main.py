import ttkbootstrap as ttk
from PIL import Image, ImageTk
import os

BMI_TABLE = {
    0.0: ('blue', 'Zayıf'),
    18.5: ('green', 'Normal'),
    25.0: ('yellow', 'Kilolu'),
    30.0: ('orange', 'Obez'),
    35.0: ('red', 'Aşırı Obez')
}


class EntryWithPlaceholder(ttk.Entry):
    def __init__(self, parent, placeholder_text="", placeholder_color="gray"):
        self.text_var = ttk.StringVar(value=placeholder_text)
        super().__init__(parent, textvariable=self.text_var)
        self.placeholder_text = placeholder_text
        self.default_color = self['foreground']
        self.placeholder_color = placeholder_color
        self.configure(foreground=self.placeholder_color)
        
        self.bind("<FocusIn>", self.focus_in)
        self.bind("<FocusOut>", self.focus_out)
    
    def focus_in(self, event):
        if str(self['foreground']) == self.placeholder_color:
            self.text_var.set("")
            self.configure(foreground=self.default_color, justify='center')
    
    def focus_out(self, event):
        if self.text_var.get() == "":
            self.text_var.set(self.placeholder_text)
            self.configure(foreground=self.placeholder_color, justify='left')

def calculate_result(event):
    width = float(ent_weight.text_var.get())
    height = float(ent_height.text_var.get()) / 100
    bmi = round(width / (height * height), 1)
    
    bmi_color, bmi_text = BMI_TABLE[0.0]
    for bmi_value, bmi_result in BMI_TABLE.items():
        if bmi > bmi_value:
            bmi_color, bmi_text = bmi_result
    
    lbl_result.config(text=f"{bmi}\n{bmi_text}", foreground=bmi_color)
            

root = ttk.Window("BMI Hesaplayıcı", themename='superhero')
root.geometry("500x600")

img_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "img", "bmi_chart.png")
img = ImageTk.PhotoImage(Image.open(img_path))
lbl_img = ttk.Label(root, image=img)
lbl_img.pack(pady=20)

ent_weight = EntryWithPlaceholder(root, "Kilonuzu giriniz:")
ent_weight.pack(pady=30)

ent_height = EntryWithPlaceholder(root, "Boyunuz kaç cm:")
ent_height.pack(pady=20)

btn_calculate = ttk.Button(root, text='Hesapla')
btn_calculate.bind('<Button-1>', calculate_result)
btn_calculate.pack(pady=20)

btn_clear = ttk.Button(root, text='Temizle', command=lambda: lbl_result.config(text="Hesapla!", foreground='gray'))
btn_clear.pack(pady=20)

lbl_result = ttk.Label(root, text="Hesapla!", foreground='gray', justify='center', font = ('Calibri', 24))
lbl_result.pack(pady=20)

root.mainloop()