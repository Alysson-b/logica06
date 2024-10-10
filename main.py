login = 'infinity'
password = '1234'

tentativas = 3

for i in range(tentativas):
    usuario = input('Digite o nome do usuario')
    senha = input('Digite sua senha')

    if usuario == login and password == senha:
        print(f"Seja bem vindo, {usuario}")
        break
    else:
        tentativas_rest = tentativas - (i + 1)
        if tentativas_rest > 0:
            print(f'login ou senha incorreto: voçe tem {tentativas_rest} tentativas restantes.') 
        else:
            for _ in range(1):
                print('acesso bloqueado.')    
