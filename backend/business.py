def get_data():
    with open('names.txt') as f:
        names = f.read().splitlines()
    return names
