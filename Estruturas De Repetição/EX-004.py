
produtos = [
    "Camiseta",
    "Calça Jeans",
    "Tênis",
    "Celular",
    "Notebook",
    "Mochila",
    "Fone de Ouvido",
    "Relógio",
    "Óculos de Sol",
    "Câmera Fotográfica",
    "Ferro de Passar",
    "Panela de Pressão",
    "Liquidificador",
    "Smart TV",
    "Tablet",
    "Bicicleta",
    "Perfume",
    "Sapato",
    "Chapéu",
    "Livro",
    "Mesa",
    "Cadeira",
    "Colchão",
    "Escova de Dentes",
    "Shampoo"
]


precos_fixos = [
    29.99,   
    79.99,   
    99.99,   
    399.99,  
    999.99,  
    49.99,       
    39.99,   
    149.99,      
    129.99,  
    299.99,      
    39.99,   
    79.99,   
    89.99,   
    799.99,  
    199.99,  
    349.99,  
    89.99,   
    69.99,   
    19.99,   
    24.99,   
    149.99,  
    99.99,   
    449.99,  
    4.99,    
    14.99    
]


for i, produto in enumerate(produtos):
    print(f'{produto}: {precos_fixos[i]}')