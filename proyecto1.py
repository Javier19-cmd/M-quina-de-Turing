from turing_machine import *

def Turing(n): 
  
  # # Función de transición para calcular el siguiente número de Fibonacci
  # transition_function = {
  #     # Transiciones para inicializar la cinta con dos primeros números de Fibonacci
  #     ('q0', '0'): ('q1', 'b', 'R'),
  #     ('q1', '0'): ('q1', '0', 'R'),
  #     ('q1', '1'): ('q2', '1', 'R'),
  #     ('q2', '0'): ('q2', '0', 'R'),
  #     ('q2', 'b'): ('q3', 'b', 'L'),
  #     # Transiciones para calcular los siguientes números de Fibonacci
  #     ('q3', '0'): ('q3', '0', 'L'),
  #     ('q3', '1'): ('q4', 'b', 'L'),
  #     ('q4', '0'): ('q5', '1', 'L'),
  #     ('q4', '1'): ('q4', '1', 'L'),
  #     ('q5', '0'): ('q6', '0', 'R'),
  #     ('q5', '1'): ('q5', '1', 'L'),
  #     ('q6', '0'): ('q6', '0', 'R'),
  #     ('q6', '1'): ('q7', '1', 'R'),
  #     ('q7', '0'): ('q3', '0', 'L'),
  #     ('q7', '1'): ('q7', '1', 'R'),
  # }

  transition_function = {}

  # Abriendo el archivo con la función de transición.
  with open('transiciones.txt', 'r') as file:
    for line in file:
        line = line.strip()
        line = line.split(' ')
        # Metiendo los datos en el diccionario.
        transition_function[(line[0], line[1])] = (line[2], line[3], line[4])
  
  print(transition_function)

  # # Máquina de Turing para calcular la sucesión de Fibonacci
  # tm = TuringMachine(
  #   {
  #     'states': ,
  #     'symbols': ,	
  #     'blank_symbol': ,
  #     'input_symbols': ,
  #     'transition_function': transition_function,
  #     'initial_state': ,
  #     'final_states': 
  #   }
  # )

  # Abriendo el archivo con los datos de la máquina de Turing.
  with open('maquina.txt', 'r') as file:
    lista = []
    for line in file: 
       lista.append(line.strip())

    print(lista)

    tm = TuringMachine(
      {
        'states': lista[0].split(' '),
        'symbols': lista[1].split(' '),
        'blank_symbol': lista[2],
        'input_symbols': lista[3].split(' '),
        'transition_function': transition_function,
        'initial_state': lista[4],
        'final_states': lista[5].split(' ')
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

      #print(tapes)

      # Calculando el siguiente número de Fibonacci
      fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])

  return fibonacci_sequence

n = 200

print(Turing(n))
