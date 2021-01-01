from threading import *# for using multi threading
import time
class datastore(Thread):
    dic={}# it is a dictionary, used to store keys and values
    def create(self,key,value,tout=0):
        self.key=key
        self.value=value
        self.tout=tout
        if ((self.key) in self.dic):
            print("raise error:key already stored")# it is a error message if key_name is already exists
        else:
            if((self.key).isalpha()):# check weather given key_name is alphabets
                if len(self.dic)<(1024*1024*8) and self.value<=(16*1024*8):# size of the file should contain less than 1GB and size of the value should be less than 16kb
                    if self.tout==0:
                        l=[self.value,self.tout]
                    else:
                        l=[self.value,time.time()+self.tout]
                    if len(self.key)<=32:# length of key_name should be less than 32
                        self.dic[self.key]=l
                        print("data successfully stored")
                else:
                    print("raise error:memory limit exceeded")# error message
            else:
                print("raise error: Invalid key 'key should contain only alphabets'")# error message
        time.sleep(0.05)


class dataread(datastore,Thread):
    def read(self,key):
        self.key=key
        if self.key not in self.dic:
            print("raise error: given key doesn't exist in the database")
        else:
            exp=self.dic[self.key]
            if exp[1]!=0:
                if time.time()<exp[1]:# compare present time with expiry time
                    s=self.key+"-"+str(exp[0])
                    print(s)
                else:
                    print("raise error:Time to live of ",self.key,"has expired")#error message
            else:
                s=self.key+"-"+str(exp[0])
                print(s)
        time.sleep(0.05)

class dataremove(dataread,Thread):
    def delete(self,key):
        self.key=key
        if self.key not in self.dic:
            print("raise error: given key doesn't exist in the database")
        else:
            exp=self.dic[self.key]
            if exp[1]!=0:
                if time.time()<exp[1]:# compare present time with expiry time
                    del self.dic[self.key]
                    print("key is successfully deleted")
                else:
                    print("raise error:Time to live of ",self.key,"has expired")# error message
            else:
                del self.dic[self.key]
                print("key is successfully deleted")
        time.sleep(0.05)
access=dataremove()

