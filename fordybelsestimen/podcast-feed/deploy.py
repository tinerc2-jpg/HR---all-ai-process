import os,json,base64,urllib.request
D=os.path.dirname(os.path.abspath(__file__));T=open(D+'/TOKEN').read().strip()
files=[]
for root,_,fs in os.walk(D+'/'+T):
  for f in fs:
    p=os.path.join(root,f);files.append({"file":os.path.relpath(p,D),"data":base64.b64encode(open(p,'rb').read()).decode(),"encoding":"base64"})
files.append({"file":"robots.txt","data":open(D+'/robots.txt').read()})
body={"name":"fordybelsestimen-feed","target":"production","files":files,"projectSettings":{"framework":None}}
r=urllib.request.Request("https://api.vercel.com/v13/deployments?skipAutoDetectionConfirmation=1",json.dumps(body).encode(),{"Content-Type":"application/json","Authorization":"Bearer x"})
print(json.load(urllib.request.urlopen(r)).get('readyState'))
