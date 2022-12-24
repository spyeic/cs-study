
def find_path(w, h):
    def find_each(x, y):
        if x > w or y > h:
            return 0
        if x == w and y == h:
            return 1
        return find_each(x + 1, y) + find_each(x, y + 1)

    return find_each(1, 1)
