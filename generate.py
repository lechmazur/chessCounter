from math import comb

path = 'u:/ChessCounter/'

f = open(path + 'combsWB.txt','w')
for w in range(0, 16):
    for b in range(0, 16):
        f.write(str(w*16+b)+'\n')
        f.write(str(float(comb(62,w)*comb(62-w,b)*5**(w+b)))+'\n')
f.close()


f = open(path + 'combs.txt','w')
for p in range(0, 31):
   f.write(str(p)+'\n')
   f.write(str(float(comb(62,p)*10**p))+'\n')
f.close()


f = open(path + 'restricted.txt','w')
c = 0
sum  = 0
xmax = 0
tmax = 0


pawnConfigs = 8+1
bishopConfigs = 2+1
knightConfigs = 2+1
rookConfigs = 2+1
queenConfigs = 3+1

for wp in range(0, pawnConfigs):
    for bp in range(0, pawnConfigs):
       for wn in range(0, knightConfigs):
          for bn in range(0, knightConfigs):
             for wb in range(0, bishopConfigs):
                for bb in range(0, bishopConfigs):
                   for wr in range(0, rookConfigs):
                      for br in range(0, rookConfigs):
                         for wq in range(0, min(min(queenConfigs,16-wp-wn-wb-wr),31-wp-wn-wb-wr-bp-bn-bb-br)):
                            for bq in range(0, min(min(queenConfigs,16-bp-bn-bb-br),31-wp-wn-wb-wr-bp-bn-bb-br-wq)):
                               c += 1
                               x = comb(62,wp) * comb(62-wp,bp) * comb(62-wp-bp,wn) * comb(62-wp-bp-wn,bn) * comb(62-wp-bp-wn-bn,wb) * comb(62-wp-bp-wn-bn-wb,bb) *\
                               comb(62-wp-bp-wn-bn-wb-bb,wr) * comb(62-wp-bp-wn-bn-wb-bb-wr,br) * comb(62-wp-bp-wn-bn-wb-bb-wr-br,wq) * comb(62-wp-bp-wn-bn-wb-bb-wr-br-wq,bq)
                               sum += x
                               t = wp+bp+wn+bn+bb+wr+br+wq+bq
                               if t>tmax:
                                  tmax = t
                                  print(tmax)   
                               if (x>xmax):
                                  xmax = x
                                  print(xmax, wp,bp,wn,bn,wb,bb,wr,br,wq,bq)

                               f.write(str(bq+wq*queenConfigs
                                           +br*queenConfigs*queenConfigs
                                           +wr*queenConfigs*queenConfigs*rookConfigs
                                           +bb*queenConfigs*queenConfigs*rookConfigs*rookConfigs
                                           +wb*queenConfigs*queenConfigs*rookConfigs*rookConfigs*bishopConfigs
                                           +bn*queenConfigs*queenConfigs*rookConfigs*rookConfigs*bishopConfigs*bishopConfigs
                                           +wn*queenConfigs*queenConfigs*rookConfigs*rookConfigs*bishopConfigs*bishopConfigs*knightConfigs
                                           +bp*queenConfigs*queenConfigs*rookConfigs*rookConfigs*bishopConfigs*bishopConfigs*knightConfigs*knightConfigs
                                           +wp*queenConfigs*queenConfigs*rookConfigs*rookConfigs*bishopConfigs*bishopConfigs*knightConfigs*knightConfigs*pawnConfigs)+'\n')
                               f.write(str(float(x))+'\n')
print(3612*2*sum, c)
print(float(3612*2*sum))
f.close()



f = open(path + 'veryRestricted.txt','w')
c = 0
sum  = 0
xmax = 0
tmax = 0

pawnConfigs = 8+1
bishopConfigs = 2+1
knightConfigs = 2+1
rookConfigs = 2+1
queenConfigs = 1+1

for wp in range(0, pawnConfigs):
    for bp in range(0, pawnConfigs):
       for wn in range(0, knightConfigs):
          for bn in range(0, knightConfigs):
             for wb in range(0, bishopConfigs):
                for bb in range(0, bishopConfigs):
                   for wr in range(0, rookConfigs):
                      for br in range(0, rookConfigs):
                         for wq in range(0, min(min(queenConfigs,16-wp-wn-wb-wr),31-wp-wn-wb-wr-bp-bn-bb-br)):
                            for bq in range(0, min(min(queenConfigs,16-bp-bn-bb-br),31-wp-wn-wb-wr-bp-bn-bb-br-wq)):
                               c += 1
                               x = comb(62,wp) * comb(62-wp,bp) * comb(62-wp-bp,wn) * comb(62-wp-bp-wn,bn) * comb(62-wp-bp-wn-bn,wb) * comb(62-wp-bp-wn-bn-wb,bb) * \
                               comb(62-wp-bp-wn-bn-wb-bb,wr) * comb(62-wp-bp-wn-bn-wb-bb-wr,br) * comb(62-wp-bp-wn-bn-wb-bb-wr-br,wq) * comb(62-wp-bp-wn-bn-wb-bb-wr-br-wq,bq)
                               sum += x
                               t = wp+bp+wn+bn+bb+wr+br+wq+bq
                               if t>tmax:
                                  tmax = t
                                  print(tmax)   
                               if (x>xmax):
                                  xmax = x
                                  print(xmax, wp,bp,wn,bn,wb,bb,wr,br,wq,bq)

                               f.write(str(bq+wq*queenConfigs
                                           +br*queenConfigs*queenConfigs
                                           +wr*queenConfigs*queenConfigs*rookConfigs
                                           +bb*queenConfigs*queenConfigs*rookConfigs*rookConfigs
                                           +wb*queenConfigs*queenConfigs*rookConfigs*rookConfigs*bishopConfigs
                                           +bn*queenConfigs*queenConfigs*rookConfigs*rookConfigs*bishopConfigs*bishopConfigs
                                           +wn*queenConfigs*queenConfigs*rookConfigs*rookConfigs*bishopConfigs*bishopConfigs*knightConfigs
                                           +bp*queenConfigs*queenConfigs*rookConfigs*rookConfigs*bishopConfigs*bishopConfigs*knightConfigs*knightConfigs
                                           +wp*queenConfigs*queenConfigs*rookConfigs*rookConfigs*bishopConfigs*bishopConfigs*knightConfigs*knightConfigs*pawnConfigs)+'\n')
                               f.write(str(float(x))+'\n')
print(3612*2*sum, c)
print(float(3612*2*sum))
f.close()

