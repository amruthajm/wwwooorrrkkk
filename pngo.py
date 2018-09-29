import requests
image_url = "http://pngimg.com/uploads/water_glass/water_glass_PNG15234.png"
r = requests.get(image_url)
with open("water_glass.png", 'wb') as f:
	f.write(r.content)
a=int(input())
b=int(input())
o=str(input())
if(o=="+"):
	print(a+b)
elif(o=="-"):
	print(a-b)
elif(o=="*"):
	print(a*b)
elif(o=="/"):
	print(a/b)
