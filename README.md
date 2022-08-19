# ThreadTeknofest

İşletme ve kurumlar için yapay zeka tabanlı sohbet botu. #Acıkhack2022TDDİ

Tanıtım videosu: https://youtu.be/AfUKFJE9zsk


## Hızlı başlangıç

Bu projeden esinlerek birşeyler yapmak istersen aşağıdaki adımları uygulayabilirsiniz. Verilerde değişiklik yaparsan bir sonraki başlıktaki veriler için yönergeyi takip etmelisin.

Dosyaları indirmek için bilgisayarınızda git yüklü olmalıdır. MacOs için Terminal'a, Windows için cmd yada powershellde aşağıdaki kod ile projeyi indirebilirsiniz. 

[Git indir](https://git-scm.com/downloads) / [Anaconda indir](https://www.anaconda.com/products/distribution) / [VS Code indir](https://code.visualstudio.com/Download)

Kullanılan kütüphaneler

```
pandas
pandas_datareader
nltk
openpyxl
scikit_learn
snowballstemmer
python-telegram-bot
jupyterlab
unicode_tr
pickle

```


İlk olarak projeyi indirelim.

```
git clone https://github.com/alierenekinci/ThreadTeknofest.git
```

Şimdi ise encv oluşturalım.
```
cd ThreadTeknofest
conda env update -f environment.yml
```

Oluşan Env aktifleştirmek için altaki komutu yazın.

```
conda activate acikhack2022tddi
```
![](https://github.com/alierenekinci/ThreadTeknofest/blob/main/resimler/env-aktif.png)

Gördüğünüz gibi PS(Poweshell) solunda (acikhack2022tddi) yazıyor. Bu şekilde bir sonuça vardıysanız gerekli ortamları yüklediğiniz için şimdi projeyi başlatabilirsiniz.


VS Code(Visual Studio Code)'da indirdiğimiz klasörü açıp gerekli kurulumu yapalım. Daha önce yüklü değilse python eklentisini indirmeniz gerekmektedir. 


![](https://github.com/alierenekinci/ThreadTeknofest/blob/main/resimler/vscode-eklenti.png)


Extensions kısmına gelip python yazarak aratıyoruz. Ve install butonuna basıp kuruyorsunuz.

![](https://github.com/alierenekinci/ThreadTeknofest/blob/main/resimler/vscode-pythoneklenti.png)


Bir .py uzantılı dosyayı açıp sağ altta bulunan kısımdan acikhack2022tddi olan env aktifleştirmeniz gerekmektedir. 

![](https://github.com/alierenekinci/ThreadTeknofest/blob/main/resimler/vscode-env-kismi.png)

[BotFather](https://sendpulse.com/knowledge-base/chatbot/create-telegram-chatbot)dan bir bot oluşturup. Tokeni  "ankarabbHibritChatbot\telegram_bot.py" dosyasında 

```python
BOT_TOKEN = "Tokeni Buraya Yapıştırın"
``` 
satırını değiştirek kendi botunuzla eşleştirebilirsiniz.

![](https://github.com/alierenekinci/ThreadTeknofest/blob/main/resimler/vscode-genel.png)

Tokeninizi atadıktan sonra "ankarabbHibritChatbot\telegram_bot.py" dosyasını sağ üsten çalıştırarak botu başlatabilirsiniz.

![](https://github.com/alierenekinci/ThreadTeknofest/blob/main/resimler/vscode-buton.png)


## Model seçimi:

Modeli seçerken daha önce yapımış olan örnekleri inceleyerek karşılaştırdık. Naive Bayes, Desicion Tree, Random Forest ve SGDClassifier ile yapıldığını gördük. Skorlarını test edip Random Forest ve SGDClassifier kullanmaya karar verdik. İki model kullanmamızın sebebi ise SGDClassifier'da predict_proba olmamasıydı. Sorunu çözmek için yaptığımız araştırmada SGDClassifier için loss fonksiyonunu "hinge" yerine "modified_huber kullandığını gördük. Tek kelimeler için RandomForestClassifer kullanmaya karar verdik. Birden fazla kelimeler içinse SGDClassifier kullandık. İsterseniz aşağıdan bizim verimiz için 

### RandomForestClassifer

RandomForestClassifer'ı tek kelimelik sorgular için kullandım. Çünkü predict_proba ile olasılıksal bir yaklaşımla doğru sonucu bulmaya çalıştım. 
 
Best score: 0.798

Best parameters set:

	clf__criterion: 'gini'
	clf__min_samples_leaf: 1
	clf__n_estimators: 100
	tfidf__norm: 'l2'
	tfidf__use_idf: False
	vect__max_df: 0.5
	vect__max_features: 10000

### SGDClassifier

SGDClassifier loss fonksiyonu için ön tanımlı olarak hinge kullanıyor. Bundan dolayı tek kelime ile yazılan cevapları doğru tahmin etmek için kullanığımız olasıksal yaklaşımda kullandığımız predict_proba() metodu SGDClassifier'da "modifed_huber" olduğunda çalışmaktaymış. Bundan terasyon ile GridSearchCV ile en iyi loss fonksiyonu bulmaya çalıştım. 

- İlk iterasyon default olarak loss= ("hinge",)
Best score (Cross Validation = 10): 0.857

Best parameters set:

	clf__alpha: 1e-05
	clf__max_iter: 80
	clf__penalty: 'l2'
	tfidf__norm: 'l1'
	tfidf__use_idf: False
	vect__max_df: 0.5
	vect__max_features: 5000
	vect__ngram_range: (1, 1)


- İkinci iterasyon loss= ("modified_huber", "hinge")
Best score (Cross Validation = 10): 0.855

Best parameters set:

	clf__alpha: 1e-05
	clf__loss: 'hinge'
	clf__max_iter: 50
	clf__penalty: 'elasticnet'
	tfidf__norm: 'l1'
	tfidf__use_idf: False
	vect__max_df: 1.0
	vect__max_features: 50000
	vect__ngram_range: (1, 1)

- Üçüncü iterasyon loss = ("modified_huber",) modified_huber ile 
Best score (Cross Validation = 10): 0.832

Best parameters set:

	clf__alpha: 1e-05
	clf__loss: 'modified_huber'
	clf__max_iter: 50
	clf__penalty: 'l2'
	tfidf__norm: 'l1'
	tfidf__use_idf: False
	vect__max_df: 0.5
	vect__max_features: None
	vect__ngram_range: (1, 1)

Daha yüksek skorundan dolayı birden çok kelime içeren metinlerde SGDClassifier tercih ettik.
 
## Veri eklemek veya çıkarmak istiyorum. Hangi adımları uygulamalıyım.

Yeni veri eklemek için veri klasöründe ankarabbSoruCevapVeriSeti-v02 adlı excel dosyasını kullanabilirsiniz.

![](https://github.com/alierenekinci/ThreadTeknofest/blob/main/resimler/excel-verilerin-kaydedilmesi.png)

Tabloya bakacak olursak her yeni etiket için cevap var. Birbirine benzeyen soruların gruplandırması için ilk soruya benzersiz bir etiket atamanız gerekmekte. Etiket atanan satırdaki verinin cevabı bir sonraki etikete kadar olan soruların cevabıdır. Bu tarzda verileri kaydetmemizin sebebi verileri aşağıdaki gibi kaydetmek istememiz.

![](https://github.com/alierenekinci/ThreadTeknofest/blob/main/resimler/veri-json.png)

Uygun şekilde kaydettikten sonra projenin bulunduğu klasörde terminali açınız

```
jupyter lab
```

yazınız.

![](https://github.com/alierenekinci/ThreadTeknofest/blob/main/resimler/jupyterlab-link.png)

Eğer tarayıcıda jupyter lab otomatik olarak açılmaz ise linke Control+Click ile açabilirsiniz 

İlk olarak egitim klasöründeki jupyter lab'ta soru_birlestirme.ipynb dosyasını çalıştırmalısınız.

![](https://github.com/alierenekinci/ThreadTeknofest/blob/main/resimler/jupyterlab-soru_birlestirme.png)

Daha sonra verilerinin önişlemesini yapması için aynı klasördeki veri_onisleme.ipynb dosyasını çalıştırmalısınız.

![](https://github.com/alierenekinci/ThreadTeknofest/blob/main/resimler/jupyterlab-veri_onisleme.png)


## Çalışma Listem:

- [x] Problem Belirle
- [x] Çözüm için literatür ve blog sayfalarında uygulanmış çözüm yollarına bak
- [x] Büyükşehir belediyesinin verileri topla
- [x] Veriyi genişlet
- [x] Verileri json veritipine çevir.
- [x] Veri düzenleme aracı yaz.
- [x] Verilerin kabaca önişlemesini yap.
- [x] stopwordlerin temizlenmesi
- [x] ngram(bigram) uygulanması
- [x] Kural Tabanlı olarak cevap sistemleri araştır.
- [x] AIML python kütüphanesi araştır.
- [x] AIML kütüphanesi xml tabanlı çalışıyor. Kendi ufak bir prototip geliştir.
- [x] Kısa sorulara cevap veren AIML alternatifi kural tabanlı yazılım için ek özellikler geliştirmeye çalış.
- [x] Yapay Zeka kullanarak yapılmış chatbotları incele.
- [x] Yapay Sinir Ağı oluşturulan chatbotları dene. (Bizim verimizde iyi çalışmadı)
- [x] Bert modeli ve lstm modellerine bak
- [x] Derin Öğrenme algoritmaları çalış
- [x] Sözlük veya tfidf değeri düşük olunca anlamadım mesajı(hangi kümede olduğunun olasılık değerinden yola çıkılarak cevap verme mekanizması eklendi)
- [x] Modellerin karşılaştırması.
- [ ] Sistem kendine update etsin, dışarıdan soru gelince kaydetme(acil - ama yetişmedi)
- [ ] morfolojik analiz eklenip eklenmemesine karar verilmesi(yetişmedi)
- [ ] vnlp ile stemmer in tekrardan düzenlenmesi (tutarlı olup olmadığına karar veremedik)

Gelecekte ne yapabiliriz. 
- [ ] Konumsal dizinleme yapmak istiyoruz.
- [ ] Önişleme adımlarını daha doğru şekilde yapmak istiyoruz.
- [ ] Doğal dil modeli kullanıp yaptığımız model ile arasındaki farkı bulmak istiyoruz.
- [ ] Eşanlamlı sözcüklerle sorgu listesi yapıp daha tutarlı sonuçlar almak istiyoruz.


“Millî hedef belli olmuştur. Ona ulaşacak yolları bulmak zor değildir. Önemli olan, çetin olan o yollar üzerinde çalışmaktır. Denebilir ki hiçbir şeye muhtaç değiliz. Yalnız tek bir şeye çok ihtiyacımız vardır: Çalışkan olmak. Toplumsal hastalıklarımızı incelersek temel olarak bundan başka, bundan önemli bir hastalık keşfedemeyiz; hastalık budur. O halde ilk işimiz bu hastalığı esaslı bir şekilde tedavi etmektir. Milleti çalışkan yapmaktır. Servet ve onun doğal sonucu olan refah ve mutluluk, yalnız ve ancak çalışkanların hakkıdır” - **Mustafa Kemal Atatürk**