"""
ANY and ALL:

 - all() -> retorna True se todos os elementos do iterável são verdadeiros ou se o iterável está vazio;
 - verifica se todos são True;

#Exemplo ALL:

print(all([0, 1, 2, 3, 4]))  #Todos os numeros são verdadeiros? False == 0;
print(all([1, 2, 3, 4]))

nomes = ['Carlos', 'Cristina', 'Caciane', 'Cleide', 'Celso']
print(all(nome[0] == 'C' for nome in nomes))
#Bom para fazer checagens;

--

- any() -> retorna True se qualquer elemento do iterável for verdadeiro;

"""

print(any([0, 1, 2, 3, 4, 5, 0]))

print(any([0, False, {}, (), []]))

nomes = ['Carlos', 'Cristina', 'Caciane', 'Cleide', 'Celso', 'Vanessa']
print(any([nome[0] == 'C' for nome in nomes]))

# <>
print(all([nome[0] == 'C' for nome in nomes]))
