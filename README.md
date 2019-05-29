# Tamplate beamer do Insper

Este template foi feito para ser utilizado com o pandoc para conversão de
documentos md em apresentacões pdf.

## Instalação
Esta primeira versão foi feita para distribuições do texlive, futuras
atualizações pretendem deixar a instalação agnostica.

Após clonado o reposiório execute o script `install.py`:

```
$sudo ./install.py
```

ele irá copiar os arquivos necessários para a pasta beamer de sua distro tex

terminada a instalação é necessário atualizar o **filename database** execute o
seguinte comando:

```
$sudo texhash
```

Utilize o exemplo.md como base, para gerar o pdf utilize:

```
$pandoc -t beamer apresentacao.md -o  apresentacao.pdf
```


