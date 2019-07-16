import matplotlib.pyplot as plt
from trees import *
decisionNode = dict(boxstyle="sawtooth",fc="0.8")
leafnode = dict(boxstyle="round4",fc="0.8")
arrow_args = dict(arrowstyle="<-")

def plotNode(nodeTxt,centerpt,parentpt,nodetype):
    createplot.ax1.annotate(nodeTxt,xy=parentpt,xycoords='axes fraction',
                            xytext=centerpt,textcoords='axes fraction',
                            va="center",ha="center",bbox=nodetype,arrowprops=arrow_args)
def createplot(intree):
    fig = plt.figure(1,facecolor='white')
    fig.clf()
    axprops = dict(xticks=[],yticks=[])
    createplot.ax1 = plt.subplot(111,frameon=False,**axprops)
    plottree.totalw = float(getnumleafs(intree))
    plottree.totald = float(gettreedepth(intree))
    plottree.xoff = -0.5/plottree.totalw
    plottree.yoff = 1.0
    plottree(intree,(0.5,1.0),'')
    plt.show()
def getnumleafs(mytree):
    numleafs = 0
    firststr = list(mytree.keys())[0]
    secondict = mytree[firststr]
    for key in secondict.keys():
        if str(type(secondict[key])) == "<class 'dict'>":
            numleafs += getnumleafs(secondict[key])
        else:  numleafs += 1
    return numleafs
def gettreedepth(mytree):
    maxdepth = 0
    firststr = list(mytree.keys())[0]
    seconddict = mytree[firststr]
    for key in seconddict.keys():
        if str(type(seconddict[key])) == "<class 'dict'>":
            thisdepth = 1+gettreedepth(seconddict[key])
        else: thisdepth = 1
        if thisdepth > maxdepth : maxdepth = thisdepth
    return  maxdepth

def retrievetree(i):
    listoftrees = [{'no surfacing': {0: 'no', 1: {'flippers': {0: 'no', 1: 'yes'}}}},
                   {'no surfacing': {0: 'no', 1: {'flippers': {0: {'head':{0:'no',1:'yes'}},1:'no'}}}}]
    return listoftrees[i]
decisionNode
def plotmidtext(cntrpt,parentpt,txtstring):
    xmid = (parentpt[0]-cntrpt[0])/2.0 + cntrpt[0]
    ymid = (parentpt[1]-cntrpt[1])/2.0 + cntrpt[1]
    createplot.ax1.text(xmid,ymid,txtstring)

def plottree(mytree,parentpt,nodetxt):
    numleafs = getnumleafs(mytree)
    depth = gettreedepth(mytree)
    firststr = list(mytree.keys())[0]
    cntrpt = (plottree.xoff + (1.0 + float(numleafs))/2.0/plottree.totalw,plottree.yoff)
    plotmidtext(cntrpt,parentpt,nodetxt)
    plotNode(firststr,cntrpt,parentpt,decisionNode)
    seconddict = mytree[firststr]
    plottree.yoff = plottree.yoff - 1.0/plottree.totald
    for key in seconddict.keys():
        if str(type(seconddict[key])) == "<class 'dict'>":
            plottree(seconddict[key],cntrpt,str(key))
        else:
            plottree.xoff = plottree.xoff + 1.0/plottree.totalw
            plotNode(seconddict[key],(plottree.xoff,plottree.yoff),cntrpt,leafnode)
            plotmidtext((plottree.xoff,plottree.yoff),cntrpt,str(key))
    plottree.yoff = plottree.yoff + 1.0/plottree.totald
