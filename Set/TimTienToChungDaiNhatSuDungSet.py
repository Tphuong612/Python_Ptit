def longest_tmp_continuous(str1, str2):
    tmp = ""
    set1 = set(str1)
    set2 = set(str2)

    min_len = min(len(str1), len(str2))

    for i in range(min_len):
        if str1[i] == str2[i]:
            tmp += str1[i]
        else:
            break

    if tmp and (tmp[-1] in set2):
        return tmp
    else:
        return ""

# Example usage:
str1 = "phuong1tran"
str2 = "phuongtran"
result = longest_tmp_continuous(str1, str2)
print("Longest common prefix:", result)

def TienToChungDaiNhat(str1, str2):
    tmp = ""
    set1 = set(str1)
    set2 = set(str2)
    
    min_len = min(len(str1), len(str2))
    for i in range(min_len):
        if str1[i] == str2[i]:
            tmp += str1[i]
        else: 
            break
        
