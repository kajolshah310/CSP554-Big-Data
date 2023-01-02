from time import sleep
from json import dumps
from kafka import KafkaProducer

Producer = KafkaProducer(bootstrap_servers = ['localhost:9092'],value_serializer = lambda x: dumps(x).encode('utf-8'))

synmyid = 'MYID'
synmyname = 'MYNAME'
synmyeyecolor = 'MYEYECOLOR'

id = input("Enter your ID: ")
name = input("Enter your name: ")
eyecolor = input("Enter your eye color: ")

my_dict = {}
my_dict[synmyid] = id

my_dict1 = {}
my_dict1[synmyname] = name

my_dict2 = {}
my_dict2[synmyeyecolor] = eyecolor

myid = my_dict
Producer.send('sample',myid)
sleep(4)

myname = my_dict1
Producer.send('sample',myname)
sleep(4)

myeyecolor = my_dict2
Producer.send('sample',myeyecolor)
sleep(4)

Producer.close()

