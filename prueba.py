class TuringMachine:
    def __init__(self, tape, head):
        self.tape = tape
        self.head = head
        self.halted = False

    def step(self):
        symbol = self.tape[self.head]

        if symbol == 0:
            # Si el símbolo es 0, cambiamos a 1 y movemos la cabeza a la derecha
            self.tape[self.head] = 1
            self.head += 1
        elif symbol == 1:
            # Si el símbolo es 1, sumamos los dos términos anteriores y escribimos el resultado en la cinta
            prev1 = self.tape[self.head - 1]
            prev2 = self.tape[self.head - 2]
            result = prev1 + prev2
            self.tape[self.head] = result
            self.head += 1
        else:
            # Si el símbolo es diferente de 0 y 1, detenemos la máquina
            self.halt()

    def run(self):
        while not self.is_halted():
            self.step()

    def halt(self):
        self.halted = True

    def is_halted(self):
        return self.halted

    def get_tape(self):
        return self.tape

tape = [10, 9] + [2] * 8 # Creamos una cinta inicializada con los primeros dos términos de la sucesión
head = 2 # Colocamos el cabezal de lectura en el tercer término de la sucesión
tm = TuringMachine(tape, head)

tm.run()
a = tm.get_tape()
print(a)