from django.http import HttpResponseNotFound, JsonResponse
from rest_framework.views import APIView

from adm.models import Profile, Mark, Project


def get_student(student_id):
    try:
        student = Profile.objects.get(id=student_id)
    except Profile.DoesNotExist:
        return HttpResponseNotFound("Такого пользователя нет!")
    return student


def get_mark(mark_id):
    try:
        mark = Mark.objects.get(id=mark_id)
    except Mark.DoesNotExist:
        return HttpResponseNotFound("Такой оценки нет!")
    return mark


def get_project(project_id):
    try:
        project = Project.objects.get(id=project_id)
    except Project.DoesNotExist:
        return HttpResponseNotFound("Такой оценки нет!")
    return project


class MarkView(APIView):
    model = Mark

    def post(self, request, mark, student_id):
        student = get_student(student_id)
        mark = Mark(mentor=request.user, student=student, mark=mark)
        try:
            mark.save()
            return JsonResponse({'data': f'Успешно поставили оценку пользователю {student.username}'}, status=200)
        except Exception as e:
            return JsonResponse({'data': f'Не удалось поставить оценку :( {e}'}, status=400)

    def delete(self, request, mark_id):
        if get_mark(mark_id):
            self.model.filter(id=mark_id).delete()
            return JsonResponse({'data': 'Оценка успешно удалена!'}, status=200)


class AddUserToProjectList(APIView):
    model = Project

    def post(self, request, user_id, project_id):
        project = get_project(project_id)
        user = get_student(user_id)
        if user.user.username not in project.users:
            project.users = project.users.append(user.user.username)
            project.save()
            return JsonResponse({'data': 'Успешно добавили в список заинтересованных лиц!'}, status=200)
        return JsonResponse({'data': 'Этот пользователь уже в списке заинтересованных лиц!'}, status=200)


class ApproveList(APIView):
    model = Project

    def get(self, request):
        project = self.model.filter(mentor=request.user).only('title', 'waiting_approve')
        return JsonResponse({'data': project}, status=200)

    def post(self, request, project_id, student_id):
        student = get_student(student_id)
        project = get_project(project_id)
        if student.user.username not in project.waiting_approve:
            return JsonResponse({'data': 'Этого пользователя нет в списке ожидания!'}, status=200)
        project.waiting_approve = project.waiting_approve.remove(student.user.username)
        project.users = project.users.append(student.user.username)
        try:
            project.save()
            return JsonResponse({'data': 'Успешно заапрувили участника проекта!'}, status=200)
        except Exception as e:
            return JsonResponse({'data': f'Не получилось заапрувить участие :( {e}'}, status=400)