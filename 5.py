def buyNoodle(tgl,uang):
    mie = int(2500)
    bonus = 0
    if tgl % 2 != 0:
        bonus +=1*int(uang/7500)
    if tgl % 2 == 0:
        bonus +=1*int(uang/10000)
    if tgl % 5 == 0:
        if bonus % 2 == 0:
            bonus *= 10
        else:
            bonus *= 5
    jumlah_mie = int((uang / mie)+ bonus)
    return jumlah_mie

