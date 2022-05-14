from Decorator import decorator_marker

# @decorator_marker('res.txt')
class FlatIterator:

    def __init__(self, multi_list):
        self.multi_list = multi_list

    def __iter__(self):
        self.iterators_stack = [iter(self.multi_list)]  # стэк иетраторовр
        return self

    def __next__(self):
        while self.iterators_stack:  # пока в стеке есть итераторы
            try:
                current_element = next(self.iterators_stack[-1])
                #  пытаемся получить следующий элемент
            except StopIteration:
                self.iterators_stack.pop()
                continue
            if isinstance(current_element, list):
                # если следующий элемент оказался списком, то
                # добавляем его итератор в стек
                self.iterators_stack.append(iter(current_element))
            else:
                # если элемент не список, то просто возвращаем его
                return current_element
        raise StopIteration