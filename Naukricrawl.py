import json , time ,requests, uuid, time, csv
from bs4 import BeautifulSoup
location=['Hyderabad','Bangalore','Kolkata','Mumbai','Pune','Ahmedabad','Patna','Chennai','Amritsar','Delhi','Gurgaon','Noida','Shimla','Silchar','Jalandhar','Bhatinda','Gaya']
stream=['pharma','it','textile','manufacturing','biotechnology','marketing','management','maintenance']
for j in range(len(stream)):
    for i in range(len(location)):
        url="https://www.naukri.com/"+stream[j]+"-jobs-in-"+location[i]
        conn=requests.get(url)
        conn=conn.content
        soup=BeautifulSoup(conn,"html5lib")
        filename="naukri"+location[i]+"-"+stream[j]+".csv"
        f=open(filename,"w")
        for row in soup.findAll("div",class_="row",type="tuple"):
            print("*"*100+location[i]+"  "+stream[j]+"*"*100)
            info=""
            if row.find("ul"):
                desig=row.find("ul").text.replace(",","|")
                print(desig)
            else:
                desig="NULL"
            if row.find("span",class_="org"):
                org=row.find("span",class_="org").text.replace(",","|")
                print(org)
            else:
                org="NULL"
            if row.find("span",class_="exp"):
                exp=row.find("span",class_="exp").text.replace(",","|")
                print(exp)
            else:
                org="NULL"
            if row.find("span",class_="loc"):
                loc=row.find("span",class_="loc").text.replace(",","|")
                print(loc)
            else:
                loc="NULL"
            info=desig+","+org+","+exp+","+loc+"\n"
            try:
                f.write(info)
            except:
                pass
f.close()