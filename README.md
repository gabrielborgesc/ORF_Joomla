# ORF_Joomla

Script para análise de vulnerabilidades de sites JOOMLA! a partir de suas dependências instaladas.

## Configuração

As versões dos componentes e plugins permitidos e padrões do [Joomla! governamental](https://github.com/joomlagovbr/joomla-3.x) devem ser configurados conforme os arquivos .INI presentes no projeto.

## Execução

Para executar o script basta utilizar o seguinte comando: 

```
python3 getComponentPath.py -i "<Diretório_do_arquivo_zipado_do_site" "<Diretório_do_arquivo_do_banco_de_dados_SQL>"
```
## Dependências

Python 3 (sem nenhuma biblioteca externa).
