from datetime import datetime
import re
import numpy as np
data_ragex_Pattern=re.compile('\d{1,2}[-/.]\d{1,2}[-/.]\d{4}')
yyyymmdd = re.compile('\d{4}[-/.\s*]\d{2}[-/.\s*]\d{2}')
date_reg_exp_DayMonthYYYY_3=re.compile('\d{1,2}?[-,'',.,/]?\s*(JAN|FEB|MAR|APR|MAY|JUN|JUL|AUG|SEP(?:t)?|OCT|NOV|DEC)\s*[-,'',.,/]?\s*(\d{2,4}?)',re.IGNORECASE)
date_reg_exp_DayMonthYYYY_4=re.compile('(\d{1,2})(ST|ND|RD|T\s*H)\s*[-,'',.,/]?\s*(JAN|FEB|MAR|APR|MAY|JUN|JUL|AUG|SEP(?:t)?|OCT|NOV|DEC)\s*[-,'',.,/]?\s*(\d{4})',re.IGNORECASE)
date_reg_exp_DayMonthYYYY_5=re.compile('\d{1,2}?[-,'',.,/]?\s*(JANUARY|FEBRUARY|MARCH|APRIL|MAY|JUNE|JULY|AUGUST|SEPTEMBER|OCTOBER|NOVEMBER|DECEMBER)\s*[-,'',.,/]?\s*(\d{4})',re.IGNORECASE)
date_reg_exp_DayMonthYYYY_6=re.compile('(\d{1,2})(ST|ND|RD|T\s*H)\s*[-,'',.,/]?\s*(JANUARY|FEBRUARY|MARCH|APRIL|MAY|JUNE|JULY|AUGUST|SEPTEMBER|OCTOBER|NOVEMBER|DECEMBER)\s*[-,'',.,/]?\s*(\d{4})',re.IGNORECASE)
def match_date(entity_value, sentence):
    global DATE
    matches = []
    found = None
    try:
        if not entity_value is np.datetime64('NaT'):
            entity_value = str(entity_value).split(" ")
            Entity_value =  datetime.strptime(entity_value[0],'%Y-%m-%d')
        for match in data_ragex_Pattern.finditer(sentence):
            date = re.sub(r'[(\.,*-/)]+', ' ', match.group())
            date_split = date.split()
            if float(date_split[0]) in range(1,32) and float(date_split[1]) in [1,3,5,7,8,10,12] and float(date_split[2]) in range(1900,2100):
                if datetime.strptime(date, '%d %m %Y') == Entity_value:
                    matches.append((match.start(),match.end(),sentence[match.start():match.end()]))
                    found = True
            elif float(date_split[0]) in range(1,31) and float(date_split[1]) in [4,6,9,11] and float(date_split[2]) in range(1900,2100):
                if datetime.strptime(date, '%d %m %Y') == Entity_value:
                    matches.append((match.start(),match.end(),sentence[match.start():match.end()]))
                    found = True
            elif float(date_split[0]) in range(1,30) and float(date_split[1]) in [2] and float(date_split[2]) in range(1900,2100):
                if datetime.strptime(date, '%d %m %Y') == Entity_value:
                    matches.append((match.start(),match.end(),sentence[match.start():match.end()]))
                    found = True
        for match in yyyymmdd.finditer(sentence):
            date = re.sub(r'[(\.,*-/)]+', ' ', match.group())
            date_split = date.split()
            if float(date_split[0]) in range(1900,2100) and float(date_split[1]) in [1,3,5,7,8,10,12] and float(date_split[2]) in range(1,32):
                if datetime.strptime(date,'%Y %m %d') == Entity_value:
                    matches.append((match.start(),match.end(),sentence[match.start():match.end()]))
                    found = True
            elif float(date_split[0]) in range(1900,2100) and float(date_split[1]) in [4,6,9,11] and float(date_split[2]) in range(1,31):
                if datetime.strptime(date,'%Y %m %d') == Entity_value:
                    matches.append((match.start(),match.end(),sentence[match.start():match.end()]))
                    found = True
            elif float(date_split[0]) in range(1900,2100) and float(date_split[1]) in [2] and float(date_split[2]) in range(1,30):
                if datetime.strptime(date,'%Y %m %d') == Entity_value:
                    matches.append((match.start(),match.end(),sentence[match.start():match.end()]))
                    found = True
        for match in date_reg_exp_DayMonthYYYY_3.finditer(sentence):
            date = re.sub(r'[(\.,*-/\s)]+', '', match.group())
            if len(date) == 6 :
                #print(date)
                if float(date[0:1]) in range(1,32) and date[1:4].lower() in ['jan','mar','may','jul','aug','oct','dec'] and float(date[4:]):
                    if datetime.strptime(date,'%d%b%y') == Entity_value:
                        matches.append((match.start(),match.end(),sentence[match.start():match.end()]))
                        found = True
                elif float(date[0:1]) in range(1,31) and date[1:4].lower() in ['apr','jun','sep','nov'] and float(date[4:]):
                    if datetime.strptime(date,'%d%b%y') == Entity_value:
                        matches.append((match.start(),match.end(),sentence[match.start():match.end()]))
                        found = True
                elif float(date[0:1]) in range(1,30) and date[1:4].lower() in ['feb'] and float(date[4:]):
                    if datetime.strptime(date,'%d%b%y') == Entity_value:
                        matches.append((match.start(),match.end(),sentence[match.start():match.end()]))
                        found = True
            if len(date) == 7 :
                #print(date)
                if float(date[0:2]) in range(1,32) and date[2:5].lower() in ['jan','mar','may','jul','aug','oct','dec'] and float(date[5:]):
                    if datetime.strptime(date,'%d%b%y') == Entity_value:
                        matches.append((match.start(),match.end(),sentence[match.start():match.end()]))
                        found = True
                elif float(date[0:2]) in range(1,31) and date[2:5].lower() in ['apr','jun','sep','nov'] and float(date[5:]):
                    if datetime.strptime(date,'%d%b%y') == Entity_value:
                        matches.append((match.start(),match.end(),sentence[match.start():match.end()]))
                        found = True
                elif float(date[0:2]) in range(1,30) and date[2:5].lower() in ['feb'] and float(date[5:]):
                    if datetime.strptime(date,'%d%b%y') == Entity_value:
                        matches.append((match.start(),match.end(),sentence[match.start():match.end()]))
                        found = True
            if len(date) == 8 :
                if float(date[0]) in range(1,32) and date[1:4].lower() in ['jan','mar','may','jul','aug','oct','dec'] and float(date[4:]) in range(1900,2100):
                    if datetime.strptime(date,'%d%b%Y') == Entity_value:
                        matches.append((match.start(),match.end(),sentence[match.start():match.end()]))
                        found = True
                elif float(date[0]) in range(1,31) and date[1:4].lower() in ['apr','jun','sep','nov'] and float(date[4:]) in range(1900,2100):
                    if datetime.strptime(date,'%d%b%Y') == Entity_value:
                        matches.append((match.start(),match.end(),sentence[match.start():match.end()]))
                        found = True
                elif float(date[0]) in range(1,30) and date[1:4].lower() in ['feb'] and float(date[4:]) in range(1900,2100):
                    if datetime.strptime(date,'%d%b%Y') == Entity_value:
                        matches.append((match.start(),match.end(),sentence[match.start():match.end()]))
                        found = True
            elif len(date) == 9 :
                if float(date[0:2]) in range(1,32) and date[2:5].lower() in ['jan','mar','may','jul','aug','oct','dec'] and float(date[5:]) in range(1900,2100):
                    if datetime.strptime(date,'%d%b%Y') == Entity_value:
                        matches.append((match.start(),match.end(),sentence[match.start():match.end()]))
                        found = True
                elif float(date[0:2]) in range(1,31) and date[2:5].lower() in ['apr','jun','sep','nov'] and float(date[5:]) in range(1900,2100):
                    if datetime.strptime(date,'%d%b%Y') == Entity_value:
                        matches.append((match.start(),match.end(),sentence[match.start():match.end()]))
                        found = True
                elif float(date[0:2]) in range(1,30) and date[2:5].lower() in ['feb'] and float(date[5:]) in range(1900,2100):
                    if datetime.strptime(date,'%d%b%Y') == Entity_value:
                        matches.append((match.start(),match.end(),sentence[match.start():match.end()]))
                        found = True
        for match in date_reg_exp_DayMonthYYYY_4.finditer(sentence):
            date = re.sub(r'[(\.,*-/\s)]+', '', match.group())
            if len(date) == 10:
                if float(date[0]) in range(1,32) and date[3:6].lower() in ['jan','mar','may','jul','aug','oct','dec'] and float(date[6:]) in range(1900,2100):
                    date = " ".join([date[0],date[3:6],date[6:]])
                    if datetime.strptime(date,'%d %b %Y') == Entity_value:
                        matches.append((match.start(),match.end(),sentence[match.start():match.end()]))
                        found = True
                elif float(date[0]) in range(1,31) and date[3:6].lower() in ['apr','jun','sep','nov'] and float(date[6:]) in range(1900,2100):
                    date = " ".join([date[0],date[3:6],date[6:]])
                    if datetime.strptime(date,'%d %b %Y') == Entity_value:
                        matches.append((match.start(),match.end(),sentence[match.start():match.end()]))
                        found = True
                elif float(date[0]) in range(1,30) and date[3:6].lower() in ['feb'] and float(date[6:]) in range(1900,2100):
                    date = " ".join([date[0],date[3:6],date[6:]])
                    if datetime.strptime(date,'%d %b %Y') == Entity_value:
                        matches.append((match.start(),match.end(),sentence[match.start():match.end()]))
                        found = True
            elif len(date) == 11:
                if float(date[0:2]) in range(1,32) and date[4:7].lower() in ['jan','mar','may','jul','aug','oct','dec'] and float(date[7:]) in range(1900,2100):
                    date = " ".join([date[0:2],date[4:7],date[7:]])
                    if datetime.strptime(date,'%d %b %Y') == Entity_value:
                        matches.append((match.start(),match.end(),sentence[match.start():match.end()]))
                        found = True
                elif float(date[0:2]) in range(1,31) and date[4:7].lower() in ['apr','jun','sep','nov'] and float(date[7:]) in range(1900,2100):
                    date = " ".join([date[0:2],date[4:7],date[7:]])
                    if datetime.strptime(date,'%d %b %Y') == Entity_value:
                        matches.append((match.start(),match.end(),sentence[match.start():match.end()]))
                        found = True
                elif float(date[0:2]) in range(1,30) and date[4:7].lower() in ['feb'] and float(date[7:]) in range(1900,2100):
                    date = " ".join([date[0:2],date[4:7],date[7:]])
                    if datetime.strptime(date,'%d %b %Y') == Entity_value:
                        matches.append((match.start(),match.end(),sentence[match.start():match.end()]))
                        found = True
        for match in date_reg_exp_DayMonthYYYY_5.finditer(sentence):
            date = re.sub(r'[(\.,*-/\s)]+', '', match.group())
            if date[0].isdigit() and date[1].isdigit():
                if float(date[0:2]) in range(1,32) and date[2:-4].lower() in ['january','march','may','july','august','october','december'] and float(date[-4:]) in range(1900,2100):
                    date_ac = date[0:2]
                    month = date[2:-4]
                    year = date[-4:]
                    DATE = " ".join([date_ac,month,year])
                    if datetime.strptime(DATE,'%d %B %Y') == Entity_value:
                        matches.append((match.start(),match.end(),sentence[match.start():match.end()]))
                        found = True
                elif float(date[0:2]) in range(1,31) and date[2:-4].lower() in ['april','june','september','november'] and float(date[-4:]) in range(1900,2100):
                    date_ac = date[0:2]
                    month = date[2:-4]
                    year = date[-4:]
                    DATE = " ".join([date_ac,month,year])
                    if datetime.strptime(DATE,'%d %B %Y') == Entity_value:
                        matches.append((match.start(),match.end(),sentence[match.start():match.end()]))
                        found = True
                elif float(date[0:2]) in range(1,30) and date[2:-4].lower() in ['february'] and float(date[-4:]) in range(1900,2100):
                    date_ac = date[0:2]
                    month = date[2:-4]
                    year = date[-4:]
                    DATE = " ".join([date_ac,month,year])
                    if datetime.strptime(DATE,'%d %B %Y') == Entity_value:
                        matches.append((match.start(),match.end(),sentence[match.start():match.end()]))
                        found = True
            else:
                if float(date[0:1]) in range(1,10) and float(date[-4:]) in range(1900,2100):
                    date_ac = date[0:1]
                    month = date[1:-4]
                    year = date[-4:]
                    DATE = " ".join([date_ac,month,year])
                #    date = str(re.sub('[a-z]','',date_split[0],flags = re.IGNORECASE) + (' '+date_split[1]) + (' '+date_split[2]))
                    if datetime.strptime(DATE,'%d %B %Y') == Entity_value:
                        matches.append((match.start(),match.end(),sentence[match.start():match.end()]))
                        found = True
        for match in date_reg_exp_DayMonthYYYY_6.finditer(sentence):
            date = re.sub('[.*,/\s-]', '', match.group())
            if date[0].isdigit() and date[1].isdigit():
                if float(date[0:2]) in range(1,32) and date[4:-4].lower() in ['january','march','may','july','august','october','december'] and float(date[-4:]) in range(1900,2100):
                    date_ac = date[0:2]
                    month = date[4:-4]
                    year = date[-4:]
                    DATE = " ".join([date_ac,month,year])
                    if datetime.strptime(DATE,'%d %B %Y') == Entity_value:
                        matches.append((match.start(),match.end(),sentence[match.start():match.end()]))
                        found = True
                elif float(date[0:2]) in range(1,31) and date[4:-4].lower() in ['april','june','september','november'] and float(date[-4:]) in range(1900,2100):
                    date_ac = date[0:2]
                    month = date[4:-4]
                    year = date[-4:]
                    DATE = " ".join([date_ac,month,year])
                    if datetime.strptime(DATE,'%d %B %Y') == Entity_value:
                        matches.append((match.start(),match.end(),sentence[match.start():match.end()]))
                        found = True
                elif float(date[0:2]) in range(1,30) and date[4:-4].lower() in ['february'] and float(date[-4:]) in range(1900,2100):
                    date_ac = date[0:2]
                    month = date[4:-4]
                    year = date[-4:]
                    DATE = " ".join([date_ac,month,year])
                    if datetime.strptime(DATE,'%d %B %Y') == Entity_value:
                        matches.append((match.start(),match.end(),sentence[match.start():match.end()]))
                        found = True
            else:
                if float(date[0:1]) in range(1,10) and float(date[-4:]) in range(1900,2100):
                    date_ac = date[0:1]
                    month = date[3:-4]
                    year = date[-4:]
                    DATE = " ".join([date_ac,month,year])
                #    date = str(re.sub('[a-z]','',date_split[0],flags = re.IGNORECASE) + (' '+date_split[1]) + (' '+date_split[2]))
                    if datetime.strptime(DATE,'%d %B %Y') == Entity_value:
                        matches.append((match.start(),match.end(),sentence[match.start():match.end()]))
                        found = True
    except Exception as e:
        logging.warning(e)
        logging.debug(sentence)
    return list(set(matches))