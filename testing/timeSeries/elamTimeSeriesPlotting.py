import plotly.express as px
import pandas as pd
import datetime
import numpy as np

# Elam's plotting code

# This is the entire function. It takes the filepath with an r before it, as well as the name of the subject.
# Ex: timegraph(r'C:\Users\99ela\OneDrive\Documents\tourscores.csv', 'Elam Blackwell')

# The function needs:
# import plotly.express as px
# import pandas as pd
# import datetime
# import numpy as np

# The csv file currently needs:
# A column of dates called "date"
# A column of scores called "score"

# Other requirements:
# Scores cannot be above 5 (I think)



def timegraph(file, name):
    #This function returns a list of lists based on frequency of scores per date
    def listcheck(x,y,z,split):  #Takes in x data list, y data list, and then two empty lists
        count=0
        i = 1
        z.append(0)
        while(count<len(x)-1):
            if x[count]==x[count+1]:
                i+=1
            else:
                z.append(i)
                i+=1
            count+=1
        z.append(i)
        count=0
        while(count<len(z)-1):
            if z[count+1]<len(y):
                split.append(y[z[count]:z[count+1]])
            else:
                split.append(y[z[count]:])
            count+=1
        sizelist=[]
        for m in range(len(split)):
            sizelist.append([split[m].count(0),split[m].count(1),split[m].count(2),split[m].count(3),split[m].count(4),split[m].count(5),split[m].count(6)])
        return sizelist

    #This function takes the list of lists created by listcheck and returns the size that each datapoint should be
    def checksize(sizel,x,y):   #This takes the list of lists created by listcheck, x data list, and y data list
        z=[]
        count=0
        i = 1
        while(count<len(x)-1):
            if x[count]==x[count+1]:
                i+=1
            else:
                z.append(i)
                i=1
            count+=1
        z.append(i)
        m=[]
        ter=0
        for o in z:
            for c in range(o):
                m.append(ter)
            ter+=1
        size = []
        cnt=0
        while(cnt<=len(y)-1):
            size.append(sizel[m[cnt]][y[cnt]])
            cnt+=1
        return size

    df = pd.read_csv(file)  #Example data in csv form


    #This section converts the csv file into usable data
    y=df["score"].tolist()

    df['date'] = pd.to_datetime(df['date'])
    xold=df['date'].tolist()
    x=[]
    for item in xold:
        x.append(item.date())


    #This calls the size fuctions to set size correctly
    xc=[]
    yc=[]
    sizelist=listcheck(x,y,xc,yc)
    size=checksize(sizelist,x,y)

    #This block creates the average data for the line graph
    avg=[]
    for t in yc:
        avg.append(np.average(t))

    del xc[-1]
    xall=[]
    for r in xc:
        xall.append(x[r])

    xnew=[]
    for thing in xc:
        xnew.append(x[thing])


    #This creates the figure
    fig = px.scatter(x=x,y=y, title="Scores for "+name,labels={'x':'Date', 'y':'Score'}, size=size)
    fig.update_xaxes(rangeslider_visible=True)
    fig.update_layout(xaxis_range=[x[0],x[-1]])
    fig.add_trace(px.line(x=xnew, y=avg, color_discrete_sequence=['#4E2A84']).update_traces(connectgaps=True).data[0])
    fig.add_trace(px.scatter(x=xnew, y=avg, color_discrete_sequence=['#4E2A84']).data[0])
    fig.show()


    
    
timegraph('./tourscores.csv','Elam Blackwell')
