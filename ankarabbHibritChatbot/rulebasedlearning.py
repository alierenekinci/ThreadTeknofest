# Rule-Based Learning
# ThreadTeknofest 2022


import json
import random


path = 'kuraltabanliveriler\\rulebasedlearning.json'
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
    



def SearchPattern(metin:str):
    for veri_ in veri:
        pointer = -1
        for i in veri[veri_]:
            pointer += 1
            for j in i["pattern"]:
                if metin == j:
                    
                    print(metin)
                    response = random.choice(veri[veri_][pointer]["response"])
                    print(response)
                    if str("<"+ metin +">") in response:

                        responseSplit = response.split("<"+ metin +">")
                        
                        if len(responseSplit) > 1:
                            if responseSplit[0] != "":
                                return(responseSplit[0] + str(get_func(metin)) + responseSplit[-1])
                            else:
                                return("".join(str(get_func(metin))) + responseSplit[-1])
                    else:
                        return response


                
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
                            metin += "`"
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
                    


# print(SearchPattern("merhaba"))
# print(SearchPattern("yaşım 18"))
# print(SearchPattern("adım Ali Eren"+"`"))
# print(SearchPattern("ben görkem"))
# print(SearchPattern("dolar"))
# print(SearchPattern("merhaba"))

