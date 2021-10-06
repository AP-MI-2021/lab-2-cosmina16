def prim(n):
    '''
    verifica daca numarul e prim
    :param n: intreg
    :return: true daca e prim ,false in caz contrar
    '''
    if n<2:
        return False
    if n==2:
        return True
    if n%2==0:
        return False
    for i in range(3,n):
        if n%i==0:
            return False
    return True

def is_superprime(n):

    '''
    verifica daca n este superprim
    :param n: intreg
    :return: true daca n e superprim ,fals altfel
    '''
    ok = True
    while n and ok:
        if prim(n):
            n//=10
        else:
            ok = False
    return ok

def test_is_superprime():
    assert is_superprime(233) is True
    assert is_superprime(237) is False



def main():
    merge = True
    while merge:
        print('1. Verifica daca n este superprim')
        print('x.iesire')
        optiune = input('Dati una din optiuni')
        if optiune == '1':
            test_is_superprime()
            n = int(input('dati un numar'))
            if is_superprime(n):
                print('nr e superprim')
            else:
                print('nr nu e superprim')
        elif optiune == "x":
            merge= False



if __name__ == '__main__':
    main()