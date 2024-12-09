from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404

def school_home(request):
    return render(request, 'school/home.html', {
        'title': 'Начальная школа',
        'description': 'В начальной школе обучаются ученики с 1 по 3 классы. Каждый класс имеет какую-либо специализацию. За классом закрепляется классный руководитель и расписание занятий. Учителя выставляют оценки в журнал, а родители узнают о результатах обучения своих детей из дневников. Ученики могут просматривать свои дневники с выставленными домашними заданиями и полученными оценками.',
    })


school_data = {
    'teachers': {
        1: {
            'id': 1,
            'name': "Иван Сергеевич",
            'subjects': ["Математика", "Информатика"],
            'classes': [1, 2],
            'grades': [
                {'student_id': 1, 'subject': "Математика", 'grade': "4"},
                {'student_id': 2, 'subject': "Русский", 'grade': "5"}
            ],
            'homeworks': [
                {'class_id': 1, 'subject': "Математика", 'homework': "Изучить текст"},
                {'class_id': 2, 'subject': "Информатика", 'homework': "Подготовиться к контрольной"},
            ],
        },
        2: {
            'id': 2,
            'name': "Анна Петровна",
            'subjects': ["Русский язык", "Литература"],
            'classes': [2],
            'grades': [
                {'student_id': 2, 'subject': "Математика", 'grade': "5"},
                {'student_id': 1, 'subject': "Русский", 'grade': "4"}
            ],
            'homeworks': [
                {'class_id': 2, 'subject': "Русский язык", 'homework': "Изучить лекцию по русскому языку"}
            ],
        },
        3: {
            'id': 3,
            'name': "Сергей Владимирович",
            'subjects': ["Физика", "Химия"],
            'classes': [1],
            'grades': [
                {'student_id': 1, 'subject': "Физика", 'grade': "5"},
            ],
            'homeworks': [
                {'class_id': 1, 'subject': "Физика", 'homework': "Решить задачи по теме \"Механика\""}
            ],
        },
        4: {
            'id': 4,
            'name': "Екатерина Алексеевна",
            'subjects': ["История", "Обществознание"],
            'classes': [2],
            'grades': [
                {'student_id': 2, 'subject': "История", 'grade': "4"},
            ],
            'homeworks': [
                {'class_id': 2, 'subject': "История", 'homework': "Прочитать главу 3 учебника"}
            ],
        },
        5: {
            'id': 5,
            'name': "Дмитрий Николаевич",
            'subjects': ["География", "Экономика"],
            'classes': [1, 2],
            'grades': [
                {'student_id': 1, 'subject': "География", 'grade': "5"},
                {'student_id': 2, 'subject': "Экономика", 'grade': "3"},
            ],
            'homeworks': [
                {'class_id': 1, 'subject': "География", 'homework': "Нарисовать карту России"},
                {'class_id': 2, 'subject': "Экономика", 'homework': "Подготовить презентацию о спросе и предложении"}
            ],
        },
        6: {
            'id': 6,
            'name': "Ольга Юрьевна",
            'subjects': ["Биология", "Экология"],
            'classes': [1],
            'grades': [
                {'student_id': 1, 'subject': "Биология", 'grade': "4"},
            ],
            'homeworks': [
                {'class_id': 1, 'subject': "Биология", 'homework': "Подготовить гербарий"}
            ],
        },
        7: {
            'id': 7,
            'name': "Николай Андреевич",
            'subjects': ["Музыка", "ИЗО"],
            'classes': [1, 2],
            'grades': [
                {'student_id': 2, 'subject': "Музыка", 'grade': "5"},
            ],
            'homeworks': [
                {'class_id': 1, 'subject': "Музыка", 'homework': "Разучить песню \"Катюша\""}
            ],
        },
        8: {
            'id': 8,
            'name': "Татьяна Владимировна",
            'subjects': ["Физкультура", "Труд"],
            'classes': [2],
            'grades': [],
            'homeworks': [
                {'class_id': 2, 'subject': "Труд", 'homework': "Сделать поделку из бумаги"}
            ],
        },
        9: {
            'id': 9,
            'name': "Алексей Викторович",
            'subjects': ["Математика", "Информатика"],
            'classes': [3],
            'grades': [
                {'student_id': 4, 'subject': "Математика", 'grade': "5"},
                {'student_id': 5, 'subject': "Информатика", 'grade': "4"}
            ],
            'homeworks': [
                {'class_id': 3, 'subject': "Математика", 'homework': "Решить задачи на умножение"},
                {'class_id': 3, 'subject': "Информатика", 'homework': "Написать программу на Python"},
            ],
        },
        10: {
            'id': 10,
            'name': "Мария Павловна",
            'subjects': ["Русский язык", "Литература"],
            'classes': [3],
            'grades': [
                {'student_id': 4, 'subject': "Русский язык", 'grade': "4"},
                {'student_id': 5, 'subject': "Литература", 'grade': "5"}
            ],
            'homeworks': [
                {'class_id': 3, 'subject': "Русский язык", 'homework': "Изучить правило о мягком знаке"},
                {'class_id': 3, 'subject': "Литература", 'homework': "Прочитать сказку \"Морозко\""},
            ],
        },
        11: {
            'id': 11,
            'name': "Виктор Николаевич",
            'subjects': ["История", "Обществознание"],
            'classes': [3],
            'grades': [
                {'student_id': 4, 'subject': "История", 'grade': "3"},
                {'student_id': 5, 'subject': "Обществознание", 'grade': "5"}
            ],
            'homeworks': [
                {'class_id': 3, 'subject': "История", 'homework': "Выучить даты из главы 2"},
                {'class_id': 3, 'subject': "Обществознание", 'homework': "Написать эссе на тему \"Что такое семья\""},
            ],
        },
        12: {
            'id': 12,
            'name': "Наталья Григорьевна",
            'subjects': ["Химия", "Физика"],
            'classes': [3],
            'grades': [
                {'student_id': 4, 'subject': "Химия", 'grade': "4"},
                {'student_id': 5, 'subject': "Физика", 'grade': "5"}
            ],
            'homeworks': [
                {'class_id': 3, 'subject': "Химия", 'homework': "Подготовить отчет о проведенном эксперименте"},
                {'class_id': 3, 'subject': "Физика", 'homework': "Рассчитать скорость движения тела"},
            ],
        },
    },
    'classes': {
        1: {
            'id': 1,
            'name': "1-А",
            'students': [1, 2],
            'homeworks': [
                {'subject': "Математика", 'homework': "Изучить текст"},
                {'subject': "Математика", 'homework': "Решить задачи по математике"},
            ],
            'specialisation': "математическая"
        },
        2: {
            'id': 2,
            'name': "2-Б",
            'students': [3],
            'homeworks': [
                {'subject': "Информатика", 'homework': "Подготовиться к контрольной"},
                {'subject': "Русский язык", 'homework': "Изучить лекцию по русскому языку"},
            ],
            'specialisation': "гуманитарная"
        },
        3: {
            'id': 3,
            'name': "3-А",
            'students': [4, 5],
            'homeworks': [
                {'subject': "Математика", 'homework': "Решить задачи на умножение"},
                {'subject': "Информатика", 'homework': "Написать программу на Python"},
            ],
            'specialisation': "техническая"
        },
        4: {
            'id': 4,
            'name': "3-Б",
            'students': [6],
            'homeworks': [
                {'subject': "Русский язык", 'homework': "Изучить правило о мягком знаке"},
                {'subject': "Литература", 'homework': "Прочитать сказку \"Морозко\""},
            ],
            'specialisation': "гуманитарная"
        },
        5: {
            'id': 5,
            'name': "1-Б",
            'students': [7, 8],
            'homeworks': [
                {'subject': "Математика", 'homework': "Изучить таблицу умножения"},
                {'subject': "Природоведение", 'homework': "Подготовить проект о животных"},
            ],
            'specialisation': "природоведение"
        },
        6: {
            'id': 6,
            'name': "2-А",
            'students': [9, 10],
            'homeworks': [
                {'subject': "География", 'homework': "Выучить названия материков"},
                {'subject': "Музыка", 'homework': "Разучить песню \"Соловей\""},
            ],
            'specialisation': "музыкальная"
        },
        7: {
            'id': 7,
            'name': "3-В",
            'students': [11, 12],
            'homeworks': [
                {'subject': "Математика", 'homework': "Повторить правила деления"},
                {'subject': "История", 'homework': "Прочитать про древнюю Русь"},
            ],
            'specialisation': "историческая"
        },
        8: {
            'id': 8,
            'name': "1-В",
            'students': [13],
            'homeworks': [
                {'subject': "Русский язык", 'homework': "Выучить алфавит"},
                {'subject': "ИЗО", 'homework': "Нарисовать пейзаж зимы"},
            ],
            'specialisation': "искусство"
        },
    },
    'students': {
        1: {
            'id': 1,
            'name': "Иванов Иван",
            'class_id': 1,
            'homeworks': [
                {'subject': "Математика", 'homework': "Изучить текст"},
                {'subject': "Математика", 'homework': "Решить задачи по математике"},
            ],
            'grades': [
                {'subject': "Математика", 'grade': "4"},
                {'subject': "Русский", 'grade': "5"},
            ],
            'parent_id': 1,
        },
        2: {
            'id': 2,
            'name': "Петров Петр",
            'class_id': 2,
            'homeworks': [
                {'subject': "Информатика", 'homework': "Подготовиться к контрольной"},
                {'subject': "Русский язык", 'homework': "Изучить лекцию по русскому языку"},
            ],
            'grades': [
                {'subject': "Математика", 'grade': "5"},
                {'subject': "Русский", 'grade': "4"},
            ],
            'parent_id': 2,
        },
        3: {
            'id': 3,
            'name': "Иван Петров",
            'class_id': 2,
            'homeworks': [],
            'grades': [],
            'parent_id': None,
        },
        4: {
            'id': 4,
            'name': "Смирнов Михаил",
            'class_id': 3,
            'homeworks': [
                {'subject': "Математика", 'homework': "Решить задачи на умножение"},
                {'subject': "Информатика", 'homework': "Написать программу на Python"},
            ],
            'grades': [
                {'subject': "Математика", 'grade': "4"},
                {'subject': "Информатика", 'grade': "5"},
            ],
            'parent_id': 3,
        },
        5: {
            'id': 5,
            'name': "Кузнецова Анна",
            'class_id': 3,
            'homeworks': [
                {'subject': "Математика", 'homework': "Решить задачи на умножение"},
            ],
            'grades': [
                {'subject': "Математика", 'grade': "5"},
            ],
            'parent_id': 4,
        },
        6: {
            'id': 6,
            'name': "Соколова Ольга",
            'class_id': 4,
            'homeworks': [
                {'subject': "Русский язык", 'homework': "Изучить правило о мягком знаке"},
                {'subject': "Литература", 'homework': "Прочитать сказку \"Морозко\""},
            ],
            'grades': [
                {'subject': "Русский язык", 'grade': "4"},
            ],
            'parent_id': 5,
        },
        7: {
            'id': 7,
            'name': "Васильев Артем",
            'class_id': 1,
            'homeworks': [
                {'subject': "Математика", 'homework': "Изучить таблицу умножения"},
            ],
            'grades': [
                {'subject': "Математика", 'grade': "3"},
            ],
            'parent_id': 6,
        },
        8: {
            'id': 8,
            'name': "Григорьева Елена",
            'class_id': 5,
            'homeworks': [
                {'subject': "Природоведение", 'homework': "Подготовить проект о животных"},
            ],
            'grades': [],
            'parent_id': 7,
        },
        9: {
            'id': 9,
            'name': "Морозов Дмитрий",
            'class_id': 6,
            'homeworks': [
                {'subject': "География", 'homework': "Выучить названия материков"},
            ],
            'grades': [
                {'subject': "География", 'grade': "5"},
            ],
            'parent_id': 8,
        },
        10: {
            'id': 10,
            'name': "Лебедева Татьяна",
            'class_id': 6,
            'homeworks': [
                {'subject': "Музыка", 'homework': "Разучить песню \"Соловей\""},
            ],
            'grades': [
                {'subject': "Музыка", 'grade': "4"},
            ],
            'parent_id': 9,
        },
        11: {
            'id': 11,
            'name': "Романов Александр",
            'class_id': 7,
            'homeworks': [
                {'subject': "История", 'homework': "Прочитать про древнюю Русь"},
            ],
            'grades': [],
            'parent_id': 10,
        },
        12: {
            'id': 12,
            'name': "Зайцева Мария",
            'class_id': 7,
            'homeworks': [
                {'subject': "Математика", 'homework': "Повторить правила деления"},
            ],
            'grades': [
                {'subject': "Математика", 'grade': "5"},
            ],
            'parent_id': 11,
        },
    },
    'parents': {
        1: {
            'id': 1,
            'name': "Иван Иванович",
            'students': [1],
        },
        2: {
            'id': 2,
            'name': "Петр Петрович",
            'students': [2],
        },
    },
}


def class_list(request):
    template = 'school/class_list.html'
    classes = sorted(school_data['classes'].values(), key=lambda x: x['name'])
    context = {
        'classes': classes
    }
    return render(request, template, context)


def teacher_list(request):
    template = 'school/teacher_list.html'
    teachers = school_data['teachers'].values()
    context = {
        'teachers': teachers
    }
    return render(request, template, context)


def get_students_list(teacher):
    students_list = []
    for class_id in teacher['classes']:
        class_obj = school_data['classes'].get(class_id)
        if class_obj:
            for student_id in class_obj['students']:
                student = school_data['students'].get(student_id)
                if student:
                    students_list.append(student['name'])
    return students_list


def teacher_dashboard(request, teacher_id):
    template = 'school/teacher_dashboard.html'
    teacher = school_data['teachers'].get(teacher_id)
    if not teacher:
        return HttpResponse("Учитель не найден", status=404)

    homeworks = teacher.get('homeworks', [])
    grades = teacher.get('grades', [])
    students = get_students_list(teacher)

    context = {
        'teacher': teacher,
        'homeworks': homeworks,
        'grades': grades,
        'students': students,
    }
    return render(request, template, context)


def parent_dashboard(request, parent_id):
    template = 'school/parent_dashboard.html'
    parent = school_data['parents'].get(parent_id)
    if parent is None:
        raise Http404("Студент не найден. Пожалуйста, проверьте, что ID корректен и студент существует.")

    students = [school_data['students'][sid] for sid in parent['students']]

    if not students:
        students_details = {
            'name': 'Нет детей',
            'homeworks': [],
            'grades': [],
        }
    else:
        students_details = []
        for student in students:
            homeworks = student['homeworks']
            grades = student['grades']

            students_details.append({
                'name': student['name'],
                'homeworks': homeworks,
                'grades': grades,
            })

    context = {
        'parent': parent,
        'students_details': students_details,
    }
    return render(request, template, context)


students_by_id = {student['id']: student for student in school_data['students'].values()}


def student_dashboard(request, student_id):
    template = 'school/student_dashboard.html'
    if not isinstance(student_id, int):
        raise Http404(f'Некорректный параметр student_id: {student_id}')
    student = students_by_id.get(student_id)
    if student is None:
        raise Http404(f'Студент с student_id {student_id} не найден')

    context = {
        'student': student,
        'homeworks': student.get('homeworks', []),
        'grades': student.get('grades', []),
    }
    return render(request, template, context)



# from django.shortcuts import render, get_object_or_404
# from django.contrib.auth.decorators import login_required
# from .models import Class, Teacher
# from grades.models import Homework, Grade
#
# @login_required
# def teacher_dashboard(request):
#     # Проверяем, что пользователь учитель
#     if request.user.role != 'teacher':
#         return render(request, '403.html')
#
#     teacher = get_object_or_404(Teacher, user=request.user)
#     classes = teacher.classes.all()
#     return render(request, 'school/teacher_dashboard.html', {'classes': classes})
#
# @login_required
# def add_homework(request, class_id):
#     # Проверяем, что пользователь учитель
#     if request.user.role != 'teacher':
#         return render(request, '403.html')
#
#     school_class = get_object_or_404(Class, id=class_id)
#     if request.method == 'POST':
#         subject = request.POST['subject']
#         description = request.POST['description']
#         due_date = request.POST['due_date']
#         Homework.objects.create(
#             school_class=school_class,
#             subject=subject,
#             description=description,
#             due_date=due_date
#         )
#         return render(request, 'school/homework_success.html', {'class': school_class})
#
#     return render(request, 'school/add_homework.html', {'class': school_class})
#
# @login_required
# def student_dashboard(request):
#     # Проверяем, что пользователь ученик
#     if request.user.role != 'student':
#         return render(request, '403.html')
#
#     student = request.user.student
#     grades = student.grades.all()
#     homework = student.school_class.homework.all()
#     return render(request, 'school/student_dashboard.html', {
#         'grades': grades,
#         'homework': homework,
#     })
#
# #@login_required
# def parent_dashboard(request):
#     # Проверяем, что пользователь родитель
#     if request.user.role != 'parent':
#         return render(request, '403.html')
#
#     children = request.user.parent.children.all()
#     return render(request, 'school/parent_dashboard.html', {'children': children})
#
#
