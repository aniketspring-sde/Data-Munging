class PartOne:

    def weather_data_calc(self,wd:list):
        print("Calling PartOne Method")
        min_diff = 2 ** 31 - 1
        # day = -1
        for i in range(len(wd)):

            for k, v in wd[i].items():

                diff = abs(int(v[6:8].strip()) - int(v[12:14].strip()))

                if min_diff > diff:
                    min_diff = diff
                    day = v[3:4].strip()
        print(f"Day:{day}\nDiff:{min_diff}")