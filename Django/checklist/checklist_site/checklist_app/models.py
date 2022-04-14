from django.db import models

# Create your models here.
class Game(models.Model):
    game_title = models.CharField(max_length=100)

    def __str__(self):
        return self.game_title

class Check(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    check_text = models.CharField(max_length=200)
    check_status = models.BooleanField(default=False)

    def __str__(self):
        return self.check_text
