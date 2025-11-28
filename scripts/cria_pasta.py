import argparse
from pathlib import Path

parser = argparse.ArgumentParser()


parser.add_argument("caminho_pasta")
parser.add_argument("nome_arquivo")
args = parser.parse_args()
print(args.nome_arquivo, args.caminho_pasta)

caminho_pasta = Path(args.caminho_pasta)
if not caminho_pasta.is_dir(): 
    print(f'{caminho_pasta} não é um caminho válido.')
