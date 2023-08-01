class User:

    def __init__(self, name, user_id, level=None):
        self.name = name
        self.user_id = user_id
        self.level = level

    def __eq__(self, other):
        return self.name == other.name and self.user_id == other.usesr_id

    def __str__(self):
        return f'Пользователь  {self.name} с id <{self.user_id}>, уровень <{self.level}>'
