from django.db import models


class Group(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name) + " " + str(self.age) + " " + str(self.group)


class Songs(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название песни")
    text = models.TextField(verbose_name="Текст песни", default="")
    translation = models.TextField(default="", verbose_name="Перевод")

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=1000, verbose_name="Ф.И.О.")
    birthday = models.DateField(verbose_name="Дата рождения")
    bio = models.TextField(default="", verbose_name="Биография")

    def __str__(self):
        return self.name
