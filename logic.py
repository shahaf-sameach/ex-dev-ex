

def calculateNextState(state, input_s):
  new_state = {}
  if state == None:
    new_state['history'] = [input_s]
    new_state['display'] = input_s
  else:
    new_state = state.copy()
    if input_s == '=':
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

    elif input_s in ['+','-','*','/']:
      new_state['op'] = input_s
      new_state['history'].append('')
    else :
      new_state['history'][-1] = state['history'][-1] + input_s
      if 'op' in state.keys() and state['op'] in ['+','-','*','/']:
        new_state['display'] = new_state['history'][-1]
      else:
        new_state['display'] = new_state['display'] + input_s
  
  return new_state

if __name__ == '__main__':
  s = None
  s = calculateNextState(s, "1")
  print s, s['display']
  s = calculateNextState(s, "2")
  print s, s['display']
  s = calculateNextState(s, "+")
  print s, s['display']
  s = calculateNextState(s, "4")
  print s, s['display']
  s = calculateNextState(s, "3")
  print s, s['display']
  s = calculateNextState(s, "=")
  print s, s['display']
  s = calculateNextState(s, "+")
  print s, s['display']
  s = calculateNextState(s, "1")
  print s, s['display']
  s = calculateNextState(s, "=")
  print s, s['display']
  s = calculateNextState(s, "5")
  print s, s['display']
