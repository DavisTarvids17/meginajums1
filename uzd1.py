# 1 try ... except ... lai noķertu kļūdas!
def nolasitDatni():
    datne=open('info.txt', encoding='utf-8')
    datni=datne.readline()
    rinda=datni.split(" ")
    print(rinda)

nolasitDatni()