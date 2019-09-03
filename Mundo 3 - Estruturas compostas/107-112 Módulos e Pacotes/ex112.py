from ex111.utilitiesCeV import coin
from ex111.utilitiesCeV.data import readMoney

p = readMoney('Digite o preço: R$')
coin.resume(p, 35, 22)
