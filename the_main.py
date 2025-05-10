from PyQt6.QtWidgets import QApplication, QMainWindow
from the_gui import Ui_ProjectWindow
import sys

class MainWindow(QMainWindow, Ui_ProjectWindow):
    """Main window of the voting app."""
    def __init__(self):
        super().__init__()
        self.setupUi(self)

def main():
    """Starts the app and shows the window."""
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()