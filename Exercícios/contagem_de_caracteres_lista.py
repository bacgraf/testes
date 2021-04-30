def contar_caracteres(s):
    carac_ord = sorted(s)
    carac_ant = carac_ord[0]

    contagem = 1

    print(s)

    for carac in carac_ord[1:]:
        if carac == carac_ant:
            contagem+=1
        else:
            print (f'{carac_ant}: {contagem}')
            carac_ant = carac
            contagem = 1

    print(f'{carac_ant}: {contagem}')



if __name__ == '__main__':
    contar_caracteres('banana')