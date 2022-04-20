def read_template(file_path):
    with open(file_path) as file:
      return file.read()

def parse_template(string):
  adjective_count = string.count("Adjective")
  noun_count = string.count("Noun")
  new_string = string.format(Adjective = "{}", Noun = "{}")
  type_tuple =()

  

  for i in range(adjective_count):
    type_tuple += ("Adjective",)
   
  
  for i in range(noun_count):
    type_tuple += ("Noun",)

  return (new_string, type_tuple)

def merge(string, words):
  return string.format(*words)


