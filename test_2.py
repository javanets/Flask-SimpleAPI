from requests import get, post

# Файл к задаче "Тестирование POST-запроса

# Напишите файл тестирования корректного запроса
# и нескольких некорректных (не менее трех).
# В файле должны присутствовать комментарии,
# в чем именно заключается некорректность запроса.

# Каждый тест должен иметь такой формат:

print(post(..., json={...}).json())

# Добавьте запрос на получение всех работ, чтобы убедиться, что работа добавлена:
print(get(...).json())
