# ORF_Joomla

Script para análise de vulnerabilidades de sites JOOMLA! a partir de suas dependências instaladas.

## Dependências

Python 3 (sem nenhuma biblioteca externa).

## Configuração

As versões dos componentes e plugins permitidos e padrões do [Joomla! governamental](https://github.com/joomlagovbr/joomla-3.x) devem ser configurados conforme os arquivos .INI presentes no projeto.


## Execução

Para executar o script basta utilizar o seguinte comando: 

```
python3 main.py -i "<Diretório_do_arquivo_zipado_do_site" "<Diretório_do_arquivo_do_banco_de_dados_SQL>"
```

## Resultado

São gerados 6 relatórios no formato csv acerca dos componentes e plugins não permitidos, além dos permitidos com versões atualizadas e os permitos com versões desatualizadas, ambos na pasta Resultados.
