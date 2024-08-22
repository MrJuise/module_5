'''
Задание "Свой YouTube":
Университет Urban подумывает о создании своей платформы, где будут размещаться дополнительные полезные ролики на тему IT
(юмористические, интервью и т.д.). Конечно же для старта написания интернет ресурса требуются хотя бы базовые знания программирования.

Именно вам выпала возможность продемонстрировать их, написав небольшой набор классов, которые будут выполнять похожий функционал на сайте.

Всего будет 3 класса: UrTube, Video, User.

Общее ТЗ:
Реализовать классы для взаимодействия с платформой, каждый из которых будет содержать методы добавления видео, авторизации и регистрации пользователя и т.д.
'''


import time


class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age
    def __str__(self):
        return self.nickname

class Video:
    def __init__(self, title, duration, time_now=0, adult_mode = False):
        self.title = str(title)
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode
class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def register(self, nickname, password, age):
        cur_user = User(nickname, password, age)
        for user in self.users:
            if cur_user.nickname == user.nickname:
                print(f'Пользователь {nickname} уже существует.')
                return
        self.users.append(cur_user)
        self.current_user = cur_user
    def log_in(self, nickname, password, age):
        cur_user = User(nickname, password, age)
        for user in self.users:
            if cur_user.nickname == user.nickname and cur_user.password == user.password and cur_user.age == user.age:
                self.current_user = cur_user
                print(f'Пользователь {nickname} авторизован.')
                return
        print(f'Пользователь {nickname} не найден')
        self.register(nickname, password, age)
    def add(self, *args):
        for vid in args:
            self.videos.append(vid)
    def get_videos(self, video_name):
        vi = []
        for vid in self.videos:
            if video_name.lower() in vid.title.lower():
                vi.append(vid.title)
        return vi
    def watch_video(self, vid_name):
        if self.current_user != None:
            if self.current_user.age >= 18:
                for vi in self.videos:
                    if vid_name in vi.title:
                        for i in range(vi.duration):
                            i += 1
                            time.sleep(1)
                            print(i, end="")
                            print(' ', end="")
                        print("Конец видео")
            else:
                print('Вам нет 18 лет, пожалуйста покиньте страницу')
        else:
            print('Войдите в аккаунт, чтобы смотреть видео')
    def log_out(self):
        self.current_user = None
        return
ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)


# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')