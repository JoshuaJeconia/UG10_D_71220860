print('=' * 25)
print('operasi matematika')
print(' 1. Jumlah \t [+]')
print(' 2. Kurang \t [-]')
print(' 3. kali \t [*]')
print(' 4. bagi \t [%]')
print('=' * 25)
operasi = input('pilihan operasi (1/2/3/4): ')
bilangan_1 = eval(input('masukan bilangan pertama: '))
bilangan_2 = eval(input('masukan bilangan kedua: '))

if operasi == '1':
  hasil = bilangan_1 + bilangan_2
  print(f'Hasil operasi dari {bilangan_1} + {bilangan_2} = {hasil}')
elif operasi == '2':
  hasil = bilangan_1 - bilangan_2
  print(f'Hasil operasi dari {bilangan_1} - {bilangan_2} = {hasil}')
elif operasi == '3':
  hasil = bilangan_1 * bilangan_2
  print(f'Hasil operasi dari {bilangan_1} * {bilangan_2} = {hasil}')
elif operasi == '4':
  hasil = bilangan_1 / bilangan_2
  print(f'Hasil operasi dari {bilangan_1} / {bilangan_2} = {hasil}')
else:
  print('Tidak valid')