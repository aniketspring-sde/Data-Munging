from src.calculator import Calculator

FILE_URL = "../data/weather.dat"

DAY_COLUMN = "Dy"
MAX_TEMP_COLUMN = "MxT"
MIN_TEMP_COLUMN = "MnT"


calculator = Calculator(
    FILE_URL,
    DAY_COLUMN,
    MAX_TEMP_COLUMN,
    MIN_TEMP_COLUMN
)

day, maximum, minimum = calculator.calculate()

print(f"Day {day} has the smallest temperature spread.")


