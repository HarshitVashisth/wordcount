text = "this this is the text and this is the text"
word_list = text.split()
# d = {'a':3, 'b':4}
# if 'a' in d:
#     print("True")
word_dict = {i : word_list.count(i) for i in word_list}
# for i in word_list:
#     if i not in word_dict:
#         word_dict[i] = word_list.count(i)
print(word_dict)
