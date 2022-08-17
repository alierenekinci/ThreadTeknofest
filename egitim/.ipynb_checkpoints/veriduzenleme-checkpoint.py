import os
import json

path = r'C:\Users\alierenekinci\Desktop\Project\ThreadTeknofest\veri'

def yukle():
    liste = os.listdir(path)
    final_path = path + "\\" + liste[-1]

    with open(final_path, encoding='utf-8') as f:
        veri = json.load(f)
    return veri

def kaydet(veri):
    liste = os.listdir(path)
    final_path = path + "\\" + liste[-1][:-7] + str(int(liste[-1][31:-5])+1) + ".json"
    with open(final_path, 'w', encoding='utf-8') as json_dosya:
        json.dump(veri, json_dosya, ensure_ascii=False)

    print("Dosya adı:", final_path)

new_dict = dict()
first_list = list()
first_dict = dict()
while True:
    print("-"*15)
    veri = yukle()
    islem = input("Liste - 1 \nDüzenleme - 2 \nHepsine Soru Ekleme - 3 \nKaydet - 4\nİşlem:")
    if islem == "1":

        print("Etiketler*\n", "-"*30)
        for veri_ in veri:
            for index in veri[veri_]:
                print(index["tag"]),
    elif islem == "2":
        tag = input("Düzenlemek istediğin veri etiketi:")
        for veri_ in veri:
            for index in veri[veri_]:      
                if index["tag"] == tag:
                    print("\n\n----\nSoru(Pattern):", index["patterns"], "\n-----\n", "Cevap(Responses):", index["responses"], "\n-----\n")
                    islem2 = input("Soru Ekle - 1 \nCevap Ekle - 2 \nHangi islemi yapacaksın: ")
                    if islem2 == "1":
                        print("\n\n----\nSoru(Pattern):", index["patterns"])
                        soru = input("Eklenecek soruyu yaz: ")
                        index["patterns"].append(soru)
                        print("Başarılı: ",index["patterns"])

                        # new_dict["patterns"] = index["patterns"]
                        # new_dict["responses"] = index["responses"]
                    elif islem2 == "2":
                        print("\n\n----\nCevap(Responses):", index["responses"])
                        cevap = input("Eklenecek soruyu yaz: ")
                        index["responses"].append(cevap)
                        print("Başarılı: ",index["responses"])
                    break

    elif islem == "3":
        for veri_ in veri: 
            index = 0
            while True:
            # for index in range(len(veri[veri_])):
            
            
                print("\n\n----\nTag:", veri[veri_][index]["tag"])
                print("Soru(Pattern):", veri[veri_][index]["patterns"], "\n-----", "\nCevap(Responses): ", veri[veri_][index]["responses"], "\n-----\n")
                islem2 = input("Soru Ekle - 1 \nCevap Ekle - 2 \nÖnceki soru - 3 \nSonraki soru - 4\nSoruyu düzenle - 5 \nKaydet ve çık - 6 \nHangi islemi yapacaksın:")
                if islem2 == "1":
                    print("\n\n----\nSoru(Pattern):", veri[veri_][index]["patterns"])
                    soru = input("Eklenecek soruyu yaz: ")
                    veri[veri_][index]["patterns"].append(soru)
                    print("Başarılı: ",veri[veri_][index]["patterns"])

                elif islem2 == "2":
                    print("\n\n----\nCevap(Responses):", veri[veri_][index]["responses"])
                    cevap = input("Eklenecek soruyu yaz: ")
                    veri[veri_][index]["responses"].append(cevap)
                    print("Başarılı: ",veri[veri_][index]["responses"])
                elif islem2 == "3":
                    index -= 2
                    
                    veri[veri_][index]["responses"]
                elif islem2 == "4":
                    continue
                elif islem2 == "5":
                    islem3 = input("Soru sil - 1 \nCevap sil - 2 \nHangi islemi yapacaksın:")
                    if islem3 == "1":
                        print("\n\n----\nindex - Soru(Pattern)")
                        for i,j in enumerate(veri[veri_][index]["patterns"]):
                            print(i, "-", j)
                        soru = int(input("Silenecek olan sorunun index numarası: "))
                        veri[veri_][index]["patterns"].pop(soru)
                        print("Başarılı: ",veri[veri_][index]["patterns"])
                        input("Diğer soruya geçmek için bir butona basın")
                    elif islem3 == "2":
                        print("\n\n----\nindex - Cevap(Responses")
                        for i,j in enumerate(veri[veri_][index]["responses"]):
                            print(i, "-", j)
                        soru = int(input("Silenecek olan cevabın index numarası: "))
                        veri[veri_][index]["responses"].pop(soru)
                        print("Başarılı: ",veri[veri_][index]["responses"])
                        input("Diğer soruya geçmek için bir butona basın")
                
                elif islem2 == "6":
                    break

                index += 1
                
            print("Otomatik kaydetme başlıyor.")
            kaydet(veri)
            veri = yukle()
            print("Kaydedildi.")
    elif islem == "4":
        kaydet(veri)
        veri = yukle()
        print("Kaydedildi. Başarılı.")
