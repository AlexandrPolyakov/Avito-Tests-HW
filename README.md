### issue-01

test_morse.py - доктесты для первого задания
- Открыть pycharm, собрать проект из всех текущих файлов
- Запустить 'Run Doctests in test_morse'
- Или python -m doctest -v -o NORMALIZE_WHITESPACE test_morse.py

### issue-02

- Открыть pycharm, собрать проект из всех текущих файлов
- Запустить 'Run pytest in test_morse_2'

### issue-03

- Открыть pycharm, собрать проект из всех текущих файлов
- Запустить 'Run Unittests in test_one_hot_encoder'

### issue-04

- Открыть pycharm, собрать проект из всех текущих файлов
- Запустить 'Run pytest in test_one_hot_encoder_2'

### issue-05

- Была незначительно изменена функция для удобства, а именно: контекстный менеджер заменен на вызов функции

- Открыть pycharm, собрать проект из всех текущих файлов
- Запустить 'Run pytest in test_what_is_year_now'
- Получить Tests passed: 6 of 6 tests, 100% покрытие
- Для проверки покрытия запускал две команды:
- coverage run -m pytest
- coverage html
- Отчет лежит в index.html