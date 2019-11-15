import tkinter as tk
from tkinter import IntVar, ttk
import re
import pandas as pd
import sys

csv_name = 'tweets.csv'

df = pd.read_csv(csv_name).fillna(0)
df.to_csv('tweets_old.csv', index = False)

tweets_idx = list(df.loc[df['answered'] == 0].index)

if len(tweets_idx) == 0:
    sys.exit('No tweets to annotate.')

tweets_idx.sort()

pointer = tweets_idx.pop(0)


window = tk.Tk()
window.title('Tweekman')
window.geometry("1400x700")

mf = tk.Frame(window)
mf.grid(row = 0, column = 0, padx = (80,120))

tf = tk.Frame(window, width=10, height=3)
tf.grid()

bf = tk.Frame(window)
bf.grid(row = 1, column = 0, pady = (20,20), padx = 30)

#labs = tk.Frame(tf)
#labs.grid()

t_area = tk.Frame(tf, width = 10, height = 3)
t_area.grid(row = 1, column = 0, )
t_area.config(width = 10, height = 3)

img = []
lb = []
C = 0

radios = []

An = 0
Bn = df.loc[df['answered'] != 0].shape[0]
Cn = df.shape[0]

HM = '{} done ({} out of {} annotated)'.format(An, Bn, Cn)

def save_df():
    global csv_name
    
    df.to_csv(csv_name, index = False)
    print("Csv saved.")
    
save = tk.Button(bf, bg = 'gold', text ="Save", command = save_df)
save.grid(row = 1, column = 0, padx = (0,30))


def incomprensibile():
    emo_scores['Incomprensibile'].set(1)




howmany = tk.Label(bf, text = HM, font='Verdana 14', bg = 'gray85')
howmany.grid(row = 2, column = 1, padx = (0,30))



def nextTweet():
    global emo_scores
    global okay
    global testi
    global mf
    global tf
    global labs
    global df
    global radios
    global tweets_idx
    global pointer
    global t_area
    global window
    global An
    global Bn
    global Cn
    global HM
    global howmany
    #global unvar
    #global un
    

    if emo_scores['Sarcasmo'].get() == 1:
         emo_scores['Ironia'].set(1)

    # if unvar==1:
    # 	emo_scores['Incomprensibile'].set(1)
    # 	unvar=False

       

    x = [emo_scores[e].get() for e in emo_scores]
    
    
    df.iloc[pointer,4:] = x
    df.iloc[pointer,3] = 1
    df.to_csv('temp.csv', index = False)
    
    if len(tweets_idx) == 0:
        save_df()
        print('End: no more tweets to annotate.')
        window.destroy()

    pointer = tweets_idx.pop(0)
    
    for e in emo_scores:
        emo_scores[e].set(0)
        
    try:
        for i in range(len(radios)):
            for ii in range(3):
                radios[i][ii].set(0)
    except:
        pass        
    
    
    An += 1
    Bn += 1
    HM = '{} done ({} out of {} annotated)'.format(An, Bn, Cn)
    howmany.config(text = HM)
    #labs.destroy()
    #labs = tk.Frame(tf)
    #labs.grid()
    t_area.destroy()
    t_area = tk.Frame(tf)
    t_area.pack()

    formatta_testo(df.loc[pointer, 'text'])   



okay = tk.Button(bf, bg = 'darkgreen', fg = 'green',  text ="Next", command = nextTweet)
okay.grid(row = 1, column = 2,padx = (0,30))



emotions = ['Gioia', 'Fiducia', 'Amore','Tristezza',
            'Rabbia', 'Disgusto', 'Paura', 'Sorpresa', 'Anticipazione',
            'Ironia','Sarcasmo','Odio', 'Offensività' ,'Contenitore', 'Contenuto']

L = len(emotions)

emo_scores = {e: IntVar() for e in emotions}
emo_scores['Incomprensibile']=IntVar()
for e in emo_scores:
    emo_scores[e].set(0)


color = ['yellow','lawn green', 'IndianRed1', 'SteelBlue1',
         'OrangeRed3', 'olive drab', 'MediumOrchid3','bisque', 'medium sea green',
         'khaki','khaki','paleturquoise','paleturquoise','peachpuff','peachpuff']






                
def formatta_testo(text):
    global t_area
    global img
    global lb
    global C

    
    text = text.replace('\n', ' ') 
    text = re.sub('[ ]+', ' ', text).split(' ')
    text = [str(t.encode('unicode-escape'))[2:-1] if '\\\\U000' in str(t.encode('unicode-escape')) else t for t in text]
    
    xx = []
    
    for i in range(len(text)):
        if '\\\\U000' in str(text[i].encode('unicode-escape')):
                
            xx += re.findall('\\\\U000.....', str(text[i].encode('unicode-escape')))
            
#        elif '\n' in text[i]:
#            aaaaa = text[i].split('\n')
#            for aaa in aaaaa[:-1]:
#                xx += [aaa]
#                xx += ['\n']
#            xx += [aaaaa[-1]]
        else:
            xx += [text[i]]
            
            
    text = [x for x in xx if x != '']
    text = [x for x in xx if x != ' ']
    
    tt = tk.Text(t_area, bd = 0, bg = 'gray85', width = 120, height = 10)
    tt.grid(row = 0, column = 0,pady = 20, padx = 20)
    
    for t in text:
#        if '\n' in t:
#            tt = tk.Text(t_area, bd = 0, bg = 'gray85', width = 120, height = 10)
#            tt.grid(pady = (0,0))
            
        if '\\U00' in t:
            try:
                img += [tk.PhotoImage(file = '72x72/'+t[5:]+'.png').subsample(3,3)]
                #img = tk.PhotoImage(file = '72x72/megaman.gif')
                #img = img.resize((25,25), Image.ANTIALIAS)
                #img =  ImageTk.PhotoImage(img)
                
                lb += [tk.Label(tt, bg = 'gray85', image = img[C])]
                tt.window_create(tk.INSERT, window = lb[C])
                C += 1
            except Exception as e:
                print(e)
        
        elif '@' in t:
            tt.window_create(tk.END, window = tk.Label(tt, font='Verdana 14', bg = 'gray85', fg= 'darkblue', text = t))
        elif re.match('^#',t):
            tt.window_create(tk.END, window = tk.Label(tt, font='Verdana 14', bg = 'gray85', fg= 'darkblue', text = t))
        else:
            tt.window_create(tk.END, window = tk.Label(tt, font='Verdana 14', bg= 'gray85', text = t))

 




def init_window():
    global emotions
    global color
    global mf
    global tf
    global emo_scores
    global L
    global testi
    global radios
    global pointer
    global df
    global img
    global check
    
    ttk.Separator(mf,orient='horizontal').grid(row=0, column = 0, columnspan=14, sticky = 'ew', pady = 20)
    
    
    for i in range(L):
        
        
        
        j = (i % 3)*5 
        r = (i // 3)*3
        
        
        
        if len(emotions[i]) < 12:
            t = emotions[i] + ' '*(12-len(emotions[i]))
        else:
            t = emotions[i]
        
            
        
        
        
        tk.Label(mf, bg = color[i], text = t, font='Courier 12 bold').grid(row = r+1, column = j + 0)
            
        check=ttk.Checkbutton(mf, variable=emo_scores[emotions[i]]).grid(row= r+2, column = j+2, padx = (10,10))

        un=tk.Button(bf, bg = 'darkgreen', fg = 'red',  text ="INCOMPRENSIBILE", command = incomprensibile )
        un.grid(row=1, column=1, padx=(0,30))

        
        if i > 5:
            ttk.Separator(mf,orient='horizontal').grid(row=r+3, column = j, columnspan=4, sticky = 'ew', pady = (20,40))
        else:
            ttk.Separator(mf,orient='horizontal').grid(row=r+3, column = j, columnspan=4, sticky = 'ew', pady = 20)
        
        if (i % 3) != 2:
            ttk.Separator(mf,orient='vertical').grid(row = r+1, column = j+4, rowspan = 2, sticky = 'ns', padx = (10,10))
    
        
    testo=df.loc[pointer,'text']+' - PROGRAMMA: ' + df.loc[pointer,'Program Name']
    formatta_testo(testo)
    
    
        

init_window()
window.mainloop()


