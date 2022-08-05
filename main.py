while True:
    try:
        x = float(input('Insira um valor : '))
        if x < 0:
            raise Exception('Proibido valor negativo')
        else:
            print(f'Tudo certo.Seu valor é {x}')
            break
    except ValueError:
        print('Somente numeros são permitidos')
    except Exception as e:
        print(e)
    finally:
        print('Finally\n')

print('Fim do while')
