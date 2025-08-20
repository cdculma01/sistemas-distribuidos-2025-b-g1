datos = [23, 5, 89, 12, 7, 34]

# 🔍 Búsqueda
buscado = 12
if buscado in datos:
    print(f"El número {buscado} está en la lista.")
else:
    print(f"El número {buscado} no está en la lista.")

# 📊 Ordenamiento
orden_asc = sorted(datos)
orden_desc = sorted(datos, reverse=True)

print("Ascendente:", orden_asc)
print("Descendente:", orden_desc)