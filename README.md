# As minhas tarefas

Este repo é um fork de https://github.com/jakerieger/FlaskIntroduction, funciona com versões do `Python v3.8` para cima.

## Objetivo

O objetivo inicial deste fork é aprender mais sobre o desevolvimento web com Python ao usar o framework Flask.

## Menções

Este projeto é baseado num fork do auto https://github.com/jakerieger

### Como correr este projeto

Abrir o terminal do projeto e na pasta do mesmo, correr os seguintes comandos:
1) Instalar o `virtualenv`, o ambiente virtual para correr o projeto;
2) Iniciar `virtualenv`, e o nome da pasta como (env)
3) Ativar os serviços
4) Instalar as dependências necessárias para correr os serviços
5) Iniciar o servidor Flask
``` 
$ pip install virtualenv
```
```
$ virtualenv env
```
Para máquinas com Windows 
```
$ .\env\Scripts\activate
```
Para máquinas com Linux 3.2
```
$ source env/bin/activate
```
Instalar os requisitos
```
$ (env) pip install -r requirements.txt
```
Iniciar o servidor 
```
$ (env) python app.py
```
O servidor vai correr por defeito na porta 5050, de forma a evitar confusões com outros servidores
Mas podem alterar essa configuração no ficheiro app.py
```python
if __name__ == "__main__":
    app.run(debug=True, port=<desired port>)
```
