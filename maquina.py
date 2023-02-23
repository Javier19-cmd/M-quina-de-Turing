# Define la clase TM (Máquina de Turing)
class TM:
  def __init__(self, tape, initial_state, final_states, transition_function):
    self.tape = tape
    self.initial_state = initial_state
    self.current_state = initial_state
    self.final_states = final_states
    self.transition_function = transition_function

  def is_final(self):
    return self.current_state in self.final_states

  def get_tape(self):
    return self.tape

  def step(self):
    char_under_head = self.tape[0]
    x = (self.current_state, char_under_head)
    if x in self.transition_function:
      y = self.transition_function[x]
      self.current_state = y[0]
      self.tape = y[1] + self.tape[1:]
    else:
      raise Exception("No transition defined for current state and symbol.")

# # Define el alfabeto y el estado inicial
# alphabet = ['0', '1']
# initial_state = 'q1'

# # Define los estados finales
# final_states = ['q2']

# # Define la función de transición
# transition_function = {
#   ('q1', '0'): ('q2', '1', 'R'),
#   ('q1', '1'): ('q1', '0', 'L'),
#   ('q2', '0'): ('q2', '0', 'R'),
#   ('q2', '1'): ('q2', '1', 'R'),
# }

# # Cree una instancia de la máquina de Turing
# tape = "0001"
# tm = TM(tape, initial_state, final_states, transition_function)

# # Ejecute la máquina de Turing hasta que llegue a un estado final
# while not tm.is_final():
#   tm.step()

# # Imprima el resultado
# print("".join(tm.get_tape()))
