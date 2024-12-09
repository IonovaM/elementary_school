import pytest
from django.urls import reverse

@pytest.mark.django_db
@pytest.mark.parametrize("url_name, kwargs, expected_status", [
    ("school_home", None, 200),  # Главная страница школы
    ("class_list", None, 200),  # Список классов
    ("teacher_list", None, 200),  # Список учителей
    ("teacher_dashboard", {"teacher_id": 1}, 200),  # Панель учителя
    ("student_dashboard", {"student_id": 1}, 200),  # Панель ученика
    ("parent_dashboard", {"parent_id": 1}, 200),  # Панель родителя
])
def test_url(client, url_name, kwargs, expected_status):
    """
    Проверяет, что URL-адрес возвращает ожидаемый HTTP-статус.
    """
    if kwargs:
        url = reverse(url_name, kwargs=kwargs)
    else:
        url = reverse(url_name)

    response = client.get(url)
    assert response.status_code == expected_status
