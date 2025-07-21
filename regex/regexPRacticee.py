import re

def parse_sentences(sentence):
 pattern =r"\s" #enter the regex pattern here
 result = re.split(pattern, sentence) #enter the re method  here
 return result

print(parse_sentences("Hello! How are you doing?")) # should return ['Hello!', 'How', 'are', 'you', 'doing?']
print(parse_sentences("what a beautiful day it is")) # should return ['what', 'a', 'beautiful', 'day', 'it', 'is']
print(parse_sentences("2 + 2 is definitely 4!")) # should return ['2', '+', '2', 'is', 'definitely', '4!']


# Example 2
print("============================================")
def find_eid(report):
  pattern = r"[A-Z]-\d{7,8}\b" #enter the regex pattern here
  result = re.findall(pattern, report) #enter the re method  here
  return result


print(find_eid("Employees B-1234567 and C-12345678 worked with products X-123456 and Z-123456789")) # Should return ['B-1234567', 'C-12345678']
print(find_eid("Employees B-1234567 and C-12345678, not employees b-1234567 and c-12345678")) #Should return ['B-1234567', 'C-12345678']