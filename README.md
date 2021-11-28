# encontrando_gatos
Exemplo de detecção de gatos em vídeos com [detectron2](https://github.com/facebookresearch/detectron2)


# Link do colab
https://colab.research.google.com/drive/12imCh4vaslov4AlNVjWQgsi0IAmawVi6?usp=sharing

# Instruções

Copie este repositório

Siga as [instruções de instalação](https://detectron2.readthedocs.io/en/latest/tutorials/install.html) do detectron.

Caso não tenha placa de vídeo compátivel com cuda, utilize a versão para CPU(mais lenta) ou rode no colab.

```
python -m pip install detectron2 -f https://dl.fbaipublicfiles.com/detectron2/wheels/cpu/torch1.10/index.html
```

Instale o opencv, torchvision e o torch

```
pip install opencv-python torch==1.10.0
```

A base de dados está na pasta "base_dados" e contém 10 vídeos, 5 com gatos e 5 sem gatos para testarmos a aplicação.

Rode com o comando:
```
python encontra_gatos.py
```
ou, dependendo do seu sistema,
```
python3 encontra_gatos.py
```