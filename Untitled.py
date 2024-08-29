#!/usr/bin/env python
# coding: utf-8

# In[54]:


def newstudent(name,cls,height,weight,sport,agility,speed):
 
    student={
        "name":name,
        "clas":cls,
        "height":height,
        "weight":weight,
        "agility":agility,
        "speed":speed,
        "sport":sport
    }
    stu1[name]=student

def prefersport(name,agility,speed):
    if agility > 10 and speed > 20 :
        stu1["name"]["sport"]="football"
    elif agility>10 and speed<20 :
        stu1["name"]["sport"]="basketball"
    elif agility<10 and speed>5 :
        stu1["name"]["sport"]="cricket"
    else :
       stu1["name"]["sport"]="volleyball"
    
stu1={}
newstudent("yash",5,1.8,80,15,25,"");
newstudent("tejas",6,1.7,75,12,15,"");

print(stu1)
for key,val in stu1.items():
    speed=val["speed"]
    agility=val["agility"]
    name=key
    prefersport(name,agility,speed)

print(stu1[name][sport])


# In[ ]:




