ask = ['string1','string1','string2','string2','string3','string4','string5','string5']
x=0
for stringname in ask:
	if ask[x]==ask[x+1]:
		ask.pop(x)
		ask.pop(x)
	x+=1
print(ask)