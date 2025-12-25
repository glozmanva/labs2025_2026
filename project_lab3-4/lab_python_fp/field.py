def field(items, *args):
    assert len(args) > 0
    if len(args) == 1:
        for item in items:
            val = item.get(args[0])
            if val is not None:
                yield val
    else:
        for item in items:
            current_dict = {key: item.get(key) for key in args if item.get(key) is not None}
            if len(current_dict) > 0:
                yield current_dict


if __name__ == '__main__':
    goods = [
        {'title': 'Ковер', 'price': 2000, 'color': 'green'},
        {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'},
        {'title': 'Стелаж', 'price': None, 'color': 'white'} 
    ]
    print(list(field(goods, 'title')))
    print(list(field(goods, 'title', 'price')))