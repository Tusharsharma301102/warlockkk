#ans1
def fun(list1, list2):
  dictionary = {}
  for i in range(len(list1)):
    dictionary[list1[i]] = list2[i]
  return dictionary




list1 = []
list2 = []

print("Enter the num:")
for element in input().split():
    list1.append(element)

print("Enter the second list:")
for element in input().split():
    list2.append(element)

dictionary = fun(list1, list2)
print(dictionary)