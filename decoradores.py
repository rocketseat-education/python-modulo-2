def meu_decorator(func):
  def wrapper():
    print("Antes da função ser chamada")
    func()
    print("Depois da função ser chamada")
  return wrapper

@meu_decorator
def minha_funcao():
  print("Minha função foi chamada")

minha_funcao()

class MeuDecoradorDeClasse:
  def __init__(self, func) -> None:
    self.func = func

  def __call__(self) -> any:
    print("Antes da função ser chamada (decorador de classe)")
    self.func()
    print("Depois da função ser chamada (decorador de classe)")

@MeuDecoradorDeClasse
def segunda_funcao():
  print("Segunda função foi chamada")

segunda_funcao()