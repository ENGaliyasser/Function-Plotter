import contextlib
from io import StringIO

import numpy as np
import pytest
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt

from Back import Back_End_Class, MplCanvas  # Adjust the import as needed


@pytest.fixture
def app(qtbot):
    test_app = QtWidgets.QApplication([])

    MainWindow = QtWidgets.QMainWindow()
    ui = Back_End_Class(MainWindow)
    MainWindow.show()
    qtbot.addWidget(MainWindow)
    qtbot.addWidget(ui)
    yield ui


    # Add more specific assertions based on the expected behavior of the setup
def test_min_max_values(app, qtbot):
    app.minInput.setText('0')
    app.maxInput.setText('10')
    app.functionInput.setText('x')
    qtbot.mouseClick(app.plot, Qt.LeftButton)

    assert app.min == 0
    assert app.max == 10


def test_invalid_min_value(app, qtbot):
    app.minInput.setText('abc')
    app.maxInput.setText('0')
    app.functionInput.setText('x')

    # Capture the print output
    with contextlib.redirect_stdout(StringIO()) as f:
        qtbot.mouseClick(app.plot, Qt.LeftButton)
        output = f.getvalue()

    assert "Please Enter the Minimum Value (Must be a Number)" in output

def test_invalid_max_value(app, qtbot):
    app.minInput.setText('0')
    app.maxInput.setText('abc')
    app.functionInput.setText('x')

    # Capture the print output
    with contextlib.redirect_stdout(StringIO()) as f:
        qtbot.mouseClick(app.plot, Qt.LeftButton)
        output = f.getvalue()

    assert "Please Enter the Maximum Value (Must be a Number)" in output

def test_min_larger_than_max(app, qtbot):
    app.minInput.setText('10')
    app.maxInput.setText('0')
    app.functionInput.setText('x')

    # Capture the print output
    with contextlib.redirect_stdout(StringIO()) as f:
        qtbot.mouseClick(app.plot, Qt.LeftButton)
        output = f.getvalue()

    assert "Min cannot be larger than Max" in output

def test_invalid_expression(app, qtbot):
    app.minInput.setText('0')
    app.maxInput.setText('10')
    app.functionInput.setText('invalid_expression')

    # Capture the print output
    with contextlib.redirect_stdout(StringIO()) as f:
        qtbot.mouseClick(app.plot, Qt.LeftButton)
        output = f.getvalue()

    assert "Some thing is wrong with your expression please check it again!" in output

def test_expression_with_syntax_error(app, qtbot):
    app.minInput.setText('0')
    app.maxInput.setText('10')
    app.functionInput.setText('x +')

    # Capture the print output
    with contextlib.redirect_stdout(StringIO()) as f:
        qtbot.mouseClick(app.plot, Qt.LeftButton)
        output = f.getvalue()

    assert "Please Check Your Syntax" in output

def test_expression_with_name_error(app, qtbot):
    app.minInput.setText('0')
    app.maxInput.setText('10')
    app.functionInput.setText('y')

    # Capture the print output
    with contextlib.redirect_stdout(StringIO()) as f:
        qtbot.mouseClick(app.plot, Qt.LeftButton)
        output = f.getvalue()

    assert 'Some thing is wrong with your expression please check it again!\n' in output

def test_valid_plot(app, qtbot):
    app.minInput.setText('0')
    app.maxInput.setText('10')
    app.functionInput.setText('x')

    qtbot.mouseClick(app.plot, Qt.LeftButton)

    # Check the plot
    assert len(app.canvas.axes.lines) == 1  # Ensure a line was plotted
    assert app.canvas.axes.get_title() == "f(x) = x"

def test_valid_plot_constant(app, qtbot):
    app.minInput.setText('0')
    app.maxInput.setText('10')
    app.functionInput.setText('5')

    qtbot.mouseClick(app.plot, Qt.LeftButton)

    # Check the plot
    assert len(app.canvas.axes.lines) == 1  # Ensure a line was plotted
    assert app.canvas.axes.get_title() == "f(x) = 5"