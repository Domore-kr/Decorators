from Decorator import decorator_marker


@decorator_marker('res.txt')
def flat_generator(multi_list):
    for item in multi_list:
        if isinstance(item, list):
            # если элемент списка оказывается списком то оборачиваем в этот же генератор
            # такой прием называется рекурсия
            for sub_item in flat_generator(item):
                yield sub_item
        else:
            yield item