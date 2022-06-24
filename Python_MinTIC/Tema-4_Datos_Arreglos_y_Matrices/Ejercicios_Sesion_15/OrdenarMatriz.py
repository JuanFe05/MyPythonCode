from operator import itemgetter
a=[[1,"Santander"],[2,"Cordoba"],[3,"Macro"]]
bco_x_des=sorted(a, key=itemgetter(0))
print(bco_x_des)