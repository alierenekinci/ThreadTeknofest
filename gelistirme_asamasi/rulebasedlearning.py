import json
import random


path = r'C:\Users\alierenekinci\Desktop\Project\ThreadTeknofest\kuraltabanliveriler\rulebasedlearning.json'
with open(path, encoding='utf-8') as f:
    veri = json.load(f)

def get_func(metin):
    if metin == "dolar":
        from pandas_datareader import data

        from datetime import date
        today = date.today()


        start_date = today
        end_date = today

        panel_data = data.DataReader('TRY=X', 'yahoo', start_date, end_date)
        return(str(panel_data["Adj Close"][0])[:5])
    if metin == "euro":
        from pandas_datareader import data

        from datetime import date
        today = date.today()


        start_date = today
        end_date = today

        panel_data = data.DataReader('EURTRY=X', 'yahoo', start_date, end_date)
        return(str(panel_data["Adj Close"][0])[:5])


def searchPattern(metin):

    # pattern search


    for veri_ in veri:
        pointer = -1
        for i in veri[veri_]:
            pointer += 1
            for j in i["pattern"]:
                if metin == j:
                    response = random.choice(veri[veri_][pointer]["response"])
                    response = response.split("<"+ metin +">")
                    if response[0] != "":
                        return(response[0] + str(get_func(metin)) + response[-1])
                    else:
                        return("".join(str(get_func(metin))) + response[-1])
                    

            for j in i["pattern"]:
                # star search
                starPointer = False
                metinList = list()
                pointText = 0
                for k in j:
                    # print(k, metin[pointText])
                    if (k == metin[pointText]):
                        pointText += 1
                    else:
                        if k == "*":
                            starPointer = True
                        else:
                            break
                    
                    while starPointer:
                        metinList.append(metin[pointText])
                        pointText += 1

    
                        if metin[pointText] == "`":
                            pointText = 0
                            # print(pointer)
                            response = random.choice(veri[veri_][pointer]["response"])
                            response = response.split("<star>")
                            
                            if response[0] != "":
                               return(response[0] + "".join(metinList) + response[-1])
                            else:
                                return("".join(metinList) + response[-1])
                    



print(searchPattern("yaşım 18"+"`"))
print(searchPattern("adım Ali Eren"+"`"))
# print(searchPattern("ben görkem"+"`"))
print(searchPattern("dolar"))

