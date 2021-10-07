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

def det_putere_10(n):
    putere=1
    while n>9:
        putere*=10
        n//=10
    return putere

def is_antipalindrome(n):
    '''
    Verifica daca un numar este antipalindrom
    :param n: un numar intreg
    :return: true daca numarul este antipalindorm sau false in caz contrar
    '''
    putere1=det_putere_10(n)
    putere2=1
    while putere1>putere2*10:
        if (n//putere1)%10==(n//putere2)%10:
            return False
        else:
            putere1//=10
            putere2*=10
    if putere1==putere2*10 and (n//putere1)%10==(n//(putere2))%10:
        return False
    return True

def get_base_2(n):  #de ce e string in cerinta??
    '''
    trece din baza 10 in baza 2 un numar
    :param n: numarul citit
    :return: returneaza numarul in baza 2
    '''
    r =0
    p=1
    nr=0
    while n!=0:
        r=n%2
        n//=2
        nr=nr+r*p
        p*=10
    return nr



def test_is_superprime():
    assert is_superprime(233) is True
    assert is_superprime(237) is False


def test_is_antipalindrome():
    assert is_antipalindrome(2773) is False
    assert is_antipalindrome(2783) is True

def test_get_base_16_from_2():
    assert get_base_2(20)==10100
    assert get_base_2(100)==1100100



def main():
    merge = True
    while merge:
        print('1. Verifica daca n este superprim')
        print('2.Verifica daca n este antipalindorm')
        print('3.trecere din baza 10 in baza 2')
        print('x.iesire')
        optiune = input('Dati una din optiuni')
        if optiune == "1":
            test_is_superprime()
            n = int(input('dati un numar'))
            if is_superprime(n):
                print('nr e superprim')
            else:
                print('nr nu e superprim')
        elif optiune=="2":
            test_is_antipalindrome()
            n = int(input('dati un numar '))
            if is_antipalindrome(n):
                print('este antipalindrom ')
            else:
                print('nu e antipalindrom')
        elif optiune == "3":
            test_get_base_16_from_2()
            n = int(input('dati un numar'))
            print(get_base_2(n))
        elif optiune == "x":
            merge= False

if __name__ =='__main__':
    main()