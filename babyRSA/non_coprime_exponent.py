from math import gcd

def find_generator_of_subgroup(e, p):
    phi_prime = (p-1)//e
    g = 1
    g_E = 1
    while g_E == 1:
        g += 1
        g_E = pow(g, phi_prime, p)
    return g_E

def find_set_of_possible_plaintexts(e, p, c):
    assert (p-1) % e == 0
    assert gcd((p-1)//e, e) == 1
    phi_prime = (p-1)//e
    d = pow(e, -1, phi_prime)
    a = pow(c, d, p)
    g_E = find_generator_of_subgroup(e, p)
    l = 1

    set_of_possible_plaintext = []
    for i in range(e):
        x = (a * l) % p
        set_of_possible_plaintext.append(x)
        l = (l * g_E) % p
    return set_of_possible_plaintext

def find_set_of_possible_plaintexts_variant(e, p, c, e2, p2):
    assert (p-1) % e == 0
    assert gcd((p-1)//e, e) == 1
    phi_prime = (p-1)//e
    d = pow(e, -1, phi_prime)
    a = pow(c, d, p)
    g_E = find_generator_of_subgroup(e, p)
    l = 1

    phi_prime2 = (p2-1)//e2

    set_of_possible_plaintext = []
    for i in range(e):
        x = (a * l) % p
        # Verify if the obtained plaintext is desired.
        if pow(x, phi_prime2, p2) == 1:
            set_of_possible_plaintext.append(x)
        l = (l * g_E) % p
    return set_of_possible_plaintext