# Uygulama :String ifadelerde cift indexleri buyuk harf, tek indexleri kucuk harf yazmak;


#########################################################################
range(len("string")) #range: iki deger arasinda sayi üretmemizi saglar.


for i in range(len("string")):
    print(i)

#########################################################################


def alternating(string):
    new_string = ""            #Yapilan degisiklikleri buraya kaydetmek istiyoruz.

    for string_index in range(len(string)): #indexlerde gezecegiz.


        if string_index % 2 == 0:  # index cift ise büyük harfe cevir.
            new_string += string[string_index].upper()

        else:  # index cift degil ise kücük harfe cevir.
            new_string += string[string_index].lower()
    print(new_string)


alternating("String")