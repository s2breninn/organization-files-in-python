import os
import pathlib
import shutil

caminho_raiz = os.getcwd()

#Pegando a última pasta
ultima_pasta = caminho_raiz.split('/')[-1]

path = pathlib.Path(os.getcwd())

for filename in path.glob("*"):
    print(filename.suffix)

sufixos = {filepath.suffix[1:] for filepath in path.glob('*')}
print(sufixos)

"""
for sufixo in sufixos:
    os.mkdir(sufixo)
"""

while os.path.isfile(os.getcwd()) and not {sufixo for sufixo in sufixos if sufixo == 'py' }:
    ...
