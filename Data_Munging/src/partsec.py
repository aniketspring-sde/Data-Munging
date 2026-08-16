class PartSec:

    def soccer_data_calc(self,fd:list):
        print("Calling PartSec Method")
        min_diff = 2 ** 31 - 1
        # team = ""
        for i in range(len(fd)):

            for k, v in fd[i].items():
                if not v[43:46].strip() == "---" or v[50:55].strip() == '---':
                    diff = abs(int(v[43:46].strip()) - int(v[50:55].strip()))

                if min_diff > diff:
                    min_diff = diff
                    team = v[7:19].strip()
        print(f"Team:{team}\nDiff:{min_diff}")