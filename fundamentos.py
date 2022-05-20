def nanana():
    print("5 MINUTOS POR DIA")

nanana()

def ela_fala_ingles_ela(arg):
    print(arg)

ela_fala_ingles_ela("Onde? No Duolingo...")

def ele_nao_fala_ingles_ainda(*args):
    print(args)
    print(type(args))

ele_nao_fala_ingles_ainda("Porque ele não usa Duo", "A Lili enche meu saco todo dia", "Quase que ele aprende klingon")

def ele_nao_fala_ingles_ainda(*args):
    for n in args:
        print(n)

ele_nao_fala_ingles_ainda("Porque ele não usa Duo", "A Lili enche meu saco todo dia", "Quase que ele aprende klingon")

def ela_partiu(**kwargs):
    print(type(kwargs))
    print(kwargs)

ela_partiu(dev_sec_ops="E a boticario levou", na_boticario="Não levou não, uhuum")

def ela_partiu(**kwargs):
    for k, v in kwargs.items():
        print(k, v)

ela_partiu(dev_sec_ops="E a boticario levou", na_boticario="Não levou não, uhuum")

def soma(*args):
    print(sum(args))

nums = [1,2,3]
soma(*nums)

def series(**kwargs):
    for nome, ano in kwargs.items():
        print(f"{nome} foi lançada em {ano}")

dict = {
    "Onisciente" : 2020,
    "Better Than Us" : 2018,
    "Mr. Robot" : 2015,
    "Sexify" : 2021,
    "Black Mirror" : 2011,
    "Love, Death and Robots" : 2019
}

series(**dict)