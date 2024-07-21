# Function Plotter GUI

## Download and Run the Executable

To use the application without setting up a Python environment, you can download the pre-built executable:

1. **Download the ZIP**:
   - Go to the [releases page](release) and download the ZIP file.

2. **Extract the ZIP**:
   - Uncompress the downloaded ZIP file to a desired location on your computer.

3. **Run the Executable**:
   - Navigate to the extracted folder and click on the `.exe` file to run the application directly.

## Overview

This Python application provides a graphical user interface (GUI) for plotting arbitrary functions of \(x\) using PySide2 and Matplotlib. Users can input mathematical functions and specify the range for \(x\) to visualize the function graphically. The application supports basic arithmetic operations and functions including addition, subtraction, multiplication, division, exponentiation, logarithms, and square roots.

## Features

- **Function Plotting**: Input and plot arbitrary mathematical functions.
- **Input Validation**: Ensure that user inputs for functions and range values are valid.
- **Error Handling**: Display user-friendly error messages for invalid inputs.
- **Embedded Matplotlib Figure**: The plot is embedded directly within the PySide2 application.
- **Simple and Beautiful GUI**: User-friendly and well-organized interface.
- **Automated Testing**: End-to-end testing of main features using `pytest` and `pytest-qt`.

## Installation (Optional)

If you prefer to run the application from the source code:

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/ENGaliyasser/Function-Plotter.git
   cd Function-Plotter
   ```

2. **Install Dependencies**:

   Ensure you have Python 3.x installed. You can install the required packages using `pip`. 

   include:

   ```
   PySide2
   matplotlib
   pytest
   pytest-qt
   ```

3. **Run the Application**:

   To run the application, use the following command:

   ```bash
   python main.py
   ```

   This will open the GUI where you can enter functions and range values to plot.

## Usage

1. **Enter Function**: Input a function of \(x\), e.g., `5*x^3 + 2*x`.
2. **Specify Range**: Enter the minimum and maximum values for \(x\).
3. **Plot Function**: Click the plot button to visualize the function.

## Input Validation

- Ensure that function inputs are valid mathematical expressions.
- Enter numerical values for the minimum and maximum range.
- The application will prompt error messages for invalid inputs.

## Error Handling

The application will display message boxes for the following errors:
- Invalid function expression
- Non-numeric values for range
- Minimum value greater than maximum value

## Automated Tests

Automated tests are included in the repository to verify the main features of the application. To run the tests, use:

```bash
pytest
```

## Contributing

Feel free to submit issues or pull requests if you have suggestions or improvements. Please ensure that any changes are well-documented and tested.


## Contact

For questions or feedback, please contact [engaliyasser7@gmail.com](mailto:engaliyasser7@gmail.com).
