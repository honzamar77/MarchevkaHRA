import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.score = 0

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            print(f"{self.name} byl zabit!")
            return True
        return False

class Enemy:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            print(f"{self.name} byl poražen!")
            return True
        return False

class Gun:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

class ShootingGame:
    def __init__(self, player):
        self.player = player
        self.enemies = []
        self.gun = Gun("Pistol", 20)

    def spawn_enemy(self):
        enemy_names = ["Goblin", "Zombie", "Alien"]
        enemy_name = random.choice(enemy_names)
        enemy_health = random.randint(50, 100)
        enemy_damage = random.randint(10, 30)
        enemy = Enemy(enemy_name, enemy_health, enemy_damage)
        self.enemies.append(enemy)
        print(f"{enemy.name} se objevil!")

    def shoot_enemy(self):
        if not self.enemies:
            print("Není žádný nepřítel k zasažení!")
            return

        enemy = random.choice(self.enemies)
        print(f"Střílíte na {enemy.name} s pomocí {self.gun.name}...")
        time.sleep(1)
        if random.random() < 0.7:  # 70% šance, že zásah
            print("Zásah!")
            enemy_alive = enemy.take_damage(self.gun.damage)
            if not enemy_alive:
                self.enemies.remove(enemy)
                self.player.score += 10
        else:
            print("Při střelbě jste minul!")

    def show_status(self):
        print(f"{self.player.name}: Zdraví: {self.player.health}, Skóre: {self.player.score}")
        print("Nepřátelé:")
        for enemy in self.enemies:
            print(f"{enemy.name}: Zdraví: {enemy.health}")

    def play(self):
        print("Vítejte ve střílečce!")
        while True:
            action = input("Stiskněte 's' pro střelbu, 'q' pro ukončení: ").lower()
            if action == 'q':
                print("Konec hry.")
                break
            elif action == 's':
                self.shoot_enemy()
                if random.random() < 0.5:  # 50% šance, že se objeví nový nepřítel po každé střelbě
                    self.spawn_enemy()
                self.show_status()

# Spuštění hry
player_name = input("Zadejte své jméno: ")
player = Player(player_name)
game = ShootingGame(player)
game.play()
