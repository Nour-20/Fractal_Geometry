
from msilib import sequence
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
from Lyapunov import evaluateLyapunov
from Tree_Of_Life import evaluateTree1
from Tree_Of_Life_v2 import evaluateTree2
from Koch_snowflake import evaluateKoch
from Sierp_Triangle import evaluateSierp
from Sierp_Carpet import evaluateSierp_Carp
from T_Square import evaluateTSqu


class Fractal_GUI(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Fractal Geometry")
        self.setFixedSize(1280, 860)

        self.createTab()

    def createTab(self):
        self.tabs = QTabWidget()
        self.tabs.setTabPosition(QTabWidget.West)
        self.tabs.setMovable(False)

        # QWidget-Tab screen
        self.tab1 = QWidget()  # Mandelbrot
        self.tab2 = QWidget()  # Julia
        self.tab3 = QWidget()  # Lyapunov
        self.tab4 = QWidget()  # Tree
        self.tab5 = QWidget()  # Koch
        self.tab6 = QWidget()  # sierp
        self.tab7 = QWidget()  # sierp_Carpet
        self.tab8 = QWidget()  # T-square

        temp = {
            "Mandelbrot": self.tab1,
            "Julia": self.tab2,
            "Lyapunov": self.tab3,
            "Tree of life": self.tab4,
            "Koch snowflake": self.tab5,
            "Sierpinski Triangle": self.tab6,
            "Sierpinski Carpet": self.tab7,
            "T-square": self.tab8
        }

        for key, value in temp.items():
            self.tabs.addTab(value, key)

        self.setCentralWidget(self.tabs)

        # Create tabs contents
        self.createMandelbrotTab()
        self.createJuliaTab()
        self.createLyapunovTab()
        self.createTreeTab()
        self.createKochTab()
        self.createSierpTab()
        self.createSierpCarpetTab()
        self.createTsquareTab()

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

    def createLyapunovTab(self):
        self.tab3.layoutV = QVBoxLayout()
        self.tab3.labelpic = QLabel()  # Lyapunov pics
        self.tab3.labelpic.setAlignment(Qt.AlignCenter)

        # Horizontal Layout
        self.tab3.layoutH = QHBoxLayout()
        self.tab3.labeltext = QLabel("Sequence")
        self.tab3.button = QPushButton("Run")

        self.tab3.sequence = QLineEdit()
        self.tab3.sequence.setFrame(True)
        self.tab3.sequence.setPlaceholderText("Enter Sequence, e.g., \"AB\"")

        self.tab3.layoutH.addWidget(self.tab3.labeltext)
        self.tab3.layoutH.addWidget(self.tab3.sequence)
        self.tab3.layoutH.addSpacing(300)
        self.tab3.layoutH.addWidget(self.tab3.button)

        # Vertical Layout
        self.tab3.layoutV.addWidget(self.tab3.labelpic)
        self.tab3.layoutV.addLayout(self.tab3.layoutH)

        # Set vertical layout as principal layout
        self.tab3.setLayout(self.tab3.layoutV)

    def createTreeTab(self):
        self.tab4.layoutV = QVBoxLayout()
        # Tree of life pics
        self.tab4.labelpic1 = QLabel()
        self.tab4.labelpic1.setAlignment(Qt.AlignCenter)
        self.tab4.labelpic2 = QLabel()
        self.tab4.labelpic2.setAlignment(Qt.AlignCenter)
        self.tab4.layoutHTop = QHBoxLayout()
        self.tab4.layoutHTop.addWidget(self.tab4.labelpic1)
        self.tab4.layoutHTop.addWidget(self.tab4.labelpic2)

        # Horizontal Layout
        self.tab4.layoutH = QHBoxLayout()
        self.tab4.labeltext = QLabel("Level")
        self.tab4.button = QPushButton("Run")

        self.tab4.SpinBox = QSpinBox()
        self.tab4.SpinBox.setMaximum(20)
        self.tab4.SpinBox.setMinimum(1)

        self.tab4.layoutH.addWidget(self.tab4.labeltext)
        self.tab4.layoutH.addWidget(self.tab4.SpinBox)
        self.tab4.layoutH.addSpacing(1000)
        self.tab4.layoutH.addWidget(self.tab4.button)

        # Vertical Layout
        self.tab4.layoutV.addLayout(self.tab4.layoutHTop)
        self.tab4.layoutV.addLayout(self.tab4.layoutH)

        # Set vertical layout as principal layout
        self.tab4.setLayout(self.tab4.layoutV)

    def createKochTab(self):
        self.tab5.layoutV = QVBoxLayout()
        self.tab5.labelpic = QLabel()  # Snowflake pics
        self.tab5.labelpic.setAlignment(Qt.AlignCenter)

        # Horizontal Layout
        self.tab5.layoutH = QHBoxLayout()
        self.tab5.labeltext = QLabel("Level")
        self.tab5.button = QPushButton("Run")

        self.tab5.SpinBox = QSpinBox()
        self.tab5.SpinBox.setMaximum(6)
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

    def createSierpTab(self):
        self.tab6.layoutV = QVBoxLayout()
        self.tab6.labelpic = QLabel()  # Sierpinski pics
        self.tab6.labelpic.setAlignment(Qt.AlignCenter)

        # Horizontal Layout
        self.tab6.layoutH = QHBoxLayout()
        self.tab6.labeltext = QLabel("Level")
        self.tab6.button = QPushButton("Run")

        self.tab6.SpinBox = QSpinBox()
        self.tab6.SpinBox.setMaximum(10)
        self.tab6.SpinBox.setMinimum(1)

        self.tab6.layoutH.addWidget(self.tab6.labeltext)
        self.tab6.layoutH.addWidget(self.tab6.SpinBox)
        self.tab6.layoutH.addSpacing(1000)
        self.tab6.layoutH.addWidget(self.tab6.button)

        # Vertical Layout
        self.tab6.layoutV.addWidget(self.tab6.labelpic)
        self.tab6.layoutV.addLayout(self.tab6.layoutH)

        # Set vertical layout as principal layout
        self.tab6.setLayout(self.tab6.layoutV)

    def createSierpCarpetTab(self):
        self.tab7.layoutV = QVBoxLayout()
        self.tab7.labelpic = QLabel()  #pics
        self.tab7.labelpic.setAlignment(Qt.AlignCenter)

        # Horizontal Layout
        self.tab7.layoutH = QHBoxLayout()
        self.tab7.labeltext = QLabel("Level")
        self.tab7.button = QPushButton("Run")

        self.tab7.SpinBox = QSpinBox()
        self.tab7.SpinBox.setMaximum(5)
        self.tab7.SpinBox.setMinimum(1)

        self.tab7.layoutH.addWidget(self.tab7.labeltext)
        self.tab7.layoutH.addWidget(self.tab7.SpinBox)
        self.tab7.layoutH.addSpacing(1000)
        self.tab7.layoutH.addWidget(self.tab7.button)

        # Vertical Layout
        self.tab7.layoutV.addWidget(self.tab7.labelpic)
        self.tab7.layoutV.addLayout(self.tab7.layoutH)

        # Set vertical layout as principal layout
        self.tab7.setLayout(self.tab7.layoutV)

    def createTsquareTab(self):
        self.tab8.layoutV = QVBoxLayout()
        self.tab8.labelpic = QLabel()  #pics
        self.tab8.labelpic.setAlignment(Qt.AlignCenter)

        # Horizontal Layout
        self.tab8.layoutH = QHBoxLayout()
        self.tab8.labeltext = QLabel("Level")
        self.tab8.button = QPushButton("Run")

        self.tab8.SpinBox = QSpinBox()
        self.tab8.SpinBox.setMaximum(6)
        self.tab8.SpinBox.setMinimum(1)

        self.tab8.layoutH.addWidget(self.tab8.labeltext)
        self.tab8.layoutH.addWidget(self.tab8.SpinBox)
        self.tab8.layoutH.addSpacing(1000)
        self.tab8.layoutH.addWidget(self.tab8.button)

        # Vertical Layout
        self.tab8.layoutV.addWidget(self.tab8.labelpic)
        self.tab8.layoutV.addLayout(self.tab8.layoutH)

        # Set vertical layout as principal layout
        self.tab8.setLayout(self.tab8.layoutV)

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
        self._view.tab3.button.clicked.connect(self.exec_Lyapunov)
        self._view.tab4.button.clicked.connect(self.exec_tree)
        self._view.tab5.button.clicked.connect(self.exec_koch)
        self._view.tab6.button.clicked.connect(self.exec_sierp)
        self._view.tab7.button.clicked.connect(self.exec_sierp_carpet)
        self._view.tab8.button.clicked.connect(self.exec_tsquare)

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

    def exec_Lyapunov(self):
        """@TODO Should check if sequence contain letters other than A and B """
        sequence = self._view.tab3.sequence.text()

        msgBox = QMessageBox()
        if (sequence.strip() == ''):
            msgBox.setText("Sequence is empty!")
            return None
        self._evaluate[2](sequence)

        self._draw('/Lyapunov.png', self._view.tab3.labelpic)

    def exec_tree(self):
        level = self._view.tab4.SpinBox.value()
        self._evaluate[3](level)
        if level > 10:
            level = 10
        self._evaluate[4](level)

        self._draw('/tree1.png', self._view.tab4.labelpic1)
        self._draw('/tree2.png', self._view.tab4.labelpic2)

    def exec_koch(self):
        level = self._view.tab5.SpinBox.value()
        self._evaluate[5](level)

        self._draw('/koch.png', self._view.tab5.labelpic)

    def exec_sierp(self):
        level = self._view.tab6.SpinBox.value()
        self._evaluate[6](level)

        self._draw('/sierp.png', self._view.tab6.labelpic)
    
    def exec_sierp_carpet(self):
        level = self._view.tab7.SpinBox.value()
        self._evaluate[7](level)

        self._draw('/sierp_carp.png', self._view.tab7.labelpic)
    
    def exec_tsquare(self):
        level = self._view.tab8.SpinBox.value()
        self._evaluate[8](level)

        self._draw('/t_square.png', self._view.tab8.labelpic)


def main():
    # Create an instance of QApplication
    app = QApplication(sys.argv)
    # Show the Fractal_GUI
    view = Fractal_GUI()
    view.show()
    # Create instances of the model and the controller
    model = (evaluateMandelbrot, evaluateJulia, evaluateLyapunov, evaluateTree1,evaluateTree2, evaluateKoch, evaluateSierp, evaluateSierp_Carp, evaluateTSqu)
    controller = Fractal_Control(view, model)
    # execute main loop
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
