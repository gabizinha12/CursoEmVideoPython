n = int(input())
cont = 1
while cont <= 10:
    calc = n * cont
    import time
    time.sleep(0.1)
    print ("{} x {} = {}".format(n, cont, calc))
    cont += 1