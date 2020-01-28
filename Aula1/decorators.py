#!/usr/bin/env python3


def modifica_cor(texto):
    def altera(texto):
        return f'\033[91m{texto}\033[0m'
    return altera


@modifica_cor
def texto(fala: str) -> str:
    return fala


print(texto('Oi'))
