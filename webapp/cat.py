import random

from django.http import request


class Cat:
    age = random.randint(1, 20)
    happiness = 10
    hunger = 40
    image = 'https://www.idlememe.com/wp-content/uploads/2021/10/beluga-cat-meme-idlememe-5.jpg'
    status = 'active'



    @classmethod
    def feed(cls):
        chance = random.randint(1, 50)
        if cls.status == 'sleep':
            return f'Котик слишком крепко спит и не реагирует даже на шуршание своего любимого корма'
        elif chance == 50:
            cls.hunger += 5
            return f'Котик проснулся, почуствовав запах еды.'
        cls.hunger += 15
        cls.happiness += 5
        if cls.hunger >= 100:
            cls.happiness -= 30
            return f'Котик чуствует себя слишком толстым, чтобы быть счастливым'
        return f'Котик покушал. '

    @classmethod
    def play(cls):
        chance = random.randint(1,3)
        cls.happiness += 15
        cls.happiness -= 10
        if cls.status == 'sleep':
            cls.happiness -= 5
            cls.status = 'active'
            return f'Котик  только что проснулся и не хочет играть'
        elif chance == 3:
            cls.happiness == 0
            return f'Котик испугался и спрятался под диван'
        return f'Котик наигрался и довольно мурлыкает'

    @classmethod
    def sleep(cls):
        chance = random.randint(1, 100)
        if cls.status == 'sleep':
            return f'Котик не может уснуть пока спит'
        elif chance == 100:
            cls.status = 'active'
            return f'Котик столкнул волчок и проснулся'
        cls.status = 'sleep'
        return 'Кота уложили спать'

    @classmethod
    def get_image(cls):
        if cls.happiness <= 10:
            cls.image = 'https://storage.googleapis.com/sticker-prod/h8KBmES9sfUo3ToQhZPR/0.png'
        if cls.happiness > 10 and cls.happiness <= 40:
            cls.image = 'https://pbs.twimg.com/media/FD-Y3soVEAE9Sjj?format=jpg&name=900x900'
        if cls.happiness > 40 and cls.happiness <= 70:
            cls.image = 'https://www.idlememe.com/wp-content/uploads/2021/10/beluga-cat-meme-idlememe-5.jpg'
        if cls.happiness > 70:
            cls.image = 'https://openseauserdata.com/files/4beb78c1fab1e6add27622cc5b92a0df.jpg'

    @classmethod
    def get_action(cls, action):
        if action:
            if action == 'sleep':
                message = cls.sleep()
            elif action == 'feed':
                message = cls.feed()
            elif action == 'play':
                message = cls.play()
            cls.get_image()
            return message

    @classmethod
    def get_status(cls):
        if cls.hunger >= 0:
            return True
        else:
            return None



