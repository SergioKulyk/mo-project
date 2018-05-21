from team5.lib5.Team5 import *


# Виводимо результат методу
def print_res(method_name="none", res=None):
    print()
    print("-" * 50, "\n")
    print(method_name)
    print(res)
    print("\n", "-" * 50)
    print()


# Тестовий приклад
def f(x):
    return (x[0] + 2 * x[1] - 7) ** 2 + (2 * x[0] + x[1] - 5) ** 2


# Створюємо обєкт класа Team5
team5 = Team5()

# ----------------------------------------------------------
# Тест методу рою частинок
s = 40
d = 2

swarm_parties_name = "Метод рою частинок"
swarm_parties_res = team5.swarm_parties(s, d, f)

print_res(swarm_parties_name, swarm_parties_res)

# ----------------------------------------------------------
