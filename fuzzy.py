import RPi.GPIO as GPIO


print('Testing for Fuzzzy Logic')

sensor1 = input('Nilai ldr1 :')
sensor2 = input('Nilai ldr21 :')
sensor3 = input('Nilai ldr3 :')
sensor4 = input('Nilai ldr4 :')

ldr1 = float(sensor1)
ldr2 = float(sensor2)
ldr3 = float(sensor3)
ldr4 = float(sensor4)

#Proses Fuzzyfikasi LDR1
if ldr1 <= 50 :
    value_gelap = 1
    value_sedang = 0 
    value_terang = 0
if ldr1 > 50 and ldr1 < 100 :
    value_gelap = (100-ldr1)/(100-50)
    value_terang = 0
if ldr1 > 50 and ldr1 < 150 :
    value_sedang = (ldr1-50)/(150-50) 
if ldr1 == 150 :
    value_gelap = 0
    value_sedang = 1
    value_terang = 0
if ldr1 > 150 and ldr1 < 250 :
    value_gelap = 0
    value_sedang = (250-ldr1)/(250-150)
if ldr1 > 200 and ldr1 <250 :
    value_gelap = 0
    value_terang = (ldr1-200)/(250-200)
if ldr1 >= 250 :
    value_gelap = 0
    value_sedang = 0
    value_terang = 1
print('Maka ')
print('Gelap' , value_gelap)
print('Sedang' , value_sedang)
print('terang', value_terang)

#Proses Fuzzyfikasi LDR2
if ldr2 <= 50 :
    value_gelap1 = 1
    value_sedang1 = 0 
    value_terang1 = 0
if ldr2 > 50 and ldr2 < 100 :
    value_gelap1 = (100-ldr2)/(100-50)
    value_terang1 = 0
if ldr2 > 50 and ldr2 < 150 :
    value_sedang1 = (ldr2-50)/(150-50) 
if ldr2 == 150 :
    value_gelap1 = 0
    value_sedang1 = 1
    value_terang1 = 0
if ldr2 > 150 and ldr2 < 250 :
    value_gelap1 = 0
    value_sedang1 = (250-ldr2)/(250-150)
if ldr2 > 200 and ldr2 <250 :
    value_gelap1 = 0
    value_terang1 = (ldr2-200)/(250-200)
if ldr2 >= 250 :
    value_gelap1 = 0
    value_sedang1 = 0
    value_terang1 = 1
print('Maka ')
print('Gelap1' , value_gelap1)
print('Sedang1' , value_sedang1)
print('terang1', value_terang1)

#Proses Fuzzyfikasi LDR3
if ldr3 <= 50 :
    value_gelap2 = 1
    value_sedang2 = 0 
    value_terang2 = 0
if ldr3 > 50 and ldr3 < 100 :
    value_gelap2 = (100-ldr3)/(100-50)
    value_terang2 = 0
if ldr3 > 50 and ldr3 < 150 :
    value_sedang2 = (ldr3-50)/(150-50) 
if ldr3 == 150 :
    value_gelap2 = 0
    value_sedang2 = 1
    value_terang2 = 0
if ldr3 > 150 and ldr3 < 250 :
    value_gelap2 = 0
    value_sedang2 = (250-ldr2)/(250-150)
if ldr3 > 200 and ldr3 <250 :
    value_gelap2 = 0
    value_terang2 = (ldr3-200)/(250-200)
if ldr3 >= 250 :
    value_gelap2 = 0
    value_sedang2 = 0
    value_terang2 = 1
print('Maka ')
print('Gelap1' , value_gelap2)
print('Sedang1' , value_sedang2)
print('terang1', value_terang2)


#Proses Fuzzyfikasi LDR4
if ldr4 <= 50 :
    value_gelap3 = 1
    value_sedang3 = 0 
    value_terang3 = 0
if ldr4 > 50 and ldr4 < 100 :
    value_gelap3 = (100-ldr4)/(100-50)
    value_terang3 = 0
if ldr4 > 50 and ldr4 < 150 :
    value_sedang3 = (ldr4-50)/(150-50) 
if ldr4 == 150 :
    value_gelap3 = 0
    value_sedang3 = 1
    value_terang3 = 0
if ldr4 > 150 and ldr4 < 250 :
    value_gelap3 = 0
    value_sedang3 = (250-ldr4)/(250-150)
if ldr4 > 200 and ldr4 <250 :
    value_gelap3 = 0
    value_terang3 = (ldr4-200)/(250-200)
if ldr4 >= 250 :
    value_gelap3 = 0
    value_sedang3 = 0
    value_terang3 = 1
print('Maka ')
print('Gelap1' , value_gelap3)
print('Sedang1' , value_sedang3)
print('terang1', value_terang3)