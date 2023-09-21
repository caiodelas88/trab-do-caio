#professor se quiser mudar a função troque os valores do return
def f(x):
    return 3 * x - 1

#professor se quiser mudar a função troque os valores do return
def g(x):
    return x+2 

def composicao_f_g(x):
    resultado_g = g(x)
    resultado_f_g = f(resultado_g)
    return resultado_f_g

def composicao_g_f(x):
    resultado_f = f(x)
    resultado_g_f = g(resultado_f)
    return resultado_g_f

from sympy import symbols, simplify

x_generico = symbols('x')

composicao_f_g_resultado = composicao_f_g(x_generico)
composicao_g_f_resultado = composicao_g_f(x_generico)

composicao_f_g_simplificada = simplify(composicao_f_g_resultado)
composicao_g_f_simplificada = simplify(composicao_g_f_resultado)

print("f ∘ g(x) =", composicao_f_g_simplificada)
print("g ∘ f(x) =", composicao_g_f_simplificada)
