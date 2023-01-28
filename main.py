
import tkinter
from tkinter import messagebox

count = 0

msg_box = messagebox.showwarning("TOMO PAPUDO!", "VOCÊ FOI HACKEADO")

if msg_box == 'ok':
    msg_box = messagebox.showwarning("PERA AI!", "PARA SER DESHACKEADO PRECISO QUE ME RESPONDA UMA PERGUNTA...")

if msg_box == 'ok':
    msg_box = messagebox.askquestion("O QUE ACHA?", "ACEITA NAMORAR COMIGO?")

while msg_box == 'no':
    count += 1
    msg_box = messagebox.askquestion("O QUE ACHA?", "ACEITA NAMORAR COMIGO?")
    if (count == 5):
        msg_box = messagebox.showerror("TO INDO AI!", "SE VAI APANHA FEIO!")
        break

if msg_box == 'yes':
    msg_box = messagebox.showinfo("BOA!", "SABIA ESCOLHA!")
