import csv
import click
from datetime import date
from datetime import timedelta
from datetime import datetime
from time import gmtime, strftime
import time
import re


@click.group()
def cli():
    pass

@click.group()
def think():
    pass
@think.command()
@click.option('-m')
def add(m):
   """you can add every thiink  with  -m to help remind and think latter  """
   contacts_info=[]
   if '@' in m:
       findc=re.search('(?<=@)\w+',m)
       name=findc.group(0)
       resualt=findcontact(name)
       if resualt != []: 
            adding(m,resualt)
       else:
            adding(m,'no')
                   
                   
   else:
        contacts_info.append('no')
        adding(m,contacts_info)
def adding(think,contact):
   """just adding function"""
   alan=date.today()
   saat=time.strftime("%H:%M:%S")
   tarikhalan=date.today()
   contacts_info=contact
   file=open('think.csv','a+')
   print(think,tarikhalan,saat,contacts_info,'--todo',file=file)
   file.close()

def findcontact(name):
    file=open('contact.csv','r')
    readingline=file.readlines()
    resualt=[]
    for i in readingline:
        if name in i:
           resualt.append(i)
    
    file.close()
    return resualt 
   
def findingthink(string):
    file=open('contact.csv','r')
    readingline=file.readlines()
    resualt=[]
    for i in readingline:
        if name in i:
           resualt.append(i)
    
    file.close()
    return resualt           
                  

@think.command()
def lthink():
   """ list all think """
   file=open('think.csv','r')
   a=file.readlines()
   b=[]   
   for i in a:
      click.echo(click.style(i,fg='blue',bold=True))
      b.append(1)
   file.close()
def linecounter():
   """countink line"""
   file=open('think.csv','r')
   a=file.readlines()
   b=[]
   for i in a:
      b.append(1)
   file.close()
   return sum(b)

@think.command()
def find():
   """ find a think """
   search=input('what')
   file=open('think.csv','r')
   a=file.readlines()
   b=[]   
   for i in a:
      if search in i:
          click.echo(click.style(i,fg='blue',bold=True))
          b.append(1)
   file.close()
   print('Total search  count  is %s'%sum(b)) 
   a=int(linecounter())
   percent=int(sum(b))/a*100
   click.echo(click.style('the Percent of this search in total is %s  '%percent,fg='red',bold=True))

cli = click.CommandCollection(sources=[cli,think])
