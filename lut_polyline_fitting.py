import copy

def getparameters(data0,data1):
    Tindex0 = (data0[0]-65) // 2
    Tindex1 = (data1[0]-65) // 2
    basedac = data0[1]
    slope = float(data1[1] - data0[1]) / float(Tindex1 - Tindex0)
    return [basedac,slope,Tindex1,Tindex0]

def plotlingfitting(param):
    lutdata = []
    i = 0
    for [basedac,slope,Tindex1,Tindex0] in param:
        while i < Tindex1:
            lutdata.append(round((i - Tindex0) * slope + basedac))
            i += 1
    while i < 84:
        lutdata.append(round((i - Tindex0) * slope + basedac))
        i += 1
    return lutdata

def lutcreate(pointdata):
    param = []
    pointdata = sorted(pointdata)
    for i in range(len(pointdata)-1):
        param.append(getparameters(pointdata[i],pointdata[i+1]))
    lutdata = plotlingfitting(param)
    return lutdata

def flattenlut(lutdata,Tindex,direction='forward'):
    new_lut = copy.copy(lutdata)
    length = len(lutdata)
    if Tindex >= length:
        return 'Tindex out of lut index!'
    else:
        if direction == 'forward':
            for i in range(Tindex,length):
                new_lut[i] = new_lut[Tindex]
        if direction == 'backward':
            for i in range(0,Tindex):
                new_lut[i] = new_lut[Tindex]
    return new_lut

def searchlutdata(lutdata,TempADC):
    Tindex = (TempADC - 65) // 2
    return lutdata[Tindex]

if __name__ == '__main__':
    import matplotlib.pyplot as plt
    testdata = [[176, 335], [148, 296], [210, 480], [190, 371], [164, 315], [198, 405], [138, 281]]
    lutdata = lutcreate(testdata)
    print(lutdata)
    lutdata_fatten_f = flattenlut(lutdata,60,'forward')
    print(lutdata_fatten_f)
    lutdata_fatten_b = flattenlut(lutdata, 20, 'backward')
    print(len(lutdata))
    print(searchlutdata(lutdata,138))
    plt.plot(lutdata)
    plt.plot(lutdata_fatten_f)
    plt.plot(lutdata_fatten_b)
    plt.show()
