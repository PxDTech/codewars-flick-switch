# def flick_switch(lst):
#     toggle = True
#     new_lst = []
#     for item in lst:
#         if item == 'flick':
#             toggle = not toggle
#             new_lst.append(toggle)
#         else:
#             new_lst.append(toggle)
#     return new_lst

def flick_switch(lst):
	res, state = [], True
	for i in lst:
		if i == 'flick':
			state = not state
		res.append(state)
	return res

print(flick_switch(['bicycle', 'jarmony', 'flick', 'sheep', 'flick']))