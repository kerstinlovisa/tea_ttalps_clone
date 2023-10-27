def info(message):
  print(message)
  
def warn(message):
  print("\033[1;33m" + message + "\033[0m")
  
def error(message):
  print("\033[1;31m" + message + "\033[0m")
  
def fatal(message):
  print("\033[1;35m" + message + "\033[0m")
