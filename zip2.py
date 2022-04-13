def zip2(ls1, ls2):
    var1, var2 = ls1, ls2
    ls1_sz, ls2_sz = len(var1), len(var2)
    arr = []
  
    if isinstance(var1, str):
        print(f"\n string")
        n = ls1_sz if ls1_sz > ls2_sz else ls2_sz

      
    if isinstance(var1, tuple):
        print(f"\n tuple")
        if ls1_sz > ls2_sz:
            var2 += ('None',)
            n = ls1_sz
        else:
            var1 += ('None',)
            n = ls2_sz

          
    if isinstance(var1, list):
        print(f"\n list")
        if ls1_sz > ls2_sz:
            var2.append('None')
            n = ls1_sz
        else:
            var1.append('None')
            n = ls2_sz

          
    for i in range(n):
        try:
            arr.append((var1[i], var2[i]))
        except IndexError:       #  string block
            if ls1_sz > ls2_sz:
              arr.append((var1[i], 'None'))
            else:
              arr.append((var2[i], 'None'))
    
    print(arr)


zip2([1, 2, 3, 4], [5, 6, 7])
zip2('helloo', 'love')
zip2((1,2),(3,4,5))