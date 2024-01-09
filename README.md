# ExtratorURL

Este projeto implementa a classe `ExtratorURL`, originalmente aprendida durante o curso "Aprenda a programar em Python com Orientação a Objetos" na plataforma Alura. A classe foi adaptada e personalizada para atender a requisitos específicos, com melhorias e modificações feitas por mim.

## Descrição

A classe `ExtratorURL` foi projetada para extrair informações de URLs relacionadas a câmbio do site "bytebank.com". Ela realiza a sanitização, validação e extração de partes da URL, além de fornecer métodos para interação e conversão de valores.

## Alterações Realizadas

Durante a adaptação do código, foram feitas as seguintes alterações:

- Adição de métodos para melhorar a funcionalidade.
- Melhorias na legibilidade do código.
- Personalização para atender a requisitos específicos.

## Exemplos de Uso

```python
# Exemplo de uso da classe ExtratorURL
url = " bytebank.com/cambio?quantidade=100&moedaOrigem=dolar&moedaDestino=real"
extrator_url = ExtratorURL(url)

print(extrator_url)
print("Tamanho da URL: ", len(extrator_url))

quantidade = extrator_url.get_valor_parametro("quantidade")
print(f"Quantidade moeda: {quantidade}")

moeda_convertida = extrator_url.conversor(5.00)
print(moeda_convertida)