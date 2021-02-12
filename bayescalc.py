# Calculadora do Teorema de Bayes em Python.
# Por Lucas Silveira Campos (lsc-g1t)

print("\n\n#### Seja bem-vindo(a) ####")

print("\n#### Este projeto foi feito para simplificar contas do Teorema de Bayes ####")

print("\n\n Vamos começar")

panome = input("\nDigite um nome para a variavel P(A): ")

pbnome = input("\nDigite um nome para a variavel P(B): ")

print(f"\nP({panome}/{pbnome}) = [ P({pbnome}/{panome}) * P({panome}) ] / P({pbnome})")

proba = input(f"\n\nDigite a probabilidade do evento {panome}: ")

probb = input(f"\n\nDigite a probabilidade do evento {pbnome}: ")

probba = input(f"\n\nDigite a probabilidade do evento {pbnome}/{panome}: ")

resproba = eval(proba)

resprobb = eval(probb)

resprobba = eval(probba)

probab = ((resprobba * resproba)/resprobb)*100

print(f"\n\nResposta: P({panome}/{pbnome}) = {probab}%\n\n")
