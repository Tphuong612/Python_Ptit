def DemKiTu(s):
    dem = 0
    for i in range(len(s)):
        if s[i] != " ":
            dem += 1
    return dem 

def Check_ChuoiCon(s1, s):
    if s1 in s:
        return True
    
