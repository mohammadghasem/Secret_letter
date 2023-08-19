def find_pattern(sen,pat,seperate_sen):
	index1=0
	index2=0
	if len(pat) == 1 :
		if (pat[0] in seperate_sen.keys()) and (seperate_sen[pat[0]] != sen[index1:]):
			return 0
		return 1	

	new_dict = seperate_sen.copy()
	if pat[0] in seperate_sen.keys() and (seperate_sen[pat[0]] != sen[index1 : len(seperate_sen[pat[0]])]): 
			return 0
	if pat[0] in seperate_sen.keys() and (seperate_sen[pat[0]] == sen[index1 : len(seperate_sen[pat[0]])]) :
			return find_pattern(sen[len(seperate_sen[pat[0]]) : ],pat[1:] , new_dict)
	while (index2 < len(sen)):#?
		new_dict[pat[0]] = sen[index1:index2+1]
		if find_pattern(sen[index2+1:],pat[1:],new_dict):
			return 1
		index2 = index2 + 1
		new_dict = seperate_sen.copy()
	return 0

#dict1={}
#print(find_pattern("crimecrimecrime","xxx",dict1))
answer=[]
number_input = int(input())
for i in range(0,number_input):
	dict1={}
	string = input()
	pattern = input()
	answer.append(find_pattern(string,pattern,dict1))
#print(answer)
for i in answer :
	if i == 1:
		print("Yes")
	else :
		print("No")