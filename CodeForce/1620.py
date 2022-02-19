def build_sides(test_case):
    for test_case in range(test_case_num):
        dimensions = [int(i) for i in input().split()]
        sides = [[] for i in range(4)]
        odd, even, side = 0, 0, 1
        for j in range(1, 5):
            points = [int(point) for point in input().split()]
            points_num = points.pop(0)
            if j % 2 != 0:
                for point_num in range(points_num):
                    point = [0, 0]
                    point[odd] = points[point_num]
                    sides[j-1].append(point)
                odd += 1
            else:
                for point_num in range(points_num):
                    point = [0, 0]
                    point[even], point[side] = points[point_num], dimensions[side]
                    sides[j-1].append(point)
                side -= 1
                even += 1
        return sides


def find_base(sides):
    max_base, max_diff, point_index, side_location = [0, 0], 0, 0, ''
    for i in range(len(sides)):
        if i <= 1:
            diff = sides[i][1][0] - sides[i][0][0]
            if diff > max_diff:
                max_diff = diff
                max_base[0], max_base[1] = sides[i][0][0], sides[i][-1][0]
                point_index = i
                side_location = 'horizontal'
        else:
            diff = sides[i][-1][1] - sides[i][0][1]
            if diff > max_diff:
                max_diff = diff
                max_base[0], max_base[1] = sides[i][0][1], sides[i][-1][1]
                point_index = i
                side_location = 'vertical'
    sides.pop(point_index)
    return max_base, sides, side_location


def find_vertex(points, side_location):
    if side_location == 'vertical':
        vertex = points[0][0][0]
        for i in points:
            for j in range(len(i)):
                if i[j][0] > vertex:
                    vertex = i[j][0]
    elif side_location == 'horizontal':
        vertex = points[0][0][1]
        for i in points:
            for j in range(len(i)):
                if i[j][1] > vertex:
                    vertex = i[j][1]
    return vertex


def calculate_area(base, height):
    base = abs(base[0] - base[1])
    return base*height

if __name__ == '__main__':
    result = []
    test_case_num = int(input())
    for i in range(test_case_num):
        sides = build_sides()
        max_base, sides, side_location = find_base(sides)
        vertex = find_vertex(sides, side_location)
        area = calculate_area(max_base, vertex)
        result.append(area)
    print(*result, sep='\n')
