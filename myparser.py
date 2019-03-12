#command line argument in python
import argparse  #argument parser

if __name__=='__main__':
    # initalize the parser

    parser=argparse.ArgumentParser(
        description="my math script"
    )
#Add the parameter positional/optional
    parser.add_argument('num1',help="Number 1", type=float) #positional argument is passed in parser var and call method add_arg
    parser.add_argument('num2',help="number 2", type=float)
    parser.add_argument('operation', help="provide operator")

    #click on terminal at the footer of pycharm and run :python myparser.py
    #python myparser.py 35 57 + will show num1=35,num2=57 ....
#parse the arguments
    args=parser.parse_args() #all args will beat arg varpython

    print(args)
    result=None #initial value of result is none
    if args.operation=='+':
        result=args.num1+args.num2

    if args.operation=='-':
        result=args.num1-args.num2
    if args.operation=='*':
        result=args.num1*args.num2
    if args.operation=='pow':
        result=pow(args.num1,args.num2)

    print(("Result: ",result))

    #enter no as defined eg: 35 57 +,  23 35 pow