def fruits(tuple_of_fruits):
    result = {}
    for fr in tuple_of_fruits:
        if all([fr['shape'] == 'sphere', 300 <= fr['mass'] <= 600, 100 <= fr['volume'] <= 500]):
            try:
                result[fr['name']] += 1
            except KeyError:
                result[fr['name']] = 1
    return result

if __name__ == '__main__':
    tuple_of_fruits = (
    {'name':'apple', 'shape': 'sphere', 'mass': 350, 'volume': 120},
    {'name':'mango', 'shape': 'square', 'mass': 150, 'volume': 120}, 
    {'name':'lemon', 'shape': 'sphere', 'mass': 300, 'volume': 100},
    {'name':'apple', 'shape': 'sphere', 'mass': 500, 'volume': 250})
    print(fruits(tuple_of_fruits))
    
