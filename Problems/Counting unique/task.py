# The following code is needed for us to check your answer, do not modify it, please.
students = json.loads(input())
Belov = students['Belov']
Smith = students['Smith']
Sarada = students['Sarada']

# Your code here. Work with the variables 'Belov', 'Smith', and 'Sarada'
list_ = []
for word in Belov:
    list_.append(word)
for word in Smith:
    list_.append(word)
for word in Sarada:
    list_.append(word)
print(len(set(list_)))
