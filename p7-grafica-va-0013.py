import numpy as np
import matplotlib.pyplot as plt
# Meredith Aguirre NC = 0013 Fecha 28/10/2026

No_lista = [1, 2, 3, 17, 48]
Califa_ml = [20, 30, 80, 100, 90]
Califa_va = [70, 90, 60, 80, 100]
plt.plot(No_lista, Califa_ml, label = "Califa ML")
plt.plot(No_lista, Califa_va, label = "Califa VA")
plt.title("Calificaciones Materias 0013")
plt.xlabel("Numero de lista")
plt.ylabel("Calificacion")

plt.legend()
plt.show()