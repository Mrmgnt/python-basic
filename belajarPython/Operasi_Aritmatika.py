#operasi aritmatika

a = 10
b = 3

# operasi tambah +
hasil = a + b
print(a,'+',b, '=',hasil)

# operasi pengurangan -
hasil = a - b
print(a,'-',b, '=',hasil)

# operasi perkalian
hasil = a * b
print(a,'x',b, '=',hasil)

# operasi perkalian
hasil = a * b
print(a,'x',b, '=',hasil)

# operasi Pembagian
hasil = a / b
print(a,'/',b, '=',hasil)

# operasi eksponen (pangkat) **
hasil = a ** b
print(a,'**',b, '=',hasil)

# operasi Modulus  (kebalikan modulus) **
hasil = a % b
print(a,'%',b, '=',hasil)

# operasi Floor division  (kebalikan modulus) **
hasil = a // b
print(a,'//',b, '=',hasil)

# Prioritas Operasi, operatiopnal preceded
'''
Urutan Operasi Matematika
        1. ()
        2.exponen **
        3.perkalian n friend * / **  %  //
        4.pertambahan n pengurangan
'''
x = 3
y = 2
z = 4

hasil = x ** y * z + x / y - y % z // x
print(x,'**', y,'*',z,'+',x,'/',y,'-',y,'%',z,'//',x,'=',hasil )

hasil = (x + y) * z
print('(',x,"+", y,')' "*", z,'=',hasil)
