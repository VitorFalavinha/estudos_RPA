import tkinter as tk

def on_button_click():
    label.config(text="Olá, Tkinter!")

# Criar a janela principal
root = tk.Tk()
root.title("Exemplo Tkinter")


# Criar um rótulo (label)
label = tk.Label(root, text="Olá, Mundo!")
label.pack()

# Criar um botão
button = tk.Button(root, text="Clique em mim", command=on_button_click)
button.pack()

# Iniciar o loop principal
root.mainloop()
