# Guia de Instalação

## OpenModelica

Baixar o instalador pelo site: https://openmodelica.org#

## Anaconda

Baixar o instalador pelo site: https://docs.anaconda.com/anaconda/install/

O miniconda pode ser usado alternativamente.

### Configuração do Ambiente Virtual

- Criar um ambiente virtual pelo anaconda com python 3.7.9.

  - Pode ser feito pela interface gráfica (Anaconda Navigator): Environments -> Create -> Python 3.7.9 -> Selecionar o ambiente criado e apertar no botão de play -> Open Terminal. 

- Usar o terminal do ambiente virtual para instalar o PyFMI e executar os scripts.

- O ambiente virtual pode ser acessado pelo terminal através do seguinte comando:

```
conda activate <nome_do_ambiente_virtual>
```
- Para sair do ambiente virtual:

```
conda deactivate
```

### Instalação do do PyFMI

No terminal do ambiente virtual contendo o Python 3.7.9:

```
conda config --add channels conda-forge
conda install pyfmi
```

# Execução dos exemplos contidos neste repositório

No terminal do ambiente virtual contendo o Python 3.7.9, dentro da pasta /src:

```
python <nome_do_exemplo>.py
```

# Documentação

PyFMI: https://jmodelica.org/pyfmi/pyfmi.html

Assimulo: https://jmodelica.org/assimulo/
