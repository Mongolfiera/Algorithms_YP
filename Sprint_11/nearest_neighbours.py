# ID 81882626
import sys

def measure_distances(size, street_map):
    """A. Ближайший ноль.
    Поиск расстояния до ближайшего нуля (пустого участка) 
    для каждого из участков заданной последовательности (плана).
    """
    right = size * 2
    left = -size
    distances = [0] * size
    for location, site in enumerate(street_map):
        if site == 0:
            if location > 0:
                half_block = max((left + location)//2 + 1, 0)
                for backwards in range(half_block, location):
                    distances[backwards] = location - backwards
            left = location
        else:
            distances[location] = min(location - left, right - location)
    return distances

def main():
    size = int(input())
    line = sys.stdin.readline().rstrip()
    street_map = list(map(int, line.split()))
    print(*measure_distances(size, street_map))

if __name__ == '__main__':
    main()
