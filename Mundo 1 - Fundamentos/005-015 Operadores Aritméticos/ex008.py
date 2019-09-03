x = float(input('Valor em Metros:'))
cm = x*100
mm = x*1000
dm = x*10
km = x / 1000
hm = x / 100
dam = x / 10

print('{} Metros, equivale a:\n{}dm\n{}cm\n{}mm\n{}km\n{}hm\n{}dam.'.format(x, dm, cm, mm, km, hm, dam))
