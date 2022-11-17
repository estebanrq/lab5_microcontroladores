import serial
import csv
import time
OUTPUT_MOVEMENT = "flex"
THRESHOLD = 10
PuertoSerial = serial.Serial(port = '/dev/ttyACM0', baudrate=115200, timeout=1) 

print("Connected")
data_rows = []
header = ['x', 'y', 'z']
# abrir o crear archivo en modo escritura
f = open(OUTPUT_MOVEMENT+'.csv', 'w', encoding='UTF8')  # nombre de archivo = gesto a grabar
# create the csv writer
writer = csv.writer(f)
print(header)
writer.writerow(header)  # escribe encabezado
 
ti = time.perf_counter()
print("\t> Data gathering began")
while(tf-ti < THRESHOLD): 
    input = PuertoSerial.readline().decode('utf-8').replace('\r', "").replace('\n', "")
    input = input.split('\t')
    #if len(input) == 3:   # avoids missing axes on first reading
    #    writer.writerow(input)
    #    print(input)
    tf = time.perf_counter()
print("\t> Data is available")