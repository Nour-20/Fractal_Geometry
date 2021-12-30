
import sys
from functools import partial

from Julia_fractal import evaluateJulia 
import os
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import ( QApplication,
                              QMainWindow, 
                              QTabWidget, 
                              QVBoxLayout,
                              QHBoxLayout, 
                              QPushButton,
                              QLabel,
                              QComboBox,
                              QLineEdit,
                              QSpinBox,
                              QWidget
                            )

class Fractal_GUI(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Fractal Geometry")
        self.setFixedSize(1280,720)
        
        self.createTab()

    def createTab(self):
        self.tabs = QTabWidget()
        self.tabs.setTabPosition(QTabWidget.West)
        self.tabs.setMovable(True)

        # QWidget-Tab screen
        self.tab1 = QWidget() # Mandelbrot
        self.tab2 = QWidget() # Julia
        self.tab3 = QWidget() # Tree
        self.tab4 = QWidget() # Koch
        self.tab5 = QWidget() # sierp

        temp = {
            "Mandelbrot":self.tab1, 
            "Julia":self.tab2,
            "Tree of life":self.tab3, 
            "Koch snowflake":self.tab4, 
            "Sierpinski":self.tab5
            }

        for key, value in temp.items():
            self.tabs.addTab(value,key)
        
        self.setCentralWidget(self.tabs)

        # Create tabs contents
        self.createMandelbrotTab()
        self.createJuliaTab()
        self.createTreeTab()
        self.createKochTab()
        self.createSierpTab()

    def createMandelbrotTab(self):
        self.tab1.layoutV = QVBoxLayout()
        self.tab1.labelpic =  QLabel() # Mandelbrot pics

        # Horizontal Layout
        self.tab1.layoutH = QHBoxLayout()
        self.tab1.labeltext = QLabel("Dimension")
        self.tab1.button = QPushButton("Run")

        self.tab1.dimension = QLineEdit()
        self.tab1.dimension.setFrame(True)
        self.tab1.dimension.setMaxLength(5)
        self.tab1.dimension.setPlaceholderText("Enter dimension")
        self.tab1.dimension.setMaximumWidth(200)

        self.tab1.layoutH.addWidget(self.tab1.labeltext)
        self.tab1.layoutH.addWidget(self.tab1.dimension)
        self.tab1.layoutH.addSpacing(900)
        self.tab1.layoutH.addWidget(self.tab1.button)

        # Vertical Layout
        self.tab1.layoutV.addWidget(self.tab1.labelpic)
        self.tab1.layoutV.addLayout(self.tab1.layoutH)

        # Set vertical layout as principal layout
        self.tab1.setLayout(self.tab1.layoutV)

    def createJuliaTab(self):
        self.tab2.layoutV = QVBoxLayout()
        self.tab2.labelpic =  QLabel() # Julia pics

        # Horizontal Layout
        self.tab2.layoutH = QHBoxLayout()
        self.tab2.labeltext = QLabel("c")
        self.tab2.button = QPushButton("Run")

        self.tab2.ComboBox = QComboBox()
        self.tab2.ComboBox.addItems(["−0.4 + 0.6i","0.285 + 0i","0.285 + 0.01i","0.45 + 0.1428i","−0.70176 − 0.3842i"," −0.835 − 0.2321i","−0.8 + 0.156i"," −0.7269 + 0.1889i","−0.8i"])

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
        self.tab3.labelpic =  QLabel() # Tree of life pics

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
        self.tab3.layoutV.addWidget(self.tab3.labelpic)
        self.tab3.layoutV.addLayout(self.tab3.layoutH)

        # Set vertical layout as principal layout
        self.tab3.setLayout(self.tab3.layoutV)

    def createKochTab(self):
        self.tab4.layoutV = QVBoxLayout()
        self.tab4.labelpic =  QLabel() # Snowflake pics

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
        self.tab5.labelpic =  QLabel() # Sierpinski pics

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

    def __init__(self,GUI,Model):
        self._evaluate = Model
        self._view = GUI
        # Connect signals and slots
        self._connectSignals()
    
    def Exec_Julia(self):
        temp_dict={
                   0:(-0.4,0.6),
                   1:(0.285,0),
                   2:(0.285,0.01),
                   3:(0.45,0.1428),
                   4:(-0.70176,-0.3842),
                   5:(-0.835,-0.2321),
                   6:(-0.8,0.156),
                   7:(-0.7269,0.1889),
                   8:(0,-0.8)
                }
        index=self._view.tab2.ComboBox.currentIndex()
        self._evaluate(temp_dict[index][0],temp_dict[index][1])
        
        self._path = os.path.dirname(os.path.realpath(__file__))
        self._pixmap=QPixmap(self._path + '/julia.png')
        self._view.tab2.labelpic.setPixmap(self._pixmap)
    
    def _connectSignals(self):
        self._view.tab2.button.clicked.connect(self.Exec_Julia)


def main():
    #Create an instance of QApplication
    app = QApplication(sys.argv)
    # Show the Fractal_GUI
    view = Fractal_GUI()
    view.show()
    # Create instances of the model and the controller
    model=evaluateJulia
    controller=Fractal_Control(view,model)
    # Execute main loop
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()