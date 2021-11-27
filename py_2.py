import random
n=int(input("Количество рядков --> "))
m=int(input("Количество столбцов --> "))
A=[[random.randint(1,9) for i in range(m)] for r in range(n)]
print(A)
print("--------------------")
for i in A:
    print(i)
c=[A[r][i] for r in range(n)for i in range(m)if r==i]
print(f"главная диагональ --> {c}")
b=[A[2][i] for i in range(m)if i==3]
print(f"индекс  --> {b}")


