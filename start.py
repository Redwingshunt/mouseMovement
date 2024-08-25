import pyautogui as pag
import random
def main():
    try :
        for i in range(1,300):
            x,y = (pag.position())
            print(x)
            print(y)
            x += random.randint(-1000,1001)
            y += random.randint(-1000,1001)
            pag.moveTo(x,y)
            print(f"{x}{y}")
    except e:
        print(e)




if __name__ =='__main__':
    main()


