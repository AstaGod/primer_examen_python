#1.la siguiente funcion debera retornar la suma de sus parametros
def suma(a,b):
  #reemplazar pass por la sintaxis correcta
  suma=a+b
  return suma

#2. la funcion debera retornar 'es menor' o 'es mayor' segun la edad que pase por parametro
def is_greater_than(edad):
  valor=18
  if edad>=valor:
    return "es mayor"
  else:
    return "es menor"
#3. la funcion recibe como parametros dos datos el primero arr recibe una array(lista) el segundo num un numero entero positivo, la funcion debera retornar un nuevo array con el num insertado en la tercera posicion del array
def new_array(arr,num):
  if num < 0:
        return "El número debe ser positivo"
    
  if len(arr) < 2:
        return "La lista debe tener al menos dos elementos"
    
  nueva_lista = arr[:2] + [num] + arr[2:]
  return nueva_lista


#4. la funcion recibe una array debera retornar la suma de los numero ejm: [4,2,8,10] retornara 24
def suma_array(arr):
  suma=0
  for numero in arr:
        suma += numero

  return suma