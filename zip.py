def zip(*args):
    iterators = [iter(iterable) for iterable in args]
    while True:
        result = []
        for iterable in iterators:
            try:
                element = next(iterable)
                result.append(element)
            except StopIteration:
                return
        yield tuple(result)


names = ['alireza', 'nima', 'hosein', 'mohammad']
college_field = ['electricity', 'electricity', 'law', 'architecture']
final_grades = [15, 17, 14, 18]

for ele in zip(names, college_field, final_grades):
    print(ele)