
import pandas as pd
import convertEMU
import re

                
'''
Declaration of Variables
'''

fields = ['TIME', 'TEXT', 'MSGID']
reTrainID = re.compile("Train (\d+)")
reVOBCID = re.compile("VOBC (\d+)|\]\((\d+)\)|SVBVOBC::(\d+)")
rePlat = re.compile("plat (.+) assigntype")
reStation = re.compile("(\S+) (\S)")
faultNo = 0


uselessMsgId = [3,25, 27, 29, 1110, 3078, 3634, 8023, 8052, 8200, 8250, 8251,\
                96, 324]

VOBC_MSG_ID = [105,106,107,108,110,111,113,114,115,116,301,302,304,307,310,311,312,\
          361,401,402,403,404,405,406,407,408,450,451,452,502,504,505,509,510,\
          550,552,553,604,606,608,609,610,611,614,615,616,632,633,634,651,652,\
          653,659,702,704,705,706,707,708,709,710,713,716,802,803,805,808,810,\
          811,903,905,907,908,909,911,912,1006,1007,1009,1010,1011,1012,1013,\
          1014,1015,1016,1017,1018,1019,1101,1102,1103,1104,1105,1106,1107,\
          1108,1109,1110,1111,1112,1114,1219,1220,1301,1303,1304,1305,1306,\
          1307,1308,1309,1311,1313,1315,1320,1321,1328,1331,1343,1345,1346,\
          1348,1350,1354,1355,1356,1357,1358,1374,1377,1378,1379,1381,1382,\
          1383,1385,1386,1387,1389,1390,1391,1393,1394,1395,1398,1399,1400,\
          1401,1402,1403,1404,6031,6032,6066,6336,8011,8107,8108,8126,8140,\
          8142,8143,8203,8204,8205,8206,8207,8208,8209,8211,8212,8213,8214,\
          8222,8238,8239,8240,8245,8247,8248,8258,8259,8260,8261,8262,8263,\
          8264,8265,9001,9002,9005,9006,9007,9008,9009,9010,9013,9014,9015,\
          9016,9017]

#uselessMsgId = [3, 8, 11, 12, 13, 14, 15, 17, 18, 19, \
#                22, 23, 25, 27,30, 31, 34, 63, 96, 97, 310, 324, 550,\
#                803, 805, 811, 1103, 1110, 1219, 1346, 1391,\
#                1403, 3072, 3075, 3078, 3169, 3172, 3173, 3634, 3651,\
#                3814, 3820, 3825, 3826, 3827, 3828, 3851, 3857,\
#                5006, 7712, 7713, 8001, 8005, 8007, 8023, 8027,\
#                8041, 8042, 8043, 8044, 8045, 8051, 8052, 8140, 8141,\
#                8200, 8223, 8225, 8235, 8251, 8276, 8277, 8282, 8283, 9002,\
#                9006, 9009, 9010, 9016, 9017, 7835, 7347, 8250, 3702, 8016,\
#                3454, 3455, 14975, 10026, 10063, 10140]

#usefulMsgId = [28, 29,  47, 301, 302, 304, 312, 502, 510,\
#               608, 609, 611, 633, 652, 653, 704, 705, 706,\
#               713, 716, 802, 802, 810, 1102, 1104, 1105, 1106,\
#               1108, 1109, 1111, 1114, 1220, 1321, 1374, 3075, \
#               3456, 3457, 3458, 3459, 3501, 3552, \
#               3630, 3631, 3632, 3700,  3703, 3725, 3811, \
#               3813, 3817, 3819, 3821, 3823, 3824, 3829, 3830, \
#               3832, 3833, 3839, 3840, 3841, 3842, 3843, 3844, \
#               3845, 3846, 3848, 3849, 3850, 3852, 3853, 3854, \
#               3855, 3860, 3863, 5001, 7342, 7348, 7782, \ 
#               7901, 7914, 8006, 8011, 8019, 8020, \
#               8021, 8031, 8032, 8054, 8064, 8065, 8069, 8076, \
#               8077, 8108, 8126, 8141, 8201, 8205, 8225, 8228, \
#               8245, 8246, 8248, 8266, 8270, 8271, 8274, 8282, \
#               8283, 9001, 9005, 9009, 9014, 9015, 9016, 9219, \
#               9220, 9221]

#Read from CSV file
def main():
    print("1. Filter Spam \n2. Filter VOBC\n3. Specific MSGID filter\n" )

    while True:
        try:
            date = int(input("Enter Date in this format (YYYYMMDD) : "))
#            msgId = int(input("Enter MSGID : "))
        except ValueError:
            print("Not a number, terminating")
            break
#        specificFilter(date,msgId)
        filterCSV_spam(date)
#        filterCSV_VOBC(date)
    
def toDateTimeISO(dateTimeStr):
    dateTimeStr = pd.to_datetime(dateTimeStr, format='%Y-%m-%d %I:%M:%S %p')
    dateTimeStr = dateTimeStr.isoformat(' ')
    return dateTimeStr

def specificFilter(date,msgId):
    trainID = []
    vobcID = []
    
    df = pd.read_csv(str(date)+'org.csv',sep=',',header=0, usecols = fields)
    df = df.loc[df['MSGID']==msgId]
    
    df = filter_EW_CHG_Track(df)
    
    #Puts in the train ID into an array
    for row in df['TEXT']:
        if reTrainID.search(row):
            trainID.append(int(reTrainID.search(row).group(1)))
        else:
            trainID.append(None)

            
    #Puts in the VOBC ID into an array
    for row in df['TEXT']:
        if reVOBCID.search(row):
            if reVOBCID.search(row).group(2) is not None:
                vobcID.append(int(reVOBCID.search(row).group(2)))
            elif reVOBCID.search(row).group(1) is not None:
                vobcID.append(int(reVOBCID.search(row).group(1)))
            elif reVOBCID.search(row).group(3) is not None:
                vobcID.append(int(reVOBCID.search(row).group(3)))
        else:
            vobcID.append("")
       
    df['TRAINID'] = trainID
    df = convertEMU.convert_df_TRAINID(df)
    
    df['VOBCID'] = vobcID
    df = convertEMU.convert_df_VOBCID(df)
    
    cond = df.TRAINID == 0
    df.TRAINID[cond] = df.VOBCID[cond]
    
    df['VOBCID'] = vobcID
    
    df['TIME'] = pd.to_datetime(df['TIME'], format='%Y-%m-%d %I:%M:%S %p')
    
#    df = filter_non_rev(df)
    
    if (msgId == 97):
        platID = []
        for row in df['TEXT']:
            if rePlat.search(row) is not None:
                tempPlat = rePlat.search(row).group(1)
                if reStation.search(tempPlat) is not None:
                    platID.append(reStation.search(tempPlat).group(1))
                else:
                    platID.append(tempPlat)
            else:
                platID.append("")
        df["Platform"] = platID
        df = df[df.Platform != "0"]
        df = df[df.TRAINID != 0]
    
    df['TRAIN/TRAINID'] = df['TRAINID'].apply(AutocompleteDT)
    writer = pd.ExcelWriter(str(date) + '-MSG' + str(msgId) +'.xlsx', engine = 'xlsxwriter')
    df.to_excel(writer, sheet_name=str(msgId), index=False)
    worksheet = writer.sheets[str(msgId)]
    worksheet.set_column('A:A', 18)
    worksheet.set_column('B:B', 100)
    writer.save()
    return df

def filter_non_rev(df):
    START_TIME = df['TIME'].iloc[0]
    
    
    START_TIME = START_TIME.replace(hour = 5, minute = 0, second = 0, microsecond = 0)
    END_TIME = START_TIME.replace(hour = 1, minute = 40, second = 0, microsecond = 0)
    
#    print (START_TIME)
#    print (END_TIME)
        
    df = df.loc[df['TIME'] < END_TIME].append(df.loc[df['TIME'] > START_TIME])
    
    return df
    

def filter_EW_CHG_Track(df):
    
    EW_TRACK = ["Track1_EW","Track2_EW","Track3_CHG","Track4_CHG"]
    
    df = df[df.TEXT.str.contains('|'.join(EW_TRACK)) == False]
    
    return df

def filterCSV_VOBC(date):
    
    trainID = []
    vobcID = []
    
    df = pd.read_csv(str(date)+'org.csv',sep=',',header=0, usecols = fields)
    df = df.loc[df['MSGID'].isin(VOBC_MSG_ID)]
    
    df = filter_EW_CHG_Track(df)
    
    #Puts in the train ID into an array
    for row in df['TEXT']:
        if reTrainID.search(row):
            trainID.append(int(reTrainID.search(row).group(1)))
        else:
            trainID.append(None)

            
    #Puts in the VOBC ID into an array
    for row in df['TEXT']:
        if reVOBCID.search(row):
            if reVOBCID.search(row).group(2) is not None:
                vobcID.append(int(reVOBCID.search(row).group(2)))
            elif reVOBCID.search(row).group(1) is not None:
                vobcID.append(int(reVOBCID.search(row).group(1)))
            elif reVOBCID.search(row).group(3) is not None:
                vobcID.append(int(reVOBCID.search(row).group(3)))
        else:
            vobcID.append("")
       
    df['TRAINID'] = trainID
    df = convertEMU.convert_df_TRAINID(df)
    
    df['VOBCID'] = vobcID
    df = convertEMU.convert_df_VOBCID(df)
    
    cond = df.TRAINID == 0
    df.TRAINID[cond] = df.VOBCID[cond]
    
    df['VOBCID'] = vobcID
    
    df['TIME'] = pd.to_datetime(df['TIME'], format='%Y-%m-%d %I:%M:%S %p')
    
    df = filter_non_rev(df)
    df['TRAIN/TRAINID'] = df['TRAINID'].apply(AutocompleteDT)
    
    writer = pd.ExcelWriter(str(date) + '-VOBC.xlsx', engine = 'xlsxwriter')
    df.to_excel(writer, sheet_name='VOBC', index=False)
    worksheet = writer.sheets['VOBC']
    worksheet.set_column('A:A', 18)
    worksheet.set_column('B:B', 100)
    writer.save()
    return df
    

def filterCSV_spam(date):
    
    trainID = []
    vobcID = []

    filteredInput = pd.read_csv(str(date)+'org.csv',sep=',',header=0, usecols = fields)
    
    #Filter out the Message IDs that are deemed useless
    x = 0
    while x < len(uselessMsgId):   
        filteredInput = filteredInput[filteredInput.MSGID != uselessMsgId[x]]
        x += 1
        
    filteredInput = filter_EW_CHG_Track(filteredInput)
    
    filteredInput['TIME'] = pd.to_datetime(filteredInput['TIME'], format='%Y-%m-%d %I:%M:%S %p')
        
    #filteredInput = filter_non_rev(filteredInput)
        
    #Puts in the train ID into an array
    for row in filteredInput['TEXT']:
        if reTrainID.search(row):
            trainID.append(int(reTrainID.search(row).group(1)))
        else:
            trainID.append(None)
            
    #Puts in the VOBC ID into an array
    for row in filteredInput['TEXT']:
        if reVOBCID.search(row):
            if reVOBCID.search(row).group(2) is not None:
                vobcID.append(int(reVOBCID.search(row).group(2)))
            elif reVOBCID.search(row).group(1) is not None:
                vobcID.append(int(reVOBCID.search(row).group(1)))
            elif reVOBCID.search(row).group(3) is not None:
                vobcID.append(int(reVOBCID.search(row).group(3)))
        else:
            vobcID.append("")
    
    
    filteredInput['TRAINID'] = trainID
    filteredInput = convertEMU.convert_df_TRAINID(filteredInput)
        
    filteredInput['VOBCID'] = vobcID
    filteredInput = convertEMU.convert_df_VOBCID(filteredInput)
    #if the Train ID is 0, VOBC ID takes over
    cond = filteredInput.TRAINID == 0
    filteredInput.TRAINID[cond] = filteredInput.VOBCID[cond]
    
    filteredInput['VOBCID'] = vobcID
    
    filteredInput['TRAIN/TRAINID'] = filteredInput['TRAINID'].apply(AutocompleteDT)
    
    
#    Print the fault counts by appearance 
#    faultCount = filteredInput.groupby(['MSGID'])['MSGID'].count().reset_index(name='count')
#    
#    print(faultCount)    
    
    writer = pd.ExcelWriter(str(date) + '-filtered.xlsx', engine = 'xlsxwriter')
    filteredInput.to_excel(writer, sheet_name='Filtered',index=False)
    worksheet = writer.sheets['Filtered']
    worksheet.set_column('A:A', 18)
    worksheet.set_column('B:B', 100)
    writer.save()
    return filteredInput

def AutocompleteDT(dt1):
   dt1int = int(dt1)
   if dt1int == 3509 or dt1int == 3532:
       return ("%d/%d" % (3509, 3532))
   if dt1int == 3510 or dt1int == 3531:
       return ("%d/%d" % (3510, 3531))
   if dt1int == 0:
       return (None)
   elif dt1int % 2 == 1:
       return ("%d/%d" % (dt1int, dt1int+1))
   elif dt1int % 2 == 0:
       return ("%d/%d" % (dt1int-1, dt1int))
   else:
       print("something's wrong with the code in AutocompleteDT")
       return (None)

main()