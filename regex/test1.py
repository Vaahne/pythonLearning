import re 
  
my_txt = "An investment in knowledge pays the best interest."

def LetterCompiler(txt):
    result = re.findall(r'([a-c]).', txt)
    print(result)
    return result

# print(LetterCompiler(my_txt))