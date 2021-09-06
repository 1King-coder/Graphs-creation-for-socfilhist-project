from datetime import datetime

def log(function):
  def wrapper():
    with open('./Logs/log.txt', 'a') as log:
      log.writelines(
        f'Function {function.__name__} initialized at'
        f' {datetime.now()} \n'
      )
    
    return function
  
  return wrapper()