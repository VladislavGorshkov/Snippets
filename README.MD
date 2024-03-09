
Инструкция по развертыванию проекта
python3 -m venv django_venv

source django_venv/bin/activate

pip install -r requirements.txt

python manage.py migrate

python manage.py runserver

Запуск ipython в контексте приложений django
python manage.py shell_plus --ipython