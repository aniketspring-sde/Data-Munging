from src.data_analyzer import DataAnalyzer
from src.data_extracter import DataExtractor


# class Calculator:
#
#     def __init__(self, file_name, key_column, column1, column2):
#         self.extractor = DataExtractor(
#             file_name, key_column, column1, column2
#         )
#
#     def calculate(self):
#         data = self.extractor.extract()
#         return DataAnalyzer(data).min_diff()




class Calculator:

    def __init__(self, file_name, key_column, column1, column2):
        self.extractor = DataExtractor(
            file_name,
            key_column,
            column1,
            column2
        )

    def calculate(self):
        data = self.extractor.extract()
        analyzer = DataAnalyzer(data)

        return analyzer.min_diff()