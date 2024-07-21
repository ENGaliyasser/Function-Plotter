
import re
import warnings
import matplotlib.pyplot as plt
import numpy as np
from PyQt5 import QtWidgets
import sys
from PyQt5.QtWidgets import QVBoxLayout, QMessageBox
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from Front import Ui_MainWindow  # Importing the UI class from the converted gui.py file

e = np.e
pi = np.pi
warnings.filterwarnings("ignore")
class MplCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)
class Back_End_Class(QtWidgets.QWidget, Ui_MainWindow):

    def __init__(self,MainWindow):

        #QtWidgets.QWidget.__init__(self)
        super().__init__()
        self.setupUi(MainWindow)

        # Setup the layout for the Matplotlib canvas
        self.canvas = MplCanvas(self, width=5, height=4, dpi=100)
        self.plot_layout = QVBoxLayout(self.widget)
        self.plot_layout.addWidget(self.canvas)

        self.setWindowTitle("Function Plotter")

        self.plot.clicked.connect(self.takeInput)

        # self.setWindowIcon(QIcon('icon.ico'))


        # inintializing vars
        self.min = 0
        self.max = 10
        pattern =  r"(?:[0-9-+*^/() ]|x|abs|sqrt|exp|ln|log|pi|e|(sin|cos|tan)h?)+"
        self.pat = re.compile(pattern)
        self.expression=""



    def takeInput(self):
        # reading min
        if self.notNumber(self.minInput.text()):
            print("Please Enter the Minimum Value (Must be a Number)")
            self.errMsg("Please Enter the Minimum Value (Must be a Number)")
            self.tabWidget.setCurrentIndex(0)
        self.min = float(self.minInput.text())
        # reading max
        if self.notNumber(self.maxInput.text()):
            print("Please Enter the Maximum Value (Must be a Number)")
            self.errMsg("Please Enter the Maximum Value (Must be a Number)")
            self.tabWidget.setCurrentIndex(0)
        self.max = float(self.maxInput.text())
        if self.min > self.max:
            print("Min cannot be larger than Max")
            self.errMsg("Min cannot be larger than Max")
            self.tabWidget.setCurrentIndex(0)
        # reading expression
        self.expression = self.functionInput.text().replace("^", "**")
        if re.fullmatch(self.pat, self.expression) == None:
             print("Some thing is wrong with your expression please check it again!")
             self.errMsg("Some thing is wrong with your expression please check it again!")
             self.tabWidget.setCurrentIndex(0)
        # lower case
        self.expression = self.expression.lower()
        self.update_graph()
        self.tabWidget.setCurrentIndex(1)



    def update_graph(self):
        x = np.arange(self.min, self.max, 0.1)
        # catch exceptions in case it passed our pattern by mistake
        try:
            y = eval(self.expression)
            # if linear create the Y array
            if not(isinstance(y,np.ndarray)):
                y = np.ones(x.size)*y
            # show any errors
        except SyntaxError as err:
            print("please check your syntax")
            self.errMsg("Please Check Your Syntax")
            self.tabWidget.setCurrentIndex(0)
        except NameError as err:
            print(str(err)+"only variable 'x' is allowed")
            self.errMsg(str(err)+", only variable 'x' is allowed")
            self.tabWidget.setCurrentIndex(0)
        except:
            print("Something Went Wrong Can't Evaluate Your Expression")
            self.errMsg("Something Went Wrong Can't Evaluate Your Expression")
            self.tabWidget.setCurrentIndex(0)
        self.canvas.axes.clear()
        self.canvas.axes.plot(x, y)
        self.canvas.axes.set_title("f(x) = "+self.functionInput.text())
        self.canvas.draw()
        return plt.plot(x, y)

    # ====validation====


    def notNumber(self,x):
        try:
            a = float(x)
        except (TypeError, ValueError):
            return True
        else:
            return False


    def errMsg(self, msg):
        msgBox = QMessageBox()
        msgBox.warning(self, "Error", msg)
        return


def cos(x):
    return np.cos(x)


def sin(x):
    return np.sin(x)


def tan(x):
    return np.tan(x)


def cosh(x):
    return np.cosh(x)


def sinh(x):
    return np.sinh(x)


def tanh(x):
    return np.tanh(x)


def ln(x):
    return np.log(x)


def log(x):
    return np.log10(x)


def exp(x):
    return np.exp(x)


def sqrt(x):
    return np.sqrt(x)



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Back_End_Class(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

