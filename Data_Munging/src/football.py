from src.calculator import Calculator

FILE_URL = "../data/football.dat"

TEAM_COLUMN = "Team"
FOR_COLUMN = "F"
AGAINST_COLUMN = "A"


calculator = Calculator(
    FILE_URL,
    TEAM_COLUMN,
    FOR_COLUMN,
    AGAINST_COLUMN
)

team, goals_for, goals_against = calculator.calculate()

print(f"{team} has the smallest goal difference.")