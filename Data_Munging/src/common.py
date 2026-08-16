class Common:
    def data_calc(self,data:list,x:int,y:int,p:int,q:int,s:int,t:int):
        print("Calling common Method")
        min_diff = 2 ** 31 - 1

        for i in range(len(data)):

            for k, v in data[i].items():

                if not v[p:q].strip() == "---" or v[s:t].strip() == '---':
                    diff = abs(int(v[p:q].strip()) - int(v[s:t].strip()))

                if min_diff > diff:
                    min_diff = diff
                    ans_col = v[x:y].strip()
        print(f"ANS_COL:{ans_col}\ndiff:{min_diff}")