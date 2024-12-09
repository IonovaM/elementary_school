from django import get_version


def test_django_version():
    min_ver = '3.2.16'
    used_ver = get_version()
    assert used_ver >= min_ver, (
        f'В проекте должна быть установлена версия Django '
        f'не менее {min_ver}. У вас Django версии {used_ver}')


def test_static_dir(settings):
    try:
        staticfiles_dirs = settings.STATICFILES_DIRS
    except AttributeError:
        raise AssertionError(
            "Убедитесь, что в файле settings.py установлена переменная "
            "`STATICFILES_DIRS`."
        )
    assert isinstance(staticfiles_dirs, list), (
        "Убедитесь, что значение переменной `STATICFILES_DIRS` в файле "
        "settings.py — список."
    )

def test_apps_registered(settings):
    installed_apps = settings.INSTALLED_APPS
    assert isinstance(installed_apps, list), (
        "Убедитесь, что `INSTALLED_APPS` определён как список в settings.py."
    )
