'''
Proyecto 1: Maquina de Turing y sucesion de fibonacci

Integrantes:
  Javier Valle
  Christopher García
  Maria Isabel Solano
  Gabriel Vicente
  Oscar Estrada
  Mario De León
'''


import time
import csv
from turing_machine import *

def Turing(n): 
  # Función de transición para calcular el siguiente número de Fibonacci
  transition_function = {
      # Transiciones para inicializar la cinta con dos primeros números de Fibonacci
      ('q0', '0'): ('q1', 'b', 'R'),
      ('q1', '0'): ('q1', '0', 'R'),
      ('q1', '1'): ('q2', '1', 'R'),
      ('q2', '0'): ('q2', '0', 'R'),
      ('q2', 'b'): ('q3', 'b', 'L'),
      # Transiciones para calcular los siguientes números de Fibonacci
      ('q3', '0'): ('q3', '0', 'L'),
      ('q3', '1'): ('q4', 'b', 'L'),
      ('q4', '0'): ('q5', '1', 'L'),
      ('q4', '1'): ('q4', '1', 'L'),
      ('q5', '0'): ('q6', '0', 'R'),
      ('q5', '1'): ('q5', '1', 'L'),
      ('q6', '0'): ('q6', '0', 'R'),
      ('q6', '1'): ('q7', '1', 'R'),
      ('q7', '0'): ('q3', '0', 'L'),
      ('q7', '1'): ('q7', '1', 'R'),
  }
  # Máquina de Turing para calcular la sucesión de Fibonacci
  tm = TuringMachine(
    {
      'states': ['q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7'],
      'symbols': ['0', '1', 'b'],	
      'blank_symbol': 'b',
      'input_symbols': {'0', '1'},
      'transition_function': transition_function,
      'initial_state': 'q0',
      'final_states': {'q7'}
    }
  )


  # Configurar la cinta con los dos primeros números de Fibonacci
  tape = (['0', '1', 'b'])

  # Calcular la sucesión de Fibonacci hasta el número n
  #n = 10  # Cambiar este valor para calcular más números
  fibonacci_sequence = [0, 1]

  for i in range(n - 1):
      result = tm.run(tape)

      action, tapes = next(result)

      # Calculando el siguiente número de Fibonacci
      fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])

  return fibonacci_sequence


# N a calcular de la sucesión de Fibonacci
# for x in range(0,1000):
# Description
start_time = time.time()
print(f'\n{"─"*124}\n{"─"*50}Bienvenido al PROYECTO 1{"─"*50}\n{"─"*104} Auth. Fans de Paulo\n')
print(' --> Teniendo en cuenta')
print('\t*\tLa representacion se da con numeros naturales')
print('\t*\tEl retorno sera el valor de la posicion solicitada')
print('\t*\tLas graficas se muestran en el archivo empirical_analysis.ipynb')
print('\t*\tPara obtener un nuevo valor ejecutar proyecto1.py nuevamente y cambiar el valor n\n')

n = 1000

# Impresión de fibonacci

print(f'--> Numero Obtenido de la sucesión de Fibonacci: {Turing(n)[-1]}\n')
end_time = time.time()

# Execution time
execution_time = end_time - start_time
print("--> El tiempo de ejecución fue:", execution_time, "segundos\n")

# Agregacion de datos a csv
with open('datos.csv', mode='a', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow([n, execution_time])