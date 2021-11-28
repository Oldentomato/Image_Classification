import os
import pandas as pd
import shutil as sh


csv = pd.read_csv('./excel/GroundTruth.csv',header=None) #csv파일을 읽어온다
csv.head()
file_list = os.listdir('./files') # 분류가 되지 않은 파일들을 읽어들여온다
count = 0

for i in file_list:
    item = i.rstrip('.jpg') #확장자를 지운 순수 이름을 item에 담아준다
    result = csv.loc[(csv[0]==item)] #csv파일에서 파일명(item)과 같은 index를 찾고 result에 담아준다
    for j in range(1,8): #해당 행에서 1~7까지 1.0 이라고 된부분을 찾고 파일을 옮겨준다
        check = (result.loc[:,[j]]=='1.0').values.tolist()[0] #타입이 오브젝트로 되있기때문에 list로 전환시켜준다(현재 2중list로 되어있다)
        if(check[0] == True): #2중 리스트이기에 한번더 [0]을 써준다
            if j == 1:
                sh.move('./files/'+i , './classificationed/melanoma/'+i)
            elif j == 2:
                sh.move('./files/'+i , './classificationed/melanocytic_nevi/'+i)
            elif j == 3:
                sh.move('./files/'+i , './classificationed/basal_cell_carcinoma/'+i)
            elif j == 4:
                sh.move('./files/'+i , './classificationed/Actinic_keratoses_and_intraepithelial_carcinoma/'+i)
            elif j == 5:
                sh.move('./files/'+i , './classificationed/benign_keratosis-like_lesions/'+i)
            elif j == 6:
                sh.move('./files/'+i , './classificationed/dermatofibroma/'+i)
            elif j == 7:
                sh.move('./files/'+i , './classificationed/vascular_lesions/'+i)
    count += 1
    print ("이미지 분류중 %.2f%%" % (count / len(file_list) * 100.0)) #실시간으로 진행상황 알려주기
