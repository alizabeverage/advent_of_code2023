f = open('/Users/alizabeverage/Downloads/adventofcode.com_2023_day_1_input.txt','r')
lines = f.readlines()
f.close()

nums_str = {'one':'1','two':'2','three':'3','four':'4','five':'5','six':'6','seven':'7','eight':'8','nine':'9'}

def get_string(line):
    found1 = 0
    switch = 'on'
    for i,ch in enumerate(line):
        if switch == 'off':continue
        for string,num in nums_str.items():
            if string in line[:i]:
                line_tmp1 = line.replace(string,num)
                switch = 'off'
                found1+=1

    found2 = 0
    switch = 'on'
    for i,ch in enumerate(line):
        if switch == 'off':continue
        for string,num in nums_str.items():
            if string in line[-(i+1):]:
                line_tmp2 = line.replace(string,num)
                switch = 'off'
                found2+=1

    if found2==0:
        line_tmp2 = line
    if found1 == 0:
        line_tmp1 = line
    return line_tmp1, line_tmp2


arr = []
for line in lines:
    left, right = get_string(line)
    
    x = ''
    switch = 'on'
    for ch in left:
        if switch == 'off': continue
        if ch in ['0','1','2','3','4','5','6','7','8','9']:
            x+=ch
            switch = 'off'

    switch = 'on'
    for ch in right[::-1]:
        if switch == 'off': continue
        if ch in ['0','1','2','3','4','5','6','7','8','9']:
            x+=ch
            switch = 'off'

    arr.append(x)

# nums_str = {'one':'1','two':'2','three':'3','four':'4','five':'5','six':'6','seven':'7','eight':'8','nine':'9'}

arrint = np.array(arr).astype(int)
arrint.sum()
