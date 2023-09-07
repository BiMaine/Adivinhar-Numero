import random
import tkinter as tk
from tkinter import messagebox

class JogoDeAdivinhacaoTkinter:
    def __init__(self, root):
        self.root = root
        self.root.title("Jogo de Adivinhação")
        self.root.geometry("400x250")
        self.root.resizable(False, False)
        
        self.numero_secreto = random.randint(1, 100)
        self.tentativas = 0
        self.max_tentativas = 5

        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        
        self.label = tk.Label(root, text="Tente adivinhar o número secreto entre 1 e 100.", font=("Helvetica", 12))
        self.label.pack(pady=10)
        
        self.entry = tk.Entry(root, font=("Helvetica", 10))
        self.entry.pack(pady=5)
        
        self.button = tk.Button(root, text="Adivinhar", command=self.verificar_palpite, font=("Helvetica", 12))
        self.button.pack(pady=5)
        
        self.reset_button = tk.Button(root, text="Reiniciar Jogo", command=self.reiniciar_jogo, font=("Helvetica", 12))
        self.reset_button.pack(pady=5)
        
        self.output = tk.Label(root, text="", font=("Helvetica", 12, "bold"), height=2, anchor="center")
        self.output.pack(pady=10)
        
    def verificar_palpite(self):
        try:
            palpite = int(self.entry.get())
        except ValueError:
            self.output.config(text="Por favor, digite um número válido.", fg="red")
            return
        
        self.tentativas += 1

        if palpite < self.numero_secreto:
            self.output.config(text="Menor do que o número secreto. Tente novamente.", fg="blue")
        elif palpite > self.numero_secreto:
            self.output.config(text="Maior do que o número secreto. Tente novamente.", fg="blue")
        else:
            self.output.config(text=f"Parabéns! Você acertou o número secreto ({self.numero_secreto}) em {self.tentativas} tentativas.", fg="green")
            messagebox.showinfo("Parabéns!", f"Você acertou o número secreto ({self.numero_secreto}) em {self.tentativas} tentativas.", fg="red")
            self.reiniciar_jogo()
            return
        
        if self.tentativas >= self.max_tentativas:
            self.output.config(text=f"Game Over! O número secreto era {self.numero_secreto}.", fg="red")
            messagebox.showinfo("Game Over", f"Game Over! O número secreto era {self.numero_secreto}.")
            self.reiniciar_jogo()
        
    def reiniciar_jogo(self):
        self.numero_secreto = random.randint(1, 100)
        self.tentativas = 0
        self.output.config(text="", fg="black")
        self.entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    jogo = JogoDeAdivinhacaoTkinter(root)
    root.mainloop()