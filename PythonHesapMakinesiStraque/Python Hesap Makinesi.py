 # Lütfen iznim olmadan bir platformda paylaşmayınız.Kendini geliştirmeye çalışanlar için yaptığım bir en basit hesap makinesidir.

print(
    '''
    ~ # Lütfen iznim olmadan bir platformda paylaşmayınız.Kendini geliştirmeye çalışanlar için yaptığım bir en basit hesap makinesidir..~
   
   
    toplama(+) 
    çıkarma(-)
    çarpma(*)
    bölme(/)
'''
)
while True:

 islem =input('yapmak istediğniiz işlemi giriniz (+-*/):')
 sayi1 = int(input("1.sayıyı giriniz:"))
 sayi2 = int(input("2.sayıyı giriniz:"))

 if islem == '+':
    print(sayi1 , '+' , sayi2 , '=' , sayi1 + sayi2)
   

 elif islem == '-':
    print(sayi1 , '-' , sayi2 , '=' , sayi1 - sayi2)
   


 elif islem == '*':
    print(sayi1 , '*' , sayi2 , '=' , sayi1 * sayi2)
   


 elif islem == '/':
    print(sayi1 , '/' , sayi2 , '=' , sayi1 // sayi2)
   

 else:
    print('geçersiz işlem girdiniz')
 
