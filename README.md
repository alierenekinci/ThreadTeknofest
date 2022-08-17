# ThreadTeknofest

İşletme ve kurumlar için yapay zeka tabanlı sohbet botu. #Acıkhack2022TDDİ


## Botu çalıştırmak

Bende denemek istiyorum. Bu projeden esinlerek birşeyler yapmak istersen aşağıdaki adımları uygulayabilirsiniz.

Dosyaları indirmek için bilgisayarınzda git yüklü olmalıdır. MacOs için Terminal'a, Windows için cmd yada powershellde aşağıdaki kod ile projeyi indirebilirsiniz. 
```
git clone https://github.com/alierenekinci/ThreadTeknofest.git
```


Ben env oluşturmak için conda kullanıyorum. Conda açık kaynaklı paket ve ortam yöneticisidir. Env oluşturmak için:
```
conda create -n acikhack2022tddi python=3.9

```
![](https://github.com/alierenekinci/ThreadTeknofest/blob/main/resimler/env-olusturma.png)

![](https://github.com/alierenekinci/ThreadTeknofest/blob/main/resimler/env-onay.png)
Onaylamak için 'y' yazıp enter'e  basın.


Env aktifleştirmek ve gerekli kütüphaneleri yüklemek için aşağıdaki komutları kullanabilirsiniz.



```
conda activate acikhack2022tddi
```
![](https://github.com/alierenekinci/ThreadTeknofest/blob/main/resimler/env-aktif.png)

Gördüğünüz gibi PS(Poweshell) solunda (acikhack2022tddi) yazıyor. Şimdi gerekli paketleri indirmek için aşağıdaki komutu kullanın.

```
cd ThreadTeknofest
conda env update -f environment.yml
```

[BotFather](https://sendpulse.com/knowledge-base/chatbot/create-telegram-chatbot)dan bir bot oluşturup. Tokeni  "ankarabbHibritChatbot\telegram_bot.py" dosyasında 

```python
Token = "Tokeni Buraya Yapıştırın"
``` 
satırını değiştirek kendi botunuzla çalışabilirsiniz. 

Todo:
[] Sistem kendine update etsin, dışarıdan soru gelince kaydetme
[] Stopword
[] Sözlük veya tfidf değeri düşük olunca anlamadım mesajı
