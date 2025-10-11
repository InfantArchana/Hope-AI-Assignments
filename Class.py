class MyAssignments():
    def Subfields():
        print("Sub-fields in AI are:")
        lists=["Machine Learning","Neural Networks","Vision", "Robotics","Speech Processing","Natural Language Processing"]
        for temp in lists:
            print(temp)
    def OddEven():
            num=int(input("Enter a number:"))
            if(num%2==1):
                print(num,"is Odd number")
                message=num,"is Odd number"
            else:
                print(num,"is Even number")
                message=num,"is Even number"
            return message 
    def eligible():
        gender=input("Your Gender:")
        age=int(input("Your Age:"))
        if(gender=="Male"):
            if(age<21):
                print("NOT ELIGIBLE")
                check="NOT ELIGIBLE"
        elif(gender=="Female"):
            if(age<18):
                print("NOT ELIGIBLE")
                check="NOT ELIGIBLE"
        return check

    def percentage():
        S1=int(input("Subject1="))
        S2=int(input("Subject2="))
        S3=int(input("Subject3="))
        S4=int(input("Subject4="))
        S5=int(input("Subject5="))
        total=S1+S2+S3+S4+S5
        print("Total=",total)
        Percent=(total/500)*100  
        print("Percentage=",Percent)
        
    def triangle():
        height=int(input("Height:"))
        base=int(input("Base:"))
        print("Area formula: (Height*Breadth)/2")
        area=(height*base)/2
        print("Area of Triangle:",area)
        height1=int(input("Height1:"))
        height2=int(input("Height2:"))
        base=int(input("Base:"))
        print("Perimeter formula: Height1+Height2+Base")
        perimeter=height1+height2+base
        print("Perimeter of Triangle:",perimeter)
        return 