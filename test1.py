from random import choice

class Rubik():

    def __init__(self):
        self.front = [1,1,1,1,1,1,1,1,1]
        self.bottom = [2,2,2,2,2,2,2,2,2]
        self.back = [3,3,3,3,3,3,3,3,3]
        self.top = [4,4,4,4,4,4,4,4,4]
        self.left = [5,5,5,5,5,5,5,5,5]
        self.right = [6,6,6,6,6,6,6,6,6]
        #self.face_temp = []
        
    def now(self):
        print "front:",self.front
        print "bottom:",self.bottom
        print "back:",self.back
        print "top:",self.top
        print "left:",self.left
        print "right:",self.right
        print " "
        #print self.face_top[1]
    
    """
    def test_move(self,index):
        if(index=="L"):
            self.face_top[0], self.face_front[0] = self.face_front[0],self.face_top[0]
        elif(index=="M"):
            self.face_top[0], self.face_front[0] = self.face_front[0],self.face_top[0]
        elif(index=="R"):
            self.face_top[0], self.face_front[0] = self.face_front[0],self.face_top[0]
        else:
            print "Move not recognized"
    """
    
    def vert_up(self,index):
        #front,top,back,bottom
        if(index==1):
            #Left
            self.top[0],self.back[0],self.bottom[0],self.front[0] = self.front[0],self.top[0],self.back[0],self.bottom[0]
            self.top[3],self.back[3],self.bottom[3],self.front[3] = self.front[3],self.top[3],self.back[3],self.bottom[3]
            self.top[6],self.back[6],self.bottom[6],self.front[6] = self.front[6],self.top[6],self.back[6],self.bottom[6]
        elif(index==2):
            #Medium
            self.top[1],self.back[1],self.bottom[1],self.front[1] = self.front[1],self.top[1],self.back[1],self.bottom[1]
            self.top[4],self.back[4],self.bottom[4],self.front[4] = self.front[4],self.top[4],self.back[4],self.bottom[4]
            self.top[7],self.back[7],self.bottom[7],self.front[7] = self.front[7],self.top[7],self.back[7],self.bottom[7]
        elif(index==3):
            #Right
            self.top[2],self.back[2],self.bottom[2],self.front[2] = self.front[2],self.top[2],self.back[2],self.bottom[2]
            self.top[5],self.back[5],self.bottom[5],self.front[5] = self.front[5],self.top[5],self.back[5],self.bottom[5]
            self.top[8],self.back[8],self.bottom[8],self.front[8] = self.front[8],self.top[8],self.back[8],self.bottom[8]
        else:
            print "Move not recognized"
    
    def vert_down(self,index):
        #front,bottom,back,top
        if(index==1):
            #Left
            self.bottom[0],self.back[0],self.top[0],self.front[0] = self.front[0],self.bottom[0],self.back[0],self.top[0]
            self.bottom[3],self.back[3],self.top[3],self.front[3] = self.front[3],self.bottom[3],self.back[3],self.top[3]
            self.bottom[6],self.back[6],self.top[6],self.front[6] = self.front[6],self.bottom[6],self.back[6],self.top[6]
        elif(index==2):
            #Medium
            self.bottom[1],self.back[1],self.top[1],self.front[1] = self.front[1],self.bottom[1],self.back[1],self.top[1]
            self.bottom[4],self.back[4],self.top[4],self.front[4] = self.front[4],self.bottom[4],self.back[4],self.top[4]
            self.bottom[7],self.back[7],self.top[7],self.front[7] = self.front[7],self.bottom[7],self.back[7],self.top[7]
        elif(index==3):
            #Right
            self.bottom[2],self.back[2],self.top[2],self.front[2] = self.front[2],self.bottom[2],self.back[2],self.top[2]
            self.bottom[5],self.back[5],self.top[5],self.front[5] = self.front[5],self.bottom[5],self.back[5],self.top[5]
            self.bottom[8],self.back[8],self.top[8],self.front[8] = self.front[8],self.bottom[8],self.back[8],self.top[8]
        else:
            print "Move not recognized"
    
    def hoz_left(self,index):
        #front,left,back,right
        if(index==1):
            #Top
            self.left[0],self.back[0],self.right[0],self.front[0] = self.front[0],self.left[0],self.back[0],self.right[0]
            self.left[1],self.back[1],self.right[1],self.front[1] = self.front[1],self.left[1],self.back[1],self.right[1]
            self.left[2],self.back[2],self.right[2],self.front[2] = self.front[2],self.left[2],self.back[2],self.right[2]
        elif(index==2):
            #Medium
            self.left[3],self.back[3],self.right[3],self.front[3] = self.front[3],self.left[3],self.back[3],self.right[3]
            self.left[4],self.back[4],self.right[4],self.front[4] = self.front[4],self.left[4],self.back[4],self.right[4]
            self.left[5],self.back[5],self.right[5],self.front[5] = self.front[5],self.left[5],self.back[5],self.right[5]
        elif(index==3):
            #Bottom
            self.left[6],self.back[6],self.right[6],self.front[6] = self.front[6],self.left[6],self.back[6],self.right[6]
            self.left[7],self.back[7],self.right[7],self.front[7] = self.front[7],self.left[7],self.back[7],self.right[7]
            self.left[8],self.back[8],self.right[8],self.front[8] = self.front[8],self.left[8],self.back[8],self.right[8]
        else:
            print "Move not recognized"
    
    def hoz_right(self,index):
        #front,right,back,left
        if(index==1):
            #Top
            self.right[0],self.back[0],self.left[0],self.front[0] = self.front[0],self.right[0],self.back[0],self.left[0]
            self.right[1],self.back[1],self.left[1],self.front[1] = self.front[1],self.right[1],self.back[1],self.left[1]
            self.right[2],self.back[2],self.left[2],self.front[2] = self.front[2],self.right[2],self.back[2],self.left[2]
        elif(index==2):
            #Medium
            self.right[3],self.back[3],self.left[3],self.front[3] = self.front[3],self.right[3],self.back[3],self.left[3]
            self.right[4],self.back[4],self.left[4],self.front[4] = self.front[4],self.right[4],self.back[4],self.left[4]
            self.right[5],self.back[5],self.left[5],self.front[5] = self.front[5],self.right[5],self.back[5],self.left[5]
        elif(index==3):
            #Bottom
            self.right[6],self.back[6],self.left[6],self.front[6] = self.front[6],self.right[6],self.back[6],self.left[6]
            self.right[7],self.back[7],self.left[7],self.front[7] = self.front[7],self.right[7],self.back[7],self.left[7]
            self.right[8],self.back[8],self.left[8],self.front[8] = self.front[8],self.right[8],self.back[8],self.left[8]
        else:
            print "Move not recognized"
        
    def randomize(self,number_moves=16):
        func_list=[self.vert_up,self.vert_down,self.hoz_left,self.hoz_right]
        index_list=[1,2,3]
        for i in range(number_moves):
            choice(func_list)(choice(index_list))
    
rub = Rubik()
rub.now()
rub.randomize(300)
rub.now()
    
    