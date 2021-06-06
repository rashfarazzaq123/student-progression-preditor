count=1
print("ANNUAL PROGRESSION OUTCOME OF THE STUDENT")

# progress=0;
# trailer=0;
# exclude=0;
# retriver=0;

def my():
 progress=0;
 trailer=0;
 exclude=0;
 retriver=0;

 while True:
  try:
    
    pass_or_quit = input("enter pass credits:")
    pas=int(pass_or_quit)
    defer=int(input("enter defer credits:"))
    fail=int(input("enter fail credits:"))
    
    if not(pas==0 or pas==20 or pas==40 or pas==60 or pas==80 or pas==100 or pas==120):
       print("range error")
    elif not(defer==0 or defer==20 or defer==40 or defer==60 or defer==80 or defer==100 or defer==120):
       print("range error")
    elif not(fail==0 or fail==20 or fail==40 or fail==60 or fail==80 or fail==100 or fail==120):
       print("range error")
 
    total=pas+defer+fail

    if total==120:
      if pas==120 and defer==fail==0:
         print("prograss")
         progress += 1
         
      elif pas==100:
        if 20>=fail>=0 and 20>=defer>=0:
             print("prograss module trailer")
             trailer += 1
      elif pas==80:
        if 40>=defer>=0 and  40>=fail>=0:
              print("Do not progress-module retriever")
              retriver += 1
      elif pas==60:
          if 60>=defer>=0 and  60>=fail>=0:
           print("Do not progress-module retriever")
           retriver += 1
      elif pas==40:
         if 80>=defer>=20 or 60>=fail>=0:
           print("Do not progress-module retriever")
           retriver += 1
         else:
           if defer==0 and fail==80:
             print("Exclude")
             exclude += 1
      elif pas==20:
          if 100>=defer>=40 and 60>=fail>=0:
            print("Do not progress-module retriever")
            retriver += 1
          else:
            if 20>=defer>=0 and  100>=fail>=80:
                print("Exclude")
                exclude += 1
      elif pas==0:
            if 120>=defer>=60 or 60>=fail>=0:
               print("Do not progress-module retriever")
               retriver += 1
            else:
              if 40>=defer>=0 and 120>=fail>=80:
                 print("Exclude")
                 exclude += 1
    elif total!=120:
           print("total incorrect")
 
  except ValueError:
      if pass_or_quit == "q":
        #PART2
        
        print("HORIZONTAL HISTOGRAM FOR THE STUDENT PROGRESSION OF THE YEAR")
        print("progress: ", end =" ")
        for x in range(progress):
         print('*', end =" ")

        print("")
        # print(progress)

        print("retriver: ", end =" ")
        for x in range(retriver):
         print('*', end =" ")

        print("")

        print("trailer: ", end=" ")
        for x in range(trailer):
          print('*',end=" ")
          
        print("")
        
        print("exclude: ", end=" ")
        for x in range(exclude):
           print('*',end=" ")
        #PART3
        print("")
        print("VERTICAL HISTOGRAM FOR THE STUDENT PROGESSION OF THE YEAR")
        print("")
        credit = ['progress', 'trailer', 'retiver', 'exclude']
        print(' '.join(credit))
        for x in range(max(progress, trailer, retriver, exclude)):
            print(" {0}     {1}     {2}     {3}".format(
            '*' if x < progress else ' ',
            '   *' if x < trailer else '    ',
            '   *' if x < retriver else '    ',
            '   *' if x < exclude else ' '
          ))
        print("Exiting the program")
        break
      else: 
        print("Number required")
count=count+1     
my()
