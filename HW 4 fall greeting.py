from graphics import*
import time

def fallGreetingCard():

    winWidth = 600
    winHeight = 600
    win = GraphWin("Points", winWidth, winHeight)
    win.setBackground(color_rgb(13,26,129))
    #set sky


    trunk = Rectangle(Point(0,0),Point(100,500))
    trunk.draw(win)
    trunk.setFill("brown")

    
    #the ground
    ground = Circle(Point(500,600),320)
    ground.draw(win)
    ground.setFill("green")

    groundLeft = ground.clone()
    groundLeft.draw(win)
    groundLeft.move(-200,0)
    
    #Text
    button = Text(Point(300,550),"Happy Fall!")
    button.draw(win)
    button.setSize(36)

    moon = Circle(Point(550,20),50)
    moon.draw(win)
    moon.setFill("white")
    moon.move(-100,-10)
    time.sleep(.5)
    


    pumpkin = Polygon(Point(229,262),Point(214,246),Point(189,239),Point(171,243),Point(161,251),Point(157,262),Point(154,276),Point(154,288),Point(156,304),Point(162,315),Point(171,326),Point(184,333),Point(202,341),Point(221,343),Point(241,342),Point(260,344),Point(283,340),Point(301,327),Point(312,309),Point(321,284),Point(320,258),Point(307,239),Point(291,236),Point(273,237),Point(257,241),Point(248,249))
    pumpkin.draw(win)
    pumpkin.setFill("orange")
    #pumpkin shape

    stem = Rectangle(Point(240,262),Point(220,235))
    stem.draw(win)
    stem.setFill("brown")
    #stem



    smile = Polygon(Point(187,302),Point(282,299),Point(282,305),Point(279,311),Point(275,316),Point(270,320),Point(259,325),Point(246,325),Point(232,326),Point(218,326),Point(203,323),Point(193,317),Point(187,310))
    smile.draw(win)
    smile.setFill("black")
    #smile

    
    eyeOne = Polygon(Point(190,270),Point(210,270),Point(200,290))
    eyeOne.draw(win)
    eyeOne.setFill("black")
    #left eye

    eyeTwo = eyeOne.clone()
    eyeTwo.move(70,0)
    eyeTwo.draw(win)
    #right eye

    treeLeaf = Polygon(Point(0,146),Point(6,146),Point(7,148),Point(16,150),Point(24,150),Point(31,149),Point(32,143),Point(32,135),Point(32,135),Point(42,136),Point(55,136),Point(65,136),Point(71,135),Point(76,129),Point(77,122),Point(77,115),Point(85,116),Point(93,116),Point(109,116),Point(117,115),Point(123,108),Point(123,103),Point(123,95),Point(122,84),Point(119,78),Point(114,74),Point(126,74),Point(141,60),Point(141,53),Point(139,44),Point(132,38),Point(126,36),Point(131,34),Point(141,31),Point(153,22),Point(153,13),Point(153,10),Point(153,0),Point(0,0))
    treeLeaf.draw(win)
    treeLeaf.setFill(color_rgb(4,101,53))

    leafOne = Polygon(Point(68,62),Point(73,63),Point(78,63),Point(86,67),Point(87,72),Point(87,78),Point(85,81),Point(79,82),Point(85,92),Point(81,86),Point(77,88),Point(76,91),Point(71,91),Point(67,86),Point(66,80),Point(65,74),Point(65,69),Point(65,64))
    leafOne.draw(win)
    leafOne.setFill(color_rgb(4,101,53))

    leafTwo = leafOne.clone()
    leafTwo.draw(win)
    leafTwo.move(-30,-30)

    leafThree = leafOne.clone()
    leafThree.draw(win)
    leafThree.move(30,30)

    leaf4 = leafOne.clone()
    leaf4.draw(win)
    leaf4.move(-50,0)
    

    leaf5 = leafOne.clone()
    leaf5.draw(win)
    leaf5.move(0,-40)

    leaf6 = leafOne.clone()
    leaf6.draw(win)
    leaf6.move(-30,30)

    leaf7 = leafOne.clone()
    leaf7.draw(win)
    leaf7.move(30,-30)


    leaf8 = leafOne.clone()
    leaf8.draw(win)
    leaf8.move(60,300)
    leaf8.setFill("yellow")

    leaf9 = leaf8.clone()
    leaf9.draw(win)
    leaf9.move(20,20)
    leaf9.setFill("red")

    leaf10 = leaf8.clone()
    leaf10.draw(win)
    leaf10.move(-20,60)
    leaf10.setFill("brown")

    leaf11 = leaf8.clone()
    leaf11.draw(win)
    leaf11.move(-20,20)
    leaf11.setFill("red")

    leaf12 = leaf8.clone()
    leaf12.draw(win)
    leaf12.move(0,80)
    leaf12.setFill("orange")

    leaf13 = leaf8.clone()
    leaf13.draw(win)
    leaf13.move(-50,30)
    leaf13.setFill("yellow")

    leaf14 = leaf8.clone()
    leaf14.draw(win)
    leaf14.move(30,60)
    leaf14.setFill(color_rgb(4,101,53))

    leaf15 = leaf8.clone()
    leaf15.draw(win)
    leaf15.move(60,60)
    leaf15.setFill("yellow")

    leaf16 = leaf8.clone()
    leaf16.draw(win)
    leaf16.move(80,50)
    leaf16.setFill("orange")

    leaf17 = leaf8.clone()
    leaf17.draw(win)
    leaf17.move(100,70)
    leaf17.setFill(color_rgb(4,101,53))

    leaf18 = leaf8.clone()
    leaf18.draw(win)
    leaf18.move(80,100)
    leaf18.setFill("brown")

    leaf19 = leaf8.clone()
    leaf19.draw(win)
    leaf19.move(100,120)
    leaf19.setFill("orange")

    leaf20 = leaf8.clone()
    leaf20.draw(win)
    leaf20.move(140,60)
    leaf20.setFill("red")
    

        
    

    

##    points = []
##    for i in range (40):
##        clickPt = win.getMouse()
##        clickPt.draw(win)
##        points.append(clickPt)
##        print("Point(" +str(clickPt.getX())+"," +str(clickPt.getY())+"),",end ="")
##
##    shape = Polygon(clickPt)
##    shape.draw(win)

    time.sleep(.5)
    leafOne.setFill("red")
    leafTwo.setFill("brown")
    leafThree.setFill("yellow")
    leaf4.setFill(color_rgb(4,101,53))
    leaf5.setFill("yellow")
    leaf6.setFill("brown")
    leaf7.setFill("red")
    #changing color

    for i in range(10):        
        time.sleep(0.2)                   
        smile.setFill("yellow")
        eyeOne.setFill("yellow")
        eyeTwo.setFill("yellow")
        leafOne.move(10,10)
        leafTwo.move(10,10)
        leafThree.move(10,10)
        leaf4.move(10,10)
        leaf5.move(10,10)
        leaf6.move(10,10)
        leaf7.move(10,10)
        leafOne.move(-5,10)
        leafTwo.move(-5,10)
        leafThree.move(-5,10)
        leaf4.move(-5,10)
        leaf5.move(-5,10)
        leaf6.move(-5,10)
        leaf7.move(-5,10)
        time.sleep(0.2)
        smile.setFill("black")
        eyeOne.setFill("black")
        eyeTwo.setFill("black")
        #flicker
        leafOne.move(10,10)
        leafTwo.move(10,10)
        leafThree.move(10,10)
        leaf4.move(10,10)
        leaf5.move(10,10)
        leaf6.move(10,10)
        leaf7.move(10,10)
        #falling leaves

    button.setText("Click Anywhere to Close")
    #click to close Text

    


    win.getMouse()
    win.close()
    
    
