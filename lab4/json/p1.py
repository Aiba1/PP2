import json 
with open("data.json") as x:
    a=json.load(x)
print("INTERFACE STATUS")
print('='*146)
print("DN"," "*50,"description"," "*50,"speed"," "*5,"MTU", )
print("-"*52,"-"*61,"-"*10,"-"*8)
for i in range(len(a["imdata"])):
    print(a["imdata"][i]["l1PhysIf"]["attributes"]["dn"]," "*72,a["imdata"][i]["l1PhysIf"]["attributes"]["speed"],"   ",a["imdata"][i]["l1PhysIf"]["attributes"]["mtu"])
