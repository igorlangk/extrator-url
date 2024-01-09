from extrator_url import ExtratorURL

url = " bytebank.com/cambio?quantidade=100&moedaOrigem=dolar&moedaDestino=real"
extrator_url = ExtratorURL(url)

print(extrator_url)
print("Tamanho da URL: ", len(extrator_url))

quantidade = extrator_url.get_valor_parametro("quantidade")
print(f"Quantidade moeda: {quantidade}")

moeda_convertida = extrator_url.conversor(5.00)
print(moeda_convertida)
