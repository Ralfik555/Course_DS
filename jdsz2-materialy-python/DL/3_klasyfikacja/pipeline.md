### Przygotowanie:
- pobrani danych i umieszczeniu w katalogu data https://www.dropbox.com/s/58pubhbzrze3fbp/data.zip?dl=0)
- Skopiowanie plików: bottleneck_features_2.py  data_augmentation_0.py  fine_tune_3.py  small_convnet_1.py  train_top_model_2.py

Zainicjowanie projektu w gicie i dvc

```console
git init
dvc init
```

1) Dodanie folderu data do dvc
```console
dvc add data 
```

2) Model konwolucyjny (podstawowy od zera), w wyniku którego otrzymamy conv_model.h5
```console
python small_convnet_1.py
```
3) Trnsformata wyuczonego modelu VGG
```console
dvc run --no-exec -f bottleneck_features.dvc -d bottleneck_features_2.py -d data -o bottleneck_features_train.npy -o bottleneck_features_validation.npy python bottleneck_features_2.py
```
4) Douczenie modelu VGG do naszych danych
```console
dvc run --no-exec -d bottleneck_features_train.npy -d bottleneck_features_validation.npy -d train_top_model_2.py -o fc_model.h5 -o logs/fc python train_top_model_2.py

```
5) Douczenie modelu uzyskanego w poprzednnim punkcie poporzez odmoro¿enie ostatnich warstw i skorzystanie z generatora (final tuning)
```console
dvc run --no-exec -d data -d fc_model.h5 -o vgg_model.h5 -o logs/vgg python fine_tune_3.py
```
6) Uruchomienie ca³ego pipeline
```console
dvc repro vgg_model.h5.dvc
```
#### Dodatkowo:
Podgl¹d pipeline (grafu):
```console
dvc pipeline show --ascii fc_model.h5.dvc
```
Logi z tensorboard:
```console
tensorboard --logdir=logs
```

