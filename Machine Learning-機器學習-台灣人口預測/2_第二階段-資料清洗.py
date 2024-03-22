import pandas as pd

file_name_old = pd.read_csv('舊縣市人口統計表87年1月-99年11月.csv')
file_name_new = pd.read_csv('新縣市人口統計表99年12月.csv')

'''__________________________________________________________1 . 設定欄位名稱'''
file_name_old = file_name_old.rename(columns = {file_name_old.columns[0] : '年月'})
file_name_new = file_name_new.rename(columns = {file_name_new.columns[0] : '年月'})

'''__________________________________________________________2 . 融合建立時間'''
date_old  = file_name_old['年月']
date_new  = file_name_new['年月']
date_df   = pd.concat([date_old, date_new], ignore_index=True)
date_df   = pd.Series(date_df , name='年月')
del date_old , date_new

'''____________________________________________________________3 . 臺北市合併'''
taipai_old  = file_name_old['臺北市']
taipai_new  = file_name_new['臺北市']
taipai_df   = pd.concat([taipai_old, taipai_new], ignore_index=True)
taipai_df   = pd.Series(taipai_df , name='臺北市')
del taipai_old , taipai_new

'''____________________________________________________________4 . 新北市合併'''
new_taipei_old = file_name_old['臺北縣']
new_taipei_new = file_name_new['新北市']
new_taipei_df  = pd.concat([new_taipei_old, new_taipei_new], ignore_index=True)
new_taipei_df  = pd.Series(new_taipei_df , name='新北市')
del new_taipei_old , new_taipei_new

'''____________________________________________________________5 . 台中市合併'''
'''舊縣市合併'''
Taichung_County        = file_name_old['臺中縣']
Taichung_City          = file_name_old['臺中市']
file_name_old["臺中市"] = Taichung_County + Taichung_City

'''新舊縣市合併'''
Taichung_old = file_name_old['臺中市']
Taichung_new = file_name_new['臺中市']
Taichung_df  = pd.concat([Taichung_old, Taichung_new], ignore_index=True)
Taichung_df  = pd.Series(Taichung_df , name='臺中市')
del Taichung_County , Taichung_City , Taichung_old , Taichung_new

'''____________________________________________________________6 . 台南市合併'''
'''舊縣市合併'''
Tainan_County          = file_name_old['臺南縣']
Tainan_City            = file_name_old['臺南市']
file_name_old["臺南市"] = Tainan_County + Tainan_City

'''新舊縣市合併'''
Tainan_old = file_name_old['臺南市']
Tainan_new = file_name_new['臺南市']
Tainan_df  = pd.concat([Tainan_old, Tainan_new], ignore_index=True)
Tainan_df  = pd.Series(Tainan_df , name='臺南市')
del Tainan_County , Tainan_City , Tainan_old , Tainan_new

'''____________________________________________________________7 . 高雄市合併'''
'''舊縣市合併'''
Kaohsiung_County        = file_name_old['高雄縣']
Kaohsiung_City          = file_name_old['高雄市']
file_name_old["高雄市"] = Kaohsiung_County + Kaohsiung_City

'''新舊縣市合併'''
Kaohsiung_old = file_name_old['高雄市']
Kaohsiung_new = file_name_new['高雄市']
Kaohsiung_df  = pd.concat([Kaohsiung_old, Kaohsiung_new], ignore_index=True)
Kaohsiung_df  = pd.Series(Kaohsiung_df , name='高雄市')
del Kaohsiung_County , Kaohsiung_City , Kaohsiung_old , Kaohsiung_new

'''____________________________________________________________8 . 宜蘭縣合併'''
Yilan_df_old = file_name_old['宜蘭縣']
Yilan_df_new = file_name_new['宜蘭縣']
Yilan_df  = pd.concat([Yilan_df_old, Yilan_df_new], ignore_index=True)
Yilan_df  = pd.Series(Yilan_df , name='宜蘭縣')
del Yilan_df_old , Yilan_df_new

'''____________________________________________________________9 . 桃園市合併'''
'''新縣市合併'''
Taoyuan_County         = file_name_new['桃園縣'].dropna()
Taoyuan_City           = file_name_new['桃園市'].dropna()
file_name_new['桃園市'] = pd.concat([Taoyuan_County , Taoyuan_City])

'''新舊縣市合併'''
Taoyuan_old = file_name_old['桃園縣']
Taoyuan_new = file_name_new['桃園市']
Taoyuan_df  = pd.concat([Taoyuan_old, Taoyuan_new], ignore_index=True)
Taoyuan_df  = pd.Series(Taoyuan_df , name='桃園市')
del Taoyuan_County , Taoyuan_City , Taoyuan_old , Taoyuan_new

'''___________________________________________________________10 . 新竹市合併'''
Hsinchu_old_City  = file_name_old['新竹市']
Hsinchu_new_City  = file_name_new['新竹市']
Hsinchu_df_City   = pd.concat([Hsinchu_old_City, Hsinchu_new_City], ignore_index=True)
Hsinchu_df_City   = pd.Series(Hsinchu_df_City , name='新竹市')
del Hsinchu_old_City , Hsinchu_new_City

'''___________________________________________________________11 . 新竹縣合併'''
Hsinchu_old_County  = file_name_old['新竹縣']
Hsinchu_new_County  = file_name_new['新竹縣']
Hsinchu_df_County   = pd.concat([Hsinchu_old_County, Hsinchu_new_County], ignore_index=True)
Hsinchu_df_County   = pd.Series(Hsinchu_df_County , name='新竹縣')
del Hsinchu_old_County , Hsinchu_new_County

'''___________________________________________________________12 . 苗栗縣合併'''
Miaoliu_old  = file_name_old['苗栗縣']
Miaoli_new   = file_name_new['苗栗縣']
Miaoli_df    = pd.concat([Miaoliu_old, Miaoli_new], ignore_index=True)
Miaoli_df    = pd.Series(Miaoli_df , name='苗栗縣')
del Miaoliu_old , Miaoli_new

'''___________________________________________________________13 . 彰化縣合併'''
Changhua_old   = file_name_old['彰化縣']
Changhua_new   = file_name_new['彰化縣']
Changhua_df    = pd.concat([Changhua_old, Changhua_new], ignore_index=True)
Changhua_df    = pd.Series(Changhua_df , name='彰化縣')
del Changhua_old , Changhua_new

'''___________________________________________________________14 . 南投縣合併'''
Nantou_old   = file_name_old['南投縣']
Nantou_new   = file_name_new['南投縣']
Nantou_df    = pd.concat([Nantou_old, Nantou_new], ignore_index=True)
Nantou_df    = pd.Series(Nantou_df , name='南投縣')
del Nantou_old , Nantou_new

'''___________________________________________________________15 . 南投縣合併'''
Nantou_old   = file_name_old['南投縣']
Nantou_new   = file_name_new['南投縣']
Nantou_df    = pd.concat([Nantou_old, Nantou_new], ignore_index=True)
Nantou_df    = pd.Series(Nantou_df , name='南投縣')
del Nantou_old , Nantou_new

'''___________________________________________________________16 . 雲林縣合併'''
Yunlin_old   = file_name_old['雲林縣']
Yunlin_new   = file_name_new['雲林縣']
Yunlin_df    = pd.concat([Yunlin_old, Yunlin_new], ignore_index=True)
Yunlin_df    = pd.Series(Yunlin_df , name='雲林縣')
del Yunlin_old , Yunlin_new

'''___________________________________________________________17 . 嘉義市合併'''
Chiayi_old_City   = file_name_old['嘉義市']
Chiayi_new_City   = file_name_new['嘉義市']
Chiayi_df_City    = pd.concat([Chiayi_old_City, Chiayi_new_City], ignore_index=True)
Chiayi_df_City    = pd.Series(Chiayi_df_City , name='嘉義市')
del Chiayi_old_City , Chiayi_new_City

'''___________________________________________________________18 . 嘉義縣合併'''
Chiayi_old_County   = file_name_old['嘉義縣']
Chiayi_new_County   = file_name_new['嘉義縣']
Chiayi_df_County    = pd.concat([Chiayi_old_County, Chiayi_new_County], ignore_index=True)
Chiayi_df_County    = pd.Series(Chiayi_df_County , name='嘉義縣')
del Chiayi_old_County , Chiayi_new_County

'''___________________________________________________________19 . 屏東縣合併'''
Pingtung_old   = file_name_old['屏東縣']
Pingtung_new   = file_name_new['屏東縣']
Pingtung_df    = pd.concat([Pingtung_old, Pingtung_new], ignore_index=True)
Pingtung_df    = pd.Series(Pingtung_df , name='屏東縣')
del Pingtung_old , Pingtung_new

'''___________________________________________________________20 . 臺東縣合併'''
Taitung_old   = file_name_old['臺東縣']
Taitung_new   = file_name_new['臺東縣']
Taitung_df    = pd.concat([Taitung_old, Taitung_new], ignore_index=True)
Taitung_df    = pd.Series(Taitung_df , name='臺東縣')
del Taitung_old , Taitung_new

'''___________________________________________________________21 . 花蓮縣合併'''
Hualien_old   = file_name_old['花蓮縣']
Hualien_new   = file_name_new['花蓮縣']
Hualien_df    = pd.concat([Hualien_old, Hualien_new], ignore_index=True)
Hualien_df    = pd.Series(Hualien_df , name='花蓮縣')
del Hualien_old , Hualien_new

'''___________________________________________________________22 . 澎湖縣合併'''
Penghu_old   = file_name_old['澎湖縣']
Penghu_new   = file_name_new['澎湖縣']
Penghu_df    = pd.concat([Penghu_old, Penghu_new], ignore_index=True)
Penghu_df    = pd.Series(Penghu_df , name='澎湖縣')
del Penghu_old , Penghu_new

'''___________________________________________________________23 . 基隆市合併'''
Keelung_old   = file_name_old['基隆市']
Keelung_new   = file_name_new['基隆市']
Keelung_df    = pd.concat([Keelung_old, Keelung_new], ignore_index=True)
Keelung_df    = pd.Series(Keelung_df , name='基隆市')
del Keelung_old , Keelung_new

'''___________________________________________________________24 . 金門縣合併'''
Kinmen_old   = file_name_old['金門縣']
Kinmen_new   = file_name_new['金門縣']
Kinmen_df    = pd.concat([Kinmen_old, Kinmen_new], ignore_index=True)
Kinmen_df    = pd.Series(Kinmen_df , name='金門縣')
del Kinmen_old , Kinmen_new

'''___________________________________________________________25 . 連江縣合併'''
Lianjiang_old   = file_name_old['連江縣']
Lianjiang_new   = file_name_new['連江縣']
Lianjiang_df    = pd.concat([Lianjiang_old, Lianjiang_new], ignore_index=True)
Lianjiang_df    = pd.Series(Lianjiang_df , name='連江縣')
del Lianjiang_old , Lianjiang_new

'''_______________________________________________________26 . 將所有資料融合'''
Fusion_df = pd.concat([date_df , taipai_df , new_taipei_df , Taichung_df , 
                Tainan_df , Kaohsiung_df , Yilan_df , Taoyuan_df ,  
                Hsinchu_df_City , Hsinchu_df_County , Miaoli_df , 
                Changhua_df , Nantou_df , Yunlin_df , Chiayi_df_City ,
                Chiayi_df_County , Pingtung_df , Taitung_df , Hualien_df , 
                Penghu_df , Keelung_df , Kinmen_df , Lianjiang_df] , axis=1)

del date_df , taipai_df , new_taipei_df , Taichung_df , Tainan_df , Kaohsiung_df , Yilan_df , Taoyuan_df ,  
del Hsinchu_df_City , Hsinchu_df_County , Miaoli_df , Changhua_df , Nantou_df , Yunlin_df , Chiayi_df_City ,
del Chiayi_df_County , Pingtung_df , Taitung_df , Hualien_df , Penghu_df , Keelung_df , Kinmen_df , Lianjiang_df

'''_________________________________________________________27 . 輸出儲存檔案'''
file_name = "全台灣各縣市-歷年月-人口統計表.csv"
Fusion_df.to_csv(file_name , index = False)





