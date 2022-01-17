#url = "http://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100"
url = " "

url = url.replace(" ", "")# trocando " " por ""

if url == "":
    raise ValueError("Url esta vazia")

indice_interrogacao = url.find("?") # procurando caractere na variavel
url_base = url[0:indice_interrogacao] # dividindo a url da posição 0 ate a 19(sem contar o 0)
print(url_base)

url_parametro = url[indice_interrogacao+1:]# sem passar o 2º parametro ele entende como ultimo caracter
print(url_parametro)

parametro_busca = "moedaOrigem"
indice_parametro = url_parametro.find(parametro_busca)
indice_valor = indice_parametro + len(parametro_busca)+1
indice_e_comercial = url_parametro.find("&", indice_valor) # encontrar & a partir de indice_valor

if indice_e_comercial == -1:
    valor = url_parametro[indice_valor:]
else:
    valor = url_parametro[indice_valor:indice_e_comercial]

print(valor)