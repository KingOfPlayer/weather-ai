# Weather Ai

Bu repoda, memostat.net ve wunderground.com sitelerinden hava durumu verilerinin kazındığı uygulamlar bulunmaktadır. Yazılan uygulamalar python dilini kullanıp, veri kazıma işlemleri için hem Selenium tabanlı web otomasyonunu hem de API entegrasyonlarını kullanmaktadır. Elde edilen veriler, analiz ve kullanım kolaylığı için JSON formatında saklanmaktadır.

JSON formatındaki hava durumu verilerin eksik datalara sahip ve analizlenmesi için uygulama bulunmaktadır. Statsmodels kütüphanesi ile trend ve mevsimselik özelikleri analiz edilmiş, Pandas kütüphanesi kullanılarak veri yönetimi  ve eksik verilerin doldurumu yapılmış, Matplotlib kütüphanesi ile verilerin grafikleştirilmesi sağlanmıştır.

[Veri Seti](https://drive.google.com/drive/folders/1iqY6zHObihoX9fCWXMg01quh8xI29JfK?usp=sharing)

# Yapay Zeka Modelleri
Yapay zeka modelleri [Time-Series-Library](https://github.com/thuml/Time-Series-Library) kütüphanesinin sağladığı Informer, Reformer, TFT, Autoformer ve FEDFormer kullanılarak oluşturulmuştur. Oluşturulan yapay zeka modelleri Colab ortamında eğitilip değerlendirilmesi yapılmıştır.  
Not: Colab ortamına [Buradan](https://drive.google.com/drive/folders/1iqY6zHObihoX9fCWXMg01quh8xI29JfK?usp=sharing) elde edilen verileri ana dizin (contents) klsörüne atıp notebookta bazı alanları buna göre düzenlemelisiniz
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/18GSl5PtQnZrLj1NpByhLgINp7qCoh--a?usp=sharing)  

