from django.db import models
from django.urls import reverse
from django.utils import timezone


class Achievement(models.Model):
    title = models.CharField("Название", max_length=500)
    image = models.ImageField("Картинка", upload_to='pictures', blank=True)
    description = models.TextField("Описание", blank=True)
    order = models.IntegerField("Порядок", default=0)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('achievement', args=[self.id])

    class Meta:
        verbose_name = 'Ачивка'
        verbose_name_plural = 'Ачивки'
        ordering = ('order', 'title')


class Student(models.Model):
    lastname = models.CharField('Фамилия', max_length=40)
    firstname = models.CharField('Имя', max_length=40)
    middlename = models.CharField('Отчество', max_length=40, blank=True)
    photo = models.ImageField("Картинка", upload_to="photos", blank=True)

    group = models.IntegerField("Отряд", choices=((1, 1), (2, 2), (3, 3), (4, "Дед")), blank=True, default=1)
    date_of_birth = models.DateField('Дата рождения', null=True, blank=True)
    phone = models.CharField('Телефон', max_length=50, blank=True)
    email = models.EmailField('Электронная почта', max_length=255, blank=True)
    comment = models.TextField('Комментарий', blank=True)

    @property
    def fullname(self):
        return (self.lastname + " " + self.firstname + " " + self.middlename).strip()

    def __str__(self):
        return self.fullname

    def get_absolute_url(self):
        return reverse('student', args=[self.id])

    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'
        ordering = ('lastname', 'firstname', 'middlename')


class Record(models.Model):
    student = models.ForeignKey(Student, models.SET_NULL, verbose_name='Студент', related_name="records", null=True)
    achievement = models.ForeignKey(Achievement, models.SET_NULL, verbose_name='Ачивка', related_name="records", null=True)
    date = models.DateField("Дата выдачи", default=timezone.now)
    comment = models.TextField('Комментарий', blank=True)

    @property
    def without_student(self):
        return "%s - %s %s" % (self.achievement, self.date, self.comment)

    @property
    def without_achievement(self):
        return "%s - %s %s" % (self.student, self.date, self.comment)

    def __str__(self):
        return "%s - %s - %s " % (self.student, self.achievement, self.date)

    class Meta:
        verbose_name = 'Запись ачивки'
        verbose_name_plural = 'Записи'
        ordering = ('-date', 'student')
