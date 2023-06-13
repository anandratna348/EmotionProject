emo=[]
data=""
var=""
x1=[] #time
num=[] #angry
numd=[] #disgust
numf=[] #fear
numh=[] #happy
nums=[] #sad
numsu=[] #surprise
numn=[] #neutral
from flask import Flask, render_template, request, url_for
from deepface import DeepFace
import cv2
import shutil
import cv2
import numpy as np
import re
import matplotlib.pyplot as plt
from tabulate import tabulate

app = Flask(__name__)

#var=input("hello")

def flim():
   # var=input("hello")

    cap = cv2.VideoCapture(var)
  
# Check if camera opened successfully
    if (cap.isOpened()== False):
        print("Error opening video file")
  
# Read until video is completed
    while(cap.isOpened()):
      
# Capture frame-by-frame
        ret, frame = cap.read()
        if ret == True:
    # Display the resulting frame
            cv2.imshow('Frame', frame)
          
    # Press Q on keyboard to exit
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break
  
# Break the loop
        else:
            break
  
# When everything done, release
# the video capture object
    cap.release()
  
# Closes all the frames
    cv2.destroyAllWindows()
    return '<html><body style="background-color:black; color:white;">Done, Thank you!</body></html>'



#vars=input("re")
def thisa (s,number):
 
  #method to parse output and retrieve the emotiion value for anger in each iteraion
    
 angry=0 #initialise the value to be returned from this method

 arr=re.findall(r"[-+]?(?:\d*\.*\d+)", s) #takes parameter s and takes all mumerical values and makes a list of them
    
 size=len(arr) #finding the length of the list

 for a in range(0,size): #for loop to go through the array and remove leading 0s which cause bugs
    
  if arr[a].startswith("0",1) and arr[a].startswith(".",2)==0 and arr[a].startswith(".",3)==0:
         #exceptions
        arr[a]='-1'
 arr = [eval(i) for i in arr]  #if statement is legal then it executes
 arr=removeNegative(arr) #calling method to remove any negative numbers in the output because they cause bugs
 angry=float(arr[number]) #the first element of array is emotion val of anger so it is returned
 return angry



def removeNegative(arr): #method to remove negatives from array
    newArr = []
 
    for x in range(0, len(arr)):
        if (arr[x] >= 0):
            newArr.append(arr[x])
 
    for x in range(0, len(newArr)):
        
     return newArr

#frameNr = 0 #keep count of frames used later
#count=0 #keep count for time

def maxim(arr): #method to find dominant emotion at each second called maximum
    intn=[] #array to keep track of maximas
    n=re.findall(r'[-+]?(?:\d*\.*\d+)', arr) #same parsing done as previously
    size=len(n)
    for a in range(0,size):    #array n has parsed output
      if n[a].startswith("0",1)and n[a].startswith(".",2)==0 and n[a].startswith(".",3)==0:
        n[a]='-1'
        
    res = [eval(i) for i in n] 
    res=removeNegative(res)

    res.pop()
    res.pop()
    res.pop() #pop no need vals
    res.pop()
    
    size1=len(res)
    for i in range(0, size1): #put in array emo the emotion that is biggest
        intn.append(float(res[i])) #res array parsed to float and stored in intn an array
  
    emotions=['   Anger','   Disgust','   Fear','   Happy','   Sadness','   Surprise','   Neutral']
    

   
    if intn.index(max(intn))==0: #if statement to check the index of the maximum 
        emo.append(emotions[0])
    if intn.index(max(intn))==1:
        emo.append(emotions[1])
    if intn.index(max(intn))==2:
        emo.append(emotions[2])
    if intn.index(max(intn))==3:
        emo.append(emotions[3])
    if intn.index(max(intn))==4:
        emo.append(emotions[4])
    if intn.index(max(intn))==5:
        emo.append(emotions[5])
    if intn.index(max(intn))==6:
        emo.append(emotions[6])
        
        
        
#part 3    
def maincode():
 global var
 
 capture = cv2.VideoCapture(var)
 frameNrs = 0
 while (True):
  success, frame = capture.read()
  if success:
   cv2.imwrite(f'/Users/97150/OneDrive/Documents/appy/static/output/frame_{frameNrs}.jpg', frame)
  else:
   break
   print("No")
  frameNrs = frameNrs+1 #this code makes your video in to frames and saves in your computer

 capture.release()    
 analysis2="" #for the dominant emotion 
#emo=[]
 frameNr=0
 count=0
 while (frameNr<frameNrs): #while loop to iterate of frames with incrementing 28 times so 10 sec vid is analyzed into 10 times only
  
  #using library deepface to produce output for emotion
   analysis = DeepFace.analyze(img_path =    cv2.imread(f'/Users/97150/OneDrive/Documents/appy/static/output/frame_{frameNr}.jpg'), actions = [ "emotion"])
 
  #print(analysis)
   global num
   global numd
   global numf
   global numh
   global nums
   global numsu
   global numn
   global x1
   analysis1=str(analysis) #converting output to string twice 
   analysis2=str(analysis)
   maxim(analysis2) #calling method to print maximim emotion at each second
   num.append(thisa(analysis1,0)) #recording each emotions valuse at each 10 seconds anger
   numd.append(thisa(analysis1,1))#disgust
   numf.append(thisa(analysis1,2))#fear
   numh.append(thisa(analysis1,3)) #happy
   nums.append(thisa(analysis1,4)) #sad
   numsu.append(thisa(analysis1,5)) #surprise
   numn.append(thisa(analysis1,6)) #neutral
   x1.append(count)
  
   count=count+1 #time ++
  
   frameNr = frameNr+28

 
 #global num
 #global numd
 #global numf
 #global numh
 #global nums
 #global numsu
 #global numn
 #global x1
#code to plot a graph of results
 plt.plot(x1, num, label = "Anger")
 plt.plot(x1, numd, label = "Disgust")
 plt.plot(x1, numf, label = "Fear")
 plt.plot(x1, numh, label = "Happy")
 plt.plot(x1, nums, label = "Sad")
 plt.plot(x1, numsu, label = "Surprise")
 plt.plot(x1, numn, label = "Neutral")
 
 plt.xlabel('time')
#naming the y axis
 plt.ylabel('value')
#giving a title to my graph
 plt.title('Emotion Values Graph')
  
 #show a legend on the plot
 plt.legend()
 btn=False  
# function to show the plot
 if(btn==True):
  
   plt.show()
 img=plt.savefig('static/img.png')
 

 return "<html><head><title>Emotion Analysis</title><link rel='stylesheet' type='text/css' href='static/video.css'></head><body><h1>Emotion Analysis</h1><button id='b1' onclick='gop()'>Analysis Ready</button><script>function gop(){window.location.href = '/out';}</script></body></html>"

t=2938

def myn():
  mylist=[]
  size2=len(emo)
  for i in range(0,size2):
   mylist.append([i,emo[i]])
  #out()
   st1='<html><head><style> table { font-family: Arial, Helvetica, sans-serif; border-collapse: collapse; width: 100%;} table td, table th { border: 1px solid #ddd;  padding: 8px;text-align:left;}table tr{background-color:white;} table tr:nth-child(even){background-color: #f2f2f2;} table tr:hover {background-color: #ddd;} table th { padding-top: 12px; padding-bottom: 12px;  text-align: left; background-color: #261d75;  color: white;} </style></head> <body style="background-color:black;color:black; "><table><tr><th>Time:s</th> <th>Dominant Emotion:</th><tr></table>'
   st2='</body></html>'
   stx=st1+tabulate(mylist, tablefmt='html')+st2
  return stx
@app.route('/')
def home():
   #ScriptPage(t)

   return render_template('first.html')
@app.route('/mains')
def mainse():
   #ScriptPage(t)

   return render_template('main.html')

@app.route('/cam')
def cameras():
   #ScriptPage(t)

   return render_template('camera.html')
@app.route('/vid')
def videos():
   #ScriptPage(t)

   return render_template('video.html')

@app.route('/pro')
def processor():
   #ScriptPage(t)

   return maincode()
@app.route('/out')
def outp():
   #ScriptPage(t)

   return render_template('temp.html')

@app.route('/runscript')
def ScriptPage():
   
    #table = [[1,2],['four','five'],['eight','nine']]
    return myn()
    #return(tabulate(table, tablefmt='html'))
   # out()
    #return frameNr
    #print("ucamt see me")
    #return redirect(url_for("HomePage"))
@app.route('/runscripter')
def Page():
   

    return flim()
@app.route('/runscript2')
def graph():
  
  return render_template('temp2.html')
@app.route('/run1')
def graph2():
  
  return render_template('tempex.html')
import os
@app.route('/process', methods=['POST'])
def process():
 data = request.get_json() # retrieve the data sent from JavaScript
	# process the data using Python code
 result = data['value'] * 2
	#return jsonify(result=result) # return the result to JavaScript
 return "hi"

@app.route('/real', methods=['GET', 'POST'])
def real():
    bar=request.form['thisvid']
    global var
    var=bar
    return render_template('video.html')

if __name__ == '__main__':
   app.run(port=8001)

   
if( KeyboardInterrupt):
  shutil.rmtree(r"C:\Users\97150\OneDrive\Documents\appy\static\output")
  os.makedirs(r"C:\Users\97150\OneDrive\Documents\appy\static\output")
  print(var)
  if os.path.exists(r"C:\Users\97150\OneDrive\Documents\appy\static\img.png"):
    os.remove(r"C:\Users\97150\OneDrive\Documents\appy\static\img.png")
  else:
    print("The file does not exist")
    
