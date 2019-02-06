class Color:
    RED = '31'
    WHITE = '47'

    def __init__(self, color, back):
        self.color = color
        self.back = back

    def __enter__(self):
            print('\033[1;{}m\033[1;{}m'.format(self.color, self.back))

    def __exit__(self, exc_type, exc_value, tb):
            print('\033[00m')
