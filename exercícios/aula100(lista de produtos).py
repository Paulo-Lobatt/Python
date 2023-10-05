import copy

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

for produto in produtos:
    print('-------------------------------')
    print(produto)
print('============================================================')
#lista normal ^





new_produto_price = copy.deepcopy(produtos)

porcentagem = 10
for produto in new_produto_price:
    price = produto['preco']
    additional_value = (porcentagem / 100) * price
    produto['preco'] += additional_value
    print(produto)
    print('-------------------------------')
print('============================================================')
#lista +10% ^





new_order = copy.deepcopy(new_produto_price)
new_order = sorted(new_order, key=lambda x: x['nome'], reverse=True)

for produto in new_order:
    print(produto)
    print('-------------------------------')
print('============================================================')
#new order ^

new_reverser_order = copy.deepcopy(new_order)
new_reverser_order = sorted(new_reverser_order, key=lambda x: x['preco'])

for produto in new_reverser_order:
    print(produto)
    print('-------------------------------')
print('============================================================')



# copy, sorted, produtos.sort ✅
# Exercícios ✅
# Aumente os preços dos produtos a seguir em 10% ✅
# Gere novos_produtos por deep copy (cópia profunda) ✅

# Ordene os produtos por nome decrescente (do maior para menor) ✅
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda) ✅

# Ordene os produtos por preco crescente (do menor para maior) ✅
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda) ✅

# new_produtos = produtos.sort

# print(new_produtos)