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

      print(tapes['state'])

      # Calculando el siguiente número de Fibonacci
      fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])

  return fibonacci_sequence


n = 10

print(Turing(n))

# def fibonacci(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)

# # Calcular la sucesión de Fibonacci hasta el número n
# n = 10  # Cambiar este valor para calcular más números
# fibonacci_sequence = [0, 1]

# for i in range(n - 1):
#     # Codificar el número en binario en la cinta de la máquina de Turing
#     binary_num = bin(fibonacci_sequence[-1])[2:]
#     tape = '0' + binary_num + '0'
    
#     # Ejecutar la máquina de Turing
#     execute = tm.run(tape)
#     action, tape = next(execute)

#     # Decodificar el número de la cinta de la máquina de Turing
#     print(str(tape))
   
#print(fibonacci_sequence)