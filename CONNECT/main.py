import cy
import Global
import time
import FindLoop0406 as cj
import numpy as np
import lyx

# COPYRIGHT@Duiduidui
# UPDATE@20200406-1
# A：分治+dfs
import sys
if __name__=='__main__':

    start1 = time.perf_counter()
    ######################################################################################################
    Global.dic = cy.READ_DATA("../dataset/test_data.txt")# 读取文件保存成字典
    end2 = time.perf_counter()
    while (len(Global.dic) != 0):
        for ID in Global.dic:
            net,eye=cy.FIND_NET(Global.dic,ID)
            if (len(net)!=1):
                # print(eye,'|',net)
                NET_ARRAY=np.array(net)
                print(NET_ARRAY)
                LEN,CIRCLE=cj.main(ds=NET_ARRAY)
                print(CIRCLE,LEN)
                #fh = open('../res/result_backtrack04061413.txt', 'a', encoding='utf-8')  # a 是追加的意思
                #for i in CIRCLE:
                    #fh.write(i + '\n')
            break

    #fh.close()

    lyx.mysort()  #对循环路径排序并保存到文件
    ######################################################################################################
    end1 = time.perf_counter()
    print("final is in : %s Seconds " % (end1 - start1))