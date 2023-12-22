# Import des modules

from math import sqrt
import matplotlib.pyplot as plt # Utilisation inspirée du tutoriel : https://datagy.io/python-matplotlib-plot-function/


# Fonctions trinômes utilisables sous leurs différentes formes

def trinomial_func_dev(a, b, c, x):
  return a * x ** 2 + b * x + c

def trinomial_func_canonical(a, alpha, beta, x):
  return a * (x - alpha) ** 2 + beta

def trinomial_func_factored(a, x1, x2, x):
  return a * (x - x1) * (x - x2)


# Formules des propriétés et graphique des trinômes

def discriminant(a, b, c):
  return b ** 2 - 4 * a * c

def quadratic_roots(a, b, c):
  delta = discriminant(a, b, c)
  if delta < 0: return ()
  x1 = (- b + sqrt(delta)) / (2 * a)
  if delta == 0: return (x1,)
  x2 = (- b - sqrt(delta)) / (2 * a)
  return (min(x1, x2), max(x1, x2))

def canonical_form(a, b, c):
  alpha = - b / (2 * a)
  beta = - discriminant(a, b, c) / (4 * a)
  return (alpha, beta)

def graph(a, b, c, xmin, xmax, points):
  inputs = number_range(xmin, xmax, points)
  outputs = [trinomial_func_dev(a, b, c, x) for x in inputs]
  ax = plt.subplots()[1]
  # Afficher les axes d'origine
  ax.axhline(y=0, color='k')
  ax.axvline(x=0, color='k')
  ax.plot(inputs, outputs)
  ax.set_xlim(xmin, xmax)
  ax.set_ylim(min(outputs), max(outputs))
  title = "f(x)=" + str_num(a) + "x²" + str_num_signed(b) + "x" + str_num_signed(c)
  ax.set_title(title, size=14)
  plt.show()


# Étude d'une fonction trinôme

def study(a, b, c, graph_auto = True):
  print("f: x ↦ " + str_num(a) + "x²" + str_num_signed(b) + "x" + str_num_signed(c))
  if a == 0:
    study_degree(b, c)
  else:
    roots = study_roots(a, b, c)
    study_factored_form(a, roots)
    alpha, beta = study_canonical_form(a, b, c)
    study_variations(a, alpha, beta)
    study_sign(a, roots)
    study_parity(alpha)
  study_graph(a, b, c, graph_auto)


# Sections de l'étude de la fonction

def study_degree(b, c):
  print("\n\tDegré du polynôme")
  print("a=0, donc f n'est pas de degré 2. Cela signifie que c'est une fonction affine.")
  print("f(x)=" + str_num(b) + "x" + str_num_signed(c))
  if c == 0:
    print("De plus c=0, donc f est une fonction linéaire.\nDe ce fait, f est une fonction paire.")
    print("f(x)=" + str_num(b) + "x")
  if b == 0:
    print("De plus b=0, donc f est une fonction constante.")
    print("f(x)=" + str_num(c))

def study_roots(a, b, c):
  print("\n\tRacines")
  roots = quadratic_roots(a, b, c)
  delta = discriminant(a, b, c)
  print("Discriminant de l'équation f(x)=0 : Δ=" + str_num(delta))
  match len(roots):
    case 0: print("Δ<0 donc f n'a pas de racines réelles.")
    case 1: print("Δ>0 donc f a une unique racine réelle : x1=x2=" + str_num(roots[0]) + "\nCe qui signifie que :")
    case 2: print("Δ=0 donc f a deux racines réelles : x1=" + str_num(roots[0]) + " et x2=" + str_num(roots[1]) + "\nCe qui signifie que :")
  for root in roots:
    print("f(" + str_num(root) + ")=0")
  return roots

def study_factored_form(a, roots):
  print("\n\tForme factorisée")
  match len(roots):
    case 0: print("L'écriture de f ne peut être factorisée, n'ayant aucune racine réelle.")
    case 1: print("L'écriture de f peut être factorisée : f(x)=" + str_num(a) + "(x" + str_num_signed(-roots[0]) + ")²")
    case 2: print("L'écriture de f peut être factorisée : f(x)=" + str_num(a) + "(x" + str_num_signed(-roots[0]) + ")(x" + str_num_signed(-roots[1]) + ")")

def study_canonical_form(a, b, c):
  print("\n\tForme canonique")
  alpha, beta = canonical_form(a, b, c)
  print("L'écriture de f peut se présenter de manière unique sous la forme canonique, c'est à dire f(x)=a(x-α)+β, avec a=" + str_num(a) + " ; α=" + str_num(alpha) + " ; β=" + str_num(beta))
  print("f(x)=" + str_num(a) + "(x" + str_num_signed(-alpha) + ")" + str_num_signed(beta))
  return alpha, beta

def study_variations(a, alpha, beta):
  print("\n\tVariations de la fonction")
  print("La fonction f atteint un extremum en α qui est de β.")
  if a > 0:
    print("Cet extremum est un minimum car a>0.")
    print("Ainsi la fonction f atteint sur ℝ un minimum de " + str_num(beta) + " en " + str_num(alpha))
    print("f est décroissante sur ]-∞;" + str_num(alpha) + "] et croissante sur [" + str_num(alpha) + ";+∞[")
    print(""" __________________________ 
|        |                 |
|   x    |  -∞    α    +∞  |
|________|_________________|
|        |                 |
|  f(x)  |     ↘  β  ↗     |
|________|_________________|""")
  elif a < 0:
    print("Cet extremum est un maximum car a<0.")
    print("Ainsi la fonction f atteint sur ℝ un maximum de " + str_num(beta) + " en " + str_num(alpha))
    print("f est croissante sur ]-∞;" + str_num(alpha) + "] et décroissante sur [" + str_num(alpha) + ";+∞[")
    print(""" __________________________ 
|        |                 |
|   x    |  -∞    α    +∞  |
|________|_________________|
|        |                 |
|  f(x)  |     ↗  β  ↘     |
|________|_________________|""")

def study_sign(a, roots):
  print("\n\tSigne de la fonction")
  if a > 0:
    print("On a>0 donc f(x) sera négatif lorsque x sera entre les deux racines de f s'il y en a deux, et positif à l'extérieur.")
    ext_sign, int_sign = "+", "-"
  elif a < 0:
    print("On a<0 donc f(x) sera positif lorsque x sera entre les deux racines de f s'il y en a deux, et négatif à l'extérieur.")
    ext_sign, int_sign = "-", "+"
  match len(roots):
    case 0:
      print("Or f n'a aucune racine.")
      print(f""" ______________________ 
|        |             |
|   x    |  -∞     +∞  |
|________|_____________|
|        |             |
|  f(x)  |      {ext_sign}      |
|________|_____________|""")
    case 1:
      print("Or f a pour unique racine : x1=" + str_num(roots[0]))
      print(f""" ____________________________ 
|        |                   |
|   x    |  -∞     x1    +∞  |
|________|___________________|
|        |         |         |
|  f(x)  |     {ext_sign}   0   {ext_sign}     |
|________|_________|_________|""")
    case 2:
      print("Or f a pour racines : x1=" + str_num(roots[0]) + " et x2="+ str_num(roots[1]))
      print(f""" ____________________________________ 
|        |                           |
|   x    |  -∞     x1      x2    +∞  |
|________|___________________________|
|        |         |       |         |
|  f(x)  |     {ext_sign}   0   {int_sign}   0   {ext_sign}     |
|________|_________|_______|_________|""")

def study_graph(a, b, c, auto):
  print("\n\tCourbe représentative")
  print("La courbe représentative de f sera tracée sur l'intervalle [xmin ; xmax], avec")
  if auto:
    xmin, xmax, quantity = -100, 100, 1_000_000
    print(f"xmin={xmin}\nxmax={xmax}\net avec un nombre de points tracés de {quantity}")
  else:
    xmin = float(input("xmin="))
    xmax = float(input("xmax="))
    quantity = int(input("et avec un nombre de points tracés de "))
  print("La courbe représentative de la fonction f sur [" + str_num(xmin) + " ; " + str_num(xmax) + "] est tracée dans une fenêtre graphique à part, le programme reprendra une fois la fenêtre graphique fermée.")
  graph(a, b, c, xmin, xmax, quantity)

def study_parity(alpha):
  print("\n\tParité")
  if alpha==0:
    print("On a α=0 donc f est une fonction paire.")
  else:
    print("On a α≠0 donc f n'est ni paire ni impaire.")


# Fonctions utiles pour manipuler des nombres

# Conversion des nombres en chaînes de caractères, sans décimales pour les entiers
def str_num(n):
  if n == 0: return "0"
  output = str(n)
  if n == int(n):
    output = output.replace(".0", "")
  return output

# Conversion des nombres en chaînes de caractères, sans décimales pour les entiers, et avec leur signe
def str_num_signed(n):
  output = str_num(n)
  if n >= 0:
    output = "+" + output
  return output

# Générer une liste de nombres uniformément répartis entre deux bornes
def number_range(min, max, quantity):
  return [min + x * abs(max - min) / (quantity - 1) for x in range(quantity)]


# Fonction principale du programme avec interface utilisateur ; menu principal

def main():
  while True:
    print("""################################################################################
#                                                                              #
#                 PROGRAMME D'OUTILS POUR POLINÔMES DE DEGRÉ 2                 #
#                                                   Par Momie_et_Masque        #
#                                                                              #
################################################################################
                              f: x ↦ ax²+bx+c, a≠0

Bonjour, quel outil souhaitez-vous utiliser ?
  1 - Étude complète d'une fonction trinôme à partir de son écriture développée
  2 - Calcul de l'image d'un réel par une fonction trinôme donnée sous sa forme développée
  3 - Calcul de l'image d'un réel par une fonction trinôme donnée sous sa forme canonique
  4 - Calcul de l'image d'un réel par une fonction trinôme donnée sous sa forme factorisée
  0 - Quitter le programme""")
    while True:
      choice = input("Votre choix : ")
      try:
        match choice:
          case "0":
            break
          case "1":
            user_study()
          case "2":
            user_dev()
          case "3":
            user_can()
          case "4":
            user_fact()
          case _:
            continue
      except Exception:
        print("\n\nDésolé, une erreur s'est produite. Cela est probablement dû à une valeur incorrecte rentrée par l'utilisateur. Retour au menu principal.")
      print("\n")
      break
    if choice == "0":
      break


# Fonctionnalités du programme avec interface utilisateur

def user_study():
  print("\n\n\t\tÉtude de trinôme du second degré\nSoit une fonction trinôme de la forme f(x)=ax²+bx+c avec pour coefficients :")
  study(float(input("a=")), float(input("b=")), float(input("c=")), False)

def user_dev():
  print("\n\n\t\tImage de réels à partir de la forme développée\nSoit une fonction trinôme de la forme f(x)=ax²+bx+c avec pour coefficients :")
  a, b, c = float(input("a=")), float(input("b=")), float(input("c="))
  print("f: x ↦ " + str_num(a) + "x²" + str_num_signed(b) + "x" + str_num_signed(c))
  while True:
    x = float(input("Calcul de f(x) avec x="))
    print("f(" + str_num(x) + ")=", str_num(trinomial_func_dev(a, b, c, x)))
    if input("Souhaitez-vous continuer à utiliser cette fonction (1) ou revenir au menu principal (0) ?\nVotre choix : ") == "0":
      break

def user_can():
  print("\n\n\t\tImage de réels à partir de la forme canonique\nSoit une fonction trinôme de la forme f(x)=a(x-α)+β avec pour constantes :")
  a, alpha, beta = float(input("a=")), float(input("α=")), float(input("β="))
  print("f: x ↦ " + str_num(a) + "(x" + str_num_signed(-alpha) + ")" + str_num_signed(beta))
  while True:
    x = float(input("Calcul de f(x) avec x="))
    print("f(" + str_num(x) + ")=", str_num(trinomial_func_canonical(a, alpha, beta, x)))
    if input("Souhaitez-vous continuer à utiliser cette fonction (1) ou revenir au menu principal (0) ?\nVotre choix : ") == "0":
      break

def user_fact():
  print("\n\n\t\tImage de réels à partir de la forme factorisée\nSoit une fonction trinôme de la forme f(x)=a(x-x1)(x-x2) avec pour constantes :")
  a, x1, x2 = float(input("a=")), float(input("x1=")), float(input("x2="))
  print("f: x ↦ " + str_num(a) + "(x" + str_num_signed(-x1) + ")(x" + str_num_signed(-x2) + ")")
  while True:
    x = float(input("Calcul de f(x) avec x="))
    print("f(" + str_num(x) + ")=", str_num(trinomial_func_canonical(a, x1, x2, x)))
    if input("Souhaitez-vous continuer à utiliser cette fonction (1) ou revenir au menu principal (0) ?\nVotre choix : ") == "0":
      break


# Corps principal du programme

# Interface utilisateur
main()

# Tests (en commentaire multi-lignes, retirer ou commenter les triples double-guillemets et commenter l'appel à main() ci-dessus pour exécuter les tests plutôt que l'interface utilisateur)
"""
print("Tests")
print("La fonction number_range donne une liste de nombres distribués uniformément entre deux bornes incluses ; elle prend en arguments la borne minimale, la borne maximale et la taille de la liste.")
print(number_range(-100, 100, 20))
print("La fonction graph donne la représentation graphique par le module matplotlib d'une fonction trinôme sous sa forme développée sur un certain intervalle ; elle prend en arguments les coefficients de la fonction, les bornes de l'intervalle de représentation et le nombre de points placés.")
graph(1, 2, 3, -100, 100, 1_000_000)
print("La fonction study() est la fonctionnalité principale du programme, elle donne l'étude complète d'une fonction du second degré en fonction des coefficients de sa forme développée.")
study(1, 0, 0) # fonction carré
study(-1, 0, 1)
study(100, 100, 100)
study(92.697, 775.15, 62.881)
"""