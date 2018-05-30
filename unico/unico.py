# coding: utf-8

def unico(string):
	nova_string = ''
	if len(string) == 0:
		nova_string = ""
	else:
		if len(string) == 1:
			nova_string += string[0]
		else:
			nova_string += string[0]
			for i in range(1, len(string)):
				if string[i] != string[i - 1]:
					nova_string += string[i]
	return nova_string

assert unico("aa***xxxzzb+++") == "a*xzb+"
assert unico("") == ""