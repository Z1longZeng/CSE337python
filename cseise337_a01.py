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


#print(is_chaotic("aabbcd"))
#print(is_chaotic('aaaabbbccd'))
#print(is_chaotic('abaacccdee'))

#Problem 2 – Balanced Brackets

def is_balanced(s):
    #括号匹配
    #使用dictionary匹配
    bracket_lr={'(':')','{':'}','[':']'}
    seq=[]# use stack to pair the left bracket and right

    for char in s:
        if char in bracket_lr: #char is one of the left bracket
            seq.append(char) #入栈
        else:#char is the right barcket
            if len(seq)==0:#空栈
                return False #不能匹配
            top= seq.pop() #成功配对
            if bracket_lr[top]!=char: #括号不匹配
                return False
    
    return not seq


#print(is_balanced('{[()]}'))
#print( is_balanced('{[(])}'))
#print( is_balanced('{{[[(())]]}}'))
#print(is_balanced("[]{}()"))


#Problem 3 – Functional Programming
def even(x):
    return int(x)%2==0

def odd(x):
    return int(x)%2==1

def winning_function(a,even,odd):
    count_even=0
    count_odd=0
    
    for num in a:
        if(even(num)): count_even+=1
        if(odd(num)): count_odd+=1
    
    if count_even>count_odd:
        return "even"
    if count_odd>count_even:
        return "odd"
    if count_odd==count_even:
        return "TIE"

#print(winning_function([2,3,4,5,6,8],even,odd))

#Problem 4 – Representing Filesystems

class FS_Item:
    def __init__(self,name):
        self.name=name #文件目录的名字
    
class Folder(FS_Item):
    def __init__(self,name):
        super().__init__(name)
        self.items=[] #文件列表

    def add_item(self,item):
        self.items.append(item) #添加文件
    
class File(FS_Item):
    def __init__(self, name,size):
        super().__init__(name)
        self.size=size #文件大小

def load_fs(Is_output):
    with open(Is_output,'r') as file:
        lines=file.readlines()
    
    root=None #初始化根文件夹
    directory={}#字典维护目录
    current_path=[]#list表示路径

    for line in lines:
        if line.strip().endswith(':'):
            #该行是目录
            path=line.strip()[:-1]#保存去除尾部：的目录名
            current_path=path.split('/')#/分割文件名
            dirname=current_path[-1]
            folder=Folder(dirname)
            if not root:
                root=folder#设置根目录
            directory[path]=folder#记录目录
            if len(current_path)>1:
                parent_path='/'.join(current_path[:-1])
                directory[parent_path].add_item(folder)#添加到父目录
        elif not line.startswith('total') and line.strip():
            parts=line.split()
            file_name=parts[-1]
            file_size=int(parts[-5])
            new_file=File(file_name,file_size)
            current_dir_path='/'.join(current_path)
            directory[current_dir_path].add_item(new_file)

    return root

'''def print_folder(folder, indent=0):
    """递归打印文件夹内容的辅助函数"""
    print('  ' * indent + folder.name)
    for item in folder.items:
        if isinstance(item, Folder):
            print_folder(item, indent + 1)  # 递归打印子文件夹
        else:
            print('  ' * (indent + 1) + item.name + ' (' + str(item.size) + ' bytes)')

# 加载文件系统结构
top_folder = load_fs('lsoutput.txt')

# 打印文件系统结构
print('文件系统结构：')
print_folder(top_folder)'''

#Problem 5 – Decoding
def decode(ct):
    # 创建一个空字典
    lexical_pos = {i: chr(ord('a') + i) for i in range(26)}
    
    pt=""
    sum=0

    first_char=ct[0]
    pt+=first_char
    sum+=int(ord(first_char))
    #print(sum)

    for char in ct[1:]:
        if char.isalpha() and char.islower():
            for i in range(97,123):
                if lexical_pos[(sum+i)%26]==char:
                    #print(chr(i))
                    pt+=chr(i)
                    sum+=i
                    #print(pt)
                    break
        else:
            pt+=char
            continue
    return pt

print(decode("i uz zwgd jqf"))
print(decode("tmny zk d pmxj."))
print(decode("sidnkw"))