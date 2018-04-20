def tambah ():
    print ('1. penjumlahan')
    a = int (input ('masukan nilai x= '))
    b = int (input ('masukan nilai y= '))
    c = a+b
    print ('x+y=',c)
    tanya()
def kurang():
    print('2.pengurangan')
    a = int(input('masukan nilai x= '))
    b = int(input('masukan nilai y= '))
    c = a-b
    print ('x+y=',c)
    tanya()
def kurang():
    print('2.pengurangan')
    a = int (input('masukan nilai x= '))
    b = int (input('masukan nilai y= '))
    c = a-b
    print ('x-y=',c)
    tanya()
def bagi():
    print('3.pembagian')
    a = int(input('masukan nilai x= '))
    b = int(input('masukan nilai y= '))
    c = a/b
    print ('x/y=',c)
    tanya()
def kali():
    print('4.perkalian')
    a = int(input('masukan nilai x= '))
    b = int(input('masukan nilai y= '))
    c =a*b
    print ('x*y=',c)
    tanya()

def tanya():
    tanya = input("\nkembali ke menu (y/t)? ")
    if tanya == "y":
        menu_kalkulator()
    elif tanya =="t":
        exit
    else:
        print("n\salah input..........!!!")

def menu_kalkulator():
    print("==================================")
    print("program kalkulator sederhana")
    print("==================================")
    print("\t1. penjumlahan")
    print("\t2. pengurangan")
    print("\t3. pembagian")
    print("\t4. perkalian")
    print("==================================")
    print("silahkan pilih 1-4")
    print(" ")
    pil = input("masukkan pilihan : ")
    if pil == '1':
        tambah()
    elif pil == '2':
        kurang()
    elif pil == '3':
        bagi()
    elif pil == '4':
        kali()
    else:
        print("maaf, input yang anda masukan salah")
        print("coba ulangi kembali...")
        tanya()
