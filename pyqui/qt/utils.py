from . import qtc, qtg, qtw


class Rect:
    __slots__ = ['width', 'height']

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    def as_QRect(self):
        return qtc.QRect(self.width//2, self.height//2, self.width, self.height)
