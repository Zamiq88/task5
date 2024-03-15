#task 1
# list1=['alma','armud','ciyelek', 'banan']
# i=0
# while i<len(list1):
#     print(list1[i])
#     i+=1
#************************
#task 2
# list2=['a','b','c','d','e','f','g','h']
# list3=['a','d','h']

# x=0

# while x<len(list2):

#     a=list2[x]
#     x+=1   
    
    
#     if a in list3:
#         continue
    
#     print(a)
#***********************
#task 3 

# k=0
# num=int(input('enter any num'))
# while k<num:
#     k+=1
#     print(k)
#*************************
#task4
# sifre='python'

# for instance in range (0,3):
#     password=input('enter password')
#     if password==sifre:
#         print('ugurlu giris')
#         break
#     k=2-instance
    

           
#     if password!=sifre and k!=0:
#             print(k, 'sansiniz qaldi')
#     elif password!=sifre and k==0:
#             print('3 defe sehv daxil etdiniz block olundunuz')    






#*********************                      
#task 5
print('1-ci sual:	İlk qülə saatı neçənci ildə düzəlib?	 A.	1432 B.	1216 C.	1345 D.	1534')


print('2-ci sual: Çempionlar liqasını 5 dəfə qaldıran klub? A)	Barselona B)Benfika C)	M. Yunayted D)	Liverpul E)	Milan')

print('3-cu sual: Pişiklərin maksimum surəti saatda neçə kilometrdir?	')

print('4-cu sual: 4 ədəd dizi olan yeganə heyvan hansıdır?')

print('5-ci sual Hansı canlının qanı bəyazdır?')
print('6ci sual: 2010cu ilde dunya kubokunu kim qazanib A)Braziliya B)Ispaniya C)Fransa D)Argentina')
duz=0
sehv=0 

cavablar=('A','C','D','A','B','C')
sizin_cavablariniz=[]
for x in range(1,7):
    cavab=input('{}-ci sualin cavabi'.format(x))
    sizin_cavablariniz.append(cavab)
for i in range(0,6):
    if cavablar[i]==sizin_cavablariniz[i]:
        duz+=1
    else:
        sehv+=1 
print('duz cavablarin sayi: ',duz-(sehv//4))
print('sehv cavablarin sayi: ', sehv) 