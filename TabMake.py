class TabMake():

    '''
    此模块为pyfx中补充的制表模块
    '''

    def Tab(list1,index = None,inped = None,sep = 'tab',t='AUTO'):
        '''
        对list1(列表组)制表
        index = "S":显示行列
        index = "H":显示和
        index = "Hpx":显示和并排序
        index = "P":显示平均数
        index = "Ppx":显示平均数并排序
        index = "Z":显示中位数
        index = "Zpx":显示中位数并排序
        index = "F":显示方差
        index = "Fpx":显示方差并排序
        index = "B":显示标准差
        index = "Bpx":显示标准差并排序
        
        inped = "H":显示和
        inped = "P":显示平均数
        inped = "Z":显示中位数
        inped = "F":显示方差
        inped = "B":显示标准差

        sep:表格格式
            tab:正常(行列)
            ---:行
            |||:列
            else:无行列

        t:\\t数量,适用于字多时
        '''
        print(TabMake.tab(list1,index,inped,sep,t))

    def tab(list1,index = None,inped = None,sep = 'tab',t='AUTO'):
        '''
        对list1(列表组)制表
        index = "S":显示行列
        index = "H":显示和
        index = "Hpx":显示和并排序
        index = "P":显示平均数
        index = "Ppx":显示平均数并排序
        index = "Z":显示中位数
        index = "Zpx":显示中位数并排序
        index = "F":显示方差
        index = "Fpx":显示方差并排序
        index = "B":显示标准差
        index = "Bpx":显示标准差并排序
        
        inped = "S":显示行列
        inped = "H":显示和
        inped = "P":显示平均数
        inped = "Z":显示中位数
        inped = "F":显示方差
        inped = "B":显示标准差

        sep:表格格式
            tab:正常(行列)
            ---:行
            |||:列
            else:无

        t:\\t数量,适用于字多时
        '''
        c = ''
        q = ''
        i = 0
        if t == 'AUTO':
            r = TabMake.twm(list1)
            t = r // 8 + 1
        if index == 'H' or index == 'Hpx':
            list1 = TabMake.tahhb(list1)
            if index == 'Hpx':
                list1 = TabMake.tabpx(TabMake.tabdx(list1),1)
                list1 = TabMake.tabdx(list1)
        elif index == 'P' or index == 'Ppx':
            list1 = TabMake.tabhb(list1,TabMake.tahp(list1))
            if index == 'Ppx':
                list1 = TabMake.tabpx(TabMake.tabdx(list1),1)
                list1 = TabMake.tabdx(list1)
        elif index == 'Z' or index == 'Zpx':
            list1 = TabMake.tabhb(list1,TabMake.tahz(list1))
            if index == 'Zpx':
                list1 = TabMake.tabpx(TabMake.tabdx(list1),1)
                list1 = TabMake.tabdx(list1)
        elif index == 'F' or index == 'Fpx':
            list1 = TabMake.tabhb(list1,TabMake.tahf(list1))
            if index == 'Fpx':
                list1 = TabMake.tabpx(TabMake.tabdx(list1),1)
                list1 = TabMake.tabdx(list1)
        elif index == 'B' or index == 'Bpx':
            list1 = TabMake.tabhb(list1,TabMake.tahb(list1))
            if index == 'Bpx':
                list1 = TabMake.tabpx(TabMake.tabdx(list1),1)
                list1 = TabMake.tabdx(list1)
        if index == 'S' or inped == 'S':
            sb = len(list1[0])
            list1 = list1 + [list(range(1,sb))]
        elif inped == 'H':
            count = len(list1[0])
            listT = []
            i = 0
            while i < count:
                i = i + 1
                listT = listT + [TabMake.h(TabMake.tablk(list1,i))]
            list1 = list1 + [listT]
        elif inped == 'P':
            count = len(list1[0])
            listT = []
            i = 0
            while i < count:
                i = i + 1
                listT = listT + [TabMake.pjs(TabMake.tablk(list1,i))]
            list1 = list1 + [listT]
        elif inped == 'Z':
            count = len(list1[0])
            listT = []
            i = 0
            while i < count:
                i = i + 1
                listT = listT + [TabMake.zys(TabMake.tablk(list1,i))]
            list1 = list1 + [listT]
        elif inped == 'F':
            count = len(list1[0])
            listT = []
            i = 0
            while i < count:
                i = i + 1
                listT = listT + [TabMake.fc(TabMake.tablk(list1,i))]
            list1 = list1 + [listT]
        elif inped == 'B':
            count = len(list1[0])
            listT = []
            i = 0
            while i < count:
                i = i + 1
                listT = listT + [TabMake.bzc(TabMake.tablk(list1,i))]
            list1 = list1 + [listT]
        if sep == 'tab':
            count = len(TabMake.listh(str(list1[0])))
            coutt = len(list1[0])
            q = '-' * (8 * t * coutt + 1) + '\n'
            c = q
            list1 = TabMake.tabbj(list1,'|')
        elif sep == '---':
            count = len(TabMake.listh(str(list1[0])))
            coutt = len(list1[0])
            q = '-' * (8 * coutt + 1) + '\n'
            c = q
        elif sep == '|||':
            list1 = TabMake.tabbj(list1,'|')
        for a in list1:
            i = i + 1
            for b in a:
                o = str(b)
                l = t - len(o) // 8
                c = c + o + '\t'*l
            if index == 'S':
                c = c + str(i)
            if sep == '|||' or sep == 'tab':
                c = c + '|'
            c = c + '\n'
            c = c + q
        c = c[0:-1]
        return c

    def tabhb(list1,list2):
        '''
        将list1与list2合并
        '''
        i=0
        listT=[]
        for a in list1:
            if type(a)==list and type(TabMake.listwz(list2,i)) != list:
                listR=a+[TabMake.listwz(list2,i)]
                listT=listT+[listR]
            elif type(a)!=list and type(TabMake.listwz(list2,i)) != list:
                listR=[a]+[TabMake.listwz(list2,i)]
                listT=listT+[listR]
            else:
                listR=a+TabMake.listwz(list2,i)
                listT=listT+[listR]
            i=i+1
        return listT

    def tabfk(tab,listn):
        '''
        删除tab中第listn列
        '''
        listT = []
        listR = []
        a = 0
        for i in tab:
            for t in i:
                a = a + 1
                if a != listn:
                    listT = listT + [t]
            listR = listR + [listT]
            listT = []
            a = 0
        return listR

    def tabset(tab,x,y,n):
        '''
        把表格中的第x列，第y行改成n
        '''
        tab = TabMake.listtset(tab,[y,x],n)
        return tab

    def tabcr(tab,x,listn):
        '''
        向表格中的第x列插入listn
        '''
        a = 0
        listT = []
        for i in tab:
            listT = listT + [TabMake.listadd(i,x,listn[a])]
            a = a + 1
        return listT

    def tablk(tab,x):
        '''
        tab list known
        知道表格中第x列
        '''
        listT = []
        for i in tab:
            listT = listT + [i[x-1]]
        return listT

    def alhb(listall):
        '''
        all list hb
        合并所有列表
        '''
        list1 = listall[0]
        a = 0
        for i in listall:
            a = a + 1
            if a != 1:
                list1 = TabMake.tabhb(list1,i)
        return list1

    def alfk(tab,listall):
        '''
        删除所有列表
        '''
        a = 0
        for i in listall:
            a = TabMake.yyds(listall,i)
            i = i - a
            tab = TabMake.tabfk(tab,i)
        return tab

    def tabpx(list1,wz=2,sx=True):
        '''
        将list1(列表组)按wz位排序
        '''
        wz = wz - 1
        count = len(list1)
        for i in range(count):
            for j in range(i + 1, count):
                a = list1[i]
                b = list1[j]
                a = a[wz]
                b = b[wz]
                if a > b:
                    list1[j],list1[i] = list1[i],list1[j]
        if sx == True:
            list1 = TabMake.dx(list1)
        return list1

    def listwz(list1,wz):
        '''
        获取list1的第wz位的项
        '''
        i=0
        for a in list1:
            if wz==i:
                return a
            i=i+1

    def dx(list1):
        '''
        对list1倒序
        '''
        listT = []
        for i in list1:
            listT = [i] + listT
        return listT

    def tabdx(tab):
        '''
        对表格的行倒序
        '''
        listT = []
        for i in tab:
            listT = listT + [TabMake.dx(i)]
        return listT

    def yyds(list1,n):
        '''
        计算list1中在n之前且大于n的个数
        '''
        listT = []
        ab = 0
        for i in list1:
            if i != n and ab == 0:
                listT = listT + [i]
            else:
                ab = 1
        a = 0
        for i in listT:
            if float(i)>float(n):
                a = a + 1
        return a       

    def a_z():
        '''
        获得A—z的列表
        '''
        return ['A','a','B','b','C','c','D','d','E','e','F','f','G','g','H','h','I','i','J','j','K','k','L','l','M','m','N','n','O','o','P','p','Q','q','R','r','S','s','T','t','U','u','V','v','W','w','X','x','Y','y','Z','z']
    
    def px(list1,list2=None,sx=True):
        '''
        对list1排序，可以默认也可以按照list2
        '''
        listT=[]
        listL=[]
        if list2==None: 
            count = len(list1)
            for i in range(count):
                for j in range(i + 1, count):
                    if list1[i] > list1[j]:
                        list1[i],list1[j] = list1[j],list1[i]
            if sx==False:
                for i in list1:
                    listT=[i]+listT
                return listT
            else:
                return list1
        else:
            for i in list2:
                for a in list1:
                    if a==i:
                        listT=listT+[i]
            a_z=TabMake.a_z()
            for i in a_z:
                for a in listT:
                    b=a[0]
                    if b==i:
                        listT=listT+[a]
            if sx==False:
                for i in listT:
                    listL=[i]+listL
                return listL
            else:
                return listT

    def qc(list1):
        '''
        去除list1中的重复项
        '''
        listT=[]
        for i in list1:
            if i not in listT:
                listT=listT+[i]
        return listT

    def jo(a):
        '''
        判断a的奇(False)偶(True)
        '''
        if int(a/2) != a/2:
            return False  
        else:
            return True
    
    def intlist(list1):
        '''
        获取list1中的整型(float)
        '''
        listT = []
        for i in list1:
            try:
                i = float(i)
            except:
                None
            listT = listT + [i]
        return listT

    def jdz(a):
        '''
        绝对值
        '''
        if a<0:
            return -a
        else:
            return a
    
    def zys(list1):
        '''
        获取list1的中位数
        '''
        list1 = TabMake.intlist(list1)
        list2=TabMake.px(list1)
        a=len(list2)
        if a/2 == int(a/2):
            b,c=list2[a+1],list2[a]
            d=(b+c)/2
        else:
            b=int((a+1)/2)
            d=list2[b]
        d = TabMake.tryint(d)
        return d

    def pjs(list1):
        '''
        获取list1的平均数
        '''
        a = TabMake.h(list1)
        b=a/len(list1)
        b = TabMake.tryint(b)
        return b

    def fc(list1):
        '''
        获取list1的方差
        '''
        list1 = TabMake.intlist(list1)
        a = TabMake.pjs(list1)
        b = 0
        for i in list1:
            b=(a-i)**2+b
        c = b/len(list1)
        c = TabMake.tryint(c)
        return c

    def bzc(list1):
        '''
        获取list1的标准差
        '''
        a=TabMake.fc(list1)
        b=TabMake.tryint(a**0.5)
        return b

    def listadd(list1,a,b,sx=True):
        '''
        往list1中的第a位添加b
        '''
        ai=0
        listT=[]
        if sx==True:
            for i in list1:
                ai=ai+1
                if ai == a:
                    listT=listT+[b]+[i]
                else:
                    listT=listT+[i]
        elif sx==False:
            su=len(list1)
            for i in list1:
                ai=ai+1
                if ai == su-a+1:
                    listT=listT+[b]+[i]
                else:
                    listT=listT+[i]
        return listT
    
    def listdel(list1,a,b=None,sx=True):
        '''
        删除list1中的第a位(b)
        '''
        ai=0
        listT=[]
        if sx==True:
            for i in list1:
                ai=ai+1
                if ai == int(a) and [i]==[b]:
                    listT=listT
                elif ai == int(a) and b==None:
                    listT=listT
                else:
                    listT=listT+[i]
        elif sx==False:
            su=len(list1)
            for i in list1:
                ai=ai+1
                if ai == su-int(a)+1 and [i]==[b]:
                    listT=listT
                elif b==None and ai == su-int(a)+1:
                    listT=listT
                else:
                    listT=listT+[i]
        return listT

    def listset(list1,place,nu):
        '''
        The first object in 'list1' is 1
        '''
        i = 1
        listT = []
        for a in list1:
            if i == place:
                listT = listT + [nu]
            else:
                listT = listT + [a]
            i=i + 1
        return listT

    def listtknown(list1,listplace):
        '''
        The first object in 'list1' is 1
        '''
        count = len(listplace)
        i = 1
        while i <= count:
            a = TabMake.listwz(listplace,(i-1))
            list1 = TabMake.listwz(list1,(a-1))
            i = i+1
        return list1

    def listtset(list1,listplace,nu):
        '''
        The first object in 'list1' is 1
        '''
        count = len(listplace)
        i = 1
        listT = nu
        listplace1 = TabMake.dx(listplace)
        for a in listplace1:
            try:
                listE = TabMake.listtknown(list1,listplace[0:(count-i)])
            except:
                listE = list1
            listT = TabMake.listset(listE,a,listT)
            i = i+1
        return listT

    def listtadd(list1,listplace,nu):
        '''
        The first object in 'list1' is 1
        '''
        count = len(listplace)
        list2 = TabMake.listtknown(list1,listplace[0:(count-1)])
        list2 = TabMake.listadd(list2,listplace[-1],nu)
        list2 = TabMake.listtset(list1,listplace[0:(count-1)],list2)
        return list2

    def listtdel(list1,listplace,nu=None):
        '''
        The first object in 'list1' is 1
        '''
        count = len(listplace)
        list2 = TabMake.listtknown(list1,listplace[0:(count-1)])
        list2 = TabMake.listdel(list2,listplace[-1],nu)
        list2 = TabMake.listtset(list1,listplace[0:(count-1)],list2)
        return list2

    def listh(list1):
        '''
        计算list1中项的总和
        '''
        str1 = ''
        for i in list1:
            str1 = str1 + str(i)
        return str1

    def mop(str1):
        '''
        获取str1中的项
        '''
        listT = []
        a = ''
        listno = [' ','/n','/t',',','.','/','?','!','@','#','$','%','^','&','*','(',')','_','-','=','+','[',']','{','}','"',"'",';',':','<','>','|','（','）','，','。','‘','’','“','”','【','】','—','…','￥','！','~','、','·','`']        
        for i in str1:
            if i not in listno:
                a = a + i
            else:
                listT = listT + [a]
                a = ''
        return listT

    def sswr(nu,ws=2):
        '''
        对nu四舍五入,保留ws位小数
        '''
        if type(nu) == 'int':
            nu = str(nu)+'.'+'0'*16
        else:
            nu = str(nu)+'0'*16
        nu1 = float(nu[0:ws+1])
        if float(nu) - nu1 >= 5*float(str(0.1**ws)[0:ws+4]):
            b = int(str(nu1)[-1])+1
            nu1 = float(str(nu1)[0:-1]+str(b))
        if ws == 0:
            nu1 = TabMake.tryint(nu1)
        return nu1

    def tryint(a):
        '''
        尝试化整,四舍五入
        '''
        if int(a) == a:
            return int(a)
        else:
            return round(a,3)

    def h(list1):
        '''
        计算list1的和
        '''
        a = 0
        for i in list1:
            try:
                a = a + float(i)
            except:
                None
        a = TabMake.tryint(a)
        return a
    
    def tablist(tab,listn):
        '''
        获取表格(tab)中的第listn列
        '''
        listT = []
        for i in tab:
            listT = listT + [i[listn-1]]
        return listT

    def tlp(tab,listn):
        '''
        tab list pjs
        计算表格(tab)中第listn列的平均数
        '''
        list1 = TabMake.tablist(tab,listn)
        list1 = TabMake.pjs(list1)
        return list1

    def tlz(tab,listn):
        '''
        tab list zys
        计算表格(tab)中第listn列的中位数
        '''
        list1 = TabMake.tablist(tab,listn)
        list1 = TabMake.zys(list1)
        return list1

    def tlf(tab,listn):
        '''
        tab list fc
        计算表格(tab)中第listn列的方差
        '''
        list1 = TabMake.tablist(tab,listn)
        list1 = TabMake.fc(list1)
        return list1

    def tlb(tab,listn):
        '''
        tab list bzc
        计算表格(tab)中第listn列的标准差
        '''
        list1 = TabMake.tablist(tab,listn)
        list1 = TabMake.bzc(list1)
        return list1

    def tlh(tab,listn):
        '''
        tab list h
        计算表格(tab)中第listn列的和
        '''
        list1 = TabMake.tablist(tab,listn)
        list1 = TabMake.h(list1)
        return list1

    def thf(tab,hang):
        '''
        tab hang fc
        计算表格(tab)中第hang行的方差
        '''
        list1 = TabMake.tablist(tab,hang)
        list1 = TabMake.fc(list1)
        return list1

    def thp(tab,hang):
        '''
        tab hang pjs
        计算表格(tab)中第hang行的平均数
        '''
        list1 = TabMake.tablist(tab,hang)
        list1 = TabMake.pjs(list1)
        return list1

    def thz(tab,hang):
        '''
        tab hang zys
        计算表格(tab)中第hang行的中位数
        '''
        list1 = TabMake.tablist(tab,hang)
        list1 = TabMake.zys(list1)
        return list1

    def thb(tab,hang):
        '''
        tab hang bzc
        计算表格(tab)中第hang行的标准差
        '''
        list1 = TabMake.tablist(tab,hang)
        list1 = TabMake.bzc(list1)
        return list1

    def thh(tab,hang):
        '''
        tab hang h
        计算表格(tab)中第hang行的和
        '''
        list1 = TabMake.tablist(tab,hang)
        list1 = TabMake.h(list1)
        return list1

    def tahp(tab):
        '''
        tab all hang pjs
        计算表格(tab)中所有行的平均数
        '''
        listT = []
        for i in tab:
            listT = listT + [TabMake.pjs(i)]
        return listT

    def tahz(tab):
        '''
        tab all hang zys
        计算表格(tab)中所有行的中位数
        '''
        listT = []
        for i in tab:
            listT = listT + [TabMake.zys(i)]
        return listT

    def tahf(tab):
        '''
        tab all hang fc
        计算表格(tab)中所有行的方差
        '''
        listT = []
        for i in tab:
            listT = listT + [TabMake.fc(i)]
        return listT

    def tahb(tab):
        '''
        tab all hang bzc
        计算表格(tab)中所有行的标准差
        '''
        listT = []
        for i in tab:
            listT = listT + [TabMake.bzc(i)]
        return listT
    
    def tahh(tab):
        '''
        tab all hang h
        计算表格(tab)中所有行的单独和
        '''
        listT = []
        for i in tab:
            listT = listT + [TabMake.h(i)]
        return listT

    def tahhb(tab):
        '''
        tab all hang (h) hb
        计算表格(tab)中所有行的单独和并合并
        '''
        list1 = TabMake.tahh(tab)
        tab = TabMake.tabhb(tab,list1)
        return tab
            
    def listxc(list1,nu):
        '''
        把list1中的每个项乘以nu
        '''
        listT=[]
        for i in list1:
            i=i*nu
            listT=listT+[i]
        return listT

    def listxj(list1,nu):
        '''
        把list1中的每个项加上nu
        '''
        listT=[]
        for i in list1:
            i=i+nu
            listT=listT+[i]
        return listT

    def listjdz(list1):
        '''
        把list1中的每个项取绝对值nu
        '''
        listT=[]
        for i in list1:
            i=TabMake.jdz(i)
            listT=listT+[i]
        return listT
    
    def listbj(list1,n):
        '''
        把n加上list1中的每个项
        '''
        listT = []
        for i in list1:
            listT = listT + [str(n)+str(i)]
        return listT
        
    def tabbj(tab,n):
        '''
        把n加上表格中的每个项
        '''
        listT = []
        for i in tab:
            listT = listT + [TabMake.listbj(i,n)]
        return listT

    def lwm(list1):
        '''
        list word max
        计算list1中的最大字数
        '''
        b = 0
        for i in list1:
            a = len(str(i))
            b = max(b,a)
        return b

    def twm(tab):
        '''
        tab word max
        计算表格中的最大字数
        '''
        b = 0
        for i in tab:
            a = TabMake.lwm(i)
            b = max(b,a)
        return b


