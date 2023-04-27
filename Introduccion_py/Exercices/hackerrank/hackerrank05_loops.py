# users_list = ['Arturo', 'Gnuxdar', 'Admin', 'Siry', 'Alexa', 'GPT']
# users_to_delete = ['Siry', 'Alexa', 'GPT']
# new_list = [x for x in users_list if x not in users_to_delete]
# print(new_list)


user_list2 = ['user00', 'user01', 'user02', 'user03', 'user04', 'user05']
to_delete = ['user00', 'user02']

new_list = [item for item in user_list2 if item not in to_delete]
print(new_list)