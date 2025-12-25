class Unique(object):
    def __init__(self, items, **kwargs):
        self.ignore_case = kwargs.get('ignore_case', False)
        self.items = iter(items)
        self.used_elements = set()

    def __next__(self):
        while True:
            current = next(self.items)
            
            check_val = current
            if self.ignore_case and isinstance(current, str):
                check_val = current.lower()
            
            if check_val not in self.used_elements:
                self.used_elements.add(check_val)
                return current

    def __iter__(self):
        return self

if __name__ == '__main__':
    data = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
    print(list(Unique(data)))

    data = ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']
    print(list(Unique(data)))
    print(list(Unique(data, ignore_case=True)))