class Game:
    def set_damage(self, damage: int):
        # QuerySet
        print(damage)
        i_get = f'I get damage - {damage}'
        i_set = self.get_damage()
        return i_get, i_set

    def get_damage(self):
        return f'I kick - {28}'

# game = Game()

# print(game.set_damage(50))
