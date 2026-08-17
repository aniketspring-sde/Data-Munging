# from src.garb.common import Common
# from src.garb.fetchdata import FetchData
# from src.garb.partone import PartOne
# from src.garb.partsec import PartSec
#
#
# def main():
#     fd_url = "data/football.dat"
#     wd_url = "data/weather.dat"
#
#     fetch_data = FetchData()
#     wd = fetch_data.fetch(wd_url)
#     fd = fetch_data.fetch(fd_url)
#     p1 = PartOne()
#     p2 = PartSec()
#     comm = Common()
#
#     p1.weather_data_calc(wd)
#     p2.soccer_data_calc(fd)
#
#     comm.data_calc(wd,3,4,6,8,12,14)
#
#
#     comm.data_calc(fd,7,19,43,46,50,55)
#
#
# if __name__ == "__main__":
#     main()

from src.calculator import Calculator

FILE_URL = "data/weather.dat"

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