enemies = []
def spawn_enemies(x, y, z):
    for i in range(z):
        j = Enemy(x + 50, y)
        x += 50
        enemies.append(j)

spawn_enemies(100, 50, 35)

sprite_group.add(enemies)

def spawn_enemies(x, y, z):
    if z > 0:
        spawn_enemies(x + 50, y, z - 1)
    enemies.append(Enemy(x, y))
