import turtle
turtle.setup(500,500,400,400)
turtle.pensize(20)
turtle.up()
turtle.fd(-200)
turtle.seth(0)
turtle.down()
turtle.pencolor("#eeaeee")#第一段颜色粉色
turtle.fd(80)#尾巴直行距离
turtle.circle(20,90)#尾巴向上拐弯90度
turtle.fd(100)#直行距离
turtle.pencolor("#Cc9933")#第二段颜色褐色
turtle.circle(-50,180)#身子第一个180转弯
turtle.fd(200)#直行距离200
turtle.pencolor("#6660FF")#第三段颜色蓝色
turtle.circle(50,180)#身子第二个180转弯
turtle.seth(45)#头部角度45度
turtle.circle(300,30)#头部确定
#眼睛
turtle.up()
turtle.seth(330)
turtle.fd(3)
turtle.down()
turtle.pensize(3)
turtle.pencolor("#00FF33")#眼睛颜色绿色
turtle.circle(5,360)



