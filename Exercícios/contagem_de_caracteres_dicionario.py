def contar_caracteres(s):


    resultado={}

    print(s)

    for carac in s:
        contagem = resultado.get(carac,0)
        contagem +=1
        resultado[carac]=contagem



    return resultado

if __name__ == '__main__':
    print(contar_caracteres('banana'))