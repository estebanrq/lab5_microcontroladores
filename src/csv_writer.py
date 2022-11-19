import serial
import csv
import time
OUTPUT_MOVEMENT = "leftright"
TIME_THRESHOLD = 10
PuertoSerial = serial.Serial(port = '/dev/ttyACM0', baudrate=115200, timeout=1) 

print("Connected")
data_rows = []
header = ['gX', 'gY', 'gZ']
# abrir o crear archivo en modo escritura
f = open(OUTPUT_MOVEMENT+'.csv', 'w', encoding='UTF8')  # nombre de archivo = gesto a grabar
# create the csv writer
writer = csv.writer(f)
print(header)
writer.writerow(header)  # escribe encabezado
 
ti = time.perf_counter()
tf = time.perf_counter()
print("Initial Time: "+str(ti))
print("\t> Data gathering began\n")
sample_counter = 0
while(tf-ti < TIME_THRESHOLD): 
    input = PuertoSerial.readline().decode('utf-8').replace('\r', "").replace('\n', "")
    input = input.split('\t')
    writer.writerow(input)
    tf = time.perf_counter()
    sample_counter = sample_counter+1
print("Final  Time: "+str(tf))
print("Samples: "+str(sample_counter))    
print("\t> Data is available on" + str(OUTPUT_MOVEMENT))