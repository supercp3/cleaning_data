import itchat

itchat.auto_login(hotReload=True)
friends=itchat.get_friends()

print(100*'&')
print(friends[25])
print(100*'&')

length=len(friends)

remarkname=[]  #备注名称
nickname=[]    #昵称
username=[]    #用户名称
contactflag=[] #1-公众号，2-群组，3-好友
sex=[]#性别
signature=[]   #个性签名
starfriend=[]  #是否为星际朋友 0-否  1-是
province=[]    #省
city=[]        #市

for i in range(length):
	remarkname.append(friends[i]['RemarkName'])
	sex.append(friends[i]['Sex'])
	province.append(friends[i]['Province'])
	city.append(friends[i]['City'])
	nickname.append(friends[i]['NickName'])	
	contactflag.append(friends[i]['ContactFlag'])	
	starfriend.append(friends[i]['StarFriend'])
	signature.append(friends[i]['Signature'])
	username.append(friends[i]['UserName'])	

print(100*'*')
print('备注','性别','省份','城市','昵称','好友（1/2/3）','星级朋友（0/1）','个性签名','用户唯一标识')
print(100*'*')
id=0
for k in range(length):
	if remarkname[k]!='':
		id+=1
		print('第'+str(id)+'名用户')
		print(remarkname[k])
		print(sex[k])
		print(province[k])
		print(city[k])
		print(nickname[k])
		print(contactflag[k])
		print(starfriend[k])
		print(signature[k])
		print(username[k])
		print('\n')
		#print(repr(remarkname[k]).rjust(4),repr(sex[k]).rjust(4),repr(province[k]).rjust(4),repr(city[k]).rjust(4),repr(nickname[k]).rjust(4),repr(contactflag[k]).rjust(4),repr(starfriend[k]).rjust(4),repr(signature[k]).rjust(4),repr(username[k]).rjust(4))
print(100*'*')