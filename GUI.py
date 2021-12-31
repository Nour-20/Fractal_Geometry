
import sys
import os
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import (QApplication,
                             QMainWindow,
                             QTabWidget,
                             QVBoxLayout,
                             QHBoxLayout,
                             QPushButton,
                             QLabel,
                             QComboBox,
                             QLineEdit,
                             QSpinBox,
                             QMessageBox,
                             QWidget
                             )

# Import fractal algorithm
from Mandelbrot import evaluateMandelbrot
from Julia_fractal import evaluateJulia
from Tree_Of_Life import evaluateTree1
from Tree_Of_Life_v2 import evaluateTree2
from Koch_snowflake import evaluateKoch
from Sierp_Triangle import evaluateSierp


class Fractal_GUI(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Fractal Geometry")
        self.setFixedSize(720, 480)

        self.createTab()

    def createTab(self):
        self.tabs = QTabWidget()
        self.tabs.setTabPosition(QTabWidget.West)
        self.tabs.setMovable(False)

        # QWidget-Tab screen
        self.tab1 = QWidget()  # Mandelbrot
        self.tab2 = QWidget()  # Julia
        self.tab3 = QWidget()  # Tree
        self.tab4 = QWidget()  # Koch
        self.tab5 = QWidget()  # sierp

        temp = {
            "Mandelbrot": self.tab1,
            "Julia": self.tab2,
            "Tree of life": self.tab3,
            "Koch snowflake": self.tab4,
            "Sierpinski": self.tab5
        }

        for key, value in temp.items():
            self.tabs.addTab(value, key)

        self.setCentralWidget(self.tabs)

        # Create tabs contents
        self.createMandelbrotTab()
        self.createJuliaTab()
        self.createTreeTab()
        self.createKochTab()
        self.createSierpTab()

    def createMandelbrotTab(self):
        self.tab1.layoutV = QVBoxLayout()
        self.tab1.labelpic = QLabel()  # Mandelbrot pics
        self.tab1.labelpic.setAlignment(Qt.AlignCenter)

        # Horizontal Layout
        self.tab1.layoutH = QHBoxLayout()
        self.tab1.labeltext = QLabel("Dimension")
        self.tab1.button = QPushButton("Run")

        self.tab1.dimension = QLineEdit()
        self.tab1.dimension.setFrame(True)
        self.tab1.dimension.setPlaceholderText("Enter dimension")

        self.tab1.layoutH.addWidget(self.tab1.labeltext)
        self.tab1.layoutH.addWidget(self.tab1.dimension)
        self.tab1.layoutH.addSpacing(300)
        self.tab1.layoutH.addWidget(self.tab1.button)

        # Vertical Layout
        self.tab1.layoutV.addWidget(self.tab1.labelpic)
        self.tab1.layoutV.addLayout(self.tab1.layoutH)

        # Set vertical layout as principal layout
        self.tab1.setLayout(self.tab1.layoutV)

    def createJuliaTab(self):
        self.tab2.layoutV = QVBoxLayout()
        self.tab2.labelpic = QLabel()  # Julia pics
        self.tab2.labelpic.setAlignment(Qt.AlignCenter)

        # Horizontal Layout
        self.tab2.layoutH = QHBoxLayout()
        self.tab2.labeltext = QLabel("c")
        self.tab2.button = QPushButton("Run")

        self.tab2.ComboBox = QComboBox()
        self.tab2.ComboBox.addItems(["−0.4 + 0.6i", "0.285 + 0i", "0.285 + 0.01i", "0.45 + 0.1428i", "−0.70176 − 0.3842i",
                                    " −0.835 − 0.2321i", "−0.8 + 0.156i", " −0.7269 + 0.1889i", "−0.8i", "-0.74543+0.11301i", "-0.75+0.11i", "-0.1+0.651i"])

        self.tab2.layoutH.addWidget(self.tab2.labeltext)
        self.tab2.layoutH.addWidget(self.tab2.ComboBox)
        self.tab2.layoutH.addSpacing(1000)
        self.tab2.layoutH.addWidget(self.tab2.button)

        # Vertical Layout
        self.tab2.layoutV.addWidget(self.tab2.labelpic)
        self.tab2.layoutV.addLayout(self.tab2.layoutH)

        # Set vertical layout as principal layout
        self.tab2.setLayout(self.tab2.layoutV)

    def createTreeTab(self):
        self.tab3.layoutV = QVBoxLayout()
        # Tree of life pics
        self.tab3.labelpic1 = QLabel()
        self.tab3.labelpic1.setAlignment(Qt.AlignCenter)
        self.tab3.labelpic2 = QLabel()
        self.tab3.labelpic2.setAlignment(Qt.AlignCenter)
        self.tab3.layoutHTop = QHBoxLayout()
        self.tab3.layoutHTop.addWidget(self.tab3.labelpic1)
        self.tab3.layoutHTop.addWidget(self.tab3.labelpic2)

        # Horizontal Layout
        self.tab3.layoutH = QHBoxLayout()
        self.tab3.labeltext = QLabel("Level")
        self.tab3.button = QPushButton("Run")

        self.tab3.SpinBox = QSpinBox()
        self.tab3.SpinBox.setMaximum(20)
        self.tab3.SpinBox.setMinimum(1)

        self.tab3.layoutH.addWidget(self.tab3.labeltext)
        self.tab3.layoutH.addWidget(self.tab3.SpinBox)
        self.tab3.layoutH.addSpacing(1000)
        self.tab3.layoutH.addWidget(self.tab3.button)

        # Vertical Layout
        self.tab3.layoutV.addLayout(self.tab3.layoutHTop)
        self.tab3.layoutV.addLayout(self.tab3.layoutH)

        # Set vertical layout as principal layout
        self.tab3.setLayout(self.tab3.layoutV)

    def createKochTab(self):
        self.tab4.layoutV = QVBoxLayout()
        self.tab4.labelpic = QLabel()  # Snowflake pics
        self.tab4.labelpic.setAlignment(Qt.AlignCenter)

        # Horizontal Layout
        self.tab4.layoutH = QHBoxLayout()
        self.tab4.labeltext = QLabel("Level")
        self.tab4.button = QPushButton("Run")

        self.tab4.SpinBox = QSpinBox()
        self.tab4.SpinBox.setMaximum(6)
        self.tab4.SpinBox.setMinimum(1)

        self.tab4.layoutH.addWidget(self.tab4.labeltext)
        self.tab4.layoutH.addWidget(self.tab4.SpinBox)
        self.tab4.layoutH.addSpacing(1000)
        self.tab4.layoutH.addWidget(self.tab4.button)

        # Vertical Layout
        self.tab4.layoutV.addWidget(self.tab4.labelpic)
        self.tab4.layoutV.addLayout(self.tab4.layoutH)

        # Set vertical layout as principal layout
        self.tab4.setLayout(self.tab4.layoutV)

    def createSierpTab(self):
        self.tab5.layoutV = QVBoxLayout()
        self.tab5.labelpic = QLabel()  # Sierpinski pics
        self.tab1.labelpic.setAlignment(Qt.AlignCenter)

        # Horizontal Layout
        self.tab5.layoutH = QHBoxLayout()
        self.tab5.labeltext = QLabel("Level")
        self.tab5.button = QPushButton("Run")

        self.tab5.SpinBox = QSpinBox()
        self.tab5.SpinBox.setMaximum(10)
        self.tab5.SpinBox.setMinimum(1)

        self.tab5.layoutH.addWidget(self.tab5.labeltext)
        self.tab5.layoutH.addWidget(self.tab5.SpinBox)
        self.tab5.layoutH.addSpacing(1000)
        self.tab5.layoutH.addWidget(self.tab5.button)

        # Vertical Layout
        self.tab5.layoutV.addWidget(self.tab5.labelpic)
        self.tab5.layoutV.addLayout(self.tab5.layoutH)

        # Set vertical layout as principal layout
        self.tab5.setLayout(self.tab5.layoutV)


class Fractal_Control:

    def __init__(self, GUI, Model):
        self._evaluate = Model
        self._view = GUI
        # Connect signals and slots
        self._connectSignals()

    def _draw(self, filename, labelpic):
        self._path = os.path.dirname(os.path.realpath(__file__))
        self._pixmap = QPixmap(self._path + filename)
        self._pixmap = self._pixmap.scaled(720, 480)
        labelpic.setPixmap(self._pixmap)

    def _connectSignals(self):
        self._view.tab1.button.clicked.connect(self.exec_mandelbrot)
        self._view.tab2.button.clicked.connect(self.exec_Julia)
        self._view.tab3.button.clicked.connect(self.exec_tree)
        self._view.tab4.button.clicked.connect(self.exec_koch)
        self._view.tab5.button.clicked.connect(self.exec_sierp)

    def exec_mandelbrot(self):
        dimension = self._view.tab1.dimension.text()
        try:
            dimension = float(dimension)
        except:
            msgBox = QMessageBox()
            if (dimension.strip() == ''):
                msgBox.setText("Dimension is empty!")
            else:
                msgBox.setText(
                    "Dimension should be a number and not a string!")
            msgBox.exec()
            return None

        if dimension < 0:
            msgBox = QMessageBox()
            msgBox.setText("Dimension should be positive number!")
            msgBox.exec()
            return None

        self._evaluate[0](dimension)

        self._draw('/mandelbrot.png', self._view.tab1.labelpic)

    def exec_Julia(self):
        temp_dict = {
            0: (-0.4, 0.6),
            1: (0.285, 0),
            2: (0.285, 0.01),
            3: (0.45, 0.1428),
            4: (-0.70176, -0.3842),
            5: (-0.835, -0.2321),
            6: (-0.8, 0.156),
            7: (-0.7269, 0.1889),
            8: (0, -0.8),
            9: (-0.74543, 0.11301),
            10: (-0.75, 0.11),
            11: (-0.1, 0.651)
        }
        index = self._view.tab2.ComboBox.currentIndex()
        self._evaluate[1](temp_dict[index][0], temp_dict[index][1])

        self._draw('/julia.png', self._view.tab2.labelpic)

    def exec_tree(self):
        level = self._view.tab3.SpinBox.value()
        self._evaluate[2](level)
        if level > 10:
            level = 10
        self._evaluate[3](level)

        self._draw('/tree1.png', self._view.tab3.labelpic1)
        self._draw('/tree2.png', self._view.tab3.labelpic2)

    def exec_koch(self):
        level = self._view.tab4.SpinBox.value()
        self._evaluate[4](level)

        self._draw('/koch.png', self._view.tab4.labelpic)

    def exec_sierp(self):
        level = self._view.tab5.SpinBox.value()
        self._evaluate[5](level)

        self._draw('/sierp.png', self._view.tab5.labelpic)


def main():
    # Create an instance of QApplication
    app = QApplication(sys.argv)
    # Show the Fractal_GUI
    view = Fractal_GUI()
    view.show()
    # Create instances of the model and the controller
    model = (evaluateMandelbrot, evaluateJulia, evaluateTree1,
             evaluateTree2, evaluateKoch, evaluateSierp)
    controller = Fractal_Control(view, model)
    # execute main loop
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
