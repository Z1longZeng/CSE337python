# Zilong Zeng
# netID: zilzeng
# studentID: 115995879

#Problem 1 – Chaotic Strings

def is_chaotic(s):
    #输入的字符串s只包含a-z
    char_count={}
    #用set统计次数
    for char in s:
        char_count[char]=char_count.get(char,0)+1
        #if char in s then return this value and +1, if not, set the value of char to 0
    
    #check
    counts=set(char_count.values())#创建一个仅包含字典中所有值的set（这些值不重复）

    if(len(counts)==len(char_count)):#如果char_count的长度（字符数）和counts的长度（不同大小的字符数）相同，说明是chaotic
        return "TOHRU"
    else:
        return "ELMA"
    
print(is_chaotic("azzwea"))

#Problem 2 – Balanced Brackets

def is_balanced(s):
    #括号匹配
    #使用stack解决