# class DataExtractor:
#
#     def __init__(self, file_url, key_column, column1, column2):
#         self.file_url = file_url
#         self.key_column = key_column
#         self.column1 = column1
#         self.column2 = column2
#
#     def extract(self):
#         data = []
#
#         with open(self.file_url) as file:
#
#             headers = file.readline().split()
#
#             key_index = headers.index(self.key_column)
#             column1_index = headers.index(self.column1)
#             column2_index = headers.index(self.column2)
#
#             for line in file:
#
#                 values = line.split()
#
#                 if not values:
#                     continue
#
#                 key = values[key_index]
#                 value1 = values[column1_index]
#                 value2 = values[column2_index]
#
#                 value1 = value1.replace("*", "")
#                 value2 = value2.replace("*", "")
#
#                 data.append((key, value1, value2))
#
#         return data
#

class DataExtractor:

    def __init__(self, file_name, key_column, column1, column2):
        self.file_name = file_name
        self.key_column = key_column
        self.column1 = column1
        self.column2 = column2

    def extract(self):
        data = []

        with open(self.file_name) as file:
            headers = file.readline().split()

            key_index = headers.index(self.key_column)
            column1_index = headers.index(self.column1)
            column2_index = headers.index(self.column2)

            for line in file:
                values = line.split()

                if not values:
                    continue

                # football.dat has ranking number: "1."
                if values[0].endswith("."):
                    values.pop(0)

                # football.dat has "-" between F and A
                if "-" in values:
                    values.remove("-")

                if len(values) <= max(key_index, column1_index, column2_index):
                    continue

                key = values[key_index]
                value1 = values[column1_index].replace("*", "")
                value2 = values[column2_index].replace("*", "")

                data.append((key, value1, value2))

        return data