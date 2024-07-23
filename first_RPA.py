import tkinter as tk
import requests 

def on_button_click():
    url = 'https://g1.globo.com/'
    response = requests.get(url)
    if response.status_code == 200:
        html_content = response.
        label = tk.Label(root, text=html_content)
        label.pack()
    else:
        label = tk.Label(root, text="Falha ao acessar o site")
        label.pack()
        

# Criar a janela principal
root = tk.Tk()
root.title("Exemplo de WebScraping")
root.geometry("800x600")


# Criar um rótulo (label)
label = tk.Label(root, text="Automatizando a busca de notícias na Web")
label.pack()

# Criar um rótulo
label = tk.Label(root, text="Digite algo no campo abaixo:")
label.pack(pady=10)

# Criar um widget Entry
entry = tk.Entry(root, width=50)  # Define a largura do campo de entrada
entry.pack(pady=10)

# Criar um botão
button = tk.Button(root, text="Atualizar", command=on_button_click)
button.pack()

# Iniciar o loop principal
root.mainloop()
