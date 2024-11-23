from images import artimages
import time
from termcolor import colored
import pygame
from pygame import mixer

pygame.init()
mixer.init()

pygame.mixer.music.load('ST.mp3')
pygame.mixer.music.set_volume(0.05)
locationindex = ['village','town-hall','dock', 'ominous cave','market']
locationintros = {'village' : ['The streets are bare', 'An eery sensation washes over you', 'The village elder wanders looking for people'],
                'town-hall':['You see a jam-packed town hall','Filled to the brim with village-folk and outsiders alike',
                             'But in the corner you see a hooded man...'],
                'dock' : ['The smell of the sea hits you','You feel unnerved and yet, comfortable','An old man sits on the rickety planks'],
                'ominous cave' : ['The cave goes on, seemingly infinite','Unfurling from the pit of your stomach, a feeling','Dread'],
                'market': ['You can only see the remnants of a once bustling market','Now empty and desolate','A man with a rucksack scrounging around behind stalls hits your eye']}

flag1 = False
flag2 = False
flag3 = False
flag4 = False
flag5 = False
flag6 = False
flag7 = False
flag8 = False
flag9 = False

def artprint(type):
    for image in artimages:
        if type == image:
            print(artimages[type])

class Player:
    def __init__(self, name, currentlocation='void'):
        self.name = name
        self.currentlocation = currentlocation #Make sure location names are same as art print equivalent
        
        self.stage = 1

    def changelocation(self, newlocation):
        if self.currentlocation == newlocation:
            print(f"You are already at the {self.currentlocation}")
            pass
        self.currentlocation = newlocation
        artprint(self.currentlocation)
        print(f"You have have reached the {self.currentlocation}")
        for intros in locationintros[self.currentlocation]:
            print(intros)
        player.Action(player.stage)

    def Action(self, stage):
        while True:
            try:
                actiontype = int(input("What would you like to do?\n1)Travel\n2)Talk\n(Respond in either '1' or '2')\n"))
            except ValueError:
                print("Sorry, you must enter a number")
                continue
            if actiontype != 1 and actiontype != 2:
                print("Please respond in '1' or '2'")
                pass
            elif actiontype == 1:
                print("Where would you like to travel?")
                number = 1
                for location in locationindex:
                    print(f"{number}) {location}")
                    number+=1
                try:
                    answer = int(input("(Please respond with the corresponding number)\n"))
                except ValueError:
                    print("Sorry, you must enter a number")
                if answer == 4 and stage < 2:
                    print("Your body refuses to go there yet...")
                    pass
                elif answer == 4 and stage == 2:
                    endgame()
                    break
                else:
                    self.changelocation(locationindex[answer - 1])
                    break
            elif actiontype == 2:
                #approach npc from corresponding location
                current_npc_name = npcslist[self.currentlocation]
                current_npc_name.approach(current_npc_name.bond, current_npc_name.type)
                pass

class NPC:
    def __init__(self, name, location):
        self.name = name
        self.bond = 0
        self.type = 0
        self.location = location
        self.dialoguelists = {0:[], 1:[], 2:[]}
        self.repeatdials = {0:'', 1:'', 2:''}

    def approach(self, bond, type):
        artprint(self.name)
        if type == 0:
            dialogue(0, self.dialoguelists[bond], self.repeatdials[bond])
            type+=1
            self.type = type
        elif type == 1:
            dialogue(1, self.dialoguelists[bond], self.repeatdials[bond])
        bondcheck()
        
def bondcheck():
    
    global flag1 
    global flag2 
    global flag3 
    global flag4 
    global flag5 
    global flag6 
    global flag7 
    global flag8 
    global flag9 
    if occultist.bond == 0 and occultist.type == 1 and flag1 == False:
        merchant.bond = 1
        print("Merchant Bond increased to 1 ")
        merchant.bond = 1
        merchant.type = 0
        flag1 = True
    if merchant.bond == 1 and merchant.type == 1 and flag2 == False:
        elder.bond = 1 
        elder.type = 0
        print("Elder Bond increased to 1 ")
        flag2 = True          
    if elder.bond == 1 and elder.type == 1 and flag3 == False:
        dockworker.bond = 1 
        dockworker.type = 0
        flag3 = True
    if dockworker.bond == 1 and dockworker.type == 1 and flag4 == False:
        occultist.bond = 1
        occultist.type = 0
        flag4 = True
    if occultist.bond == 1 and occultist.type == 1 and flag5 == False:
        elder.bond = 2
        elder.type = 0
        merchant.bond = 2
        merchant.type = 0
        flag5 = True
    if elder.bond == 2 and merchant.bond == 2 and flag6 == False:
        if elder.type == 1 and merchant.type == 1:
            occultist.bond = 2
            occultist.type = 0
            flag6 = True
    if occultist.bond == 2 and occultist.type == 1 and flag7 == False:
        dockworker.bond = 2
        dockworker.type = 0
        flag7 = True
    if dockworker.bond == 2 and dockworker.type == 1 and flag8 == False:
        occultist.bond = 3
        occultist.type = 0
        merchant.bond = 3
        merchant.type = 0
        elder.bond = 3
        elder.type = 0
        flag8 = True
    if occultist.bond == 3 and merchant.bond == 3 and elder.bond == 3 and flag9 == False:
        if occultist.type == 1 and merchant.type == 1 and elder.type == 1:
            player.stage = 2
            flag9 = True


def dialogue(type, dialoguelist=[], repeatdial=''):
    if type == 0:
        for dialogue in dialoguelist:
            print(dialogue)
            time.sleep(2)
    elif type == 1:
        print(repeatdial)

def endgame():
    dialogue(0, Cave1)
    print(colored("AAAAAHHHHHHHHHHHHHHHHH",color='red'))
    time.sleep(2)
    dialogue(0, Cave2)
    artprint('monster')
    dialogue(0, Cave3)
    print(colored("It sees you",color='red'))
    time.sleep(2)
    dialogue(0,Fight1)
    choice(correct=3)
    dialogue(0,Fight2)
    choice(correct=2)
    dialogue(0,Fight3)
    print(colored("Daddy? My Daddy is waiting for me at home",'light_blue'))
    time.sleep(2)
    print(colored("It hurts sir...",'light_blue'))
    time.sleep(2)
    dialogue(0,Fight4)
    print(colored("IT HURTS DOESNT IT",'red'))
    time.sleep(2)
    dialogue(0,Fight5)
    choice(correct=4)
    dialogue(0,Fight6)
    print(colored("Please I-",'light_blue'))
    time.sleep(2)
    dialogue(0,Fight7)
    choice(correct=1)

def choice(correct):
    while True:
        time.sleep(2)
        for choice in choices:
            print(choice)
        try:
            option = int(input("What will you do?\n"))
        except ValueError:
            print("Sorry, you must enter a number")
            continue
        if option == correct:
            break
        else:
            print("No... thats not right...")

#Set up Monster
Cave1 = ['It keeps going','and going','and going...','Finally you seem to reach an opening','Its empty',
        'Why is it empty?','There are only rocks','Big rocks, thats it','Too big','You touch the Massive stone formation',
        'It seems almost... hollow','You scrape off a piece and']
Cave2 = ['The shriek startles you','You blink and by the time your eyes open']
Cave3 = ['What....is that', 'A massive almost shrine-like monument of flesh','You can even see... eyes','Human eyes',
         'Oh god, are those...','They were lured in here and they turned into THAT?','How many did this thing consume','...',
         'It needs to die']
choices = ["1) Use the Sword","2) Use the Powder", "3) Use the Torch", "4) Use the Potion"]

Fight1 = ['Tendrils of flesh come at you','Spiked and slimy, disgusting','They want to hurt you','You must protect yourself']
Fight2 = ['You ward off the tendrils','They burn from the intense heat of the torch and wince in pain','The monster shrieks in the voice of many',
          'Man, Woman, and Child, all were consumed by this abomination','This time you rush in','Dodging and weaving through a series of attacks',
          'You must get to the heart','You must go farther','But its stone-flesh shell is too strong','You need to get through']
Fight3 = ['You throw the powder at the shell','...','It does Nothing!','Why?!','Maybe it needs something more... a spark?',
          'You set the powder ablaze and','Lo and behold, It sizzles and cracks and burns through everything in your path', 'You walk into this... garden of flesh'
          'The crying and screaming is getting louder now','Its changed from shrieks to words','A voice reaches your ears','You see the face of a child ']
Fight4 = ['You had your guard down','A spiked tooth pierces your abdomen from behind']
Fight5 = ['Shamble past the now laughing child','As children cackle, you think-','I need to do something','I need to live']
Fight6 = ['You take drink the potion','It tastes like the most nefarious concoction of herbs and mushrooms','You almost puke','But it works',
          'You feel the energy surge in your body once more','You are at the heart','An unholy orb made of people','You hear yet another voice and yet another face']
Fight7 = ['Shut up','You stomp your heel into its face','Your deception works on me no longer','Hide behind the veil of innocent children',
          'Children that YOU killed','I will rid this world of you']
Conclusion = ['You stab into the orb','The shrieks stop','The monster is killed','Finally, the journey is concluded',
              'You have done well','You deserve a hard earned rest','You go back to the village','Tell the elder of the news',
              'The village people hail you as a hero','Not only you, they finally seem to accept the occultist as one of them',
              'The merchant smirks from a distance, forever notorious','And far off at the docks','it seems the dockworker and the fishermen seem to be getting close',
              'Thank you dear Knight','For you have saved the day once more']

#Set up NPCs
elder = NPC('elder', 'village')
elder.dialoguelists = {0:['Hey', 'You awake?', 'I\'m the village\'s elder', 'you have been asleep for a while, Sir Knight',
                          'Please help us', 'We are in dire need of a savior', 'Many of our village residents have disappeared',
                          'Some say its a demon or maybe bandits', 'But no one knows','....','Help us, please',
                          'It\'s gotten to a point where I moved every one to the Town-Hall',
                          'At least until we find out the cause of this', 'Go to the Town-Hall and ask around there, maybe you\'ll find something'],
                       1:['Hm?','You found young Peter the occultist I see','Are you sure he is to be trusted?','Regardless...','The dockworker eh?',
                          'Here take this','Henry\'ll know I sent you if you show him this.','...','What is it?','I think that\'s his story to tell'],
                       2:['...','My, creatures made of flesh...' ,'that truly is disturbing...','I know not about such things','But I can tell you about the disappearances',
                          'There\'s a somewhat secluded area near the sea where the fishermen and their families live','They fish and have their own food, they are a peaceful people',
                          'So us village folk and them have never had any issues, nor much exposure to each other','But it was about two score days ago when...',
                          'I heard banging on my door, and this wailing','It was one of the fishermen families standing outside','When I opened the door',
                          'It was a wife and husband, but neither was crying','I\'d heard it, without mistake','The father held his boy but it was\'nt his boy',
                          'The little boy died soon after','Talking about wanting to go somewhere or the other...'],
                       3:['The children went THERE of all places?','My god','The CAVE is stuff of legends','My grandfather told me to never step foot in the CAVE',
                          'That\'s how terrifying of a place it is','People joke around, saying they\'re not scared','But no one dares enter, even if it is a superstition',
                          'If you\'re going in there, use this powder','It will burn through anything organic','Be careful it smells disgusting, but it\'ll get the job done','Be safe...']}

elder.repeatdials = {0:'Go to the Town-Hall and ask around there, maybe you\'ll find something', 1: 'Ol\' Henry will believe you if you show him... that.',
                     2:'Those fishermen... I feel sorry for them..',3:'Use the powder... and maybe you\'ll survive'}

occultist = NPC('occultist', 'town-hall')
occultist.dialoguelists =  {0:['Please...','I\'ve done nothing wrong', '...', 'Huh?','You\'re not with... them?',
                              'Ah, my apologies','I have been pelted with stones and beat relentlessly','but since all this began...',
                              'it has gotten worse','I take an interest in the occult','and these times are not friendly to one such as myself',
                              'Say, you\'re a knight?','Well... though they have rained upon me much suffering','I do not wish for them to die',
                              'If you go to some affected places and investigate',
                              'Perhaps I can help you with a solution','The markets and the docks, were where it all started...'],
                            1:['What all do you know?','Flesh...','Missing Children...','This helps','But I need more','How are these two linked?',
                              'Try asking Michael the merchant and Joshua, our elder','They\'d be the most in the know of such things','If I just find out what it is, I can do something'],
                            2:['What did you find?','...','It seems this is some sort of transmissable disease', 'But something that causes frenzy and death...',
                              'Seems to me those children ate the \'infected\' fish','but where did they go...','This is all related to the fishing colony, the dockworker would know best'],
                            3:['...','Then it is as I feared','An ancient evil has nested itself in the CAVE','From the times of my great grandfather have children been told stories of it',
                               'To now finally, it awakening','I want to stop you, but I know I can\'t','Here, take this','It is a Shortsword, passed down 4 generations of my family',
                               'It is invaluable, but you go there to save us, you will need it']}       

occultist.repeatdials = {0:'Maybe investigate the markets and the docks',1:'We must find the link between the creatures and the missing kids',
                         2:'The missing children are the key to this \'disease\', go to the docks once more',3:'Use the sword, rend its flesh'}

dockworker = NPC('dockworker', 'dock')
dockworker.dialoguelists = {0:['Who are you?','I don\'t talk to newcomers', 'Go away'],
                            1:['I told you to go away you little-','That- Thats..','...','My girl made me that','She wanted to grow up to be a carpenter',
                               'The other girls she played with wanted to be princess','But not her','When disease took her from me','No one helped',
                               'Not one other than Joshua','If he sent ya here, we must really be in trouble','Whatd\'ya need?','...',
                               'Started about two score days ago','My nets started catching these awful looking things','Not fish, not plant, but... a sorta flesh amalgam'
                               'It was just a few at the start','Then it... didn\'t stop'],
                            2:['You\'re back?', 'What\'s this all about now?','...','oh','the kids','yeah, I saw.','It was a little after I started seeing those fish',
                               'I was laying my nets and I saw em', 'A group of children looking all dazed', 'I tried to warn em to stay off the east side as usual',
                               'But they acted like I wasn\'t there','Making these... sounds.. sounded like rattling, clicking','and while they left, I turned away',
                               'But just for a moment, I heard a shriek','I saw them go to..','I saw them go to the CAVE','Don\'t go there, but if you do... use fire',
                               'Take this torch, it\'s all I have']}
dockworker.repeatdials = {0:'...', 1:'That\'s all I know. Come back if you need',2:'Use the torch to keep danger away'}

merchant = NPC('merchant','market')
merchant.dialoguelists = {0:['IM NOT STEALING IM BORROWING','Oh you\'re not from the king\'s army','Great!','I was stealing',
                             'Well, carry on now','Just a little thievery going on here'],
                          1:['hum da dum....','AHA A LIFE LIKE STATUE OF A KNIGHT!','Wait no... that\'s just a knight...',
                             'Good work dashing my hopes and dreams sir knight','Go on, tell me what you want','...',
                             'Investigate? Hooded man? Monster?','What are you on about, it\'s all just hysteria',
                             'A few kids go missing and the whole town is up in arms about some \"Monster\"','Well if you insist on bothering me',
                             'I can tell you one thing','There are rumors that the monster is weak to...','milk','Ridiculous. It\'s as I told you',
                             'Hysteria','Go talk to the old dockworker, he knows about such things','but he don\'t talk to no one other than the elder'],
                          2:['What do you want now?!','Can\'t a man steal in peace!','...','Don\'t know nothing bout no weird fish','But if you give me 500 silver I\'ll tell you-',
                             'What do you mean you\'re poor??','Fine... being the Hero I am, I\'ll tell you with no charge', 'I overheard two of my customers talking',
                             'They said they saw a bunch of those fish people\'s kids acting all... frenzied','Right before they disappeared too', 'Seems to me they got some sorta water madness',
                             'That\'s all I know','Anyhow would you be interested in-','HEY DON\'T LEAVE IM TALKING HERE'],
                          3:['Heyyyy Sir knight!','What brings you here again?','Finally interested in buying something?','The CAVE...','You\'ll die','I\'m a merchant, I go where money goes',
                             'There were rumors of the CAVE having treasure','Everyone went in','No one came out','My friends','My father','That place is no joke','Many able bodied men went in',
                             'People who thought they were finally going to dispell the legend','Their families mourn still','Do you think you can do it?','...',
                             'Here, this potion is used to burn away wounds','I don\'t get wounds anymore so I have no need of it','Good luck']}
merchant.repeatdials = {0:'Oooh! This one will be at least two hundred!', 1: 'Do you think people would buy oil made of... snakes?',2:'hum da dum....',3:'Use the potion and... no freebies next time'}

progress = 0

npcslist = {'village': elder, 'town-hall': occultist, 'dock': dockworker, 'market':merchant}

#START GAME 

print("Please have your terminal set to fullscreen before you start")
time.sleep(5)
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

print("You are a Knight.")
time.sleep(2)
name = input("What is your name, noble knight?\n") 
name = name.capitalize()
player = Player(name, 'void')
time.sleep(2)
print(f"Hello Knight {player.name}")
time.sleep(2)
artprint('void')
print("You are in the nothingness of the void")
time.sleep(2)
while True:
    answer = input("Would you like to wake up?\n")
    if answer.lower() == 'yes' or answer.lower() == 'y': 
        break
    else:
        time.sleep(2)
pygame.mixer.music.play(-1)
elder.approach(elder.bond, elder.type)

player.changelocation('village')
#Reach Village
time.sleep(3)

dialogue(0, Conclusion)
print(f"Thank you {player.name}")
print(colored("THE END",'green'))







