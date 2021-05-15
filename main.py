import numpy as np
import pandas as pd
import datetime
import matplotlib.pyplot as plt
# import csv

class EveryDayCorona:
    def __init__(self):
        self.src = 'http://ncov.mohw.go.kr/bdBoardList_Real.do?brdId=1&brdGubun=13'
        self.craw = pd.DataFrame(pd.read_html(self.src,encoding='utf8')[0]).to_numpy()
        # 속성값이 이상해서 변경하는 코드
        # self.craw.columns = ['시도명','합계','국내발생','해외유입','확진환자','격리중','격리해제','사망자','발생률']
        # print(self.craw.shape)

        self.total = self.craw[0,:]
        self.craw = self.craw[1:-1,:]

        # print(self.craw)
        self.area = self.craw[:,0]
        self.totalInfect = self.craw[:,1]
        self.inArea = self.craw[:,2]
        self.outArea = self.craw[:,3]
        self.infect = self.craw[:,4]
        self.quarantine = self.craw[:,5]
        self.freedom = self.craw[:,6]
        self.dead = self.craw[:,7]
        self.Incidence = self.craw[:,8]

        self.csv = self.Grap()

    def processing(self):
        print(self.craw)

    def processingCsv(self):
        date = datetime.datetime.today().strftime('%Y-%m-%d-%H%M%S')
        self.craw.to_csv(date+'.csv')

    def GrapOutput(self,a,b):
        self.csv.Circle(a,b)

    class Grap:
        def __init__(self):
            pass

        def Circle(self,title,data,file:bool=False):
            try:
                np.column_stack([title,data])
                plt.Circle(title,data)
                plt.show()
                if file:
                    date = datetime.datetime.today().strftime('%Y-%m-%d-%H%M%S')
                    plt.savefig(date+'.png')

            except:
                print('매개변수 확인')

