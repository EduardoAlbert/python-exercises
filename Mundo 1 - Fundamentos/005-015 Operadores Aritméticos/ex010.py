print('Saiba quantos dólares você pode comprar:')
vr = float(input('Quantos reais você tem?R$'))
vd = vr / 3.76

print('Com R${} você pode comprar:'.format(vr))
print('US${:.2f}'.format(vd))