import re

class ExtratorURL:
    def __init__(self, url):
        self._url = self.sanitiza_url(url)
        self.valida_url()

    def sanitiza_url(self, url):
        return url.strip() if isinstance(url, str) else ""

    def valida_url(self):
        if not self._url:
            raise ValueError("A URL está vazia.")

        padrao_url = re.compile("(http(s)?://)?(www.)?bytebank.com(.br)?/cambio")
        match = padrao_url.match(self._url)
        if not match:
            raise ValueError("A URL não é válida.")

    def url_base(self):
        return self._url.split("?")[0]

    def url_parametros(self):
        return self._url.split("?")[1] if "?" in self._url else ""

    def __str__(self):
        return f"{self._url} \nURL Base: {self.url_base()} \nParâmetros: {self.url_parametros()}"

    def __len__(self):
        return len(self._url)

    def __eq__(self, other):
        return self._url == other._url

    def get_valor_parametro(self, nome_parametro):
        parametros = self.url_parametros().split("&")
        for parametro in parametros:
            if nome_parametro in parametro:
                return parametro.split("=")[1]

    def conversor(self, valor_dolar):
        moeda_origem = self.get_valor_parametro("moedaOrigem")
        quantidade = float(self.get_valor_parametro("quantidade"))
        valor_convertido = round(quantidade * valor_dolar, 2) if moeda_origem == "dolar" else round(
            quantidade / valor_dolar, 2)
        return f"{valor_convertido:.2f} {"reais" if moeda_origem == "dolar" else "dólares"}"