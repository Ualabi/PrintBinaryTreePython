class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def izqder(self,Node):
    #    print(Node.val)
        x = []
        if Node.left:
            x += self.izqder(Node.left)
        x += [Node.val]
        if Node.right:
            x += self.izqder(Node.right)
        return x
    
    def nodos(self,Node):
    #    print(Node.val)
        x = []
        if Node.left:
            x += self.nodos(Node.left)
        x += [Node]
        if Node.right:
            x += self.nodos(Node.right)
        return x
    
    def levels(self,Node):
        x = [[Node]]
        if Node.left or Node.right:
            y = []
            z = []
            if Node.left:
                y = self.levels(Node.left)
            if Node.right:
                z = self.levels(Node.right)
            a = min(len(y),len(z))
            for index in range(a):
                x.append(y[index]+z[index])
            x += y[a:]+z[a:]
        return x
    
    def __str__(self):
        A = self.nodos(self)
        B = self.levels(self)
        
        s = ''
        lima = len(A)
        limb = len(B)
        matrix = []
        for x in range(2*limb-1):
            aux = []
            for y in range(lima):
                aux.append('  ')
            matrix.append(aux)
        
        for x in range(limb):
            for y in B[x]:
                leftindex = A.index(y)
                rightindex = leftindex+1
                aux = A[leftindex]
                if aux.left:
                    leftindex = A.index(aux.left)
                if aux.right:
                    rightindex = A.index(aux.right)+1
                
                # print(y," ",leftindex," ",A.index(y)," ",rightindex)            
                if aux.left and aux.right:
                    for z in range(leftindex,rightindex):
                        if z == leftindex:
                            if z == A.index(y): matrix[2*x][z] = self.valstr(y.val)
                            matrix[2*x+1][z] = ' /'
                        elif z == rightindex-1:
                            if z == A.index(y): matrix[2*x][z] = self.valstr(y.val)
                            else:   matrix[2*x][z] = '_ '
                            matrix[2*x+1][z] = ' \\'
                        elif z == A.index(y):
                            matrix[2*x][A.index(y)] = self.valstr(y.val)
                        else:
                            matrix[2*x][z] = '__'
                elif aux.left:
                    for z in range(leftindex,rightindex):
                        if z == leftindex:
                            if z == A.index(y): 
                                matrix[2*x][z] = self.valstr(y.val)
                            matrix[2*x+1][z] = ' /'
                        elif z == A.index(y):
                            matrix[2*x][A.index(y)] = self.valstr(y.val)
                        else:
                            matrix[2*x][z] = '__'
                elif aux.right:
                    for z in range(leftindex,rightindex):
                        if z == rightindex-1:
                            if z == A.index(y): matrix[2*x][z] = self.valstr(y.val)
                            else:   matrix[2*x][z] = '_ '
                            matrix[2*x+1][z] = ' \\'
                        elif z == A.index(y):
                            matrix[2*x][A.index(y)] = self.valstr(y.val,1)
                        else:
                            matrix[2*x][z] = '__'
                else:
                    matrix[2*x][A.index(y)] = self.valstr(y.val,1)
        
        #print('')
        s += '\n'
        for x in matrix:
            for y in x:
                #print(y,end='')
                s += y
            #print('')
            s += '\n'
        
        return s
    
    def valstr(self,val,opt=0):
        if val < 10:
            if opt == 0:
                return '_'+str(val)
            else:
                return ' '+str(val)
        else:
            return str(val)

def getTree(s):
    if s[-1] != ' ':
        s += ' '
    past = ""
    mylist = []
    for element in s:
        if element == ' ':
            mylist.append(int(past))
            past = ''
        else:
            past += element
    
    #print(mylist)
    head = TreeNode(mylist[0])
    elements = [head]
    mylist = mylist[1:]
    while elements:
        aux = len(elements)
    
        for y in range(aux):
            point = elements[0]
            
            if mylist:
                value = mylist[0]
                mylist = mylist[1:]
                if value != -1:
                    point.left = TreeNode(value)
                    elements.append(point.left)
            else:
                elements = elements[1:]
                break
            
            if mylist:
                value = mylist[0]
                mylist = mylist[1:]
                if value != -1:
                    point.right = TreeNode(value)
                    elements.append(point.right)
            else:
                elements = elements[1:]
                break
            
            elements = elements[1:]
    
    return head

def getList(Node):
    if Node:
        s = str(Node.val)+' '
        s += getList(Node.left)
        s += getList(Node.right)
        return s
    else: 
        return '-1 '

def strToList(s):
    if s[-1] != ' ':
        s += ' '
    past = ""
    mylist = []
    for element in s:
        if element == ' ':
            mylist.append(int(past))
            past = ''
        else:
            past += element
    return mylist

###############################################################################

class Solution:
    # @param A : root node of tree
    # @return an integer
    def maxPathSum(self, A):
        maxim = self.aux(A)
        return max(maxim)

    def aux(self, Node):
        if Node.left: A = self.aux(Node.left)
        else: A = None
        
        if Node.right: B = self.aux(Node.right)
        else: B = None
        
        if A and B:
            C = max(Node.val, Node.val+A[0], Node.val+B[0])
            D = max(Node.val+A[0]+B[0], A[1], B[1],C)
        elif A:
            C = max(Node.val, Node.val+A[0])
            D = max(Node.val+A[0], A[1],C)
        elif B:
            C = max(Node.val, Node.val+B[0])
            D = max(Node.val+B[0], B[1],C)
        else:    
            C = Node.val
            D = Node.val
        return [C,D]

###############################################################################

#s = "1 2 3 4 5 6 7 8 -1 9 -1 10 11 12 13 -1 -1 -1 14 -1 15 -1 -1 16 -1 -1 17 -1 -1 -1 -1 -1 -1 -1 18 -1 -1"
#s = "1 2 3 8 5 6 7 -1 4 9 -1 10 11 12 13 -1 -1 -1 14 -1 15 -1 -1 16 -1 -1 17 -1 -1 -1 -1 -1 -1 -1 18 -1 -1"
#s = "1 6 1 7 1 6 7 10 -1 9 -1 10 11 12 13 -1 -1 -1 14 -1 15 -1 -1 16 -1 -1 17 -1 -1 -1 -1 -1 -1 -1 18 -1 -1"
#s = "47 42 52 41 44 50 64 40 -1 43 45 49 51 63 77 -1 -1 -1 -1 -1 46 48 -1 -1 -1 55 -1 75 88 -1 -1 -1 -1 53 58 69 76 81 94 -1 54 56 60 68 73 -1 -1 79 87 92 100 -1 -1 -1 57 59 61 66 -1 72 74 78 80 85 -1 89 93 96 102 -1 -1 -1 -1 -1 62 65 67 71 -1 -1 -1 -1 -1 -1 -1 84 86 -1 90 -1 -1 95 99 101 -1 -1 -1 -1 -1 -1 -1 70 -1 83 -1 -1 -1 -1 91 -1 -1 98 -1 -1 -1 -1 -1 82 -1 -1 -1 97 -1 -1 -1 -1 -1"
#s = '8 3 13 2 5 11 25 1 -1 4 6 10 12 24 38 -1 -1 -1 -1 -1 7 9 -1 -1 -1 16 -1 36 49 -1 -1 -1 -1 14 19 30 37 42 55 -1 15 17 21 29 34 -1 -1 40 48 53 61 -1 -1 -1 18 20 22 27 -1 33 35 39 41 46 -1 50 54 57 63 -1 -1 -1 -1 -1 23 26 28 32 -1 -1 -1 -1 -1 -1 -1 45 47 -1 51 -1 -1 56 60 62 -1 -1 -1 -1 -1 -1 -1 31 -1 44 -1 -1 -1 -1 52 -1 -1 59 -1 -1 -1 -1 -1 43 -1 -1 -1 58 -1 -1 -1 -1 -1'
#s = '863 64 217 343 207 391 145 304 248 80 389 225 86 168 233 56 349 114 223 284 269 57 71 334 149 4 411 399 279 87 352 52 -1 -1 105 78 427 181 250 297 344 221 51 166 111 378 374 266 -1 296 28 59 424 44 193 160 229 318 -1 242 406 -1 328 175 199 48 342 408 -1 368 -1 116 25 -1 47 338 215 50 231 -1 262 189 -1 153 -1 340 -1 277 -1 -1 -1 41 -1 -1 197 10 224 326 120 108 414 228 316 310 117 109 367 91 119 8 -1 -1 -1 -1 382 -1 -1 -1 361 332 -1 -1 118 425 -1 205 -1 -1 423 150 134 -1 182 131 327 -1 337 325 386 173 196 291 -1 365 32 247 -1 -1 -1 -1 -1 -1 130 419 187 219 -1 -1 180 177 66 420 285 161 37 76 303 154 377 -1 353 -1 366 370 309 -1 170 272 -1 -1 -1 -1 333 431 -1 317 -1 -1 206 292 -1 192 -1 -1 -1 -1 -1 39 -1 -1 -1 -1 -1 -1 396 357 259 300 -1 240 -1 -1 265 -1 330 335 195 256 -1 428 -1 -1 -1 -1 -1 -1 -1 -1 77 -1 410 204 -1 -1 99 360 320 62 324 -1 163 415 -1 -1 214 141 421 -1 90 -1 283 143 354 17 110 218 19 75 -1 351 36 167 191 244 429 174 404 123 74 294 165 -1 79 275 67 -1 381 243 267 -1 -1 -1 -1 394 413 -1 -1 230 -1 213 176 22 -1 -1 -1 83 -1 -1 -1 -1 409 -1 358 -1 398 7 157 -1 255 -1 -1 -1 373 323 -1 346 282 234 222 26 54 270 49 -1 -1 200 -1 302 -1 -1 -1 138 -1 290 -1 -1 -1 -1 339 314 216 124 -1 171 274 13 308 -1 376 315 70 403 355 137 388 142 383 31 -1 260 92 58 30 281 159 209 251 407 -1 23 144 43 -1 94 132 -1 -1 295 -1 -1 241 306 245 -1 -1 179 -1 -1 -1 98 -1 249 -1 -1 -1 -1 -1 136 -1 -1 -1 -1 -1 -1 106 -1 307 -1 -1 -1 -1 -1 -1 -1 169 -1 -1 -1 372 -1 -1 -1 299 -1 112 -1 287 115 -1 -1 -1 -1 -1 -1 53 -1 16 -1 -1 -1 125 278 253 401 -1 18 384 201 183 188 400 20 276 402 122 -1 -1 198 -1 -1 203 254 -1 63 -1 208 -1 258 178 -1 129 246 34 393 235 220 -1 -1 151 -1 185 100 -1 286 -1 416 88 190 -1 -1 -1 -1 369 103 341 -1 1 162 82 133 -1 -1 35 -1 9 -1 -1 -1 11 107 29 -1 -1 -1 -1 68 -1 412 -1 405 128 -1 -1 -1 -1 -1 -1 -1 417 -1 311 418 -1 -1 -1 -1 -1 12 -1 -1 322 226 93 263 359 38 126 73 -1 312 -1 -1 -1 -1 2 -1 -1 329 127 211 -1 60 -1 -1 172 -1 -1 -1 -1 -1 -1 5 -1 -1 140 -1 395 -1 -1 -1 84 15 -1 -1 -1 155 -1 257 264 -1 -1 148 95 -1 -1 -1 14 380 350 -1 -1 -1 -1 375 -1 -1 371 -1 -1 65 89 298 -1 -1 236 -1 -1 184 102 158 72 -1 -1 -1 -1 -1 305 -1 -1 46 293 -1 101 -1 -1 -1 -1 362 -1 -1 -1 104 -1 -1 -1 -1 -1 348 -1 186 -1 -1 -1 -1 321 113 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 390 364 -1 268 -1 -1 -1 331 -1 -1 -1 -1 -1 -1 319 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 69 239 -1 -1 152 135 -1 -1 -1 -1 55 -1 -1 202 261 96 -1 -1 -1 -1 6 -1 301 -1 -1 -1 -1 -1 -1 363 -1 -1 -1 -1 -1 -1 -1 -1 -1 238 252 97 -1 -1 -1 -1 392 -1 -1 -1 288 -1 -1 -1 271 -1 -1 -1 -1 -1 422 -1 -1 -1 212 -1 387 24 3 -1 -1 -1 21 40 -1 -1 -1 -1 273 139 -1 -1 -1 -1 237 61 -1 -1 81 -1 -1 -1 -1 -1 147 347 227 -1 -1 33 -1 385 -1 121 -1 -1 -1 -1 289 -1 397 -1 426 -1 -1 -1 -1 -1 -1 -1 -1 232 -1 280 356 164 -1 -1 45 336 -1 146 -1 -1 -1 -1 -1 -1 379 430 194 -1 -1 313 42 85 210 345 27 -1 -1 -1 -1 -1 156 -1 -1 -1 -1 -1 -1 -1 -1 -1'
#s = "727 721 838 538 724 757 859 322 709 -1 -1 754 811 844 937 268 487 685 718 730 -1 802 814 841 853 925 970 91 307 484 496 661 691 715 -1 -1 736 796 805 -1 832 -1 -1 850 856 871 928 949 982 64 136 283 319 364 -1 493 508 565 664 688 700 712 -1 733 745 763 799 -1 808 823 835 847 -1 -1 -1 868 886 -1 931 946 961 979 1000 4 67 127 148 271 292 316 -1 346 460 490 -1 502 523 562 616 -1 673 -1 -1 694 703 -1 -1 -1 -1 742 748 760 775 -1 -1 -1 -1 820 829 -1 -1 -1 -1 862 -1 883 916 -1 934 940 -1 955 964 976 -1 988 1015 1 10 -1 73 94 133 139 262 -1 274 286 295 313 -1 343 352 373 478 -1 -1 499 505 520 526 541 -1 598 637 667 682 -1 697 -1 706 739 -1 -1 751 -1 -1 769 793 817 -1 826 -1 -1 865 880 -1 904 919 -1 -1 -1 943 952 958 -1 967 973 -1 985 994 1006 -1 -1 -1 7 19 70 82 -1 112 130 -1 -1 145 199 265 -1 280 -1 289 -1 298 310 -1 325 -1 349 361 370 430 469 481 -1 -1 -1 -1 517 -1 -1 532 -1 550 589 613 622 646 -1 670 679 -1 -1 -1 -1 -1 -1 -1 -1 -1 766 772 781 -1 -1 -1 -1 -1 -1 -1 874 -1 898 913 -1 922 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 991 997 1003 1009 -1 -1 16 52 -1 -1 76 85 109 121 -1 -1 142 -1 196 223 -1 -1 277 -1 -1 -1 -1 304 -1 -1 -1 337 -1 -1 358 -1 367 -1 376 436 466 475 -1 -1 511 -1 529 535 547 553 583 595 607 -1 619 631 640 649 -1 -1 676 -1 -1 -1 -1 -1 778 787 -1 877 889 901 907 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 1012 13 -1 49 55 -1 79 -1 88 106 -1 118 124 -1 -1 193 -1 202 244 -1 -1 301 -1 328 340 355 -1 -1 -1 -1 403 433 442 463 -1 472 -1 -1 514 -1 -1 -1 -1 544 -1 -1 559 568 586 592 -1 604 610 -1 -1 625 634 -1 643 -1 655 -1 -1 -1 -1 784 790 -1 -1 -1 895 -1 -1 -1 910 -1 -1 -1 -1 22 -1 -1 61 -1 -1 -1 -1 97 -1 115 -1 -1 -1 154 -1 -1 214 232 247 -1 -1 -1 331 -1 -1 -1 -1 385 415 -1 -1 439 448 -1 -1 -1 -1 -1 -1 -1 -1 556 -1 -1 571 -1 -1 -1 -1 601 -1 -1 -1 -1 628 -1 -1 -1 -1 652 658 -1 -1 -1 -1 892 -1 -1 -1 -1 25 58 -1 -1 103 -1 -1 151 178 211 217 229 241 -1 253 -1 334 379 394 409 418 -1 -1 445 454 -1 -1 -1 574 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 34 -1 -1 100 -1 -1 -1 166 190 205 -1 -1 220 226 -1 238 -1 250 259 -1 -1 -1 382 388 397 406 412 -1 427 -1 -1 451 457 -1 577 31 46 -1 -1 157 172 181 -1 -1 208 -1 -1 -1 -1 235 -1 -1 -1 256 -1 -1 -1 -1 391 -1 400 -1 -1 -1 -1 424 -1 -1 -1 -1 -1 -1 580 28 -1 40 -1 -1 163 169 175 -1 184 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 421 -1 -1 -1 -1 -1 37 43 160 -1 -1 -1 -1 -1 -1 187 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1"
s = "-100 -200 -1 -300 -400 -1 -1 -1 -1"

print(s)
head = getTree(s)
print(head)

sol = Solution()
aux = sol.maxPathSum(head)
print(aux)


##head.left.printer(|)
#print(getList(head))