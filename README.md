# Guia de Instalação

## OpenModelica

Baixar o instalador pelo site: https://openmodelica.org#

## Anaconda

Baixar o instalador pelo site: https://docs.anaconda.com/anaconda/install/

O miniconda pode ser usado alternativamente (não possui GUI).

### Configuração do Ambiente Virtual

Criar um ambiente virtual pelo anaconda com python 3.7.9.

- Pode ser feito pela interface gráfica (Anaconda Navigator): Environments -> Create -> Python 3.7.9 -> Selecionar o ambiente criado e apertar no botão de play -> Open Terminal. 

Usar o terminal do ambiente virtual para instalar o PyFMI e executar os scripts.

O ambiente virtual pode ser acessado pelo terminal através do seguinte comando:

```
conda activate <nome_do_ambiente_virtual>
```
Para sair do ambiente virtual:

```
conda deactivate
```

### Instalação do do PyFMI

No terminal do ambiente virtual contendo o Python 3.7.9:

```
conda config --add channels conda-forge
conda install pyfmi
```

# Arquivos contidos no repositório:

/src:
- rc_serie.mo -> Código em Modelica do modelo de um circuito RC série.
- exemplo_1.py -> Execução do modelo sem modificar seus parâmentros.
- exemplo_2.py -> Execução do modelo modificando seus parâmetros.
- exemplo_3.py -> Loop simples de feedback e integração com passo fixo do modelo.

/fmu:
- FMU do modelo do circuito RC série usado nas simulações (gerado a partir do código em Modelica). 

Execução dos exemplos:

- No terminal do ambiente virtual contendo o Python 3.7.9, dentro da pasta /src:

```
python <nome_do_exemplo>.py
```

# Documentação

PyFMI: https://jmodelica.org/pyfmi/pyfmi.html

Assimulo: https://jmodelica.org/assimulo/
