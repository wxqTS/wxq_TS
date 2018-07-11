# coding=utf-8
import pymysql
from scrapy.utils.project import get_project_settings #����seetings����

class DBHelper():
    
    '''�����Ҳ�Ƕ�ȡsettings�е����ã������޸Ĵ�����в���'''
    def __init__(self):
        self.settings=get_project_settings() #��ȡsettings���ã�������Ҫ����Ϣ
        
        self.host=self.settings['MYSQL_HOST']
        self.port=self.settings['MYSQL_PORT']
        self.user=self.settings['MYSQL_USER']
        self.passwd=self.settings['MYSQL_PASSWD']
        self.db=self.settings['MYSQL_DBNAME']
    
    #���ӵ�mysql���������ӵ���������ݿ�
    def connectMysql(self):
        conn=pymysql.connect(host=self.host,
                             port=self.port,
                             user=self.user,
                             passwd=self.passwd,
                             #db=self.db,��ָ�����ݿ���
                             charset='utf8') #Ҫָ�����룬�������Ŀ�������
        return conn
    #���ӵ���������ݿ⣨settings�����õ�MYSQL_DBNAME��
    def connectDatabase(self):
        conn=pymysql.connect(host=self.host,
                             port=self.port,
                             user=self.user,
                             passwd=self.passwd,
                             db=self.db,
                             charset='utf8') #Ҫָ�����룬�������Ŀ�������
        return conn   
    
    #�������ݿ�
    def createDatabase(self):
        '''��Ϊ�������ݿ�ֱ���޸�settings�е�����MYSQL_DBNAME���ɣ����ԾͲ�Ҫ��sql�����'''
        conn=self.connectMysql()#�������ݿ�
        
        sql="create database if not exists "+self.db
        cur=conn.cursor()
        cur.execute(sql)#ִ��sql���
        cur.close()
        conn.close()
    
    #������
    def createTable(self,sql):
        conn=self.connectDatabase()
        
        cur=conn.cursor()
        cur.execute(sql)
        cur.close()
        conn.close()
    #��������
    def insert(self,sql,*params):#ע������paramsҪ��*,��Ϊ���ݹ�������Ԫ�飬*��ʾ������������
        conn=self.connectDatabase()
        
        cur=conn.cursor();
        cur.execute(sql,params)
        conn.commit()#ע��Ҫcommit
        cur.close()
        conn.close()
    #��������
    def update(self,sql,*params):
        conn=self.connectDatabase()
        
        cur=conn.cursor()
        cur.execute(sql,params)
        conn.commit()#ע��Ҫcommit
        cur.close()
        conn.close()
    
    #ɾ������
    def delete(self,sql,*params):
        conn=self.connectDatabase()
        
        cur=conn.cursor()
        cur.execute(sql,params)
        conn.commit()
        cur.close()
        conn.close()
        
        

'''����DBHelper����'''
class TestDBHelper():
    def __init__(self):
        self.dbHelper=DBHelper()
               
    #���Դ������ݿ⣨settings�����ļ��е�MYSQL_DBNAME,ֱ���޸�settings�����ļ����ɣ�
    def testCreateDatebase(self):
        self.dbHelper.createDatabase() 
    #���Դ�����
    def testCreateTable(self):
        sql="create table testtable(id int primary key auto_increment,name varchar(50),url varchar(200))"
        self.dbHelper.createTable(sql)
    #���Բ���
    def testInsert(self):
        sql="insert into testtable(name,url) values(%s,%s)"
        params=("test","test")
        self.dbHelper.insert(sql,*params) #  *��ʾ���Ԫ�飬����insert��*params���������Ԫ��
    def testUpdate(self):
        sql="update testtable set name=%s,url=%s where id=%s"
        params=("update","update","1")
        self.dbHelper.update(sql,*params)
    
    def testDelete(self):
        sql="delete from testtable where id=%s"
        params=("1")
        self.dbHelper.delete(sql,*params)
    
if __name__=="__main__":
    testDBHelper=TestDBHelper()
    #testDBHelper.testCreateDatebase()  #ִ�в��Դ������ݿ�
    #testDBHelper.testCreateTable()     #ִ�в��Դ�����
    #testDBHelper.testInsert()          #ִ�в��Բ�������
    #testDBHelper.testUpdate()          #ִ�в��Ը�������
    #testDBHelper.testDelete()          #ִ�в���ɾ������