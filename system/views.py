from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import TemplateView
from system.models import Student, Group, Songs, Author
import sqlite3


class HomeView(TemplateView):
    template_name = "index.html"

    # def dispatch(self, request, *args, **kwargs):
    #     if request.method == 'GET':
    #         search_name = request.POST.get("search_name")
    #         if search_name != "":
    #             conn = sqlite3.connect('Chinook_Sqlite.sqlite')
    #             cursor = conn.cursor()
    #             songs = cursor.execute("SELECT name FROM Songs ORDER BY name")
    #             for search in songs:
    #                 if search_name == search:
    #                     return redirect(reverse("songs"))
    #             conn.close()
    #     context = {
    #         'method': request.method,
    #     }
    #
    #     return render(request, self.template_name, context)


class NirvanaSmells(TemplateView):
    template_name = "1.1.html"


class NirvanaHeart(TemplateView):
    template_name = "1.2.html"


class NirvanaMan(TemplateView):
    template_name = "1.3.html"


class GreenAmerican(TemplateView):
    template_name = "2.1.html"


class GreenDreams(TemplateView):
    template_name = "2.2.html"


class GreenWake(TemplateView):
    template_name = "2.3.html"


class ParkNumb(TemplateView):
    template_name = "3.1.html"


class ParkEnd(TemplateView):
    template_name = "3.2.html"


class ParkDone(TemplateView):
    template_name = "3.3.html"


class AcBlack(TemplateView):
    template_name = "4.1.html"


class AcHell(TemplateView):
    template_name = "4.2.html"


class AcThunder(TemplateView):
    template_name = "4.3.html"


class GracePain(TemplateView):
    template_name = "5.1.html"


class GraceMachine(TemplateView):
    template_name = "5.2.html"


class GraceRace(TemplateView):
    template_name = "5.3.html"


class StudentsView(TemplateView):
    template_name = "students.html"

    def get_context_data(self, **kwargs):
        name = self.request.GET.get("name", "")
        age = self.request.GET.get("age", None)

        students = Student.objects.filter(name__contains=name)
        if age is not None:
            students = Student.objects.filter(age=age)
        return {
            'name': name,
            'title': "Все студенты",
            'students': students
        }

    def dispatch(self, request, *args, **kwargs):
        students = Student.objects.all().order_by("-age")
        context = {
            'students': students
        }
        return render(request, self.template_name, context)


class StudentView(TemplateView):
    template_name = "student.html"

    def dispatch(self, request, *args, **kwargs):
        student_id = kwargs['id']
        student = Student.objects.get(pk=student_id)
        context = {
            'student': student
        }
        return render(request, self.template_name, context)


class GroupView(TemplateView):
    template_name = "students.html"

    def get_context_data(self, **kwargs):
        group_id = kwargs['group_id']

        title = "Список студентов"
        try:
            group = Group.objects.get(pk=group_id)
            title = "Студенты группы " + group.name
        except Group.DoesNotExist:
            title = "Такая группа не найдена"

        students = Student.objects.filter(group=group_id)
        return {
            'title': title,
            'students': students
        }


class GroupsView(TemplateView):
    template_name = "groups.html"

    def get_context_data(self, **kwargs):
        groups = Group.objects.all()
        return {
            'title': "Все студенты",
            'groups': groups,
        }


class CreateGroupView(TemplateView):
    template_name = "forms/group_form.html"

    def dispatch(self, request, *args, **kwargs):
        message = ""
        if request.method == 'POST':
            name = request.POST.get("group_name")
            group = Group(name=name)
            group.save()
            return redirect(reverse("groups"))

        context = {
            'method': request.method,
            'message': message
        }

        return render(request, self.template_name, context)


class AuthorsView(TemplateView):
    template_name = "authors.html"

    def dispatch(self, request, *args, **kwargs):
        authors = Author.objects.all()
        context = {
            'authors': authors
        }
        return render(request, self.template_name, context)


class SongsView(TemplateView):
    template_name = "SongFromBD.html"

    def dispatch(self, request, *args, **kwargs):
        songs = Songs.objects.all()

        context = {
            'songs': songs
        }
        return render(request, self.template_name, context)

    def get_context_data(self, **kwargs):
        name = self.request.GET.get("name")
        song = Songs.objects.filter(name__contains=name)
        return {
            'name': name,
            'song': song
        }


class SongView(TemplateView):
    template_name = "song.html"

    def dispatch(self, request, *args, **kwargs):
        song_id = kwargs['id']
        song = Songs.objects.get(pk=song_id)
        context = {
            'song': song
        }
        return render(request, self.template_name, context)
