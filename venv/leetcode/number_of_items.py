class solution():
    def countmatches( items, rulekey, rulevalue):
        d = {'type': 0, 'color': 1, 'name': 2}
        c = 0

       # items = [["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]]
        #ruleKey = "color"
        #ruleValue = "silver"
        index= d[rulekey]


        for item in items:
            if rulevalue == item[index]:
                c +=1
        return c
    if __name__=='__main__':
         items = [["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]]
         ruleKey = "color"
         ruleValue = "silver"

         print (countmatches(items, ruleKey, ruleValue))


