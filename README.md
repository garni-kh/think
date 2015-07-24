# think
think you have write like git commit 
"think" python base ,console base  "todo list "application ,run in console in unix and linux or may be in windows ,it is for the people may be want write the think which want do it in past ,very simple 
the way is simple just python and i inspire from git ,and my thank to  armin ronacher for click  python mudoles  which help me do it in command line .

$ con add -m "stability test server methot"

$ con add -m "call @home "

$ con search

what stability 

## git about code , "think "about life think  

it  can manage 
Percent of work witch we do and we must do it  , in end of day make you happy when see improvement in number  

"think" do not use database ,every think save in simple  csv  file 
i start this project when i think i have concentrate problem ,i can not  track my work i always think about every think and do nothing when i  do  work ."think" about think  ,read some text  and try write my  think in paper  then i made this for write in this ,may be help  you concentrate problem and hope solve that and filing happy .

# installation 

you need :

1.python3.3 deploy on you system 

2.virtualvenv

3.git

installing steps:

$ sudo easy_install virtualenv 

or better

$ pip install virtualenv-3.3

$ git clone https://github.com/garni-kh/think.git

$ cd think

$ virtualvenv-3.3 venv

$ . venv/bin/activate 

now you can pip click

(venv)$ pip install Click

after this you setup con command work in  ccommand line. 

(vevn)$ pip install --editable .

now you can test 

(venv)$ con add -m "hello works"

you can vim think.csv  if you in think directory 

and see new line added with time and date 

or just 

$ con

Usage: con [OPTIONS] COMMAND [ARGS]...

Options:

  --help  Show this message and exit.

Commands:

  add     you can add every thiink to help remind and...
  
  find    find a think
  
  lthink  list all think

# working with think 

after setup think , you can use con in command line until (venv) active .

why i disided using con ,"con"  is from  concentrate  , and hope  this method of working help you  , when some think in midle of console come and distube your  oncentrate  just  fire up think  and write  it  ,and  try  think about that problem in past. think work with vim or any  text editing  aplication but of course vi or vim better in midle of console when add think or i say it consentrate abusing think just

$ con add -m "do a good work every day "

my first think i remeber in child hood (scout) ,

$ vim think.csv 

and you see added line .

do a good work a day 2015-07-24 23:33:14 ['no'] --todo

you can have report for youre  think list  with

$  con lthink

hello works 2015-07-24 21:55:57 ['no'] --todo

do a good work a day 2015-07-24 23:33:14 ['no'] --todo

or you can find some work let  try 

$ con find
what good
do a good work a day 2015-07-24 23:33:14 ['no'] --todo

total search  count  is 1

the Percent of this search in total is 50

con say you good is 1  think you have   and  50%   of you   con   problem   

ok when done  a nice  work  then what ,just open up think .csv  with vim  and find  the line  and  you  can edit  --todo  to --do ,i do this now

in end of the day you want know how much  development in works  

$ con find

what --do

do a good work a day 2015-07-24 23:33:14 ['no'] --do

total search  count  is 1

the Percent of this search in total is 50.0 

ok you can now  50%  work done  with find  

in contact.csv you can add your contact list just 

$ vim contact.csv 

add for example

home,0218888222

save it and close

if you want contact information Appear in task list or think list  after adding  contact  name and  call  information  you can do this  

$ con add -m "call @home" 

$ con lthink

hello works 2015-07-24 21:55:57 ['no'] --todo

do a good work a day 2015-07-24 23:33:14 ['no'] --do

call @home 2015-07-25 00:33:17 ['home,0218888222\n'] --todo

you can see home contact information  in new  think list  ,  just pick up  phone   and call  


#note

this is my first git hub aplication ,very simple just python help for editing file ,i hope this concept help  pepole  which tired from task managment aplication and like old style ..   I'd be happy  if you help me to improve  this  concept .again i want to say my thank to click author armin  and  Guido van Rossum   for creation of python   .  

