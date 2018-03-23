

class Calculator(object):

  @staticmethod
  def calculateNextState(state, input_s):
    new_state = {}
    if state == None:
      new_state['history'] = [input_s]
      new_state['display'] = input_s
      new_state['op'] = ''
    else:
      new_state = state.copy()
      if input_s in "+-*/=":
        if len(new_state['history']) > 1 and not new_state['history'][1] is '':
          a, b = int(state['history'][0]), int(state['history'][1])  
          if new_state['op'] == '+':
            c =  a + b
          elif new_state['op'] == '-':
            c =  a - b
          elif new_state['op'] == '*':
            c =  a * b
          else:
            c =  a / b

          new_state['history'] = [str(c)]
          new_state['display'] = str(c)

        new_state['op'] = input_s

      elif input_s in '0123456789':
          if new_state['op'] == '=':
            new_state['history'] = [input_s]
            new_state['display'] = input_s
          else:
            if new_state['op'] != '' and new_state['op'] in '+-*/':
              if len(new_state['history']) == 1:
                new_state['history'].append('')

            new_state['history'][-1] = state['history'][-1] + input_s
            new_state['display'] = new_state['history'][-1]
      else:
        pass
    
    return new_state

if __name__ == '__main__':
  s = None
  s = Calculator.calculateNextState(s, "1")
  print s, s['display']
  s = Calculator.calculateNextState(s, "2")
  print s, s['display']
  s = Calculator.calculateNextState(s, "+")
  print s, s['display']
  s = Calculator.calculateNextState(s, "4")
  print s, s['display']
  s = Calculator.calculateNextState(s, "3")
  print s, s['display']
  s = Calculator.calculateNextState(s, "=")
  print s, s['display']
  s = Calculator.calculateNextState(s, "+")
  print s, s['display']
  s = Calculator.calculateNextState(s, "1")
  print s, s['display']
  s = Calculator.calculateNextState(s, "=")
  print s, s['display']
  s = Calculator.calculateNextState(s, "5")
  print s, s['display']
