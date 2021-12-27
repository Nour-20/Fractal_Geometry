#!/usr/bin/env python3

# Filename: Lorenz.py

import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import (
    FigureCanvasQTAgg as FigureCanvas,
    NavigationToolbar2QT as NavigationToolbar)
from matplotlib.animation import FuncAnimation , FFMpegWriter, PillowWriter

# Import QApplication and the required widgets from PyQt5.QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QWidget


class LorenzUi(QMainWindow):
    """Lorenz's View (GUI)."""

    def __init__(self):
        """View initializer."""
        super().__init__()
        # Set some main window's properties
        self.setWindowTitle('Lorenz')
        self.setFixedSize(720, 720)
        # Set the central widget and the general layout
        self.generalLayout = QVBoxLayout()
        self.bottom = QHBoxLayout()
        self._centralWidget = QWidget(self)
        self.setCentralWidget(self._centralWidget)
        self._centralWidget.setLayout(self.generalLayout)
        # Create the display and the buttons
        self._createInput()

    def _createInput(self):
        """Create the 3 input screens.
        sigma, rho and beta."""
        # Create the display widget
        self.play = QPushButton("Play")
        self.sigma = QLineEdit()
        self.rho = QLineEdit()
        self.beta = QLineEdit()
        # Set some display's properties
        self.sigma.setFixedHeight(35)
        self.sigma.setAlignment(Qt.AlignLeft)
        self.rho.setFixedHeight(35)
        self.rho.setAlignment(Qt.AlignLeft)
        self.beta.setFixedHeight(35)
        self.beta.setAlignment(Qt.AlignLeft)
        # self.display.setReadOnly(True)
        # Add the display to the general layout
        self.bottom.addWidget(self.play)
        self.bottom.addWidget(self.sigma)
        self.bottom.addWidget(self.rho)
        self.bottom.addWidget(self.beta)
        self.generalLayout.addLayout(self.bottom)

    def getSigma(self):
        """Get sigma's text."""
        return self.sigma.text()

    def getRho(self):
        """Get rho's text."""
        return self.rho.text()

    def getBeta(self):
        """Get beta's text."""
        return self.beta.text()

    def addMatplot(self, fig):
        self.canvas = FigureCanvas(fig)
        self.generalLayout.addWidget(self.canvas)
        self.canvas.draw()
        # self.toolbar = NavigationToolbar(self.canvas,
        #         self, coordinates=True)
        # self.addToolBar(self.toolbar)


# Create a Controller class to connect the GUI and the model
class LorenzCtrl:
    """Lorenz's Controller."""

    def __init__(self, model, view):
        """Controller initializer."""
        self._evaluate = model
        self._view = view
        # Connect signals and slots
        self._connectSignals()

    def _connectSignals(self):
        """Connect signals and slots."""
        self._view.play.clicked.connect(self._plot)

    def _plot(self):
        """Evaluate expressions."""
        sig = self._view.getSigma()
        ro = self._view.getRho()
        bet = self._view.getBeta()

        fige = self._evaluate(float(sig), float(ro), float(bet))
        self._view.addMatplot(fige)


def compute_F(y, t, sigma):
    sig, rho, beta = sigma
    f1 = sig*(y[1]-y[0])
    f2 = y[0]*(rho-y[2])-y[1]
    f3 = y[0]*y[1]-beta*y[2]
    return np.array([f1, f2, f3])


def compute_K(f, y, t, h, sigma):
    kk = np.zeros((4, 3), dtype=np.float64)
    kk[0, :] = h*f(y, t, sigma)
    kk[1, :] = h*f(y+kk[0, :]/2, t+(h/2), sigma)
    kk[2, :] = h*f(y+kk[1, :]/2, t+(h/2), sigma)
    kk[3, :] = h*f(y+kk[2, :], t+h, sigma)
    return kk


def compute_Y(y_previous, k):
    y_next = np.zeros(3)
    y_next[0] = y_previous[0]+(1/6)*(k[0, 0]+2*k[1, 0]+2*k[2, 0]+k[3, 0])
    y_next[1] = y_previous[1]+(1/6)*(k[0, 1]+2*k[1, 1]+2*k[2, 1]+k[3, 1])
    y_next[2] = y_previous[2]+(1/6)*(k[0, 2]+2*k[1, 2]+2*k[2, 2]+k[3, 2])
    return y_next


def plot(sig, ro, bet):
    sigma = (sig, ro, bet)
    t = 0
    N = 10000
    a = 0
    b = 100
    step = (b-a)/N

    f = np.zeros((N, 3))
    k = np.zeros((N, 4, 3))
    y = np.zeros((N+1, 3))
    y[0, :] = np.array([3, 0, 0])

    for i in range(0, N):
        f[i, :] = compute_F(y[i, :], t, sigma)
        k[i, :, :] = compute_K(compute_F, y[i, :], t, step, sigma)
        y[i+1, :] = compute_Y(y[i, :], k[i, :, :])

        t += i*step

    fig = plt.figure()
    ax = fig.gca(projection="3d")

    def animate(i):
        ax.clear()
        ax.plot3D(y[:, 0], y[:, 1], y[:, 2])

    ani = FuncAnimation(fig, animate, frame=24)

    plt.show()

    return fig



if __name__ == '__main__':
    """Main function."""
    # Create an instance of QApplication
    lorenz = QApplication(sys.argv)
    # Show the calculator's GUI
    view = LorenzUi()
    # Create instances of the model and the controller
    model = plot
    app = LorenzCtrl(model=model, view=view)

    view.show()
    # Execute the calculator's main loop
    sys.exit(lorenz.exec_())


    # sigma = (10, 28, 8/3)
    # t = 0
    # N = 2000
    # a = 0
    # b = 100
    # step = (b-a)/N

    # f = np.zeros((N, 3))
    # k = np.zeros((N, 4, 3))
    # y = np.zeros((N+1, 3))
    # y[0, :] = np.array([3, 0, 0])

    # for i in range(0, N):
    #     f[i, :] = compute_F(y[i, :], t, sigma)
    #     k[i, :, :] = compute_K(compute_F, y[i, :], t, step, sigma)
    #     y[i+1, :] = compute_Y(y[i, :], k[i, :, :])

    #     t += i*step

    # x = []
    # xx = []
    # xxx = []
    # fig = plt.figure()
    # ax = fig.gca(projection="3d")

    # def animate(i):
    #     x.append(y[i,0])
    #     xx.append(y[i,1])
    #     xxx.append(y[i,2])
    #     ax.clear()
    #     ax.plot3D(x, xx, xxx)

    # ani = FuncAnimation(fig, animate, frames=N, interval=1, repeat=False)

    # writermp4 = PillowWriter(fps=60) 
    # ani.save("movie.gif", writer=writermp4)
