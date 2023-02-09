from main import calcularDispositivoBebe
import io
import sys

def test_portabebe():
    capturedOutput = io.StringIO()                  # Create StringIO object
    sys.stdout = capturedOutput                     #  and redirect stdout.

    calcularDispositivoBebe(0.5, 10, 74)

    sys.stdout = sys.__stdout__                     # Reset redirect.
    print ('Captured', capturedOutput.getvalue())   # Now works as before.

    assert capturedOutput.getvalue()== "Portabebé\n"


def test_silla():
    capturedOutput = io.StringIO()                  # Create StringIO object
    sys.stdout = capturedOutput                     #  and redirect stdout.

    calcularDispositivoBebe(2, 10, 78)

    sys.stdout = sys.__stdout__                     # Reset redirect.
    print ('Captured', capturedOutput.getvalue())   # Now works as before.

    assert capturedOutput.getvalue()== "Silla\n"
    
    
def test_con_respaldar():
    capturedOutput = io.StringIO()                  # Create StringIO object
    sys.stdout = capturedOutput                     #  and redirect stdout.

    calcularDispositivoBebe(5,17,111)

    sys.stdout = sys.__stdout__                     # Reset redirect.
    print ('Captured', capturedOutput.getvalue())   # Now works as before.

    assert capturedOutput.getvalue()== "Asiento con respaldar\n"

def test_sin_respaldar():
    capturedOutput = io.StringIO()                  # Create StringIO object
    sys.stdout = capturedOutput                     #  and redirect stdout.

    calcularDispositivoBebe(8,25,117)

    sys.stdout = sys.__stdout__                     # Reset redirect.
    print ('Captured', capturedOutput.getvalue())   # Now works as before.

    assert capturedOutput.getvalue()== "Asiento sin respaldar\n"