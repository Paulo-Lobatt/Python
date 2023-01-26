import os


secret_word = 'sapo'
letters = ''
attempt = 0

while True:
    
    word = input('digite uma letra: ').strip()
    attempt += 1

    if len(word) > 1:
        print('você digitou mais que uma letra')
        continue
    if word in secret_word:
        letters += word

    palavra_formada = ''
    for secret_letter in secret_word:
        if secret_letter in letters:
            palavra_formada += secret_letter
        else:
            palavra_formada += '*'

    print(f'palavra formada: {palavra_formada}')

    if palavra_formada == secret_word:
        os.system('cls')
        print('parabéns, vc ganhou')
        print(f'tentativas: {attempt}')
        secret_word = 'sapo'
        letters = ''
        attempt = 0