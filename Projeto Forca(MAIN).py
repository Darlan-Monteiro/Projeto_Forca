import palavras_forca as pf  
from palavras_forca import palavra_escolhida, palavras_df

letras_usuario = []
chances = 4
ganhou = False
palavra = palavra_escolhida
print('+---------------------------------------+')
print('|  BEM-VINDO(A) AO NOSSO JOGO DA FORCA  |')
print('+---------------------------------------+')
print('INSTRUÇÕES: ','- Você só terá 4 chances para errar, então tenha atenção.','- As palavras são de todos os assuntos.', '- Atenção com a acentuação gráfica, pois há palavras com Â, etc.',sep='\n')
print('+---------------------------------------+\n')
print('       JOGO INICIADO, BOA SORTE.         \n\n')


while True:
  
  for letra in palavra:
    
    if letra.upper() in letras_usuario:
      print(letra, end=' ')
      
    else:
      print('_',end='')
      
  print(f'\n- Você tem {chances} chances')
  
  tentativa = str(input('\n| Digite a letra desejada: '))
  letras_usuario.append(tentativa.upper())
  
  if tentativa.upper() not in palavra.upper():
    chances -= 1
    
  ganhou = True
  
  for letra in palavra:
    
    if letra.upper() not in letras_usuario:
      ganhou = False
      
  if chances == 0 or ganhou:
    break
    
if ganhou:
  print(f'\nParabéns! VocÊ ganhou. A palavra era: {palavra}')

else:
  print(f'\nVocê perdeu! A palavra era: {palavra}')


