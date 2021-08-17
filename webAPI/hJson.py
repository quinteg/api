
def indexKey(list):
    i = 0
    for k in list:
        if "Key" == k:
            break;
        else:
            i = i + 1
    return i


def dataDict(dstring):
    helper = {}
    h1 = {}
    h2 = {}
    for d in dstring:
        if d != 'Key':
            h1.update({d: dstring[d]})

    h2['DATA'] = h1
    helper[dstring['Key']] = h2['DATA']

    return helper


def getResult(matrix):
    count = 0
    res = {}
    datadict = {}
    for dict in matrix:
        count = count + 1
        for list in dict:
            if list in res:
                var = {}
                var1 = {}
                for key in dict[list]:
                    if key in res[list]:
                        fvres = getfirstvalue(res[list][key])
                        fvdict = getfirstvalue(dict[list][key])

                        if fvdict in res[list][key]:
                            datadict = getDicts(res[list][key][fvdict], dict[list][key][fvdict])
                            var1[fvdict] = datadict
                            datadict = res[list][key]
                            datadict.update(var1)
                            var[key] = datadict
                        else:
                            datadict = res[list][key]
                            datadict.update(dict[list][key])
                            var[key] = datadict

                if len(var) > 0:
                    dict[list] = var

                d4 = {}
                d4.update(res[list])
                d4.update(dict[list])
                res[list] = d4
            else:
                res.update(dict)
    return res


def getDicts(hres, hdict):
    helper = {}
    datadict = {}
    fvres = getfirstvalue(hres)
    fvdict = getfirstvalue(hdict)

    if fvres == fvdict and fvdict != 'DATA':
        datadict[fvres] = getDicts(hres[fvres], hdict[fvdict])
        helper = datadict
    else:
        if fvdict in hres:
            datadict[fvdict] = getDicts(hres[fvdict], hdict[fvdict])
            helper = hres
            helper.update(datadict)
        else:
            helper = hres
            helper.update(hdict)

    return helper


def getfirstvalue(v):
    first_value = next(iter(v))
    return first_value















