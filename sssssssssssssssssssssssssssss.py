import tkinter as tk
import random
from PIL import Image, ImageTk

# Třída hráče
class Player:
    def __init__(self, canvas, image_path):
        self.canvas = canvas
        self.image = Image.open(image_path)
        self.tk_image = ImageTk.PhotoImage(self.image)
        self.id = canvas.create_image(200, 200, anchor=tk.CENTER, image=self.tk_image)

    def move(self, x, y):
        self.canvas.move(self.id, x, y)

# Třída mince
class Coin:
    def __init__(self, canvas, image_path):
        self.canvas = canvas
        self.image = Image.open(image_path)
        self.tk_image = ImageTk.PhotoImage(self.image)
        self.id = canvas.create_image(random.randint(50, 750), random.randint(50, 550), anchor=tk.CENTER, image=self.tk_image)

# Hlavní funkce pro pohyb hráče
def move_player(event):
    if event.keysym == 'Up':
        player.move(0, -10)
    elif event.keysym == 'Down':
        player.move(0, 10)
    elif event.keysym == 'Left':
        player.move(-10, 0)
    elif event.keysym == 'Right':
        player.move(10, 0)

# Inicializace okna
root = tk.Tk()
root.title("Pokročilá hra s animacemi")
canvas = tk.Canvas(root, width=800, height=600)
canvas.pack()

# Vytvoření hráče
player = Player(canvas, "player.png")  # Nahraďte "player.png" cestou k vašemu obrázku hráče

# Vytvoření mincí
coins = []
for _ in range(10):
    coins.append(Coin(canvas, "coin.png"))  # Nahraďte "coin.png" cestou k vašemu obrázku mince

# Nastavení pohybu hráče
root.bind('<KeyPress>', move_player)

root.mainloop()
