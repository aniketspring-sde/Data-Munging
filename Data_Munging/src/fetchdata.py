import csv


class FetchData:


    def fetch(self,url):
        with open(url, "r") as file:
            rows = csv.DictReader(file)

            return list(rows)