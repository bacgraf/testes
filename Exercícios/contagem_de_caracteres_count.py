def contar_caracteres(s):

    resultado={}

    print(s)

    for carac in s:
        resultado[carac] = s.count(carac)


    return resultado



if __name__ == '__main__':
    print(contar_caracteres('banana com chocolate   '))
    print(contar_caracteres('alojamento'))