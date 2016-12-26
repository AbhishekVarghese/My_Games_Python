import highscore
from direct.showbase.ShowBase import ShowBase
from math import pi, sin, cos
from direct.task import Task
from direct.actor.Actor import Actor
from pandac.PandaModules import Point3
from direct.interval.IntervalGlobal import Sequence,Parallel
from direct.gui.OnscreenText import OnscreenText
from direct.showbase.DirectObject import DirectObject
import time,random
from panda3d.core import TextNode, DirectionalLight, VBase4

time_given = 480
my_name = raw_input("Enter your full name before playing : ")
my_score = 0
print
print
def write_scores(my_name,my_score) :
    o = open('scores.txt','a')
    o.write(str(my_name)+":"+str(my_score)+"\n")
    o.close()
print '''----------------Read the following before playing-------------------

Story :

Extracts from the diary of Gordon Heyman (Physiscist & biologist) -

May 21 10,000 AD : We reached The International Space Station today at 1200 hrs. My group decides to have a day's rest before we begin.

May 22 10,000 AD : We started today at 900 hrs and probably will complete our study in a month. The organic specimen we broght from the earth is secure. Our Study will include the effect of electromagnetic radiations on cell structure. Hopefully we will give somthing to our planet when we get back home.

May 29 10,000 AD : One week has passed. We made certain observations which stunned us. The cells of these creatures seems to change its composition on absorbing some of the lines of the spectrum. Fascinatingly these creautres did not die even after the composition of their cells changed. Looks like they have learnt to cope up with cellular changes.

June 1 10,0000 AD : Horrible things are happening !! Yesterday one of these creatures woke up from cry sleep and killed one of the scientists. Somehow we put it back in the cryo. The cryo had stopped functioning due to a power cut. We are still shaken from this incident

June 2 10,000 AD : Frequent power loss in ISS. Dont know why, but the solar cells and the transformers have stopped generating power. Looks like EMP(Electro Magnetic Pulse) fried our circuits. But source of the EMP was not found. Something's not right!
___________________________________________________________________________________________________

Controlls :

W = Move Drone Forward globaly
s = Move Drone Backward globaly
A = Move Drone Left globaly
D = Move Drone Right globaly
Q = Move Drone Down globaly
E = Move Drone Up globaly

Up = Rotate camera Up
Down = Rotate camera Down
Left = Rotate camera Left
Right = Rotate camera Right

Space = Interact with objects
_____________________________________________________________________________________________________

Situation and Instructions :

On 3rd June 10,000 AD a massive power faliure resulted in complete faliure of Cryo Bay. All the genetically transformed creatures awoke.
There was havoc in ISS. The creatures Started killing the crew aboard the ISS.

You are Gordon. You managed to flee to the escape capsule. With you is the captain who was leading the mission in The ISS. You both are currently the lone survivors in the ISS.
But the captain couldnt make it in time to the escape capsule and is now trapped in a cabin between the escape capsule and the main body of the ship.
You are inside the escape capsule and you have a remote in your hand. There is a drone in the cabin where the captian is stranded. 
You need to open the door to the escape capsule with help of your drone and rescue the captain. Faliure will result in your Death and later the complete Anhilation of the planet Earth by These Creatures.
Follow the instructions which will be given to you.

And remember : Time and Fate Waits for None!!'''
raw_input("\nPress Enter to start")
arrow_set = False
bomb_planted = False
lose_anim= [0,0,0,0,0,0]

key_pos = random.choice([[30,-12,4],[39,-18,4],[40,-10,16],[25,-23,4],[23,-23,5],[32,-23,5],[27,-19,4.0],[-26,-19,4.5],[-26,-19,4.5],[32,-24,4],[28,-11,5],[54,23,3],[54,23,3],[54,23,3]])
hurry = False
cap_found =False
key_found = False
door_close = False
end_good = False
end_bad = False
temp = [False,0]
anim_start = False
pil_played = False
goout1_played = False
lose = False
stop= False
level2 = False
bomb_found = False
seeker_down = False
energy_found = False
try1 = False
cap_see = False
everything_not_over = False
score_not_written = True
def addInstructions(pos, msg):
    return OnscreenText(text=msg, style=1, fg=(1,1,1,1),
                        pos=(-1.3, pos), align=TextNode.ALeft, scale = .05)

def addTitle(text):
    return OnscreenText(text=text, style=1, fg=(1,1,1,1),
                        pos=(1.3,-0.95), align=TextNode.ARight, scale = .07)

def getcoordinates(thing) :
    a = str(thing.getPos())
    l = a[10 : len(a) - 1 ] + ','
    r = []
    t = ''
    for i in l:
       
        if i.isdigit() :

            t+=i
        elif i ==',' :
            r.append(int(t))
            t = ''
        
    return r
camx= -30
camy = 19
camz = 3

camxy = -90
camzx = 0
camyz = 0


'''def spinCameraTask(task):
        angleDegrees = task.time * 6.0
        angleRadians = angleDegrees * (pi / 180.0)
        camera.setPos(20.0 * sin(angleRadians), -20.0 * cos(angleRadians),3)
        camera.setHpr(angleDegrees, 0,0)
        return Task.cont
'''

def Move_seeker(task):
    global seeker_down
    if not seeker_down :
        angleDegrees = task.time*100
        angleRadians = angleDegrees * (pi / 180.0)
        seeker.setPos(62,3 ,8 + 5*sin(angleRadians))
        seeker_copy.setPos(62,8 ,8 + -5*sin(angleRadians))
        return Task.cont
    
screen = ShowBase()
screen.title = addTitle("3d Python Game!! : Created by Abhishek")
addInstructions(0.90, "[A]: Move Drone Left globaly")
addInstructions(0.85, "[D]:Move Drone Right globaly")
addInstructions(0.80, "[W]: Move Drone Forward globaly")
addInstructions(0.75, "[S]: Move Drone Forward globaly")
addInstructions(0.70, "[Q]: Move Drone Down globaly")
addInstructions(0.65, "[E]: Move Drone UP globaly")

addInstructions(0.55, "[Left]: Rotate Camera Left")
addInstructions(0.50, "[Right]: Rotate Camera Right")
addInstructions(0.45, "[UP]: Rotate Camera UP")
addInstructions(0.40, "[DOWN]: Rotate Camera Down")

addInstructions(0.30, "[Space]: Interact with Objects")

addInstructions(0.20, "The Drone Can peirce the walls and ojects\nThick walls can be pierced only to some extent")

#addInstructions(0.65, "Find the captain and do as he says")
screen.camLens.setFocalLength(1)
def set_cam(task) :
    global hurry,score_not_written,my_score,stop,seeker_down,anim_start,everything_not_over,pil_played, goout1_played,pil,goout,goout1,temp,level2,arrow_set,bomb_planted,cap_see,try1,cap_found,end_good,lose,lose_anim
    camera.setPos(camx,camy,camz)
    camera.setHpr(camxy,camyz,camzx)
    if not lose and not level2 and task.time > time_given:
        lose = True
        end_good = False
        cap_found = True
        my_score -= 200
        Theme2.stop()

    if lose :
        
        if lose_anim[0] == 0 :
            
            seeker_fall.start()
            spark.play()
            seeker_down = True
            lose_anim[0] = 1
            lose_anim[5] = 1
            my_score -= 100
            
        elif lose_anim[5] == 1 and seeker_fall.isStopped():
            seeker_roll.start()
            
            lose_anim[1] = 1
            
            lose_anim[5] = 0

        elif lose_anim[1] == 1 and seeker_roll.isStopped() :
            my_score -= 100
            end_anim_lose.start()
            lose_anim[2] = 1
            lose_anim[1] = 0
            shout_man.play()
            
            temp = [task.time,False]
        elif lose_anim[2] == 1 and end_anim_lose.isStopped() :
            my_score  -= 300
            final_kill.play()
            lose_anim[2] = 0
            lose_anim[3] = 1
            temp = [task.time,False]

        elif lose_anim[3] == 1 and task.time - temp[0] >3:
            go_for_kill.start()
            temp = [task.time,False]
            my_score -= 500
            lose_anim[3] = 0
            lose_anim[4] = 1
        elif lose_anim[4] == 1 :
            
            if 2 > task.time - temp[0] > 1 :
                go4.start()
               
            elif 5 > task.time - temp[0] > 4 :
                
                dlnp = render.attachNewNode(dlight)
                
                dlnp.setHpr(0, -60, 0)
                render.setLight(dlnp)
                dlight.setColor(VBase4(0, 0, 0, 0))
            elif 6 > task.time - temp[0] > 5  and scream.status()!= 2:
                scream.play()
                
            elif Theme_last.status() == 1 :
                Theme_last.play()
                everything_not_over = True
               

            elif everything_not_over and task.time - temp[0]>15:
                
                my_score = my_score - int(task.time)
                write_scores(my_name,my_score)
                highscore.get_highscores(my_name)
                raw_input("Enter to exit")
                everything_not_over = False

            elif  task.time - temp[0]>20 :
                print "Sorry! You lost"
                
            
        
        
            
    if not lose :
        if task.time > 360 and not level2 and not hurry:
            talk_to_hurry.play()
            hurry = True
            for i in range(10) :
                print 'Hurry. Time is running out'
        if try1 and not wrong.status() == 2:
            sound4b.play()
            cap_found = True
            try1 = False
            
        if not (end_bad):
            if int(task.time) == 3 :
            
                sound1.setVolume(0.5)
                sound1.play()
            
            if not cap_see and int(task.time)%30 == 0 and int(task.time) !=0 :
            
                sound2.setVolume(0.5)
                sound2.play()
                time.sleep(3)
                sound3.setVolume(0.5)
                sound3.play()
            
            

            
            
        if end_good :
            
           
            
            if not anim_start :
                opened.play()
                goout.start()
                anim_start = True
                
        
            elif goout.isStopped() and not (pil.isPlaying() or pil_played) :
                thank1.play()
                pil.start()
                
                pil_played= True
                
            elif pil.isStopped() and goout.isStopped() and not (goout1.isPlaying() or goout1_played):
                
                goout1.start()
                goout1_played = True
                temp = [True,task.time]
                opened.play()
               
        if bomb_planted and temp[0]:
            temp[1] = task.time
            temp[0] = not temp[0]
        if bomb_planted and 4 <int(task.time) - int(temp[1]) < 8  and not stop:
            talk3.play()
        if bomb_planted and int(task.time) - int(temp[1]) > 12 and not stop:
            
            if Level2_music.status() == 2 :
                Level2_music.stop()
                timer_bomb.stop()
                dlight.setColor(VBase4(0, 0, 0, 0))
            
            if int(task.time) - int(temp[1])  > 17 :
                final_explosion.play()
                stop = True
                time.sleep(5)
                end_music.play()
            
            elif 13 < int(task.time) - int(temp[1]) >15 :
                
                explosion1.play()
                time.sleep(2)
                explosion1.play()
                time.sleep(1)
                explosion1.play()
                time.sleep(0.5)
                explosion1.play()
                time.sleep(0.1)
                explosion1.play()
                time.sleep(0.1)
                explosion1.play()
                time.sleep(0.3)
                explosion1.play()
                time.sleep(0.5)
                explosion1.play()
                time.sleep(0.5)
                
        if stop and int(end_music.getTime()) == 7 :
            if score_not_written :
                score_not_written = False
                my_score = my_score - int(task.time)
                write_scores(my_name,my_score)
                highscore.get_highscores(my_name)
                print
                raw_input("Enter to quit")
           
            end_music.setTime(0)
            print "Congratulations You won !!!"
            
            
                
                
            
            

        elif level2 :
            if (int(task.time) - int(temp[1]) == 2 ) and not seeker_down :
                Level2_music.setVolume(0.3)
                talk1.play()
            if (int(task.time) - int(temp[1]) == 16 ) and not seeker_down :
                spark.play()
                Level2_music.setVolume(0.48)
                seeker_fall.start()
                seeker_down = True
                temp[0] = not temp[0]
                
            elif (int(task.time) - int(temp[1]) < 25 ) and seeker_fall.isStopped() and not seeker_roll.isPlaying() and temp[0]:
                temp[0] = not temp[0]
                seeker_roll.start()
               

            if arrow_set :
                arrow.setPos(0,0,5)
                arrow.loop('anim')
                arrow_set = False

        


            
        
        if pil.isStopped() and goout.isStopped and temp[0] and (int(task.time) - int(temp[1]) == 6) and not level2:
            temp[0] = False
            Theme2.stop()
            closed.play()
            
            level2 = True
            temp[1] = task.time
            dlight.setColor(VBase4(0.8, 0.8, 0.5, 1))
            dlnp = render.attachNewNode(dlight)
            dlnp.setHpr(0, -60, 0)
            render.setLight(dlnp)
            Level2_music.play()
            print 'playing'
        

    
        
    return Task.cont

dlight = DirectionalLight('my dlight')
            

sound1 = screen.loader.loadSfx("sound1.wav")
sound1.setVolume(0.01)
sound2 = screen.loader.loadSfx("sound2.mp3")
sound3 = screen.loader.loadSfx("sound3.mp3")
sound4 = screen.loader.loadSfx("Search for key 1.mp3")
sound4b = screen.loader.loadSfx("Search for key 2.mp3")
sound4.setVolume(1)

thank1 = screen.loader.loadSfx("thank1.mp3")
thank1.setVolume(1)
talk1 = screen.loader.loadSfx("talk1.mp3")
talk1.setVolume(1)
talk2 = screen.loader.loadSfx("talk2.mp3")
talk2.setVolume(1)
talk3 = screen.loader.loadSfx("talk3.mp3")
talk3.setVolume(1)
talk4 = screen.loader.loadSfx("talk4.mp3")
talk4.setVolume(1)
talk_to_hurry = screen.loader.loadSfx("talk_to_hurry.mp3")
talk_to_hurry.setVolume(1)

wrong = screen.loader.loadSfx("wrong.mp3")
spark = screen.loader.loadSfx("spark.mp3")
spark.setVolume(1)
got = screen.loader.loadSfx("levelup.wav")
got.setVolume(0.5)
timer_bomb = screen.loader.loadSfx("beeping.mp3")
timer_bomb.setLoop(True)
timer_bomb.setVolume(0.5)
explosion1 = screen.loader.loadSfx("explosion1.mp3")
final_explosion = screen.loader.loadSfx("final_explosion.wav")
final_kill = screen.loader.loadSfx("bc_attackgrowl3.wav")
scream =  screen.loader.loadSfx("fallscream.wav")


checkpoint = screen.loader.loadSfx("checkpoint.wav")
shout_man = screen.loader.loadSfx("special7.wav")
opened = screen.loader.loadSfx("open.wav")
opened.setPlayRate(0.75)
closed = screen.loader.loadSfx("close.mp3")
closed.setVolume(1)

Theme_last = screen.loader.loadSfx("a.wav")
#Theme1 = screen.loader.loadSfx("guilt1.mp3")
Theme2 = screen.loader.loadSfx("jurassicpark1.mp3")
Theme2.setVolume(0.6)
Theme2.setPlayRate(0.5)
Theme2.setLoop(True)
Theme2.play()
end_music = screen.loader.loadSfx("miami_success.mp3")
end_music.setLoop(True)
end_music.setPlayRate(0.9)


Level2_music = screen.loader.loadSfx("level2_music.mp3")
Level2_music.setVolume(0.6)
Level2_music.setLoop(True)

environ = screen.loader.loadModel("bvw-f2004--milleniumfalcon/falcon.egg")
environ.reparentTo(screen.render)
environ.setScale(3,3,3)
environ.setPos(0, 0, 0)

actor = Actor("pilot/pilot-model",{"idle": "pilot/pilot-idle"})
actor.setScale(0.1,0.1,0.1)
actor.reparentTo(screen.render)
actor.setPos(8,-5,0)
actor.setHpr(90,0,0)
actor.loop('idle')



alien = Actor("alien/alienmodel.egg",{"kill": "alien/alienmodelwalkanim.egg"})
alien.setScale(0.8,0.8,0.8)
alien.reparentTo(screen.render)
alien.setPos(100,100,100)
alien.setHpr(0,10,0)


enemy = Actor("enemyship2/monster3-anim-idle",{"shoot": "enemyship2/monster3-anim-shoot"})
enemy.setScale(1,1,1)
enemy.reparentTo(screen.render)
enemy.setPos(100,100,100)
enemy.setHpr(90,0,0)
enemy.loop('shoot')


bomb = Actor("enemyship1/monster2",{"blast": "enemyship1/monster2-anim-fire"})
bomb.setScale(1,1,1)
bomb.reparentTo(screen.render)
bomb.setPos(39,-26,0)
bomb.setHpr(90,0,0)
bomb.loop('blast')


seeker = Actor("seeker/seeker.egg")
seeker.setScale(1,1,1)
seeker.reparentTo(screen.render)
seeker_copy = Actor("seeker/seeker.egg")
seeker_copy.setScale(1,1,1)
seeker_copy.reparentTo(screen.render)

key = Actor("key/key.egg")
key.setScale(1.5,1.5,1.5)
key.reparentTo(screen.render)
key.setPos(key_pos[0],key_pos[1],key_pos[2])

crate = screen.loader.loadModel("crate/crate.egg")
crate.setScale(1,8,8)
crate.reparentTo(screen.render)
crate.setPos(-40,5,5)

arrow = Actor("squarrow/squarrow-model.egg",{'anim' : "squarrow/squarrow-anim.egg"})
arrow.reparentTo(screen.render)
arrow.setPos(110,110,110)

blast_can = Actor("capsule/capsule.egg")
blast_can.reparentTo(screen.render)
blast_can.setScale(0.1,0.1,0.1)
blast_can.setHpr(90,90,-90)
blast_can.setPos(-25,-23,13.5)


console = Actor("controlpanel/controlpanelmodel.egg")
console.setScale(1,1,1)
console.reparentTo(screen.render)
console.setPos(-37,5,8)
console.setHpr(90,0,0)


# Animations --------------
a= crate.posInterval(9,Point3(-40,5,30),startPos=Point3(-40,5,5))
b =console.posInterval(9,Point3(-37,5,20),startPos=Point3(-37, 5,7))
c = key.posInterval(9,Point3(-34,5,20),startPos=Point3(-34, 5, 7))
goout = Parallel(a,b,c)
        
            
        

d1 = actor.hprInterval(1,Point3(230,0,0),startHpr=Point3(90, 0, 0))
d12 = actor.posInterval(3,Point3(8, -5, 5),startPos=Point3(8, -5, 0))
d2 = actor.posInterval(5,Point3(-49,5,5),startPos=Point3(8, -5, 5))

pil = Sequence(d1,d12,d2)
        

a1 = crate.posInterval(9,Point3(-40,5,5),startPos=Point3(-40,5,30))
b1 =console.posInterval(6,Point3(-37,5,7),startPos=Point3(-37, 5,20))
c1 = key.posInterval(6,Point3(-36,5,7),startPos=Point3(-36, 5, 20))
goout1 = Parallel(a1,b1,c1)
        
# --- Seeker down anim ------------
e1 = seeker.posInterval(1,Point3(62,8,2),startPos=Point3(62,8,7))
e2 = seeker_copy.posInterval(1,Point3(62,3,2),startPos=Point3(62,3,9))
seeker_fall = Parallel(e1,e2)

ex1 = seeker.hprInterval(2,Point3(0,0,-360),startHpr=Point3(90, 0, 0))
ex2 = seeker_copy.hprInterval(3,Point3(0,0,-360),startHpr=Point3(90, 0, 0))

ex21 = seeker.posInterval(2,Point3(40,2,1),startPos=Point3(62,3,3))
ex22 = seeker_copy.posInterval(3,Point3(30,9,1),startPos=Point3(62, 8, 3))
enen = enemy.posInterval(7,Point3(10,8,7),startPos=Point3(65, 7, 7))
seeker_roll = Parallel(ex1,ex2,ex21,ex22,enen)                    

# --- Game over anim ----------------
go1 =  alien.posInterval(3,Point3(62,6,1),startPos=Point3(62,17,1))
go2 =  alien.hprInterval(2,Point3(-90,10,0),startHpr=Point3(0, 10, 0))
go3 =  alien.posInterval(2,Point3(50,6,1),startPos=Point3(62,6,1))
go4 =  alien.hprInterval(2,Point3(0,10,0),startHpr=Point3(-90, 10, 0))
end_anim_lose = Sequence(go1,go2,go3)

go_for_kill = alien.posInterval(3,Point3(5,0,0),startPos=Point3(50,6,1))

class KeyHandler(DirectObject):
  
  def __init__(self):
    self.accept('arrow_left-repeat', self.lookLeft)
    self.accept('arrow_right-repeat', self.lookRight)
    self.accept('arrow_up-repeat', self.lookUp)
    self.accept('arrow_down-repeat', self.lookDown)
    self.accept('w-repeat', self.Moveforward)
    self.accept('s-repeat', self.Movebackward)
    self.accept('a-repeat', self.Moveleft)
    self.accept('d-repeat', self.Moveright)
    self.accept('q-repeat', self.MoveDown)
    self.accept('e-repeat', self.MoveUp)
    self.accept('space', self.Dotask)
  def lookLeft(self):
    global camxy
    camxy += 2
  def lookRight(self):
    global camxy
    camxy -= 2
  def lookUp(self):
    global camyz
    camyz += 2
  def lookDown(self):
    global camyz
    camyz -= 2

    
  def Moveforward(self):
    global camx
    if camx < 57 :
        camx += 1
  def Movebackward(self):
    global camx
    if camx > -32 :
        camx -= 1
        
  def Moveleft(self):
    global camy
    if camy < 42 :
        camy += 1
  def Moveright(self):
    global camy
    if camy > -36 :
        camy -= 1
  def MoveUp(self):
    global camz
    if camz < 15 :
        camz += 0.5
  def MoveDown(self):
    global camz
    if camz >1 :
        camz -= 0.5
  def Dotask(self) :
    global key_pos,my_score,bomb_planted,energy_found,camx,camy,camz,cap_found,key_found,door_close,end_good,level2,bomb_found,arrow_set,try1,cap_see
    my_score -= 5
    if (-3 < camx <15) and (-15 <camy < 1) and camz < 10 and not level2 and not cap_see :
        print 'gotme'
        cap_see = True
        sound4.play()
        my_score += 50
    
        
            
    elif (key_pos[0] - 4 < camx < key_pos[0] + 4) and (key_pos[1] - 4 <camy <key_pos[1] + 4) and  key_pos[2] - 4 <camz < key_pos[2] + 4 and cap_found and (not key_found) and not level2:
        print 'found'
        got.play()
        key_found = True
        arrow.setPos(-25,5,7)
        arrow.setHpr(0,0,90)
        arrow.loop('anim')
        key.setPos(100,100,100)
        my_score += 100
    elif (-27 > camx) and (1 <camy <10) and ( 7  <camz <= 12) and not door_close and not level2:
        if not cap_found or not key_found :
            print 'locked'
            wrong.play()
            my_score -= 20
            if cap_see :
                try1 = True
                
        elif key_found and cap_found :
            print "unlocked"
            arrow.setPos(100,100,100)
            arrow.setHpr(0,0,0)
            arrow.stop()
            door_close = True
            end_good = True
            key.setHpr(0,0,90)
            key.setPos(-36,5,8)
            my_score += 100
            checkpoint.play()
            
    if level2 :
        if (34 < camx < 43) and (-33 <camy <-22) and camz < 10.5 and not bomb_found:
            bomb.setPos(100,100,100)
            bomb_found = True
            arrow_set = True
            my_score += 500
            got.play()
            talk4.play()

        elif (-29 < camx < -21) and (-26 <camy <-15) and 13 < camz  and bomb_found and not energy_found:
            blast_can.setPos(100,100,100)
            energy_found = True
            my_score += 1000
            got.play()
        elif bomb_found and (-5 <camx < 5) and (-5 < camy < 5) and camz < 5 :
            bomb.setPos(0,0,0)
            my_score += 2000
        if energy_found and (-5 <camx < 5) and (-5 < camy < 5) and camz < 5 :
            
            Level2_music.setVolume(0.2)
            blast_can.setPos(1.5,0,0.5)
            blast_can.setHpr(90,0,90)
            energy_found = False
            bomb_found = False
            bomb_planted = True
            print 'planted'
            timer_bomb.play()
            talk2.play()
            my_score += 2000
            temp[0] = not temp[0]
            
            

        
            
        




a = KeyHandler()


taskMgr.add(set_cam, "setcamTask")
taskMgr.add(Move_seeker, "move Task")
run()
