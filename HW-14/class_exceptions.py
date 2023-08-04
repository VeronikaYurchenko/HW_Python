class Class_exceptions(Exception):
    pass


class LevelError(Class_exceptions):
    def __init__(self, user_level, admin_level):
        self.user_level = user_level
        self.admin_level = admin_level

    def __str__(self):
        return f"Ошибка уровня доступа! Уровень доступа должен быть <= {self.admin_level}! Текущий уровень: {self.user_level}."


class AccessError(Class_exceptions):
    def __init__(self, user_name, user_id):
        self.user_name = user_name
        self.user_id = user_id

    def __str__(self):
        return f'Ошибка доступа! Пользователь с именем  {self.user_name}, или id {self.user_id}> отсутствуют в списке пользователей!'


class LevelValueError(Class_exceptions):
    def __init__(self, min_val, max_val):
        self.min_val = min_val
        self.max_val = max_val

    def __str__(self):
        return f'Уровень пользователя должен быть от  {self.min_val} до {self.max_val - 1}!'