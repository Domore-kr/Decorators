import datetime


def decorator_marker(filepath):
    def decorator(func):
        def new_func(*args, **kwargs):
            result = func(*args, **kwargs)
            with open(filepath, mode='a') as res:
                res.write(f'Дата и время вызова функции: {datetime.datetime.today()}\n'
                          f'Имя функции - {func.__name__}\n'
                          f'Аргументы: {args} {kwargs}\n'
                          f'Результат - {result}\n'
                          '***********************')

            return result

        return new_func

    return decorator
