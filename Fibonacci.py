def turing_machine_fibonacci(n):
    state = 'q0'  # Estado inicial
    tape = ['1', '1']  # Inicializamos la cinta con los primeros dos números de Fibonacci
    head_position = 0  # Posición inicial de la cabeza de lectura/escritura
    steps = 0  # Contador de pasos de la Máquina de Turing

    while state != 'qf':  # Estado de aceptación
        if state == 'q0':
            if tape[head_position] == '1':  # Encontramos el primer '1'
                state = 'q1'
                head_position += 1
                steps += 1
            else:  # Si no encontramos '1' significa que llegamos al final de la cinta
                state = 'qf'
        elif state == 'q1':
            if tape[head_position] == '1':  # Encontramos el segundo '1'
                state = 'q2'
                head_position += 1
                steps += 1
            else:  # Si no encontramos '1' significa que el número de Fibonacci se ha calculado
                state = 'qf'
        else:  # Estado q2
            # Sumamos los dos últimos números de Fibonacci y los escribimos en la cinta
            new_number = str(int(tape[head_position-1]) + int(tape[head_position-2]))
            for i, char in enumerate(new_number):
                tape.insert(head_position+i, char)

            # Movemos la cabeza de lectura/escritura al final del nuevo número
            head_position += len(new_number)

            # Nos movemos hacia atrás dos posiciones para leer los dos últimos números de Fibonacci
            head_position -= 2

            # Actualizamos el estado
            state = 'q1'
            steps += 1

    # Imprimimos el resultado
    print(f"El número de Fibonacci en la posición {n} es: {tape[n-1]}")
    print(f"La Máquina de Turing se detuvo después de {steps} pasos")

    return tape[n-1]

turing_machine_fibonacci(1)
