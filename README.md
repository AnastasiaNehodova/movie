Репозиторий веб-сервиса на базе фреймворка Django для ввода отзыва о фильме с автоматическим присвоением рейтинга (от 1 до 10) и статуса комментария (положительный или отрицательный).
Веб-сервис оценивает комментарии с помощью модели машинного обучения movie/best_model.pkl, детали создания модели можно посмотреть в movie/rating_of_comments.ipynb, данные, на которых была обучена модель расположены в movie/data/.
movie/AnalyzerApp/ - файлы веб-сервиса, movie/analyzer/ - приложение. movie/manage.py - утилита командной строки Django для выполнения административных задач.
movie/report.pdf - отчет о проделанной работе.
Веб-сервис расположен по ссылке http://anastasianehodova.pythonanywhere.com/
