# -*- coding: utf-8 -*-

#----------------------------------------------------------------------------
def s2bin(s):
    return reduce(lambda a,b:a+('000000000000000'+bin(ord(b))[2:])[-16:],s,'')
#----------------------------------------------------------------------------
def bin2s(b):
    return ''.join([unichr(int(b[i:i+16],2)) for i in range(0, len(b), 16)])
#----------------------------------------------------------------------------

#----------------------------------------------------------------------------
class Node:
    def __init__(self):
        self.plus={}    
        self.minus={}    
    def str(self):
        return str(self.id)+" p="+str(self.plus)+" m="+str(self.minus)+""

#----------------------------------------------------------------------------
class NodeList:
    def __init__(self):
        self.nodes=[]

        root=self.root=Node()        
        root.id=-1

        

        n=self.create()
        self.link(root,n,n)

        n=self.create()
        self.link(root,n,n)

    def create(self):
        node=Node()
        node.id=len(self.nodes)
        self.nodes.append(node)
        return node

    def link(self,a,b,c):
        a.plus[b.id]=c.id;
        c.minus[b.id]=a.id

    def getKnownNode(self,node,data):
        if(len(data)==0):
            return node,data
        v=data[0]
        if v in node.plus:
            nextNode=self.nodes[node.plus[v]]
            return self.getKnownNode(nextNode,data[1:])
        else:
            return node,data

    def readNextNode(self,node1,data1): 

        if(len(data1)==0):
            return node1

        node2,data2=self.getKnownNode(self.root,data1)

        node3=self.create() 
        self.link(node1,node2,node3)

        return self.readNextNode(node3,data2)
           
        
        
    def read(self,s):
        return self.readBin(s2bin(s))

    def readBin(self,s):        
        data = [int(s[i]) for i in range(0,len(s))]   
        node1,data1=self.getKnownNode(self.root,data)
        return self.readNextNode(node1,data1)

    def str(self):
        print '\n'.join([node.str()+"\t"+self.nodeVal(node) for node in self.nodes])

    def nodeVal(self,node):
        if node.id<=1:
            return str(node.id)
        for idB in node.minus:
            b=self.nodes[idB]
            idA=node.minus[idB]
            a=self.nodes[idA]
            return self.nodeVal(a)+self.nodeVal(b)


#----------------------------------------------------------------------------
nodes=NodeList()
# nodes.readBin('00000000000000000000000000000000')
nodes.read(u'test')


#nodes.parse(u'test')
#nodes.str()
