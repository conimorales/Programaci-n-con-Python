def es_primo(numero):
  primo = True
  c = 0
  for i in range(1, numero + 1):
    if numero % i == 0:
      c = c + 1
      if c==2:
        primo = True
      else:
        primo = False
  return primo
