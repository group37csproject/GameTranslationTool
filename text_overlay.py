from PySide6 import QtWidgets, QtCore, QtGui

class TextOverlay(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint | QtCore.Qt.FramelessWindowHint | QtCore.Qt.Tool | QtCore.Qt.WindowTransparentForInput)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.text = ""
        self.font = QtGui.QFont("Arial", 24)
        self.text_color = QtGui.QColor(255, 255, 255)
        self.bg_color = QtGui.QColor(0, 0, 0, 128)

    def set_text(self, text):
        self.text = text
        self.update()
        
    def set_text_color(self, color: QtGui.QColor):
        self.text_color = color
        self.update()

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        painter.setRenderHint(QtGui.QPainter.Antialiasing)

        # Draw background
        painter.setBrush(self.bg_color)
        painter.setPen(QtCore.Qt.NoPen)
        painter.drawRect(self.rect())

        # Draw text
        painter.setFont(self.font)
        painter.setPen(self.text_color)
        painter.drawText(self.rect(), QtCore.Qt.AlignCenter, self.text)