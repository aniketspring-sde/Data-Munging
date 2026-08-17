# class DataAnalyzer:
#
#     def __init__(self, data):
#         self.data = data
#
#     def min_diff(self):
#         min_difference = float("inf")
#         result = None
#
#         for row in self.data:
#             value1 = float(row[1])
#             value2 = float(row[2])
#
#             difference = abs(value1 - value2)
#
#             if difference < min_difference:
#                 min_difference = difference
#                 result = row
#
#         return result

class DataAnalyzer:

    def __init__(self, data):
        self.data = data

    def min_diff(self):
        minimum = float("inf")
        result = None

        for row in self.data:
            value1 = float(row[1])
            value2 = float(row[2])

            difference = abs(value1 - value2)

            if difference < minimum:
                minimum = difference
                result = row

        return result