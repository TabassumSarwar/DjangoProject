from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
res={}
boundarytriangle = [[1,1,1,'Equilateral'],[1,1,2,'Isosceles'],[1,2,1,'Isosceles'],[2,1,1,'Isosceles'],[5,5,5,'Equilateral'],
                    [10,9,10,'Isosceles'],[5,5,1,'Isosceles'],[1,5,5,'Isosceles'],[5,1,5,'Isosceles'],[9,10,10,'Isosceles'],
                    [10,10,9,'Isosceles'],[10,10,10,'Equilateral'],[-2,3,5,'Not a Triangle'],[4,5,6,'Scalene']]
boundarycommission = [[1,1,1,100,10],[1,1,2,125,12.5],[1,2,1,130,13],[2,1,1,145,14.5],[5,5,5,500,50],[10,10,9,975,97.5],[10,9,10,970,97],
                      [9,10,10,955,95.5],[10,10,10,1000,100],[10,10,11,1025,103.75],[10,11,10,1030,104.5],[11,10,10,1045,106.75],
                      [14,14,14,1400,160],[18,18,17,1775,216.5],[18,17,18,1770,215.5],[17,18,18,1755,213.5],[18,18,18,1800,220],[18,18,19,1825,225],
                      [18,19,18,1830,226],[19,18,18,1845,229],[48,48,48,4800,820],[70,80,89,7775,1415],[70,79,90,7770,1414],[69,80,90,7755,1411],
                      [70,80,90,7800,1420],[11,10,8,995,99.5],[10,11,9,1005,100.75],[19,17,19,1795,219.25],[18,19,17,1805,221]]
boundarynextdate = [[1,1,1812,1,2,1812],[1,1,1813,1,2,1813],[1,1,1912,1,2,1912],[1,1,2012,1,2,2012],[1,1,2013,1,2,2013],[1,2,1812,1,3,1812],[1,2,1813,1,3,1813],[1,2,1912,1,3,1912],
                    [1,2,2012,1,3,2012],[1,2,2013,1,3,2013],[1,15,1812,1,16,1812],[1,15,1813,1,16,1813],[1,15,1912,1,16,1912],[1,15,2012,1,16,2012],[1,15,2013,1,16,2013],[1,30,1812,1,31,1812],[1,30,1813,1,31,1813],
                    [1,30,1912,1,31,1912],[1,30,2012,1,31,2012],[1,30,2013,1,31,2013]]
equitriangle = [[5,5,5,'Equilateral'],[2,2,3,'Isosceles'],[3,4,5,'Scaelene'],[4,1,2,'Not a Triangle'],[-1,5,5,'Not a Triangle'],[5,-1,5,'Not a Triangle'],
                [5,5,-1,'Not a Triangle'],[11,5,5,'Not a Triangle'],[5,11,5,'Not a Triangle'],[5,11,5,'Not a Triangle'],[-1,5,5,'Not a Triangle'],[5,-1,5,'Not a Triangle'],[5,5,-1,'Not a Triangle'],[-1,-1,5,'Not a Triangle'],
                [5,-1,-1,'Not a Triangle'],[-1,5,-1,'Not a Triangle'],[-1,-1,-1,'Not a Triangle']]
equicommission = [[1,1,1,100,10],[1,1,2,125,12.5],[1,2,1,130,13],[2,1,1,145,14.5],[5,5,5,500,50],[10,10,9,975,97.5],[10,9,10,970,97],[9,10,10,955,95.5],[10,10,10,1000,100],[10,10,11,1025,103.75],[10,11,10,1030,104.75],[11,10,10,1045,106.75],
                  [14,14,14,1400,160],[18,18,17,1775,216.25],[18,17,18,1770,215.25],[17,18,18,1755,213.25],[18,18,18,1800,220],[18,18,19,1825,225],[18,19,18,1830,226],[19,18,18,1845,229],[48,48,48,4800,820],[70,80,89,7775,1415]]
decitriangle = [[20,5,5,'Not a Triangle'],[3,15,11,'Not a Triangle'],[4,5,20,'Not a Triangle'],[5,5,5,'Equilateral'],[10,10,9,'Isosceles'],[5,6,7,'Scalene']]
decicommission =[[20,30,-5,0,0],[15,-2,45,0,0],[-4,15,16,0,0],[15,80,100,0,0],[88,29,90,0,0],[100,200,25,0,0],[-5,400,-9,0,0],[15,20,25,1900,490]]
def output1(request):
    if request.method == 'POST':
        if request.POST.get('run'):
            g = "p1"
            tr = boundarytriangle
        elif request.POST.get('run1'):
            g = "p4"
            tr= equitriangle
        elif request.POST.get('run2'):
            g = "p7"
            tr = decitriangle
    for li in tr:
        if (((li[1] + li[2]) >= li[0]) & ((li[1] + li[0]) >= li[2]) & ((li[0] + li[2]) >= li[1])):
            if li[1] == li[2] == li[0]:
                if li[3] == 'Equilateral':
                    li.append('Equilateral')
                    li.append('Pass')
                else:
                    li.append('Equilateral')
                    li.append('Fail')
            elif (li[1] == li[2]) | (li[2] == li[0]) | (li[0] == li[1]):
                if li[3] == 'Isosceles':
                    li.append('Isosceles')
                    li.append('Pass')
                else:
                    li.append('Isosceles')
                    li.append('Fail')
            else:
                if li[3] == 'Scalene':
                    li.append('Scalene')
                    li.append('Pass')
                else:
                    li.append('Scalene')
                    li.append('Fail')
        else:
            if li[3] == 'Not a Triangle':
                li.append('Not a triangle')
                li.append('Pass')
            else:
                li.append('Not a triangle')
                li.append('Fail')
    if g == "p1":
        return render(request, 'blog/second.html', {'res1': tr})
    elif g == "p4":
        return render(request, 'blog/fourth.html', {'res1': tr})

def output2(request):
    if request.method == 'POST':
        if request.POST.get('run'):
            g = "p2"
            tc = boundarycommission
        elif request.POST.get('run1'):
            g = "p5"
            tc= equicommission
        elif request.POST.get('run2'):
            g = "p8"
            tc = decicommission
        for li in tc:
            locks = li[0]
            stocks = li[1]
            barrels = li[2]
            lprice =45.0
            sprice =30.0
            bprice =25.0
            c1 = (locks<=0 or locks>70)
            c2 =(stocks<=0 or stocks>80)
            c3 = (barrels<=0 or barrels>90)
            if (c1 and c2 and c3):
                li.append('0')
                li.append('0')
                li.append('Fail')
            else:
                sales = lprice*locks+sprice*stocks+bprice*barrels
            if sales>0:
                if sales<=1000:
                    comm=0.10*sales
                elif sales<1800:
                    comm = 0.10*1000
                    comm += 0.15*(sales-1000)
                else:
                    comm = 0.10*sales
                    comm += 0.15 * 800
                    comm += 0.20 * (sales - 1000)
                li.append(sales)
                li.append(comm)
            else:
                li.append(0)
                li.append(0)
            if li[3]==sales and li[4]==comm:
                li.append("Pass")
            else:
                li.append("Fail")
        if g == "p2":
            return render(request, 'blog/second.html', {'res1': tc})
        elif g == "p5":
            return render(request, 'blog/p5.html', {'res1': tc})
        elif g == "p8":
            return render(request, 'blog/p8.html', {'res1': tc})
def output3(request):
    ndout = request.POST.get('run')
    if ndout == 'p3':
        tn = boundarynextdate
        for li in tn:
            month = li[0]
            date = li[1]
            year = li[2]
            if date<=0 or date>31:
                li.append(0)
                li.append(0)
                li.append(0)
            elif month<1 or month>12:
                li.append(0)
                li.append(0)
                li.append(0)
            elif(month in [4,6,9,11] and date == 31):
                li.append(0)
                li.append(0)
                li.append(0)
            elif year<=1812 or year>2013:
                li.append(0)
                li.append(0)
                li.append(0)
            elif month==2:
                if ((year % 4==0 and year %100!=0)or year%400 ==0):
                    if date>29:
                        li.append(0)
                        li.append(0)
                        li.append(0)
                else:
                    if date>28:
                        li.append(0)
                        li.append(0)
                        li.append(0)
            else:
                tomyear = year
                tommonth = month
                tomdate = date
                if month in [1,3,5,7,8,10]:
                    if date<31:
                        tomdate = date+1
                    else:
                        tomdate = 1
                        tommonth = month+1
                elif month in [4,6,9,11]:
                    if date<30:
                        tomdate =date+1
                    else:
                        tomdate =1
                        tommonth=month+1
                elif month ==12:
                    if date<31:
                        tomdate=date+1
                    else:
                        tomdate=1
                        tommonth=1
                        if year==2013:
                            tomyear = 0
                        else:
                            tomyear = year+1
                elif month == 2:
                    if date<28:
                        tomdate = date+1
                    elif ((year % 4==0 and year %100!=0)or year%400 ==0):
                        if date==28:
                            tomdate= date+1
                    elif date ==28 or date==29:
                        tomdate=1
                        tommonth=3
                li.append(tommonth)
                li.append(tomdate)
                li.append(tomyear)
            if li[3]==li[6] and li[4]==li[7] and li[5]==li[8]:
                li.append('Pass')
            else:
                li.append('Fail')
        return render(request, 'blog/p3.html', {'res1': tn})


def home(request):
    return render(request, 'blog/home.html')

def intro(request):
    return render(request, 'blog/intro.html')
def about(request):
    return render(request, 'blog/about.html')
def contact(request):
    return render(request,'blog/contact.html')
def second(request):
    return render(request,'blog/second.html')
def fourth(request):
    return render(request,'blog/fourth.html')
def two(request):
    return render(request, 'blog/p2.html')
def third(request):
    return render(request, 'blog/p3.html')
def fifth(request):
    return  render(request, 'blog/p5.html')
def sixth(request):
    return render(request, 'blog/p6.html')
def seventh(request):
    return render(request, 'blog/p7.html')
def eighth(request):
    return render(request, 'blog/p8.html')
def ninth(request):
    return render(request, 'blog/p9.html')
def tenth(request):
    return render(request, 'blog/p10.html')
def video(request):
    return render(request, 'blog/video.html')
def quiz(request):
    ou = request.POST.get('question-1-answers-C')
    print(ou)
    t = "apple"
    return render(request, 'blog/quiz.html',{'res':t})
def grade(request):
    return render(request, 'blog/grade.html')