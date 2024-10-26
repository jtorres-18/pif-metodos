
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QTextEdit
from math import exp, sin, cos, tan, log

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PYTHERACIONES")
        self.setGeometry(100, 100, 400, 300)

        central_widget = QWidget()
        layout = QVBoxLayout()

        self.function_label = QLabel("Ingrese la función:")
        self.function_input = QLineEdit()
        self.initial_guess_label = QLabel("Ingrese una aproximación inicial:")
        self.initial_guess_input = QLineEdit()
        self.tolerance_label = QLabel("Ingrese la tolerancia:")
        self.tolerance_input = QLineEdit("0.0001")
        self.max_iterations_label = QLabel("Ingrese el número máximo de iteraciones:")
        self.max_iterations_input = QLineEdit("100")
        self.calculate_button = QPushButton("Calcular")
        self.calculate_button.clicked.connect(self.calculate_root)
        self.result_label = QLabel("Resultado:")
        self.result_text = QTextEdit()

        layout.addWidget(self.function_label)
        layout.addWidget(self.function_input)
        layout.addWidget(self.initial_guess_label)
        layout.addWidget(self.initial_guess_input)
        layout.addWidget(self.tolerance_label)
        layout.addWidget(self.tolerance_input)
        layout.addWidget(self.max_iterations_label)
        layout.addWidget(self.max_iterations_input)
        layout.addWidget(self.calculate_button)
        layout.addWidget(self.result_label)
        layout.addWidget(self.result_text)

        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def calculate_root(self):
        function = self.function_input.text()
        initial_guess = float(self.initial_guess_input.text())
        tolerance = float(self.tolerance_input.text())
        max_iterations = int(self.max_iterations_input.text())

        root = self.newton_raphson(function, initial_guess, tolerance, max_iterations)
        self.result_text.setPlainText(str(root))

    def newton_raphson(self, function, initial_guess, tolerance, max_iterations):
        def f(x):
            return eval(function)

        def df(x):
            h = 0.0001
            return (f(x + h) - f(x)) / h

        x = initial_guess
        print(f"Inicial: x = {x}, f(x) = {f(x)}")
        for i in range(max_iterations):
            fx = f(x)
            dfx = df(x)
            print(f"Iteración {i}: x = {x}, f(x) = {fx}, f'(x) = {dfx}")
            if abs(fx) < tolerance:
                print(f"Solución encontrada: x = {x}")
                return x
            if dfx == 0:
                print(f"La derivada es cero en x = {x}")
                return x
            x = x - fx / dfx

        print("No se encontró una solución dentro de la tolerancia y el número máximo de iteraciones.")
        return x
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())