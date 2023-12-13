asgiref==3.5.2
Django~=4.1.0
Pillow==9.2.0
sqlparse==0.4.2
git+https://github.com/python-social-auth/social-app-django.git@20fabcd7bd9a8a41910bc5c8ed1bd6ef2263b328
git+https://github.com/django-extensions/django-extensions.git@25a41d8a3ecb24c009c5f4cac6010a091a3c91c8
werkzeug==2.2.2
pyOpenSSL==22.0.0
requests==2.28.1
easy-thumbnails==2.8.3
django-debug-toolbar==3.6.0
redis==4.3.4

В данном пректе был использован Redis. Был добавлен Django Debug Toolbar. Было создано несколько приложений для изображения, профили пользователя, отдельно приложения для отслеживания действий.
Также добалены элементы JS по созданию закладок и отмечать изображения с других сайтов.
Команда для запуска Redis  docker run -it --rm --name redis -p 6379:6379 redis
Команда для запуска проекта с сертификатом python manage.py runserver_plus --cert-file cert.crt
Весь проект был написан блогодаря книге "Django 4 by Example" ссылка на его репозиторий - https://github.com/PacktPublishing/Django-4-by-example/tree/main
