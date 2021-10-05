bums=open('teksts.txt', 'a', encoding='utf8')
bums.write('Grobiņā nav sniega!')

bums=open('teksts.txt', 'r', encoding='utf8')
print(bums.read())



bums.close()