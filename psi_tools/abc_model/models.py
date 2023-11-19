from django.db import models
from django.urls import reverse, reverse_lazy


class Emotion(models.Model):
    class Meta:
        verbose_name = "Эмоция"

    emotion = models.CharField(max_length=100, verbose_name="эмоция", unique=True)

    def __str__(self):
        return self.emotion


class ABCModel(models.Model):
    # class Meta:
    #     verbose_name = ""

    # slug = models.SlugField(max_lingth=255, unique=True, db_index=True)
    # user
    # activating beliefs consequences emotions date_create
    activating = models.TextField(verbose_name="событие", blank=True)
    beliefs = models.TextField(verbose_name="оценка", blank=True)
    consequences = models.TextField(verbose_name="реакция", blank=True)
    emotions = models.ManyToManyField("Emotion")
    date_create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"abc {self.pk}"

    def get_absolute_url(self):
        return reverse("abc_item", kwargs={"pk": self.pk})
        # return reverse("abc_item", kwargs={"id_model": self.pk})

# '''
# Модель выглядит как формула ABC, где A — активирующее событие (activating experience)[2], B — личные верования либо способы оценки событий[3] (рациональные и/или иррациональные убеждения, «B» означает beliefs — мнение, убеждение[2]), C — эмоциональные или поведенческие паттерны, возникающие вследствие B[3] («C» означает consequences — последствия[2]).
# '''
#
# '''
# G — наша цель в данном контексте. Цель, которая привела к событию (A). К примеру, цель устроиться на работу (G), на работу не приняли (A).
# A — событие. Пример: на работу не приняли.
# B — наше убеждение по поводу этого события. Пример: «Я должен получить эту работу, иначе я это не переживу».
# C — наши уместные и неуместные чувства по поводу этого события.
# D — дискуссионные вопросы об иррациональных представлениях. Когда мы обнаруживаем iBs — надо начать задавать вопросы, проверяющие убеждение на подлинность. Пример таких вопросов: «На основании каких данных сделано это заключение?», «Как одно исходит из другого?», «Есть ли доказательства у этого утверждения?».
# E — новая эффективная философия. Переформулирование убеждения так, чтобы оно было рациональным. Пример: «Я очень хочу эту работу, и если я её не получу — это будет грустно. Но жизнь продолжается!»
# '''