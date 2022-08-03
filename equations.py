# Program, który dla zadanego układu równan liniowych z trzema niewiadomymi wykona wizualizacje w przestrzeni trójwymiarowej

import csv                                  # Zaimportowanie odpowiednich funkcji
import numpy as np
import matplotlib.pyplot as plt

file = "dane.csv"                           # Zdefiniowanie potrzebnych danych

def solve_system_of_equations(file):

    """Funkcja rozwiązująca układ równań z 3 niewiadomymi.
        Args:
            file (str): plik z danymi
        Returns:
            x: rozwiązanie układu
            result: tablica z zapisanymi wynikami A, b i x
    """
    dane = []

    with open("dane.csv", "r", newline = "") as file:             # Otwarcie pliku csv i odczyt danych
        rd = csv.reader(file, delimiter=",")
        for line in rd:
            numbers = []
            for element in line:
                numbers.append(int(element))
            dane.append(numbers)
    
    line_1 = dane[0]
    line_2 = dane[1]
    line_3 = dane[2]

    U = np.matrix([line_1[:],                                      # Zapis do macierzy 3x4
                    line_2[:],
                    line_3[:]])
    
    A = np.matrix([line_1[:3],                                     # Zapis do macierzy 3x3
                    line_2[:3],
                    line_3[:3]])

    row_A = np.linalg.matrix_rank(A)
    row_U = np.linalg.matrix_rank(U)
    n = 3

    if n == row_A and n == row_U:                                  # Sprawdzenie czy układ jest oznaczony
        b = np.matrix([2, -5, 0]).T
        x = np.linalg.inv(A) * b
        print("Układ ma jedno rozwiązanie równe:\n" + str(x))
    
    if row_A == row_U and n > row_U:                               # Sprawdzenie czy układ jest nieoznaczony
        print("Układ ma nieskończenie wiele rozwiązań.")
    
    if row_A != row_U:                                             # Sprawdzenie czy układ jest sprzeczny
        print("Układ nie ma rozwiązań.")
    
    result = []                                                    # Zapis wyników do tablicy
    result.append(A)
    result.append(b)
    result.append(x)

    return result

result = solve_system_of_equations(file)

def show_system_of_equations(result):

    """Funkcja wizualizująca układ równań z 3 niewiadomymi.
        Args:
            result: tablica z wyliczonymi wartościami A, b i x
        Returns:
            graph: wykres ilustrujący rozwiązanie układu równań
    """

    x = result[2]                                                         # Rozpakowanie danych z tablicy
    b = result[1]
    A = result[0]
    
    x1 = x2 = np.linspace(-3, 3, 10)
    X1, X2 = np.meshgrid(x1, x2)

    X3_1 = -A[0, 0]/A[0, 2] * X1 - A[0, 1]/A[0, 2] * X2 + b[0]/A[0, 2]
    X3_2 = -A[1, 0]/A[1, 2] * X1 - A[1, 1]/A[1, 2] * X2 + b[1]/A[1, 2]
    X3_3 = -A[2, 0]/A[2, 2] * X1 - A[2, 1]/A[2, 2] * X2 + b[2]/A[2, 2]
    
    graph = plt.figure()                                                    # Tworzenie wykresu 3D
    os = graph.gca(projection='3d')
    
    os.plot_surface(X1, X2, X3_1, alpha=0.4, color='r')
    os.plot_surface(X1, X2, X3_2, alpha=0.4, color='g')
    os.plot_surface(X1, X2, X3_3, alpha=0.4, color='b')
    os.text(X1[0, 0], X2[0, 0], X3_1[0, 0], '$x_1$')
    os.text(X1[0, 0], X2[0, 0], X3_2[0, 0], '$x_2$')
    os.text(X1[0, 0], X2[0, 0], X3_3[0, 0], '$x_3$')
    os.scatter(x[0, 0], x[1, 0], x[2, 0], color='k')
    os.text(x[0, 0], x[1, 0], x[2, 0], '$x$')
    os.set_xlabel('$x_1$')
    os.set_ylabel('$x_2$')
    os.set_zlabel('$x_3$')
    plt.show()

show_system_of_equations(result)