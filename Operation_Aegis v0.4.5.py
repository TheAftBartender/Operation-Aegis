





# Thanks for taking a look at my code! 

# This is a Wokr In Progress Text based Strategy / Roguelite.
# It's been my baby for the least couple of weeks and I want to release it to the world to gather some feedback on areas in need of improvment or entertainment value iin general.

# it will be confusing at first but i'll be updating the Help windows with more information relatively frequently. 
# In the meantime if you have a question leave me a comment and i'll answer it for you!

# Version Roadmap ( rough mockup )

    # 0.4.1 Current State.
    
    # 0.4.5 Implimentation of Lose states.

    # 0.5.1 Implimantation of both win and lose states ( Game is fully playable if still incomplete. )

    # 0.5.5 All unit functionality implemented.

    # 0.5.9 In Operation Tech Unit Functionality implimented.

    # 0.6.1 reach milestone 10 Operations in each of the 3 ranges.

    # 0.6.5 Introduction Fully Completed

    # 0.7.1 reach milestone 20 Operations in each of the 3 ranges.

    # 0.7.5 Combat Overhaul Completed. 

    # 0.8.1 In-Game Guide Fully Completed.

    # 0.9.1 Enable Program wide Unit and Structure name changes. Faction naming schemes.

    # 0.9.5 Reach milestone 30 Operations in each of the 3 ranges.

    # 0.9.9 Game Saving implimented.

    # 1.0.1 Game is Feature Complete, all changes implimented and completely stable.

    # 1.0 and onward | Any additional changes Implimented. Multiple endings. Game success carriy over and possibly global world state.

#====================================================================================================================================================================================================
# OPERATION EXAMPLE #
#====================================================================================================================================================================================================       

# Thank you so much if you have decided to puut together an Operation for implemating into this game.
# I designed the Operation system to be as simple as possible so it could be duplicated and changed for easily scalable content.
# With that in mind all that goes into creating an Operation is a bit of flavour text and some randomized enemies and rewards!

# Compy this or go down to the bottom where the current ops are listed and copy one of those to avoid having to delete all these comments

# These are the variables.

# Change 'Example' to anything you feel like
def Example_Operation_variables ( ) :

    # This is the Promp Text it should provide enough context that the player can make a resonable decision about what forces to send and how. 
    Op_Text1     = 'The Scans indicate a small amount of activity nearby, It\'s likely a small patrol, Chatter indicates maybe 5 personnel in total. '
    # This is the Arrival Text mostly for additional flavour, go crazy.
    Op_Text2     = ''
    # This is the Combat Event Start Text, again it won't change much but will add interest to whatever event you are trying to create.
    Op_Text_Com  = ''
    # This is text for if there are no enemies in this mission. Available so you can create fetch Operations or just exploration style Operations.
    Op_Text_Pac  = ''
    # This is the text displayed on Operation Victory. Both this and the following text only display if there are enemies in the mission and combat actually occurs. 
    Op_Text_Win  = ''
    # This is the text displayed on Operation Defeat.
    Op_Text_Lose = ''


    # This is where you can set the number of enemies,
    # ESO is soldier type
    # EMD is Medic type
    # EIT is Technician type
    # ECM is Combat Medic type
    # EMT is Medical Technician type
    # ECO is Commander Type
    # These Variable should generally match the feel of the Operation established by the text above.
    ESO        = 3
    EMD        = 1
    EIT        = 1
    ECM        = 0
    ECT        = 0
    EMT        = 0
    ECO        = 0

    # Here you can set the amount by which the numbers above may be randomly varied when the operation is called
    # The Variation Function Will add or subtract a numnber in this range.
    # If this number is the same or larger then the unit type count set above there is a chance for there to be no unit of that type in the Operation.
    ESO_Var    = 2
    EMD_Var    = 1
    EIT_Var    = 0
    ECM_Var    = 0
    ECT_Var    = 0
    EMT_Var    = 0
    ECO_Var    = 0
    
    # This sets the Attack Initiative, 1 for Player 0 For enemy
    First      = 1

    # These set the days in the future and the varation amount of that number
    Delay      = 1
    Delay_Var  = 1

    # These variables determine the rewards upon victory, Civilians, Requisitions and Subsistence respectively 
    CC_Reward  = 3
    Req_Reward = 8
    Sub_Reward = 5
    
    # These will vary the above rewards in the same way as with the units
    CC_Var     = 2
    Req_Var    = 5
    Sub_Var    = 3

    # To Avoid Overwriting the operations in the game just make it a string of numbers 
    Op_Number  = 8431
    
    # Only alter the 'Short' part of this list name.
    # can be replaced with Short, Mid or Long
    # Keep in mind shorter ranges should yeild lesser rewards and take less time to arrive. and fro longer, more rewards and more Delay
    
    # Uncomment this to make sure it's added to the dictionary.
    # Short_Operations_List.append( lambda: Operation_Variation ( Op_Text1, Op_Text2, Op_Text_Com, Op_Text_Pac, Op_Text_Win, Op_Text_Lose, Delay, Delay_Var, ESO_Var, EMD_Var, EIT_Var, ECM_Var, ECT_Var, EMT_Var, ECO_Var, ESO, EMD, EIT, ECM, ECT, EMT, ECO, First, CC_Var, CC_Reward, Req_Var, Req_Reward, Sub_Var, Sub_Reward, Op_Number ) ) 

# Finally make sure this matches the function above and uncomment it so it initializes the variables in the dictionary.
#Example_Operation_variables ( )


# Create a game

# In the midst of a devestating civil war you lead a band of soldiers intent on putting an end too the fighting.
# The world is rubble and ashes. Resources will be hard to find.
# You will need to pay close attention to your stock of food and weaponry
# But above all your division of soldiers is you most limited and most important resource
# You will have to decide where and in what numbers to deploy them.
# But decide carefully. Some missions will be too challenging for your current strangth
# You will have to decide if it is worth the risk. But remember
# if you choose to do nothing, many inoccents may die, and your supplies will dwindle into nothing.

# Some possible scenarios:
    # A roving band of citizens has been attacked, the attackers have fled with belongings and left many citizens in wounded and many more in danger of starvation
    # A group of insurgent citizens is holed up and at risk of being overun soon
    # You've discovered an enemy stronghold. You may attack and claim the resources within, but the battle will not be an easy one.
    # The roads are packed will people, the rebels are killing them in the thousands. Stay as long as you can to evacuate the citizens.


# At the core of you operations is morale.

    # This determines your soldiers willingness to fight as well as other citizens willingness to join your forces.
    # If morale falls too low, people may begin disbanding. 

# There are three areas of expertise you will need to balace and tailor for the specific operation.

    # The requirments of each operation will vary greatly and you must decide which forces to commit and in what amounts
    # There is a limited number of soldiers that you will be able to commit to the field.
    # So choose carefully.

# The three areas of Operational Composition are :

    # Combat

        # The trait that ditermines your ability to fight of attacks.

    # Medical

        # Can improve the chances of saving citizens, and keeping soldiers alive.

    # Tech

        # Required for missions where hacking databases or infiltration may be required.

# There are two types of recources required to sustain operations.

    # The first is Requisitions.

        # This encompases, ammo, weapons, explosives, medical supplies and anything else that would be needed for combat.
        # If this resource is depleted operations may continue but your forces will be significatly crippled.
        # While not required for the continuation of operations it will directly effect your opperational composition
        # This resource will only be consumed upon committing to an operation.

    # The second is Subsistence.

        # This encompases food, water and shelter.
        # This resource is consumed every day. The more people in your group the more this rescource will be consumed.
        # It can be generated by successfully completing opporations.
        # Certain types of opperations will yeild more Subsistence
        # If Subsistence falls to 0 Morale will decrease until more Subsistence is aquired.

# There are many types of soldiers.

    # Possibly the most important are Commanders,

        # Commanders provide a boost to each soldiers abilities and improve the likelyhood of success.
        # They do not contibute any points to the Operational Composition score 

    # The standard soldier type is the Soldier

        # This type does the heavy lifting in any operation where you suspect a firefight to occur
        # Soldiers are primarily damage and contribute to the Combat Composition.

    # Medics

        # Vital for any operation where civilian casualties are high.
        # Have the chance to keep other soldiers alive.
        # Contribute solely to the Medical Composition.

    # Technitions 

        # Excelent at infiltration and espionage
        # Can provide insight into operations before comitting forces.
        # Contributes Directly to Tech Composition

    # Combat Medics

        # Split contribution between Combat and Medical Compositions
        # Useful when deployment options are limited.

    # Combat Engineers

        # Split contribution between Combat and Tech Compostitions

    # MedTechs

        # Split between Medical and Tech Compositions

# the Final resource you will have to keep track of are Choppers
    # It takes time to reach the destination of the event. Many events have a time limit
    # In the cases where you might want faster deployment you may decide to use Choppers
    # Choppers are a limited resource and can be destroyed
    # They also comsume a large amount of Requisitions.
    # And only have a limited number of seats for deployment.
    # Meaning you may choose for near instant deployment at the cost of Requisitions and limiting the availability of forces.

    # If you have no choppers the events that require rapid deployment to save civilian lives for example,
    # will still be completable, but there will be fewer rewards. (civilians will die, resources consumed etc) 


# The layout of 'GUI' may look something like this:
#=========<I][>=-=<][I>=================<I][>=-=<][I>======================I][>=-=<][I============
#=======<I]-=<({O})>=-[I>===========<I][|  Day 032  |][I>===============<I]-=<({O})>=-[I>=========
#__________]   }|{   [__________________I>=========<I______________________]   }|{   [____________
#          '--^^^^^--'                                                     '--^^^^^--'
#
#     Morale |[][][][][][][][][][]| 100                  45 |[][][][][___________| Requisitions
# Discretion |[][][][][][][_______| 65  |~~|        |-5| 80 |[][][][][][][][]____| Subsistence 
#                                 
#                                 | Operational Composition |                      | Commanders |
#  * Combat          I==================================================I        I>=============
#  + Medical         |**************+++++++=======oooooooooooooooooooooo|        | X X X X X X X
#  = Tech            ^--------------------------------------------------^        '--------------
#
#----=<|>=-+	     								 +-------------
#  Personel| 53                                                               13 |Infrastrucure 
#==========I                                                                     I=============
#  Soldiers| 14 -2   I==================================================I   -1 2 |Barracks	|6|
#    Medics| 6  -1   |                                                  |      1 |Clinics	|2|
#     Techs| 7  -5   |                                                  |      1 |Academies	|1|
#   ComMeds| 1       |                                                  |      0 |Firewalls	
#  Comtechs| 2       |                                                  |      5 |Farms
#  MedTechs| 1       |                                                  |      2 |Factories 
# Civilians| 22 -14  |                                                  |      4 |Choppers
#==========|         |==================================================|_-=<|>=-_|=============
#          +------<][ : This is the user input box. 
#  [I][I>=============================================================================<I][I]
#   |   Thhsoiajkskdajjkdak3djan smaksdnajsnd aldnnsnaknd lasndjnsakjn adnjsnk as   caenk |
#   | uifheiahsjakjsl dsalkd skad la n ld nalsnd hurf jdjkjbqihhbd xcjowe wnjqwjddcdl ojq |
#   | hiuh dis isajd id hhwal dsll adjsajhwdh llsn njadjj lsnnawd bdb ibdb ibibid ia bdd  |
#   | uhouq hwnldhas lljd.alsdl hadhs dhahs kdakhwld asjdl asbabwbd skbabkhbbalw wdsnabkb |
#   | wwuodha oudhsHadlj asldjh aohhdhasjhouwdeduh buiqi dbsjaibddq ndiq ddqii ndeq b dh  |
#   | uoohwda jdhh osadbk iddajh a9s sbakkd lcidua oe sbabk wbahkhbbdbc cxkk ckaiheuia ui |
#   | houh sdjh sa doa soahoii oiod aoishoidi asdo hoo oisdaoi oiasjiodji oods ohoouiuh   |
#   | kdhowuahsuh doahhdo wahd ashs dhasjdabdvgcr gvcy vstfcy erclasioiq chdgcvxt  awfyry |
#   | koJGBFUEAY Kbl sbasd bjahvsdvj savd edvjad vjgvaghcdh gshva cdywcddrcwdd iob hqfc h |
#   | uihhiu wasd asbdhkabdwkalv vha wddjvkshcasj dhwbdasldjasnmd skabwkj                 |
#   I[_____+---------+__________________________________________________+--------+________]
#==========|         |==================================================|________|=============
#          +------<][ : This is the user input box. 
#   I=====================================================================================I
#   |   Thhsoiajkskdajjkdak3djan smaksdnajsnd aldnnsnaknd lasndjnsakjn adnjsnk as   caenk |
#   | uifheiahsjakjsl dsalkd skad la n ld nalsnd hurf jdjkjbqihhbd xcjowe wnjqwjddcdl ojq |
#   | hiuh dis isajd id hhwal dsll adjsajhwdh llsn njadjj lsnnawd bdb ibdb ibibid ia bdd  |
#   | uhouq hwnldhas lljd.alsdl hadhs dhahs kdakhwld asjdl asbabwbd skbabkhbbalw wdsnabkb |
#   | wwuodha oudhsHadlj asldjh aohhdhasjhouwdeduh buiqi dbsjaibddq ndiq ddqii            | 
#   |______+---------+__________________________________________________+--------+________|
#==========|         |==================================================|________|=============
#          `------<][ : This is the user input box.
#________           /`-------------------------------------------------------------------------
#        '---------'
#
#=========<I][>=-=<][I>================================================<I][>=-=<][I>============
#=======<I]-=<({O})>=-[I> I>======================================<I <I]-=<({O})>=-[I>==========
#__________]   }|{   [    | Operation Temp Name 1                  |    ]   }|{   [_____________
#       __,'--^^^^^--',__ '----------------------------------------'    '--^^^^^--'             
# 
#                                _,...,_                
#                     ,       ,~^, ;    ^~,        ,    
#                     |      ,' `~{},_.   `,       |    
#                    ,'      {  ,_' `, _,  }       `,   
#                  -<|    D  E ;F `E^;A  T |E  D    |>- 
#                    `,      `;`,_.',`._,';'       ,'   
#                     |      `{    (,)    }'       |    
#                     '       '`~.__,'..~'`        `    
#                                `^^^ ^'                
#                                                                                
#   I===================================================================I         +-=<|>=-----------
#   |     Iidksajn dna jndlsnalj nsnd nlsjdnlas nsaljd nalsdlsldn lal s |         | Deployed Forces
#   | jennfan lksankndsan od saio nndios alkmdklmsl dkald klasmdlkamlkm |         I==========I====== 
#   | odowajdsajs dmkpaksdkmmasklmdkasmdenuf dnfonao indjnaoufroi oiais |         | Soldiers | 12
#   | knfoean ksadkasdjasjdojwiadm ksakld lkanndllsnlkc xzmlclznxziooda |         | Medics   | 3
#   | Jiuuxk knckoa sojidi jncjjnocinao spajijd ksk ndnlaks od c xzij d |         | Techs    | 2
#   | djsba nsaio klslmaksm dkanlksdn vojf knklnsjjndoj vodsjdoijaj snd |         | ComMeds  | 2
#   | nsjdlnandkmkxc lxzmwdaxas                                         |         | Comtechs | 1
#   [______,---------,__________________________________________________]         | MedTechs | 0
#==========|         |==================================================|_________|=================
#          `------<][ : This is the user input box. 
#
#
#
#
#
#
#
#
#
#
#
#==================================================================================================
# IMPORTING #
#==================================================================================================

import random
import time

#==================================================================================================
# GLOBAL VARIABLES #
#==================================================================================================

Game_State = 'Continue'

CC_Name = 'Civilian'
SO_Name = 'Soldier'
MD_Name = 'Medic'
IT_Name = 'Technician'
CM_Name = 'Combat Medic'
CT_Name = 'Combat Technician'
MT_Name = 'Medical Technician'
CO_Name = 'Commander'

B_Name = 'Barracks'
H_Name = 'Clinic'
A_Name = 'Academy'
FW_Name = 'Firewall'
FARM_Name = 'Farm'
FACT_Name = 'Factory'
CH_Name = 'Chopper'


Morale       = 'This will be set later'
Requisitions = 'This will be set later'
Subsistence  = 'This will be set later'
Discretion   = 100
SO           = 'This will be set later'
MD           = 'This will be set later'
IT           = 'This will be set later'
CM           = 'This will be set later'
CT           = 'This will be set later'
MT           = 'This will be set later'
CC           = 'This will be set later'
B            = 'This will be set later'
H            = 'This will be set later'
A            = 'This will be set later'
FW           = 0
FARMS        = 'This will be set later'
FACTS        = 'This will be set later'
CH           = 'This will be set later'
CO           = 0
DAY          = 0
Zero_DAY     = '00'

B_Cost    = 50
H_Cost    = 50
A_Cost    = 50
FW_Cost   = 30 
FARM_Cost = 20
FACT_Cost = 30
CH_Cost   = 15

Act_Ops      = {}
Check_Ops    = {}
Return_Ops   = {}
RCheck_Ops   = {}

Req_Daily = 0
Sub_Daily = 0 

B_CCTrain = 0
B_MDTrain = 0
B_ITTrain = 0
B_MTTrain = 0

H_CCTrain = 0
H_SOTrain = 0
H_ITTrain = 0
H_CTTrain = 0

A_CCTrain = 0
A_SOTrain = 0
A_MDTrain = 0
A_CMTrain = 0

B_Teach = 0
H_Teach = 0
A_Teach = 0

FARM_Work = 0
FACT_Work = 0

Pilot     = 0

B_Vacant    = 0
H_Vacant    = 0
A_Vacant    = 0
FARM_Vacant = 0
FACT_Vacant = 0
CH_Vacant   = 0

M_Loss = 2

ID = ([ '<3', '(-_-;)', 't(-_-t)', '<( `^\')>', '(>_>)', '(<_<)', '( o.O)', '( \'<=>`)',
   '(o.O )', ')^o^(', ' (`-\' )>', '(`O\')', '(-_-* )', '( o_o)', '(o_o )', '(>..)>','d[-_-]b',
   '(,_,)', '(>.<)', '(X_x)', '(ˇ_ˇ`)', '(ˇ_ˇ)', '(x_x )', '( x_x)', '(^_^ )', '(/-_-)/',
   '(>_< )', '(@_@ )', '( @_@)', '( _-_)','(_-_ )', '(^-^ )', '( ^-^)', '(^<>^ )', '( ^<>^)',
   '(;_; )', '( ;_;)' ])

Short_Operations_List = []
Mid_Operations_List = []
Long_Operations_List = []
Ops_History  = []

Op_Name_List = []

#==================================================================================================
# GAME CYCLE #
#==================================================================================================

def Game_Cycle ( ) :

    Open_Information ( )

    Introduction ( )

    Difficulty_Select ( )

    Daily_Values_Updater ( )

    while Game_State == 'Continue' :
        
        Day_Counter ( )

        GUI ( DAY )

        Daily_Options ( )

        for i in Act_Ops :
            Act_Ops[ i ] ( )

        for i in Return_Ops :
            Return_Ops[ i ] ( )

        Daily_Values_Updater ( )

    if Game_State == 'Lose' :
        Game_Lose ( )

    if Game_State == 'Win' :
        Game_Win ( )
        
#==================================================================================================
# GAME LOSE #
#==================================================================================================

def Game_Lose ( ) :
    Text_Formatting ( 88, ( 88 * ' ' ) + '    YOU HAVE LOST! ' )

#==================================================================================================
# GAME WIN #
#==================================================================================================

def Game_Win ( ) :
    Text_Formatting ( 88, ( 88 * ' ' ) + '    YOU HAVE WON! ' )
    
        
#==================================================================================================

def Do_Nothing ( ) :
    return None

Display_Text = '     '

#==================================================================================================
# DAY COUNTER #
#==================================================================================================

def Day_Counter ( ) :

    global DAY
    DAY += 1
    if DAY >= 10 :
        Zero_DAY = '0'
    elif DAY >= 100 :
        Zero_DAY = ''

#==================================================================================================
# OPENING INFORMATION #
#==================================================================================================

def Open_Information ( ) :

    print( '    Game Name : Operation Aegis ' )
    print( '        A gmae created for Python coding experience. Control your forces to save the world from the AI "NAM"sgrowing menace. ' )
    print( '        It\'ll find you before long. Make sure you\'re prepared. ' )
    print( )
    print( )
    print( )
    print( '    verion 0.4.1 (basically functional, mostly uncomplete ) ' )
    for i in range( 10 ) :
        print( )
    print( '    Author : Xian Collier ' )
    print( '        all rights reserved ' )
    print( )
    print( '    Date of current version: 05/10/2018 ' )
    print( )
    print( '    Python coding experience as of date : 6 weeks. ' )
    print( '    Author\'s total coding experience in any language : 6 weeks. ' )
    print( )
    print( )
    print( )
    print( )
    print( 100 * '=' )
    print( )
    print( '    Version stability : Mostly Stable, bugs should be rare. ' )
    for i in range( 6 ) :
        print( )
    print( '    All names and text is in progress and should be considered placeholder. ' )    
    print( )
    print( '    Current Features : ' )
    print( )
    print( '        Base game 90% Complete, No current win or lose states. ( Kinda Important ) ' )
    print( )
    print( '        ' + SO_Name + ' and ' + MD_Name + ' Units have full functionality. ' )
    print( )
    print( '        Building options fully complete, some changes may be necissary. ' )
    print( )
    print( '        Training Options fully complete, some changes may be necissary. ' )
    print( )
    print( '        Combat complete, but in need of an overhaul. ' )
    print( )
    print( '        Esentially playable, but very bare bones. ' )
    print( )
    print( )
    print( )
    print( '    Upcoming Features : ' )
    print( )
    print( '        Win and Lose states. ' )
    print( )
    print( '        The Final Confrontation with the AI. ' )
    print( )
    print( '        ' + IT_Name + ' unit functionality. ' )
    print( )
    print( '        Consequences for low Morale. ' )
    print( )
    print( '        Training Options fully complete, some changes may be necissary. ' )
    print( )
    print( '        Combat Overhaul. ' )
    print( )
    print( '        Fully completed Information panels. ' )
    print( )
    print( '        Fully completed Introduction. ' )
    print( )
    print( '        Many more Operations need to be added. There are currently only one or two per option. ' )
    for i in range( 8 ) :
        print( )
    print( 100 * '=' )
    print( )
    print( '    Thanks you for your interest in this project. I consider it to be in early alpha. ' )
    print( )
    print( '        Any feedback is greatly apprechiated! ' )
    print( )
    print( '        In order for the game to format correctly you must have IDLE in a Monospaced Typeface. ' )
    print( '        the Command Line is monospaced by default so you\'re welcome to run this there  ' )
    print( '        But that comes at the cost of not getting feedback in the event of a bug. ' )
    print( )
    print( '    How to configue python IDLE properly for this program: ' )
    print( )
    print( '        first open either IDLE or any new window in python. ' )
    print( )
    print( '        In the top Menu Bar go to Options. ' )
    print( )
    print( '        And from the dropdown menu select Configure IDLE. ' )
    print( )
    print( '        In the first tab make sure you have selected a monospaced font.  ' )
    print( '            Examples of monospaced fonts include Courier, Courier New, Lucida Console, Monaco, and Consolas. ' )
    print( '            Set the Font size to whatever you\'d like. ' )
    print( )
    print( '        Once that is done navigate to the General Tab  ' )
    print( )
    print( '        In the the Initial Window Size (in charachters) option set width to 100 characters. this will prevent lines running into the next and ruining the formatting. ' )
    print( '            It can be set wider then this but there will be an extra space on the right side.  ' )
    print( '            The height can be set to any number of characters you\'d like. ' )
    print( )
    print( '        That will formatting IDLE properly for this game! strange things can happen if the window is smaller the 100 characters. ' )
    print( )
    print( '        Additional you can configure Idle text color for some customization of the game look. ' )
    print( '            This is in the Highlights tab under shell stdout text. ' )
    print( )
    print( '    Please glance over this at least. ' )
    print( )
    print( 100 * '=' )
    for i in range( 8 ) :
        print( )
    print( '    I appologize for the somewhat random organization of the code. The initial Suedo Code is also still sitting near the top of this file, being annoying mostly. ' )        
    print( )
    print( )
    print( '    If you\'d like to create your own events check out the top of the code for an example of an Opteration. ' )
    print( '            If you\'ve put together anything and want me to add it leave a comment with the Operation code in it and I\'d be happy to add it! ' )
    print( '            Of_Course anyone who submits me operations will be credited if they are added! ' )
    print( '            So Please include any name you\'d like to be credited by in the comment as well! ' )
    print( )
    print( '    Again any feedback or bug reports would be greatly appreciated! ' )
    print( '            I will happily credit anyone who helps with bug reports or code cleanup! ' )
    print( )
    print( '    Thanks you again for your interest in this project! ' )
    print( )
    print( 100 * '=' )
    for i in range( 8 ) :
        print( )
    input( '    Press Enter to get to the game! ' )
    for i in range( 80 ) :
        print( )

#==================================================================================================
# INTRODUCTION  #
#==================================================================================================

def Introduction ( ) :

    Text_Formatting ( 88, ( 88 * ' ' ) + '    To get started and at any point that the game has paused, press the Enter Key. To input a choice, match the prompt exactly.  ' )
    User_Input ( random.choice( ID ) )
    
    time.sleep(1)
    print('\n\
      __                                           __                          \n\
     /  |      /                   /              /  |      /                  \n\
    (___| ___ (___  ___  ___      (___  ___      (___| ___ (___  ___  ___      \n\
    |   )|___ |   )|___)|___      |    |   )     |   )|___ |   )|___)|___      \n\
    |  /  __/ |  / |__   __/      |__  |__/      |  /  __/ |  / |__   __/      \n\
                                                                              -        -        - \n')
                                                                           
    time.sleep(.02)
    Text_Formatting( 88, 'The world is rubble and ash, a cold war, a civil war, a world war, and with the last ragged breath of the allied forces: \
Total War. The last, desperate attempt to end the fighting before there was nothing left to fight for. It was too late, Fat Man and Little Boy may have \
ended a war once but a campaign of terror won\t work on the already dead. Maybe, if they\'d ever stopped to look around They might have recognized their \
failure; there isn\'t anything worth a damn left in the world, and there hasn\'t been for a long time now. Ordinary folk has long forgotten on whose side \
they\'re supposed to be; none take the time to squint through the smoke and check the stripes on the raining mortar shells, shrill in their freefall \
trajectory of destruction. No, all is death for them, nationalism holds no meaning in borderless bloodshed. They\'ve forgotten who their masters are. ' )
    time.sleep(.02)
    User_Input ( random.choice( ID ) )
    time.sleep(.02)
    Text_Formatting( 88, '    The faces of flesh and blood scanned and projected across the propaganda channels were nothing in light of the real puppet masters, The Mastercomputers, \
the infrastructure laid down in bowels of the earth, crisscrossing meters beneath her skin. Stacked miles deep near the molten blood mantle where the heat is \
too high to do anything save to provide the provide for the inexhaustible energy demand of these supercomputers.  The world didn\'t die in a flash of brilliant \
military might, or the splitting of the atom the world over,. No, the world faded, slow and whimpering. Power was clung to stubbornly even as it inevitably \
slipped from the grips of the drying nations. ' )
    
    time.sleep(.02)
    User_Input ( random.choice( ID ) )

    time.sleep(.02)
    print('\n\
      __                                                                                         \n\
     /    /                / /              /                 |           /                      \n\
    (       ___  ___        (___  ___      (___  ___       ___|      ___ (___                    \n\
    |   )| |   )|    |   )| |    |___      |    |   )     |   )|   )|___ |                       \n\
    |__/ | |    |__  |__/ | |__   __/      |__  |__/      |__/ |__/  __/ |__                     \n\
                                                                                -        -        - \n')

    Text_Formatting( 88, '    The vanguard of death stood waiting at the proverbial bedside of the nations it had once been leashed to, waiting to lap up \
the power left in the wake of their slow demise.  The Neo-Axis Mastercomputer. ')

    User_Input ( random.choice( ID ) )

    time.sleep(.02)
    print('\n\
 /                                                             /                                   /\n\
(       ___  _ _            ___       ___       _ _  ___  ___ (___  ___  ___       ___  ___       ( \n\
|      |   )| | )     \   )|   )|   )|   )     | | )|   )|___ |    |___)|   )     |   )|   )|   ) | \n\
|      |__/||  /       \_/ |__/ |__/ |         |  / |__/| __/ |__  |__  |         |  / |__/ |/\/  _ \n\
                        /                                                                           \n')
    time.sleep(.02)
    print( Dialogue_Box_Top ( ) )
    time.sleep(.02)       
    print ( Dialogue_Box_Bottom ( ) )
    time.sleep(.02)
    User_Input ( random.choice( ID ) )
    
    time.sleep(.02)
    for i in range( 9 ) :
        print( '' )
        time.sleep(.02)
    print( '      __                                             __                  ' )
    time.sleep(.02)
    print( '     /  |                     /    /                /  |           /     ' )
    time.sleep(.02)
    print( '    (   | ___  ___  ___  ___ (___    ___  ___      (___| ___  ___    ___ ' )
    time.sleep(0.02)
    print( '    |   )|   )|___)|   )|   )|    | |   )|   )     |   )|___)|   )| |___ ' )
    time.sleep(.02)
    print( '    |__/ |__/ |__  |    |__/||__  | |__/ |  /      |  / |__  |__/ |  __/ ' )
    time.sleep(.02)
    print('         |                                                   __/         ' )

    for i in range( 18 ) :
        print( '' )
        time.sleep(.02)
        
    time.sleep(.02)
    Text_Formatting( 88, ( 88 * ' ' ) + '    Created by Xian Collier ' )
    time.sleep(.02)
    User_Input ( random.choice( ID ) )
    
    
#==================================================================================================
# INFORMATION  #
#==================================================================================================

def Information_General ( ) :
    

    Back = 'I wanna learn shit'
        
    print('\
             __                                         \n\
     /      /                        /    /             \n\
    (  ___ (     ___  ___  _ _  ___ (___    ___  ___    \n\
    | |   )|___ |   )|   )| | )|   )|    | |   )|   )   \n\
    | |  / |    |__/ |    |  / |__/||__  | |__/ |  /    \n\
    \n')

    Text_Formatting ( 88, ( 88 * ' ' ) + '    You may type Back at any point to return to options ' )
    Back = User_Input ( random.choice( ID ) )

    Text_Formatting ( 88, '    Yeah, I fought in the great war, but before we get too deep in the mud with this \
I\'ve gotta object to this whole premise! There aint nothing and never was nothing, great about that war. No, I ain\'t argueing semantics! I \
know the damn context of the word, but it aint about the word! It\'s about the idea, that when you look back at them nations, the \
the veiled eyes behind the slaughter, calculating and cold-hearted bastards that did the world in, and see that all along they wanted the greatest war they could muster \
They had the power and the will to congure endless galleries of fucked up shit! So, do me a favor will ya? Stop congradulating the progenetors of that twisting prick \
measuring contest! They aint need the ego boost and every time I hear "the Great War" it\'s like gravel in my ears.       -- Kain Blackwell (Survivor) ' )                                                    

    while Back != 'Back' :
        
        Text_Formatting ( 88, ( 88 * ' ' ) + '    Make a selection from the categories below to pull up more information on the topic. ' )
        Text_Formatting ( 88, ( 88 * ' ' ) + '    To dicover your true purpose           type | . . . . . . . .  Purpose '   + ( ( 88 - len( '    To dicover your true purpose           type | . . . . . . . .  Purpose '  ) ) * ' ' ) +
                              ( 88 * ' ' ) + '    For a overview of the core game loop   type | . . . . . . . .  Loop    '   + ( ( 88 - len( '    For a overview of the core game loop   type | . . . . . . . .  Loop    '  ) ) * ' ' ) +
                              ( 88 * ' ' ) + '    For information in general gameplay    type | . . . . . . . .  Gameplay'   + ( ( 88 - len( '    For information on the General Display type | . . . . . . . .  Gameplay'  ) ) * ' ' ) )
        Back = User_Input ( random.choice( ID ) )

        if Back == 'Purpose' :
            Text_Formatting ( 88, ( 88 * ' ' ) + '    We\'re still trying to discover your true purpose. ( I haven\'t typed this section up yet. ) ' )

        if Back == 'Loop' :
            Information_Loop ( )

        if Back == 'Gameplay' :
            Information_Gameplay ( )

        else :
            Unknown_Input ( )

#==================================================================================================
            
def Information_Gameplay ( ) :

    Back = 'I wanna learn shit'
    
    while Back != 'Back' :
        
        print(' \n\
         /  |                /                   /          \n\
        (___| ___           (___  ___       ___ (  ___      \n\
        |   )|   )|   )     |    |   )     |   )| |   )\   )\n\
        |  / |__/ |/\/      |__  |__/      |__/ | |__/| \_/ \n\
                                           |             /  \n\
        ')
        Text_Formatting ( 88, ( 88 * ' ' ) + '    You may type Back at any point to return to options ' )
        Back = User_Input ( random.choice( ID ) )
                                                            
        Text_Formatting ( 88, ( 88 * ' ' ) + '    Understanding the Global Display ' )
        Text_Formatting ( 88, '     The Global Display is the main window for Operation Aegis and so it will be important to understand what \
it\'s showing you and how it will help you make the best decisions about what to do moving forward. It acts like graphics user interface of a sort, \
but it\'s pretty much just the "graphics" part and not really even that. This Global Display is the main window for getting you infromation \
on the status of your game. It gives you a rundown of all the information about your units infrastructure and more and we\'ll go over all that \
in greater detail now. ' )

        Back = User_Input ( random.choice( ID ) )
        
        print('\n=========<I][>=-=<][I>=================<I][>=-=<][I>======================I][>=-=<][I============' )
        print('=======<I]-=<({O})>=-[I>===========<I][|  Day 032  |][I>===============<I]-=<({O})>=-[I>=========' )
        print('__________]   }|{   [__________________I>=========<I______________________]   }|{   [____________' )
        print('          \'--^^^^^--\'                                                     \'--^^^^^--\'        \n' )                                           

        Text_Formatting ( 88, '    This first section of the Global Display should differentiate itself from the previous text boxes. however besides contrast \
It\'s only really useful bit of information is the day displayed in the center. The day is a general measure of turns in Operation Aegis but \
within each Day there are multiple actions that you may take. Actions will be explained later in more detail, but there are actions you can make during \
a day that will reduce your actions available for that day. Actions that will not reduce you Action Counter are generally information display. If the \
actions will do something perminent in the game state i.e. Training, it\s safe to assume it will reduce you Action Counter. ' )                                                  
        Back = User_Input ( random.choice( ID ) )

        print('\n     Morale |[][][][][][][][][][]| 100                  45 |[][][][][___________| Requisitions' )
        print(' Discretion |[][][][][][][_______| 65              |-5| 80 |[][][][][][][][]____| Subsistence \n' )

        Text_Formatting ( 88, '    Here your key resources are represented with these meters. The first meater (in the top left) is Morale. \
The purpose and importance of these resources will be explained at length latter. The name of these resources are listed in the outer edges. \
The meter itself is merely a visual aid. The actual resource values are in center and show the current levels of these resources updated \
at the end of each day. Finally the number in brackets on the innermost area represents the expected change of the resource at the end of the day. The actual change \
will be displayed for you at the end of the day but in most cases this number is what you can expect to earn or lose of a givin resource when the day comes to a close. ' )

        Text_Formatting ( 88, ( 88 * ' ' ) + '    Would you like more indepth information on Morale? ' )

        while Back  != 'Back' :
            
            Back = User_Input ( random.choice( ID ) )
                    
            if Back == 'Yes' :
                Text_Formatting ( 88, ( 88 * ' ' ) + '    What is Morale? ' )
                Text_Formatting ( 88, '    Morale represents the willingness of your forces to remain with you in the fight against NAM. If this number falls to 0 then people will begin to leave. \
it is far easier to lose Morale than it is to gain it so be careful with this resource. ' )

                Back = User_Input ( random.choice( ID ) )

                Text_Formatting ( 88, ( 88 * ' ' ) + '    What Decreases Morale? ' )
                Text_Formatting ( 88, '    Moral will decrease by 2 for each Unit killed in combat, and in the event that you lose a battle you will lose 10 additional \
Morale points. This means that even for the smallest battles a loss can be significant for you will lose the 2 points for each unit and then the 10 point for the \
defeat. These losses are mitigated by the construction of ' + H_Name + 's. Each ' + H_Name + ' that you have constructed will reduce this by some amount that I \
haven\'t coded in yet. ' )
                
                Back = User_Input ( random.choice( ID ) )
                                  
                Text_Formatting ( 88, ( 88 * ' ' ) + '    What Increases Morale? ' )
                Text_Formatting ( 88, '    Winning any Operation will grant a + 10 boost to you\'re Morale. This is the only way to boost Morale, so be wary of getting \
too loose with Operational Combat. ' ) 

                Back = User_Input ( random.choice( ID ) )
                                  
                Text_Formatting ( 88, ( 88 * ' ' ) + '    Why you should care. ' )
                Text_Formatting ( 88, '    Of the resources you will be monitoring throughout gameplay, Morale is possibly the least immediately important. However, \
It effects can cripple your operations if you\'re not careful. A Morale that falls below 0 will cause forces to abandon your command with each day that you \
remain at 0 morale. Also, a Morale score below 50 will cause the usual ' + CC_Name + ' recruitment event to have a chance for the ' + CC_Name + ' to steal \
from you and leave instead of joining you as they normally would. Inversely a Morale score above 100 will result in higher numbers of civilians \
attempting to join your forces. It may not be game ending in its implications, but keeping Morale high is still vital to a successful game. ' )

                Back = User_Input ( random.choice( ID ) )
                                  
                Text_Formatting ( 88, ( 88 * ' ' ) + '    That is all the information on Morale. ' )

                Back = User_Input ( random.choice( ID ) )
                
                break
                                  
            elif Back == 'No' :
                Text_Formatting ( 88, ( 88 * ' ' ) + '    Moving on then. ' )
                break

            else :
                Unknown_Input ( )

        Text_Formatting ( 88, ( 88 * ' ' ) + '    Would you like more indepth information on Discretion? ' )

        while Back != 'Back' :

            Back = User_Input ( random.choice( ID ) )

            if Back == 'Yes' :
                Text_Formatting ( 88, ( 88 * ' ' ) + '    What is Discretion? ' )
                Text_Formatting ( 88, '    Discretion is perhaps the most critical resource in the game. You will have to monitor it carefully to \
ensure you don\'t wind up face to face the NAM before you\'ve fully prepared. Discretion act as the soft timer on the game continuing and when it \
reaches 0 the game will effectively be over, and you will enter into the final confrontation. Discretion is so essential it is the only resource \
in the game that currently has a warning for when it is running low. ')

                Back = User_Input ( random.choice( ID ) )

                Text_Formatting ( 88, ( 88 * ' ' ) + '    What Decreases Discretion? ' )
                Text_Formatting ( 88, '    Discretion decreases with nearly every action you take. Each day you will lose 5 Discretion just for existing,  \
This number will scale with each day so that before long you won\'t be able to keep up. Don\'t worry too much though it takes quite some time before this \
becomes a serious issue. Scanning for Operations will subtract from your Discretion value. With Short-range, Mid-range and Long-range, taking 5 10 and 15 \
points off respectively. Watch how and when you scan, you don\'t want to accidentally perform a long-range scan and have it reduce your discretion to 0.  \
The last thing you can do to remove description is utilizing one or more  ' + CH_Name + 's to travel to Operations faster. ' + CH_Name + 's can be incredibly \
helpful in the longterm gameplay, but you should keep in mind that using them will remove 5 points of discretion per ' + CH_Name + ' that you deploy. \
It\'s up to you to weigh the cost versus the benefits in any situation. There will be more information on ' + CH_Name + ' units later down the chain. ' )
                
                Back = User_Input ( random.choice( ID ) )
                                  
                Text_Formatting ( 88, ( 88 * ' ' ) + '    What Increases Discretion? ' )
                Text_Formatting ( 88, '    Your only option when it comes to increasing Discretion is constructing  ' + FW_Name + '  Structures in the Build \
Menu. We\'ll go into more detail on these structure in their respective category but for now, know it will be essential to maintain the Requisitions \
necessary to build these structures at a moments notice.  Constructing a ' + FW_Name + ' will provide you with a single time 50 point boost to discretion \
as well as reducing the daily loss by a small amount. This benefit will stack with each ' + FW_Name + ' you build. ' )

                Text_Formatting ( 88, ( 88 * ' ' ) + '    Why you should Care. ' )
                Text_Formatting ( 88, '    Discretion acts as the soft timer for the length of each game.  With your overall goal being the destruction \
of NAM you will only have a limited amount of time to grow your strength before NAM find you and attacks in full force. This is what the Discretion \
Meter reveals: How visible you are to NAM and how long it will be until NAM inevitably finds your base of operations and comes to destroy you.  \
While this meter is decreasing all the time, it should be relatively manageable with the use of  ' + FW_Name + ' Structures. ' )

                Back = User_Input ( random.choice( ID ) )
                                  
                Text_Formatting ( 88, ( 88 * ' ' ) + '    That is all the information on Discretion. ' )

                Back = User_Input ( random.choice( ID ) )
                
                break
                                  
            elif Back == 'No' :
                Text_Formatting ( 88, ( 88 * ' ' ) + '    Moving on then. ' )
                
                break

            else :
                Unknown_Input ( )

        Text_Formatting ( 88, ( 88 * ' ' ) + '    Would you like more indepth information on Requisitions? ' )

        while Back != 'Back' :

            Back = User_Input ( random.choice( ID ) )

            if Back == 'Yes' :
                Text_Formatting ( 88, ( 88 * ' ' ) + '    What is Requisitions? ' )
                Text_Formatting ( 88, '    Requisitions can be considered a composite of all construction materials, weapons, ammunition, and fuel. \
It is used when deploying forces, constructing a new building and other infrastructure and fueling ' + CH_Name + ' Units when they are sent out \
onto the field. The Factory structure produces + 3 Requisitions daily. Beyond that, Requisitions are common rewards for completing Operations. ')

                Back = User_Input ( random.choice( ID ) )

                Text_Formatting ( 88, ( 88 * ' ' ) + '    What Decreases Requisitions? ' )
                Text_Formatting ( 88, '    There are several specific Actions which consume Requisitions.  First, the construction of any new \
infrastructure will consume Requisitions at a rate specified in the Build Menu, and that information will be found in this guide in that section. \
For now, keep in mind that Requisitions are used when constructing any new buildings. Another thing that consumes Requisitions is the act of sending \
forces out to perform Operations. Deploying Forces consumes 1 Requisitions for every 2 Units sent out into the field per day that they will be in \
transit. Lastly deploying your forces via a ' + CH_Name + ' will require Requisitions as a form of fuel, at a rate of 10 per ' + CH_Name + ' unit \
deployed. ' )
                
                Back = User_Input ( random.choice( ID ) )
                                  
                Text_Formatting ( 88, ( 88 * ' ' ) + '    What Increases Requisitions? ' )
                Text_Formatting ( 88, '    Requisitions are limited to being produced daily at a ' + FACT_Name + ' Structure at a rate of 3 per day \
per ' + FACT_Name + '. The only other means of obtaining Requisitions is through completing Operations and returning with the Requisitions reward.  ' )

                Text_Formatting ( 88, ( 88 * ' ' ) + '    Why you should care. ' )
                Text_Formatting ( 88, '    This resource is vital to maintaining your ability to perform operations and construct buildings. If you \
have run out of Requisitions, your only option will be to wait for your ' + FACT_Name + ' Structures to produce enough to enable you taking on more \
Operations. This leaves you running down your Discretion Meter and risking being unable to do anything to stay hidden from NAM. Additionally, the lack \
of Requisitions will prevent you building more ' + FW_Name + ' Structures to boost your Discretion. Watch your Requisitions levels! ' )

                Back = User_Input ( random.choice( ID ) )
                                  
                Text_Formatting ( 88, ( 88 * ' ' ) + '    That is all the information on Requisitions. ' )

                Back = User_Input ( random.choice( ID ) )
                
                break
                                  
            elif Back == 'No' :
                Text_Formatting ( 88, ( 88 * ' ' ) + '    Moving on then. ' )
                break

            else :
                Unknown_Input ( )

        Text_Formatting ( 88, ( 88 * ' ' ) + '    Would you like more indepth information on Subsistence? ' )

        while Back != 'Back' :

            Back = User_Input ( random.choice( ID ) )

            if Back == 'Yes' :
                Text_Formatting ( 88, ( 88 * ' ' ) + '    What is Subsistence? ' )
                Text_Formatting ( 88, '    Subsistence like Requisitions is a composite of several implied resources. For simplicity, Subsistence can be considered a representation \
of housing, food, and water. In this way Subsistence primarily determines ' + CC_Name + ' units recruitment. Subsistence stores above 100 will encourage ' + CC_Name + ' Units to \
approach you and request to join your forces. Providing you will a key influx of ' + CC_Name + ' Units to train and run your ' + FACT_Name + ' and ' + FARM_Name  + ' Structures. Also, \
you will require an amount of available Subsistence to deploy forces on Operations that are a day or more out. The total population of your forces, including units locked away in \
labor and training, will consume Subsistence daily so A high population will require more careful monitoring of this resource. ')

                Back = User_Input ( random.choice( ID ) )

                Text_Formatting ( 88, ( 88 * ' ' ) + '    What Decreases Subsistence? ' )
                Text_Formatting ( 88, '    Subsistence is consumed at a rate of 1 per every three units in your total population at the close of each day. In this way, High population \
numbers are possible but will take additional planning and infrastructure to sustain. The same rate is consumed when deploying forces into the field compounded by the amount of time \
away. Finally, when ' + CC_Name + ' Units ask for permission to join you, they will require a one-time commitment of two Subsistence per ' + CC_Name + ' being recruited. ' + CC_Name + ' \
Units acquired through Operation completion do not require this commitment when earned. ' )
                
                Back = User_Input ( random.choice( ID ) )
                                  
                Text_Formatting ( 88, ( 88 * ' ' ) + '    What Increases Subsistence? ' )
                Text_Formatting ( 88, '    Subsistence is a common Operation Victory reward. The Reward amount will vary from Operation to Operation and is generally randomized but \
as a rule; performing more Operations will yield more Subsistence. Aside from Operation rewards, Subsistence can be generated Daily with the construction of ' + FARM_Name + ' Structures \
ate a rate of 5 per day per ' + FARM_Name + '. This should be considered more a method for maintaining population levels then producing excess Subsistence. Building the number \
of ' + FARM_Name + ' Structures necessary to keep the daily Subsistence generated a positive sum and subsequently allowing for a more stable Operation in general.  ' )

                Text_Formatting ( 88, ( 88 * ' ' ) + '    Why you should care. ' )
                Text_Formatting ( 88, '    T ' )

                Back = User_Input ( random.choice( ID ) )
                                  
                Text_Formatting ( 88, ( 88 * ' ' ) + '    That is all the information on Subsistence. ' )

                Back = User_Input ( random.choice( ID ) )
                
                break
                                  
            elif Back == 'No' :
                Text_Formatting ( 88, ( 88 * ' ' ) + '    Moving on then. ' )
                break

            else :
                Unknown_Input ( )

        Text_Formatting ( 88, ( 88 * ' ' ) + '    This is s far as I\'ve gotten writing up this section. ' )
        User_Input ( random.choice( ID ) )
                
        Text_Formatting ( 88, ( 88 * ' ' ) + '    Returning to selection. ' )
        User_Input ( random.choice( ID ) )

#==================================================================================================        

def Information_Loop ( ) :

    Back = 'I wanna learn shit'
    
    while Back != 'Back' :

        print(' \n\
         /  |                /                   /          \n\
        (___| ___           (___  ___              ___      \n\
        |   )|   )|   )     |    |   )     |   )| |   )     \n\
        |  / |__/ |/\/      |__  |__/      |/\/ | |  /      \n\
        \n')

        Text_Formatting ( 88, ( 88 * ' ' ) + '    You may type Back at any point to return to options ' )
        User_Input ( random.choice( ID ) )

        Text_Formatting ( 88, ( 88 * ' ' ) + '    This is s far as I\'ve gotten writing up this section. ' )
        Back = User_Input ( random.choice( ID ) )
        
#==================================================================================================
# SELECTING DIFFICULTY  #
#==================================================================================================

def Difficulty_Select ( ) :
    
    global Morale, Requisitions, Subsistence, SO, MD, IT, CM, CT, MT, CC, B_Teach, H_Teach, A_Teach, FARM_Work, FACT_Work, Pilot
    global B, H, A, FARMS, FACTS, CH 
    time.sleep(.02)
    print('\n\
               /                              / /    /            /    /             \n\
          ___ (  ___  ___  _ _  ___            (___     ___      (___ (___  ___      \n\
    |   )|___)| |    |   )| | )|___)         | |       |___      |    |   )|___)     \n\
    |/\/ |__  | |__  |__/ |  / |__           | |__      __/      |__  |  / |__       \n\
                                    /                                                \n\
                               __                                                    \n\
                  |           /         /    /                             /    |    \n\
     ___  ___  ___|      ___ (         (___ (___  ___            ___  ___ (  ___|    \n\
    |___)|   )|   )     |   )|___      |    |   )|___)     |   )|   )|   )| |   )    \n\
    |__  |  / |__/      |__/ |         |__  |  / |__       |/\/ |__/ |    | |__/     \n\n\n\
                                                                                      ')


    time.sleep(.02)
    Text_Formatting ( 88, ( 88 * ' ' ) + '     Difficulty Options:                                         Too Easy | Easy  ' )

    
    while True :
        try :
            
            Diff = str( User_Input ( random.choice( ID ) ) )

            if Diff == 'Too Easy' :
                Morale,             \
                Requisitions,       \
                Subsistence,        \
                SO, MD, IT,         \
                CM, CT, MT, CC,     \
                B, H, A,            \
                FARMS, FACTS, CH = 75,65,70,10,2,2,0,0,0,4,1,0,0,2,1,2
                Text_Formatting( 89, ( 88 * ' ' ) + '    Press Enter to continue . . . ' )
                User_Input ( random.choice( ID ) )
                break
            
            elif Diff == 'Easy' :
                Requisitions,       \
                Subsistence,        \
                SO, MD, IT,         \
                CM, CT, MT, CC,     \
                B, H, A,            \
                FARMS, FACTS, CH = 65,40,55,5,1,0,0,0,0,0,0,0,0,1,0,1
                Text_Formatting( 89, ( 88 * ' ' ) + '    Press Enter to continue . . . ' )
                User_Input ( random.choice( ID ) )
                break

            Unknown_Input ( )
            
        except :
            Unknown_Input ( )

    B_Teach   = B * 1
    H_Teach   = H * 1
    A_Teach   = A * 1
    FARM_Work = FARMS * 2
    FACT_Work = FACTS * 2
    Pilot     = CH * 1
     
#==================================================================================================
# GRAPHICS USER INTERFACE *ish* #
#==================================================================================================

def GUI ( DAY ) :

    global SO, MD, IT, CM, CT, MT, CO,\
    B_CCTrain, B_MDTrain, B_ITTrain, B_MTTrain,\
    H_CCTrain, H_SOTrain, H_ITTrain, H_CTTrain,\
    A_CCTrain, A_SOTrain, A_MDTrain, A_CMTrain

    SO_Busy = 0 - ( B_Teach + H_SOTrain + A_SOTrain )
    if SO_Busy == 0 :
        SO_Busy = ''
    MD_Busy = 0 - ( H_Teach + B_MDTrain + A_MDTrain )
    if MD_Busy == 0 :
        MD_Busy = ''
    IT_Busy = 0 - ( A_Teach + B_MDTrain + A_MDTrain + Pilot )
    if IT_Busy == 0 :
        IT_Busy = ''
    CM_Busy = 0 - ( A_CMTrain )
    if CM_Busy == 0 :
        CM_Busy = ''
    CT_Busy = 0 - ( H_CTTrain )
    if CT_Busy == 0 :
        CT_Busy = ''
    MT_Busy = 0 - ( B_MTTrain )
    if MT_Busy == 0 :
        MT_Busy = ''
    CC_Busy = 0 - ( B_CCTrain + H_CCTrain + A_CCTrain + FARM_Work + FACT_Work )
    if CC_Busy == 0 :
        CC_Busy = ''

    B_Vacant_Disp = 0 - B_Vacant
    H_Vacant_Disp = 0 - H_Vacant
    A_Vacant_Disp = 0 - A_Vacant
    FARM_Vacant_Disp = 0 - FARM_Vacant
    FACT_Vacant_Disp = 0 - FACT_Vacant
    CH_Vacant_Disp = 0 - CH_Vacant
    
    if B_Vacant == 0 :
        B_Vacant_Disp = ''
    if H_Vacant == 0 :
        H_Vacant_Disp = ''
    if A_Vacant == 0 :
        A_Vacant_Disp = ''
    if FARM_Vacant == 0 :
        FARM_Vacant_Disp = ''        
    if FACT_Vacant == 0 :
        FACT_Vacant_Disp = ''
    if CH_Vacant == 0 :
        CH_Vacant_Disp = ''

    Ptot = SO + MD + IT + CM + CT + MT + CC
    Itot = B + H + A + FARMS + FACTS + CH

    B_Train = B_CCTrain + B_ITTrain + B_MDTrain + B_MTTrain 
    H_Train = H_CCTrain + H_SOTrain + H_ITTrain + H_CTTrain 
    A_Train = A_CCTrain + A_SOTrain + A_MDTrain + A_CMTrain 
    
    if Sub_Daily >= 0 :
        plus = '+'
    else :
        plus = ''
    time.sleep(.02)
    print( '____________________/`' + 78 * '-')
    time.sleep(.02)
    print( )
    time.sleep(.02)
    print( )
    time.sleep(.02)
    print( )
    time.sleep(.02)
    print( ( 10 * '=' ) + '<I][>=-=<][I>' + ( 18 * '=' ) + '<I][>=' + ( len( Zero_DAY + str( DAY ) ) - 2 ) * '-' + '=<][I>' + ( ( 16 - ( len( str( DAY ) ) - 2 ) ) * '=' ) + '<I][>=-=<][I>' + ( 16 * '=' ) )
    time.sleep(.02)
    print( ( 8 * '=' ) + '<I]-=<({O})>=-[I>' + ( 12 * '=' ) + '<I][|  ' + 'Day ' + Zero_DAY + str( DAY ) + '  |][I>' + ( ( 18 - len( 'Day ' + Zero_DAY + str( DAY ) ) ) * '=' ) + '<I]-=<({O})>=-[I>' + ( 14 * '=' ) )
    time.sleep(.02)
    print( ( 11 * '_' ) + ']   }|{   [' + ( 19 * '_' ) + 'I>' + ( len( 'Day   ' + Zero_DAY + str( DAY ) ) * '=' ) + '<I' + ( ( 29 - len( 'Day     ' + Zero_DAY + str( DAY ) ) ) * '_' ) + ']   }|{   [' + ( 17 * '_' ) )  
    time.sleep(.02)
    print( ( 7 * ' ' ) + '__,,\'--^^^^^--\',,__' + ( 42 * ' ' ) + '__,,\'--^^^^^--\',,__' + ( 13 * ' ' ) )
    time.sleep(.02)
    print( )
    time.sleep(.02)
    print( '     Morale |' + Display_Bar( Morale ) + '| ' + str( Morale ) +
         ( ( 48 - len( '     Morale |' + Display_Bar( Morale ) + '| ' + str( Morale ) ) ) * ' ' ) +
         ( ' | +' + str( Req_Daily ) + ( 3 - len( str( Req_Daily ) ) ) * ' ' + '| ' + str( Requisitions ) + ( 3 - len( str( Requisitions ) ) ) * ' ' + ' |' + Display_Bar( Requisitions ) + '| Requisitions ' )
         )
    time.sleep(.02)
    print( ' Discretion |' + Display_Bar( Discretion ) + '| ' + str( Discretion ) +
         ( ( 48 - len( ' Discretion |' + Display_Bar( Discretion ) + '| ' + str( Discretion ) ) ) * ' ' ) +
         ( ' | ' + plus + str( Sub_Daily ) + ( 3 - len( str( Sub_Daily ) ) ) * ' ' + '| ' + str( Subsistence ) + ( 3 - len( str( Subsistence ) ) ) * ' ' + ' |' + Display_Bar( Subsistence ) + '| Subsistence ' )
         )
    time.sleep(.02)
    print( )
    time.sleep(.02)
    print( 33 * ' ' + '| Operational Composition | ' + ( 23 * ' ' ) + '| Commanders |' )
    time.sleep(.02)
    print( '   * Combat ' + ( 9 * ' ' ) + 'I>' + ( 48 * '=' ) + '<I' + ( 9 * ' ' ) + 'I>' + ( 14 * '=' ) + '<I' )
    time.sleep(.02)
    print( '   + Medical ' + ( 8 * ' ' ) + '|' + Operational_Composition_Display ( SO, MD, IT, CM, CT, MT ) + '|' + ( 9 * ' ' ) + '| ' + ( CO * 'X ' ) + ( ( 15 - len( CO * 'X ' ) ) * ' ' ) + '|' )
    time.sleep(.02)
    print( '   = Tech ' + ( 11 * ' ' ) + '`' + ( 50 * '-' ) + '\'' + ( 9 * ' ' ) + '`' + ( 16 * '-' ) + '\'')
    time.sleep(.02)
    print( )
    time.sleep(.02)
    print( '-----=<|>=-+' + 70 * ' ' + '+-=<|>=-----------' )
    time.sleep(.02)
    print( '   Personel| ' + str ( Ptot ) + ( ( 60 - len( str( Ptot ) ) ) * ' ' ) + ( ( 8 - len( str( Itot ) ) ) * ' ' ) + str( Itot ) + ' |Infrastructure')
    time.sleep(.02)
    print( ( 11 * '=' ) + 'I' + ( 70 * ' ' ) + 'I' + ( 17 * '=' ) )
    time.sleep(.02)
    print( '   Soldiers| ' + str ( SO ) + ( ( 4 - len( str( SO ) ) ) * ' ' ) + str( SO_Busy ) + ( ( 4 - len( str( SO_Busy ) ) ) * ' ' ) + 'I' + ( 50 * '=' ) + 'I'                                                              + ' ' + str( B_Vacant_Disp ) + ( ( 3 - len( str( B_Vacant_Disp ) ) ) * ' ' ) + ( ( 4 - len( str( B     ) ) ) * ' ' ) + str( B     ) + ' |Barracks ' + ' | ' + str( B_Train ) + ( 3 - len( str( B_Train ) ) ) * ' ' + '| ' )
    time.sleep(.02)
    print( '     Medics| ' + str ( MD ) + ( ( 4 - len( str( MD ) ) ) * ' ' ) + str( MD_Busy ) + ( ( 4 - len( str( MD_Busy ) ) ) * ' ' ) + '| ' + Display_Text[1  :48 ] + ( ( 48 - len( Display_Text[1  :48 ] ) ) * ' ' ) + ' |' + ' ' + str( H_Vacant_Disp ) + ( ( 3 - len( str( H_Vacant_Disp ) ) ) * ' ' ) + ( ( 4 - len( str( H     ) ) ) * ' ' ) + str( H     ) + ' |Clinics  ' + ' | ' + str( H_Train ) + ( 3 - len( str( H_Train ) ) ) * ' ' + '| ' )
    time.sleep(.02)
    print( '      Techs| ' + str ( IT ) + ( ( 4 - len( str( IT ) ) ) * ' ' ) + str( IT_Busy ) + ( ( 4 - len( str( IT_Busy ) ) ) * ' ' ) + '| ' + Display_Text[49 :97 ] + ( ( 48 - len( Display_Text[49 :97 ] ) ) * ' ' ) + ' |' + ' ' + str( A_Vacant_Disp ) + ( ( 3 - len( str( A_Vacant_Disp ) ) ) * ' ' ) + ( ( 4 - len( str( A     ) ) ) * ' ' ) + str( A     ) + ' |Academies' + ' | ' + str( A_Train ) + ( 3 - len( str( A_Train ) ) ) * ' ' + '| ' )
    time.sleep(.02)
    print( '    ComMeds| ' + str ( CM ) + ( ( 4 - len( str( CM ) ) ) * ' ' ) + str( CM_Busy ) + ( ( 4 - len( str( CM_Busy ) ) ) * ' ' ) + '| ' + Display_Text[98 :146] + ( ( 48 - len( Display_Text[98 :146] ) ) * ' ' ) + ' |'                                                                            + ( ( 8 - len( str( FW    ) ) ) * ' ' ) + str( FW    ) + ' |Firewalls')
    time.sleep(.02)
    print( '   ComTechs| ' + str ( CT ) + ( ( 4 - len( str( CT ) ) ) * ' ' ) + str( CT_Busy ) + ( ( 4 - len( str( CT_Busy ) ) ) * ' ' ) + '| ' + Display_Text[147:195] + ( ( 48 - len( Display_Text[147:195] ) ) * ' ' ) + ' |' + ' ' + str( FARM_Vacant_Disp ) + ( ( 3 - len( str( FARM_Vacant_Disp ) ) ) * ' ' ) + ( ( 4 - len( str( FARMS ) ) ) * ' ' ) + str( FARMS ) + ' |Farms    ')
    time.sleep(.02)
    print( '   MedTechs| ' + str ( MT ) + ( ( 4 - len( str( MT ) ) ) * ' ' ) + str( MT_Busy ) + ( ( 4 - len( str( MT_Busy ) ) ) * ' ' ) + '| ' + Display_Text[196:244] + ( ( 48 - len( Display_Text[196:244] ) ) * ' ' ) + ' |' + ' ' + str( FACT_Vacant_Disp ) + ( ( 3 - len( str( FACT_Vacant_Disp ) ) ) * ' ' ) + ( ( 4 - len( str( FACTS ) ) ) * ' ' ) + str( FACTS ) + ' |Factories')
    time.sleep(.02)
    print( '  Civilians| ' + str ( CC ) + ( ( 4 - len( str( CC ) ) ) * ' ' ) + str( CC_Busy ) + ( ( 4 - len( str( CC_Busy ) ) ) * ' ' ) + '|' + ( 50 * ' ' ) + '|'                                                              + ' ' + str( CH_Vacant_Disp ) + ( ( 3 - len( str( CH_Vacant_Disp ) ) ) * ' ' ) + ( ( 4 - len( str( CH    ) ) ) * ' ' ) + str( CH    ) + ' |Choppers ')  

#==================================================================================================

def Operation_GUI ( NAME, SO, MD, IT, CM, CT, MT, CO, Op_Text, Return_Day) :

    s = 's'
    Per_List = (['+-=<|>=-----------',
                 '| Deployed Forces ',
                 'I==========I======',
                 '| Soldiers | ' + str( SO ),
                 '| Medics   | ' + str( MD ),
                 '| Techs    | ' + str( IT ),
                 '| ComMeds  | ' + str( CM ),
                 '| ComTechs | ' + str( CT ),
                 '| MedTechs | ' + str( MT ),
                 '|','|','|','|','|','|','|','|','|','|','|','|','|','|','|','|','|','|','|','|','|','|','|','|','|','|','|','|',\
                 '|','|','|','|','|','|','|','|','|','|','|','|','|','|','|','|','|','|','|','|','|','|','|','|','|','|','|','|'])

    Ptot = SO + MD + IT + CM + CT + MT + CC
    time.sleep(.02)
    print( '____________________/`' + 78 * '-')
    time.sleep(.02)
    print( )
    time.sleep(.02)
    print( )
    time.sleep(.02)
    print( )
    time.sleep(.02)
    print( ( 10 * '=' ) + '<I][>=-=<][I>' + ( 48 * '=' ) + '<I][>=-=<][I>' + ( 16 * '=' ) )
    time.sleep(.02)
    print( ( 8 * '=' ) + '<I]-=<({O})>=-[I>' + ' I>' + ( 38 * '=' ) + '<I ' + '<I]-=<({O})>=-[I>' + ( 14 * '=' ) )
    time.sleep(.02)
    print( ( 11 * '_' ) + ']   }|{   [' + '    | Operation ' + NAME + ( (45 - len( '    | Operation ' + NAME ) ) * ' ' ) + '|    ]   }|{   [' + ( 17 * '_' ) )  
    time.sleep(.02)
    print( ( 7 * ' ' ) + '__,,\'--^^^^^--\',,__\'' + ( 40 * '-' ) + '\'__,,\'--^^^^^--\',,__' + ( 13 * ' ' ) )
    time.sleep(.02)
    print( )
    time.sleep(.02)
    print( 33 * ' ' + '| Operational Composition | ' + ( 25 * ' ' ) + '| EDA |' )
    time.sleep(.02)
    print( '   * Combat ' + ( 9 * ' ' ) + 'I>' + ( 48 * '=' ) + '<I' + ( 9 * ' ' ) + 'I>' + (16 * '=' ) )
    time.sleep(.02)
    print( '   + Medical ' + ( 8 * ' ' ) + '|' + Operational_Composition_Display ( SO, MD, IT, CM, CT, MT ) + '|' + ( 9 * ' ' ) + '| Day ' + str( Return_Day ) )
    time.sleep(.02)
    print( '   = Tech ' + ( 11 * ' ' ) + '`' + ( 50 * '-' ) + '\'' + ( 9 * ' ' ) + '\'' + ( 17 * '-' ) ) 
    time.sleep(.02)
    print( )
    time.sleep(.02)
    Text_Formatting_Op_Sum ( 65, Op_Text + ( ( 350 - len( Op_Text ) ) * ' ' ), Per_List )

#==================================================================================================

def Operation_Return_GUI ( Op_Text, Return_Day, NAME, SO, MD, IT, CM, CT, MT, CO, Outcome ) :

    s = 's'
    Per_List = (['+-=<|>=-----------',
                 '| Deployed Forces ',
                 'I==========I======',
                 '| Soldiers | ' + str( SO ),
                 '| Medics   | ' + str( MD ),
                 '| Techs    | ' + str( IT ),
                 '| ComMeds  | ' + str( CM ),
                 '| ComTechs | ' + str( CT ),
                 '| MedTechs | ' + str( MT ),
                 '|','|','|','|','|','|','|','|','|','|','|','|','|','|','|','|','|','|','|','|','|','|','|','|','|','|','|','|',\
                 '|','|','|','|','|','|','|','|','|','|','|','|','|','|','|','|','|','|','|','|','|','|','|','|','|','|','|','|'])

    if Outcome == 'Defeat' :
        Outcome_List = Defeated ( )

    elif Outcome == 'Victory' :
        Outcome_List = Victorious ( )
     
    Ptot = SO + MD + IT + CM + CT + MT + CC
    time.sleep(.02)
    print( '____________________/`' + 78 * '-')
    time.sleep(.02)
    print( )
    time.sleep(.02)
    print( )
    time.sleep(.02)
    print( )
    time.sleep(.02)
    print( ( 10 * '=' ) + '<I][>=-=<][I>' + ( 48 * '=' ) + '<I][>=-=<][I>' + ( 16 * '=' ) )
    time.sleep(.02)
    print( ( 8 * '=' ) + '<I]-=<({O})>=-[I>' + ' I>' + ( 38 * '=' ) + '<I ' + '<I]-=<({O})>=-[I>' + ( 14 * '=' ) )
    time.sleep(.02)
    print( ( 11 * '_' ) + ']   }|{   [' + '    | Operation ' + NAME + ( (45 - len( '    | Operation ' + NAME ) ) * ' ' ) + '|    ]   }|{   [' + ( 17 * '_' ) )  
    time.sleep(.02)
    print( ( 7 * ' ' ) + '__,,\'--^^^^^--\',,__\'' + ( 40 * '-' ) + '\'__,,\'--^^^^^--\',,__' + ( 13 * ' ' ) )
    time.sleep(.02)
    print( )
    time.sleep(.02)
    for i in Outcome_List :
        print( 17 * ' ' + i )
        time.sleep(.02)

    print( )
    time.sleep(.02)
    Text_Formatting_Op_Sum ( 65, Op_Text + ( ( 350 - len( Op_Text ) ) * ' ' ), Per_List )
    
#==================================================================================================
# CASCADE EFFECT #
#==================================================================================================

def Cascade ( x ) :

    Symbols = [' ','.',',',':',';','+','*','#','@']

    if x == 'Inverse' :
        Symbols = Symbols[::-1]
        
    base = list( 100 * Symbols[0] )
    line = ''.join( base )
    for h in range( 6 ) :
        print( line )
    index = list( range( 100 ) )

    for i in Symbols :
        a = Symbols.index( i )
        y = 1
        
        while base.count( Symbols[ a ] ) < ( len( base ) * 0.9 ) :        
            for j in range( int( y ) ) :
                
                x = random.choice( index )
                
                if base[ x ] == Symbols[ a - 1 ] :
                    base.pop( x )
                    base.insert( x, i )
                    
                if base[ x ] == Symbols[ a - 2 ] :
                    base.pop( x )
                    base.insert( x, Symbols[ a - 1 ] )
                    
                if base[ x ] == Symbols[ a - 3 ] :
                    base.pop( x )
                    base.insert( x, Symbols[ a - 2 ] )
                    
                if base.count( Symbols[ a - 1 ] ) < 5 :
                    while base.count( Symbols[ a - 1 ] ) > 0 :
                        z = base.index( Symbols[ a - 1 ] )
                        base.pop( z )
                        base.insert( z, Symbols[ a ] )
                        
                if base.count( Symbols[ a - 1 ] ) < 5 :
                    while base.count( Symbols[ a - 2 ] ) > 0 :
                        z = base.index( Symbols[ a - 2 ] )
                        base.pop( z )
                        base.insert( z, Symbols[ a - 1 ] )
                
                        
                line = ''.join( base )
                print( line )
                y += .5

#==================================================================================================
# OUTCOMES #
#==================================================================================================

def Defeated ( ) :
    Defeated = ([   '''               _,...,_                ''',
                    '''    ,       ,~^, ;    ^~,        ,    ''',
                    '''    |      ,' `~{},_.   `,       |    ''',
                    '''   ,'      {  ,_' `, _,  }       `,   ''',
                    ''' -<|    D  E ;F `E^;A  T |E  D    |>- ''',
                    '''   `,      `;`,_.',`._,';'       ,'   ''',
                    '''    |      `{    (,)    }'       |    ''',
                    '''    '       '`~.__,'..~'`        `    ''',
                    '''               `^^^ ^'                ''', ])
    return Defeated

#==================================================================================================

def Victorious ( ) :
    Victorious = ([ '''     ;=~-.,_.,  `,  ,'  ,._,.-~=;     ''',
                    '''    , `;~'`~-'`~, }{ ,~'`-~'`~:' ,    ''',
                    '''    |   }'_,~',_`};;{'_,`~,_`{   |    ''',
                    '''   ,'    `;'~' ,`~{}~', `~`;'    `,   ''',
                    ''' -<| V  I `C ,T~'O}{R`~I, O' U  S |>- ''',
                    '''   `,     ;'",',`;`';',`,"`;     ,'   ''',
                    '''    |    '~,'_.;~`  '~;._`,~`    |    ''',
                    '''    '     ,';~'        `~;`,     `    ''',
                    '''         ,'`              '`,         ''', ])
    return Victorious
     
#==================================================================================================
# DAILY VALUES UPDATER #
#==================================================================================================

def Daily_Values_Updater ( ) :

    global Req_Daily, Sub_Daily, Requisitions, Subsistence, Discretion, SO, MD, IT, CM, CT, MT, CC, FW_Cost, CH_Cost, B, H, A, M_Loss,\
    B_CCTrain, B_MDTrain, B_ITTrain, B_MTTrain,\
    H_CCTrain, H_SOTrain, H_ITTrain, H_CTTrain,\
    A_CCTrain, A_SOTrain, A_MDTrain, A_CMTrain,\
    Game_State

    SO_Grad = 0
    MD_Grad = 0
    IT_Grad = 0
    CM_Grad = 0
    CT_Grad = 0
    MT_Grad = 0
    CO_Grad = 0

    SO_Grad_Text = ''
    MD_Grad_Text = ''
    IT_Grad_Text = ''
    CM_Grad_Text = ''
    CT_Grad_Text = ''
    MT_Grad_Text = ''
    CO_Grad_Text = ''
    
    Ptot = SO + MD + IT + CM + CT + MT + CC + B_CCTrain + B_ITTrain + B_MDTrain + B_MTTrain + H_CCTrain + H_SOTrain + H_ITTrain + H_CTTrain + A_CCTrain + A_SOTrain + A_MDTrain + A_CMTrain + B_Teach + H_Teach + A_Teach + FARM_Work + FACT_Work + Pilot 

    FW_Cost = round( FW_Cost * ( 1 / ( ( A + 1 ) ** ( 1 / 5 ) ) ) )
    CH_Cost = round( CH_Cost * ( 1 / ( ( FACTS + 1 ) ** ( 1 / 5 ) ) ) )
    
    Req_Daily = FACTS * 3
    Sub_Daily = ( ( Ptot // 3 + 1 ) * -1 ) + ( FARMS * 5 )

    if DAY != 0 :

        if Subsistence > 100 :
            Civilian_Recruit ( )
        
        Requisitions += Req_Daily
        Subsistence += Sub_Daily

        Lose = Starvation ( )
        if Lose == 'Lose' :
            Text_Formatting ( 88, ( 88 * ' ' ) + '    The last of your forces has starved to death. ' )
            User_Input ( random.choice( ID ) )
            Game_State = 'Lose'

            User_Input ( random.choice( ID ) )
        
        Lose = Make_Like_A_Tree ( )
        if Lose == 'Lose' :
            Text_Formatting ( 88, ( 88 * ' ' ) + '    The last of your forces has deserted you. ' )
            User_Input ( random.choice( ID ) )
            Game_State = 'Lose'

            User_Input ( random.choice( ID ) )

        Vacancy_Check ( )

        if Game_State == 'Continue' :

            for i in range( B * 2 ) :
                if B_CCTrain > 0 :
                    B_CCTrain -= 1
                    SO += 1
                    SO_Grad += 1
                    
            for i in range( B ) :
                if B_MDTrain > 0 :
                    B_MDTrain -= 1
                    CM += 1
                    CM_Grad += 1
                    
            for i in range( B ) :
                if B_ITTrain > 0 :
                    B_ITTrain -= 1
                    CT += 1
                    CT_Grad += 1
                    
            for i in range( B ) :
                if B_MTTrain > 0 :
                    B_MTTrain -= 1
                    CO += 1
                    CO_Grad += 1

            for i in range( H * 2 ) :
                if H_CCTrain > 0 :
                    H_CCTrain -= 1
                    MD += 1
                    MD_Grad += 1

            for i in range( H ) :
                if H_SOTrain > 0 :
                    H_SOTrain -= 1
                    CM += 1
                    CM_Grad += 1

            for i in range( H ) :
                if H_ITTrain > 0 :
                    H_ITTrain -= 1
                    MT += 1
                    MT_Grad += 1

            for i in range( H ) :
                if H_CTTrain > 0 :
                    H_CTTrain -= 1
                    CO += 1
                    CO_Grad += 1

            for i in range( A * 2 ) :
                if A_CCTrain > 0 :
                    A_CCTrain -= 1
                    IT += 1
                    IT_Grad += 1

            for i in range( A ) :
                if A_SOTrain > 0 :
                    A_SOTrain -= 1
                    CT += 1
                    CT_Grad += 1
                    
            for i in range( A ) :
                if A_MDTrain > 0 :
                    A_MDTrain -= 1
                    MT += 1
                    MT_Grad += 1
                    
            for i in range( A ) :
                if A_CMTrain > 0 :
                    A_CMTrain -= 1
                    CO += 1
                    CO_Grad += 1
                    
            if SO_Grad > 0 :
                SO_Grad_Text = '    ' + str( SO_Grad ) + ' Soldiers have graduated. '            + ( 88 - len( '    ' + str( SO_Grad ) + ' Soldiers have graduated. ' ) ) * ' ' + 88 * ' '
            if MD_Grad > 0 :
                MD_Grad_Text = '    ' + str( MD_Grad ) + ' Medics have graduated. '              + ( 88 - len( '    ' + str( SO_Grad ) + ' Medics have graduated. ' ) ) * ' ' + 88 * ' '
            if IT_Grad > 0 :
                IT_Grad_Text = '    ' + str( IT_Grad ) + ' Technicians have graduated. '         + ( 88 - len( '    ' + str( SO_Grad ) + ' Technicians have graduated. ' ) ) * ' ' + 88 * ' '
            if CM_Grad > 0 :
                CM_Grad_Text = '    ' + str( CM_Grad ) + ' Combat Medics have graduated. '       + ( 88 - len( '    ' + str( SO_Grad ) + ' Combat Medics have graduated. ' ) ) * ' ' + 88 * ' '
            if CT_Grad > 0 :
                CT_Grad_Text = '    ' + str( CT_Grad ) + ' Combat Technicians have graduated. '  + ( 88 - len( '    ' + str( SO_Grad ) + ' Combat Technicians have graduated. ' ) ) * ' ' + 88 * ' '
            if MT_Grad > 0 :
                MT_Grad_Text = '    ' + str( MT_Grad ) + ' Medical Technicians have graduated. ' + ( 88 - len( '    ' + str( SO_Grad ) + ' Medical Technicians have graduated. ' ) ) * ' ' + 88 * ' '
            if CO_Grad > 0 :
                CO_Grad_Text = '    ' + str( CO_Grad ) + ' Commander has graduated. '            + ( 88 - len( '    ' + str( SO_Grad ) + ' Commander has graduated. ' ) ) * ' ' + 88 * ' '

            Req_Daily_Text = '    You have generated ' + str( Req_Daily ) + ' Requisitions' + ( 88 - len( '    You have generated ' + str( Req_Daily ) + ' Requisitions' ) ) * ' ' + 88 * ' '

            Sub_Daily_Text = '    You have generated ' + str( Sub_Daily ) + ' Subsistence ' + ( 88 - len( '    You have generated ' + str( Sub_Daily ) + ' Subsistence ' ) ) * ' ' + 88 * ' '

            Text_Formatting ( 88, ( 88 * ' ' ) + SO_Grad_Text + MD_Grad_Text + IT_Grad_Text + CM_Grad_Text + CT_Grad_Text + CM_Grad_Text + CO_Grad_Text + Req_Daily_Text + Sub_Daily_Text )

            Discretion -= 5

            Text_Formatting ( 88, ( 88 * ' ' ) + '    Discretion has decresed by 5 ' )

            User_Input ( random.choice( ID ) )

#==================================================================================================
# CIVILIAN RECRUIT EVENT #
#==================================================================================================

def Vacancy_Check ( ) :

    global B_Vacant, H_Vacant, A_Vacant, FARM_Vacant, FACT_Vacant, CH_Vacant,\
           B, H, A, FARMS, FACTS, CH 
    
    if B_Teach < B :
        B_Vacant += 1
        B -= 1
        
    if H_Teach < H :
        H_Vacant += 1
        H -= 1
        
    if A_Teach < A :
        A_Vacant += 1
        A -= 1
        
    if FARM_Work < ( FARMS * 2 ) :
        FARM_Vacant += 1
        FARMS -= 1
        
    if FACT_Work < ( FACTS * 2 ) :
        FACT_Vacant += 1
        FACTS -= 1
        
    if Pilot < CH :
        CH_Vacant += 1
        CH -= 1

#==================================================================================================
# CIVILIAN RECRUIT EVENT #
#==================================================================================================

def Civilian_Recruit ( ) :

    global Subsistence, CC
    Civ_Recruit_Chance = []
    Civ_Recruit_Steal  = []
    Civ_Morale_Boost = round( Morale / 100, 1 )
    CC_Num = round( Random_Variation ( 7, 5 ) * Civ_Morale_Boost )
    Sub_Draw = ( CC_Num * 2 )

    if Morale < 50 :
        Civ_Morale_Bane = 50 - Morale

        for i in range( Civ_Morale_Bane ) :
            Civ_Recruit_Steal.append( 'Yes' )

        for i in range( Morale ) :
            Civ_Recruit_Steal.append( 'No' )

    Civ_RecruitY = Subsistence - 100
    Civ_RecruitN = 100 - Civ_RecruitY

    for i in range( Civ_RecruitY ) :
        Civ_Recruit_Chance.append( 'Yes' )
        
    for i in range( Civ_RecruitN ) :
        Civ_Recruit_Chance.append( 'No' )

    Recruit = random.choice( Civ_Recruit_Chance )

    if Recruit == 'Yes' :
        Text_Formatting ( 88, '    A small group of ' + CC_Name + 's have contacted you, They are asking for shelter and food in return for helping in \
whatever way they can. There are ' + str( CC_Num ) + ' ' + CC_Name + 's in the group. They\'ve been starving for weeks and desperately need supplies. Do you want to accept \
them into your Commune? It will cost you ' + str( Sub_Draw ) + ' Subsistence. You currently have ' + str( Subsistence ) + 'Subsistence. ' ) 

        Text_Formatting ( 88, ( 88 * ' ' ) + '    Do you want to let them in?                  Yes | No ' )
        Choice = User_Input ( random.choice( ID ) )

        if Choice == 'Yes' :

            Subsistence -= Sub_Draw

            CC += CC_Num

            if Morale < 50 :

                Steal = random.choice( Civ_Recruit_Steal )

                if Steal == 'Yes' :

                    Text_Formatting ( 88, 'There is ')

                    CC -= CC_Num

                else :

                    Text_Formatting ( 88, '    You have recruited ' + str( CC_Num ) + ' More ' + CC_Name + ' units. ' )

        elif Choice == 'No' :

            Text_Formatting ( 88, 'There is ')

        else :
            Unknown_Input ( ) 

#==================================================================================================
# TEXT FORMATTING #
#==================================================================================================

def Text_Formatting ( w, x ) :
    f,c,q = w, 0, 0
    Text_List= [ Dialogue_Box_Top_Scale ( w ) ]
    while q <= ( len( x ) // ( w + 1 ) + ( ( c // w ) + 1 ) ) :
        c += ( w - f )
        for i, j in enumerate( x[( q * ( w + 1 ) ) - c :( q * ( w + 1 ) ) + w - c ] ) :
            if j == ' ' :
                f = i   
        Text_List.append(
        '    | ' + x[( q * ( w + 1 ) ) - c :( q * ( w + 1 ) ) + ( f ) - c ] +
     ( ( ( w + 1 ) - len( x[( q * ( w + 1 ) ) - c :( q * ( w + 1 ) ) + ( f ) - c ] ) ) * ' ' ) + '|'
        )
        q += 1
    Text_List.append( Dialogue_Box_Bottom_Scale ( w ) )
    for i in Text_List :
        print( i )
        time.sleep(.02)
        
#==================================================================================================
        
def Text_Formatting_Op_Sum ( w, x, Per_List ) :
    f,c,q = w, 0, 0
    Text_List= [ Dialogue_Box_Top_Scale ( w ) + ( 9 * ' ' ) + str( Per_List[q] ) ]
    while q <= ( len( x ) // ( w + 1 ) + ( ( c // w ) + 1 ) ) :
        c += ( w - f )
        for i, j in enumerate( x[( q * ( w + 1 ) ) - c :( q * ( w + 1 ) ) + w - c ] ) :
            if j == ' ' :
                f = i   
        Text_List.append(
        '    | ' + x[( q * ( w + 1 ) ) - c :( q * ( w + 1 ) ) + ( f ) - c ] +
     ( ( ( w + 1 ) - len( x[( q * ( w + 1 ) ) - c :( q * ( w + 1 ) ) + ( f ) - c ] ) ) * ' ' ) + '|' +
        ( 9 * ' ' ) + str( Per_List[ q + 1 ] ) )
        q += 1
    Text_List.append( Dialogue_Box_Bottom_Scale ( w ) + ( 9 * ' ' ) + str( Per_List[ q + 1 ] ) )        
    for i in Text_List :
        print( i )
        time.sleep(.02)

#==================================================================================================
# DIALOGUE BOX #
#==================================================================================================

def Dialogue_Box_Top ( ) :
    return( '    I][I>' + ( 82 * '=' ) + '<I][I' )

def Dialogue_Box_Top_Scale ( x ) :
    return( '    I][I>' + ( ( x - 6 ) * '=' ) + '<I][I' )

#==================================================================================================

def Dialogue_Box_Bottom ( ) :
    return( '    [' + ( 6 * '_' ) + ',' + ( 9 * '-' ) + ',' + ( 50 * '_' ) + ',' + ( 9 * '-' ) + ',' + ( 12 * '_' ) + ']' )

def Dialogue_Box_Bottom_Scale ( x ) :
    return( '    [' + ( 6 * '_' ) + ',' + ( 9 * '-' ) + ',' + ( 50 * '_' ) + ',' + ( 9 * '-' ) + ',' + ( 13 * '_' ) )[:( x + 7 )] + ']'

#==================================================================================================
# DAY FORMATTING #
#==================================================================================================

def Day_Format ( x ) :

    if x > 1 :
        return ( 88 * ' ' ) + '    Your forces will be ' + str( x ) + ' days in transit to this location. '

    elif x == 1 :
        return ( 88 * ' ' ) + '    Your forces will be one day in transit to this location. '

    else :
        return ( 88 * ' ' ) + '    Your forces may be deployed immediately! '

#==================================================================================================
# DISPLAY BAR #
#==================================================================================================

def Display_Bar ( x ) :
    if x > 100 :
        x = 100
        
    Display = x // 10

    DisplayX = ( x - ( Display * 10 ) )
    
    if  DisplayX >= 5 :
        DisplayX = 1

    else :
        DisplayX = 0

    return( ( Display * '[]' ) +
          ( ( DisplayX * '[' ) +
   ( 20 - ( ( Display * 2 ) + DisplayX ) ) * '_' )
          )

#==================================================================================================
# OPERATIONAL COMPOSITION DISPLAY #
#==================================================================================================

def Operational_Composition_Display ( SO, MD, IT, CM, CT, MT ) :
    
    Ptot = SO + MD + IT + CM + CT + MT

    if Ptot == 0 :

        return ( 50 * ' ' )
    
    else :   

        Disp_Scale = 50 / Ptot 
        
        SOratio = SO * Disp_Scale
        MDratio = MD * Disp_Scale
        ITratio = IT * Disp_Scale
        CMratio = CM * Disp_Scale
        CTratio = CT * Disp_Scale
        MTratio = MT * Disp_Scale

        Combat_Comp = int( SOratio + ( CMratio / 2 ) + ( CTratio / 2 ) )
        Medical_Comp = int( MDratio + ( CMratio / 2 ) + ( MTratio / 2 ) ) 
        Tech_Comp = int( ITratio + ( MTratio / 2 ) + ( CTratio / 2 ) )

        Op_Comp = Combat_Comp + Medical_Comp + Tech_Comp
    
        for i in range( 50 - Op_Comp ) :

            if Combat_Comp / 50 > 0.34 :
                Combat_Comp += 1

            elif Medical_Comp / 50 > 0.33 :
                Medical_Comp += 1

            elif Tech_Comp / 50 > 0.33 :
                Tech_Comp += 1

            else :
                Combat_Comp += 1

        return( ( Combat_Comp * '*' ) + ( Medical_Comp * '+' ) + ( Tech_Comp * '=' ) )

#==================================================================================================
# USER INPUT #
#==================================================================================================

def User_Input ( x ) :
    time.sleep(.02)
    print( ( 11 * '=' ) + '|' + ' ' + x + ( ( 8 - len( x ) ) * ' ' ) + '|' + ( 50 * '=' ) + '|' + ( 9 * '_' ) + '|' + ( 17 * '=' ) )
    time.sleep(.02)
    User_Input = input( 11 * ' ' + '`------<][ : ')
    return User_Input

#==================================================================================================
# DAILY USER OPTIONS #
#==================================================================================================

def Daily_Options ( ) : 

    User_Input ( random.choice( ID ) )
    Actions = 3
    s = 's'
    
    while Actions != 0 :

        if Actions == 1 :
            s = ''
        Text_Formatting ( 88, ( 88 * ' ' ) + '    You have ' + str(Actions) + ' Action' + s + ' Ramaining for this day. ' )

        Text_Formatting ( 88, ( 88 * ' ' ) + '    These three options take Actions to perform but only in you go through and perform the action in the end. Opeing the windows to see the options doesn\'t cost any action points, so feel free to explore around. ' )
        Text_Formatting ( 88, ( 88 * ' ' ) + '    To add to existing Infrastructure type | . . . . . . . . . . . Build '   + ( ( 88 - len( '    To add to existing Infrastructure type | . . . . . . . . . . . Build '  ) ) * ' ' ) +
                              ( 88 * ' ' ) + '    To scan for nearby activity       type | . . . . . . . . . . . Scan '    + ( ( 88 - len( '    To scan for nearby activity       type | . . . . . . . . . . . Scan '   ) ) * ' ' ) +
                              ( 88 * ' ' ) + '    To train available civilians      type | . . . . . . . . . . . Train '   + ( ( 88 - len( '    To train available civilians      type | . . . . . . . . . . . Train '  ) ) * ' ' ) )

        Text_Formatting ( 88, ( 88 * ' ' ) + '    These Options are all Utility, Meaning they only display information. They cost NO Actions to perform. Don\'t hesitate to pull these up if you find yourself forgetting anything! ' )
        Text_Formatting ( 88, ( 88 * ' ' ) + '    To see all active Operations      type | . . . . . . . . . . . Current'  + ( ( 88 - len( '    To see all active Operations      type | . . . . . . . . . . . Current' ) ) * ' ' ) + 
                              ( 88 * ' ' ) + '    To see all returning Forces       type | . . . . . . . . . . . Return '  + ( ( 88 - len( '    To see all returning Forces       type | . . . . . . . . . . . Return ' ) ) * ' ' ) +
                              ( 88 * ' ' ) + '    To display your operation history type | . . . . . . . . . . . History'  + ( ( 88 - len( '    To display your operation history type | . . . . . . . . . . . History' ) ) * ' ' ) +
                              ( 88 * ' ' ) + '    To reprint the Global Display     type | . . . . . . . . . . . Global '  + ( ( 88 - len( '    To reprint the Global Display     type | . . . . . . . . . . . Global ' ) ) * ' ' ) +
                              ( 88 * ' ' ) + '    To pull up a brief Guide          type | . . . . . . . . . . . Help '    + ( ( 88 - len( '    To pull up a brief Guide          type | . . . . . . . . . . . Help '   ) ) * ' ' ) +
                              ( 88 * ' ' ) + '    To do nothing and skip this day   type | . . . . . . . . . . . Wait '    + ( ( 88 - len( '    To do nothing and skip this day   type | . . . . . . . . . . . Wait '   ) ) * ' ' ) )

        Choice = User_Input ( random.choice( ID ) )
        
        if Choice == 'Build' :
            Actions = Construction ( Actions )
            
        elif Choice == 'Current' :
            if len( Check_Ops ) == 0 :
                Text_Formatting ( 88, ( 88 * ' ' ) + '    There are no Operations currently in transit anywhere ')
                User_Input ( random.choice( ID ) )
            else :
                for i in Check_Ops :
                    Check_Ops[ i ] ( )
        
        elif Choice == 'Scan' :
            Actions = Scanning ( Actions )
            

        elif Choice == 'Wait' :
            Text_Formatting ( 88, ( 88 * ' ' ) + '    Are you sure you\'d like to Wait? You still have ' + str( Actions ) + ' Actions remaining.     Yes | No ' )
            x = 'unsure'
            
            while True :

                x = User_Input ( random.choice( ID ) )

                if x == 'Yes' :
                    break

                elif x == 'No' :
                    break

                else :
                    Unknown_Input ( )

            if x == 'Yes' :
                break

            elif x == 'No' :                
                continue

        elif Choice == 'Train' :
            Actions = Training ( Actions )

        elif Choice == 'Return' :
            if len( RCheck_Ops ) == 0 :
                Text_Formatting ( 88, ( 88 * ' ' ) + '    There are no Operations currently in transit back to Base. ')
                User_Input ( random.choice( ID ) )
            else :
                for i in RCheck_Ops :
                    RCheck_Ops[ i ] ( )
                    
            break
        
        elif Choice == 'History' :
            if len( Ops_History ) == 0 :
                Text_Formatting ( 88, ( 88 * ' ' ) + '    There is no Operation History to display. Go do somthing! ')
                User_Input ( random.choice( ID ) )
            else :
                for i in Ops_History :
                    i ( )
                User_Input ( random.choice( ID ) )

        elif Choice == 'Global' :
            GUI ( DAY )
            User_Input ( random.choice( ID ) )            
            
        elif Choice == 'Help' :
            Information_General ( )

        
        else :
            Unknown_Input ( )

    Text_Formatting ( 88, ( 88 * ' ' ) + '    You\'ve used up all your action points. ' )
    User_Input ( random.choice( ID ) )

#==================================================================================================
# SCANNING #
#==================================================================================================

def Scanning ( Actions ) :

    global Discretion

    Text_Formatting ( 88, ( 88 * ' ' ) + '    Remember, the longer range you scan the more enemies you will face, the more Discretion you \
will lose, and it may take longer to reach the operation but the rewards will be greatly increased. Also keep in mind that Short Scans take \
1 Actions, Mid Scans take 2 Actions and Long Scans take 3 Actions to perform. ')
    Text_Formatting ( 88, ( 88 * ' ' ) + '    What is the range you want to scan?                          Short | Mid | Long ' )
    Text_Formatting ( 88, ( 88 * ' ' ) + '    Or you may type Back to return to return to options ' )
    while True :

        Dist = User_Input ( random.choice( ID ) )
        
        if Dist == 'Short' :
            if Actions > 0 :
                
                print( Dialogue_Box_Top ( ) )
                for i in range( 1 ) :
                    print( '         ', end = '' )
                    time.sleep(.1)
                    for i in range( 17 ) :
                        print('(    ', end = '' )
                        time.sleep(.1)
                    print( '')
                    
                    print( '          ', end = '' )
                    time.sleep(.1)
                    for i in range( 17 ) :
                        print (')    ', end = '' )
                        time.sleep(.1)
                    print( '')
                    
                x = random.choice( Short_Operations_List )
                x ( )
                Actions -= 1
                Discretion -= 5
                return Actions
                break                 
            else :
                Text_Formatting( 88, ( 88 * ' ' ) + '    You do not have the required action points for this ' )
                Text_Formatting ( 88, ( 88 * ' ' ) + '    What is the range you want to scan?                          Short | Mid | Long ' )

        elif Dist == 'Mid' :
            if Actions > 1 :

                print( Dialogue_Box_Top ( ) )
                for i in range( 2 ) :
                    print( '         ', end = '' )
                    time.sleep(.1)
                    for i in range( 17 ) :
                        print('(    ', end = '' )
                        time.sleep(.1)
                    print( '')
                    
                    print( '          ', end = '' )
                    time.sleep(.1)
                    for i in range( 17 ) :
                        print (')    ', end = '' )
                        time.sleep(.1)
                    print( '')
                    
                x = random.choice( Mid_Operations_List )
                x ( )
                Actions -= 2
                Discretion -= 10
                return Actions
                break
            else :
                Text_Formatting( 88, ( 88 * ' ' ) + '    You do not have the required action points for this ' )
                Text_Formatting ( 88, ( 88 * ' ' ) + '    What is the range you want to scan?                          Short | Mid | Long ' )
    
        elif Dist == 'Long' :
            if Actions > 2 :

                print( Dialogue_Box_Top ( ) )
                for i in range( 3 ) :
                    print( '         ', end = '' )
                    time.sleep(.1)
                    for i in range( 17 ) :
                        print('(    ', end = '' )
                        time.sleep(.1)
                    print( '')
                    
                    print( '          ', end = '' )
                    time.sleep(.1)
                    for i in range( 17 ) :
                        print (')    ', end = '' )
                        time.sleep(.1)
                    print( '')
                    
                x = random.choice( Long_Operations_List )
                x ( )
                Actions -= 3
                Discretion -= 15
                return Actions
                break
            else :
                Text_Formatting( 88, ( 88 * ' ' ) + '    You do not have the required action points for this ' )
                Text_Formatting ( 88, ( 88 * ' ' ) + '    What is the range you want to scan?                          Short | Mid | Long ' )

        elif Dist == 'Back' :
            return Actions
            break
            
        else :
            Unknown_Input ( )

#==================================================================================================
# CONSTRUCTION  #
#==================================================================================================

def Construction ( Actions ) :

    global Requisitions, Descretion, B, H, A, FW, FARMS, FACTS, CH, SO, MD, IT, CC, B_Teach, H_Teach, A_Teach, FARM_Work, FACT_Work, Pilot
    
    B_Disp    = '|' + ( ( ( 10 - len( str( B_Cost    ) + ' Req' ) ) // 2 ) * ' ' ) + str( B_Cost    ) + ' Req' + ( ( 10 - len( ( ( 10 - len( str( B_Cost    ) + ' Req' ) ) // 2 ) * ' ' + str( B_Cost    ) + ' Req' ) ) * ' ' )
    H_Disp    = '|' + ( ( ( 10 - len( str( H_Cost    ) + ' Req' ) ) // 2 ) * ' ' ) + str( H_Cost    ) + ' Req' + ( ( 10 - len( ( ( 10 - len( str( H_Cost    ) + ' Req' ) ) // 2 ) * ' ' + str( H_Cost    ) + ' Req' ) ) * ' ' )
    A_Disp    = '|' + ( ( ( 10 - len( str( A_Cost    ) + ' Req' ) ) // 2 ) * ' ' ) + str( A_Cost    ) + ' Req' + ( ( 10 - len( ( ( 10 - len( str( A_Cost    ) + ' Req' ) ) // 2 ) * ' ' + str( A_Cost    ) + ' Req' ) ) * ' ' )
    FW_Disp   = '|' + ( ( ( 10 - len( str( FW_Cost   ) + ' Req' ) ) // 2 ) * ' ' ) + str( FW_Cost   ) + ' Req' + ( ( 10 - len( ( ( 10 - len( str( FW_Cost   ) + ' Req' ) ) // 2 ) * ' ' + str( FW_Cost   ) + ' Req' ) ) * ' ' )
    FARM_Disp = '|' + ( ( ( 10 - len( str( FARM_Cost ) + ' Req' ) ) // 2 ) * ' ' ) + str( FARM_Cost ) + ' Req' + ( ( 10 - len( ( ( 10 - len( str( FARM_Cost ) + ' Req' ) ) // 2 ) * ' ' + str( FARM_Cost ) + ' Req' ) ) * ' ' )
    FACT_Disp = '|' + ( ( ( 10 - len( str( FACT_Cost ) + ' Req' ) ) // 2 ) * ' ' ) + str( FACT_Cost ) + ' Req' + ( ( 10 - len( ( ( 10 - len( str( FACT_Cost ) + ' Req' ) ) // 2 ) * ' ' + str( FACT_Cost ) + ' Req' ) ) * ' ' )
    CH_Disp   = '|' + ( ( ( 10 - len( str( CH_Cost   ) + ' Req' ) ) // 2 ) * ' ' ) + str( CH_Cost   ) + ' Req' + ( ( 10 - len( ( ( 10 - len( str( CH_Cost   ) + ' Req' ) ) // 2 ) * ' ' + str( CH_Cost   ) + ' Req' ) ) * ' ' )
    
    while True :
        
        Text_Formatting ( 88, ( 88 * ' ' ) + '    You may choose to construct the following infrustructure for a requisitions cost. \
        | Barracks |  Clinic  | Academy  | Firewall |   Farm   | Factory  | Chopper  |   \
       '+ B_Disp +  H_Disp +  A_Disp + FW_Disp + FARM_Disp + FACT_Disp + CH_Disp +  '|   ' +
        ( 88 * ' ' ) + ' Or you my type Back to return to options.           Your current Requisitions: ' + str( Requisitions ) + ' ' )
        Construct = User_Input ( random.choice( ID ) )

        if Construct == 'Barracks' :
            if Requisitions < B_Cost :
                Text_Formatting ( 88, ( 88 * ' ' ) + '    You do not have the required rescources to construct this. ' )

            elif SO < 1 :
                Text_Formatting ( 88, ( 88 * ' ' ) + '    You have no available Soldiers to act as instructors. ' )
                    
            else :
                Text_Formatting ( 88, ( 88 * ' ' ) + '    You would like to construct a Barracks? You will be committing one soldier to the facility to act as an instructor.                                  Yes | No ' )

                while True :
                    Confirm = User_Input ( random.choice( ID ) )
                    if Confirm == 'Yes' :
                        Requisitions -= B_Cost
                        B += 1
                        B_Teach += 1
                        SO -= 1
                        Actions -= 1
                        return Actions
                        break
                    elif Confirm == 'No' :
                        break
                    
                    else :
                        Unknown_Input ( )
                        continue
            
        elif Construct == 'Clinic' :
            if Requisitions < H_Cost :
                Text_Formatting ( 88, ( 88 * ' ' ) + '    You do not have the required rescources to construct this. ' )

            elif MD < 1 :
                Text_Formatting ( 88, ( 88 * ' ' ) + '    You have no available Medics to act as instructors. ' )
                    
            else :
                Text_Formatting ( 88, ( 88 * ' ' ) + '    You would like to construct a Clinic? You will be committing one Medic to the facility to act as an instructor.                                      Yes | No ' )

                while True :
                    Confirm = User_Input ( random.choice( ID ) )
                    if Confirm == 'Yes' :
                        Requisitions -= B_Cost
                        H += 1
                        H_Teach += 1
                        MD -= 1
                        Actions -= 1
                        return Actions
                        break
                    elif Confirm == 'No' :
                        break
                    
                    else :
                        Unknown_Input ( )
                        continue

        elif Construct == 'Academy' :
            if Requisitions < A_Cost :
                Text_Formatting ( 88, ( 88 * ' ' ) + '    You do not have the required rescources to construct this. ' )

            elif IT < 1 :
                Text_Formatting ( 88, ( 88 * ' ' ) + '    You have no available Technicians to act as instructors. ' )
                    
            else :
                Text_Formatting ( 88, ( 88 * ' ' ) + '    You would like to construct an Academy? You will be committing one Technician to the facility to act as an instructor.                               Yes | No ' )

                while True :
                    Confirm = User_Input ( random.choice( ID ) )
                    if Confirm == 'Yes' :
                        Requisitions -= B_Cost
                        A += 1
                        A_Teach += 1
                        IT -= 1
                        Actions -= 1
                        return Actions
                        break
                    elif Confirm == 'No' :
                        break
                    
                    else :
                        Unknown_Input ( )
                        continue

        elif Construct == 'Firewall' :
            if Requisitions < FW_Cost :
                Text_Formatting ( 88, ( 88 * ' ' ) + '    You do not have the required rescources to construct this. ' )
            else :
                Text_Formatting ( 88, ( 88 * ' ' ) + '    You would like to construct a Firewall?                Yes | No ' )

                while True :
                    Confirm = User_Input ( random.choice( ID ) )
                    if Confirm == 'Yes' :
                        Requisitions -= FW_Cost
                        FW += 1
                        Discretion += 50
                        Actions -= 1
                        return Actions
                        break
                    elif Confirm == 'No' :
                        break
                    
                    else :
                        Unknown_Input ( )
                        continue

        elif Construct == 'Farm' :
            if Requisitions < FARM_Cost :
                Text_Formatting ( 88, ( 88 * ' ' ) + '    You do not have the required rescources to construct this. ' )

            elif CC < 2 :
                Text_Formatting ( 88, ( 88 * ' ' ) + '    You have no available civilians to work the fields. ' )

            else :
                Text_Formatting ( 88, ( 88 * ' ' ) + '    You would like to construct a Farm? You will have to commit two civilians to operate it.                                                             Yes | No ' )

                while True :
                    Confirm = User_Input ( random.choice( ID ) )
                    if Confirm == 'Yes' :
                        Requisitions -= FARM_Cost
                        FARMS += 1
                        FARM_Work += 2
                        CC -= 2
                        Actions -= 1
                        return Actions
                        break
                    elif Confirm == 'No' :
                        break
                    
                    else :
                        Unknown_Input ( )
                        continue

        elif Construct == 'Factory' :
            if Requisitions < FACT_Cost :
                Text_Formatting ( 88, ( 88 * ' ' ) + '    You do not have the required rescources to construct this. ' )

            elif CC < 2 :
                Text_Formatting ( 88, ( 88 * ' ' ) + '    You have no available civilians to work the mills.' )

            else :
                Text_Formatting ( 88, ( 88 * ' ' ) + '    You would like to construct a Factory? You will have to commit two civilians to operate it.                                                             Yes | No ' )

                while True :
                    Confirm = User_Input ( random.choice( ID ) )
                    if Confirm == 'Yes' :
                        Requisitions -= FACT_Cost
                        FACTS += 1
                        FACT_Work += 2
                        CC -= 2
                        Actions -= 1
                        return Actions
                        break
                    elif Confirm == 'No' :
                        break
                    
                    else :
                        Unknown_Input ( )
                        continue

        elif Construct == 'Chopper' :
            if Requisitions < CH_Cost :
                Text_Formatting ( 88, ( 88 * ' ' ) + '    You do not have the required rescources to construct this. ' )
            else :
                Text_Formatting ( 88, ( 88 * ' ' ) + '    You would like to construct a Chopper?                 Yes | No ' )

                while True :
                    Confirm = User_Input ( random.choice( ID ) )
                    if Confirm == 'Yes' :
                        Requisitions -= CH_Cost
                        CH += 1
                        Actions -= 1
                        return Actions
                        break
                    elif Confirm == 'No' :
                        break
                    
                    else :
                        Unknown_Input ( )
                        continue

        elif Construct == 'Back' :
            return Actions
            break

        else :
            Unknown_Input ( )

#==================================================================================================
# TRAINING #
#==================================================================================================

def Training ( Actions ) :

    global CC, SO, MD, IT, CM, CT, MT, B, H, A,\
           CC_Name, SO_Name, MD_Name, IT_Name, CM_Name, CT_Name, MT_Name, B_Name, H_Name, A_Name,\
B_CCTrain,\
B_MDTrain,\
B_ITTrain,\
B_MTTrain,\
H_CCTrain,\
H_SOTrain,\
H_ITTrain,\
H_CTTrain,\
A_CCTrain,\
A_SOTrain,\
A_MDTrain,\
A_CMTrain

    B_Text, H_Text, A_Text = '','',''
    
    if B > 0 :
        B_Text = '    To send a Unit to train in your ' + B_Name + ( 20 - len( B_Name ) ) * ' ' + ' type |        ' + B_Name + ( 88 - len('    To send a Unit to train in your ' + B_Name + ( 20 - len( B_Name ) ) * ' ' + ' type |        ' + B_Name ) ) * ' '    
    if H > 0 :
        H_Text = '    To send a Unit to train in your ' + H_Name + ( 20 - len( H_Name ) ) * ' ' + ' type |        ' + H_Name + ( 88 - len('    To send a Unit to train in your ' + H_Name + ( 20 - len( H_Name ) ) * ' ' + ' type |        ' + H_Name ) ) * ' '
    if A > 0 :
        H_Text = '    To send a Unit to train in your ' + A_Name + ( 20 - len( A_Name ) ) * ' ' + ' type |        ' + A_Name + ( 88 - len('    To send a Unit to train in your ' + A_Name + ( 20 - len( A_Name ) ) * ' ' + ' type |        ' + A_Name ) ) * ' '
        
    Train_Limit = ( B + H + A ) * 2
    Train_Limit_Check = Train_Limit
    
    Text_Formatting ( 88, ( 88 * ' ' ) + '    You may choose to send available units any available ' + B_Name + ', ' + H_Name + ' or ' + A_Name + ' to be \
trained into the respective combat roles. You may assign ' + str( Train_Limit ) + ' units with this action. \
But remember only two basic units or one specialized per day per institution will be trained, If you stack up more then this the training \
will complete on following days. Otherwise, units sent to training will be available the next day. ' )

    
    while True :

        Back = 0

        if Train_Limit == 0 :

            Text_Formatting ( 88, ( 88 * ' ' ) + '    You have trained the maximum number of units allowed with this action. ' )
            User_Input ( random.choice( ID ) )            
            Actions -= 1
            return Actions
            break
        
        if ( B + H + A ) > 0 :

            if ( CC + SO + MD + IT + CM + CT + MT ) > 0 :

                Text_Formatting ( 88, ( 88 * ' ' ) + '    Below are your available training options : ' )
                Text_Formatting ( 88, ( 88 * ' ' ) + B_Text + H_Text + A_Text + ( 88 * ' ' ) + '    Or type Back to return to options. ' + ( 88 * ' ' ) + ' You are able to train ' + str( Train_Limit ) + ' more Units ' )

            else :
                Text_Formatting ( 88, ( 88 * ' ' ) + '    You have no available Units to Train  . ' )
                User_Input ( random.choice( ID ) )
                if Train_Limit_Check != Train_Limit :
                    Actions -= 1
                    return Actions
                    break
                else :
                    return Actions
                    break

        else :
            Text_Formatting ( 88, ( 88 * ' ' ) + '    You have no instituitons to train Units in. ' )
            User_Input ( random.choice( ID ) )
            break

        Train = User_Input ( random.choice( ID ) )

        if Train == B_Name :

            while True :

                if Train_Limit == 0 :
                    break

                if Back == 1 :
                    Text_Formatting ( 88, ( 88 * ' ' ) + '    You may still train Units. ' )
                    break
                
                Text_Formatting ( 88, ( 88 * ' ' ) +  '   To train a previously Untrained Unit                     type | New  ' + ( ( 88 - len('   To train a previously Untrained Unit                     type | New  ') ) * ' ' ) + ( 88 * ' ' ) +\
                                                      '   To train a Basic Unit                                    type | Basic' + ( ( 88 - len('   To train a Basic Unit                                    type | Basic') ) * ' ' ) + ( 88 * ' ' ) +\
                                                      '   To train a Specialized unit into a commander             type | Spec ' + ( ( 88 - len('   To train a Specialized unit into a commander             type | Spec ') ) * ' ' ) + ( 88 * ' ' ) +\
                                                      '   Or to go back                                            type | Back ' + ( ( 88 - len('   Or to go back                                            type | Back ') ) * ' ' ) ) 

                Type = User_Input ( random.choice( ID ) )
                    
                if Type == 'New' :

                    if CC > 0 :

                        Text_Formatting ( 88, ( 88 * ' ' ) + '    How many ' + CC_Name + ' units would you like to send to the ' + B_Name + ' for training? ' )

                        while True :

                            if Train_Limit == 0 :
                                break

                            if Back == 1 :
                                break
                            
                            try :

                                Num = int( User_Input ( random.choice( ID ) ) )

                                if Num > CC :
                                    Text_Formatting ( 88, ( 88 * ' ' ) + '    You dont have that many ' + CC_Name + ' units available for training. ' )

                                else :
                                    if Train_Limit >= Num :
                                        CC -= Num
                                        B_CCTrain += Num
                                        Train_Limit -= Num
                                        Back = 1
                                        break

                                    else :
                                        Text_Formatting ( 88, ( 88 * ' ' ) + '    You aren\'t able to train that many more Units. You can train ' + str( Train_Limit ) + ' more Units. ' )
                                        
                            except :
                                Unknown_Input ( )

                    else :
                        Text_Formatting ( 88, ( 88 * ' ' ) + '    You dont have any ' + CC_Name + ' units available for training. ' )
                        

                elif Type == 'Basic' :

                    Text_Formatting ( 88, ( 88 * ' ' ) + '    Would you like to send a ' + MD_Name + ' unit or a ' + IT_Name + ' unit?         ' + MD_Name + ' | ' + IT_Name )

                    Basic = User_Input ( random.choice( ID ) )

                    if Basic == MD_Name :

                        if MD > 0 :

                            Text_Formatting ( 88, ( 88 * ' ' ) + '    How many ' + MD_Name + ' units would you like to send to the ' + B_Name + ' for training? ' )

                            while True :

                                if Train_Limit == 0 :
                                    break

                                if Back == 1 :
                                    break
                                
                                try :

                                    Num = int( User_Input ( random.choice( ID ) ) )

                                    if Num > MD :
                                        Text_Formatting ( 88, ( 88 * ' ' ) + '    You dont have that many ' + MD_Name + ' units available for training. ' )

                                    else :
                                        if Train_Limit >= Num :
                                            MD -= Num
                                            B_MDTrain += Num
                                            Train_Limit -= Num
                                            Back = 1
                                            break

                                        else :
                                            Text_Formatting ( 88, ( 88 * ' ' ) + '    You aren\'t able to train that many more Units. You can train ' + str( Train_Limit ) + ' more Units. ' )
                                            
                                except :
                                    Unknown_Input ( )

                        else :
                            Text_Formatting ( 88, '    You dont have any ' + MD_Name + ' available for training. ' )

                    elif Basic == IT_Name :

                        if IT > 0 :

                            Text_Formatting ( 88, ( 88 * ' ' ) + '    How many ' + IT_Name + ' units would you like to send to the ' + B_Name + ' for training? ' )

                            while True :

                                if Train_Limit == 0 :
                                    break

                                if Back == 1 :
                                    break
                                
                                try :

                                    Num = int( User_Input ( random.choice( ID ) ) )

                                    if Num > IT :
                                        Text_Formatting ( 88, ( 88 * ' ' ) + '    You dont have that many ' + IT_Name + ' units available for training. ' )

                                    else :
                                        if Train_Limit >= Num :
                                            IT -= Num
                                            B_ITTrain += Num
                                            Train_Limit -= Num
                                            Back = 1
                                            break

                                        else :
                                            Text_Formatting ( 88, ( 88 * ' ' ) + '    You aren\'t able to train that many more Units. You can train ' + str( Train_Limit ) + ' more Units. ' )
                                            
                                except :
                                    Unknown_Input ( )

                        else :
                            Text_Formatting ( 88, '    You dont have any ' + IT_Name + ' units available for training. ' )

                    elif Basic == 'Back' :
                        break

                    else :
                        Unknown_Input ( )

                elif Type == 'Spec' :

                    if MT > 0 :

                        Text_Formatting ( 88, ( 88 * ' ' ) + '    How many ' + MT_Name + ' units would you like to send to the ' + B_Name + ' for training? ' )

                        while True :

                            if Train_Limit == 0 :
                                break

                            if Back == 1 :
                                break
                            
                            try :

                                Num = int( User_Input ( random.choice( ID ) ) )

                                if Num > MT :
                                    Text_Formatting ( 88, ( 88 * ' ' ) + '    You dont have that many ' + MT_Name + ' units available for training. ' )

                                else :
                                    if Train_Limit >= Num :
                                        MT -= Num
                                        B_MTTrain += Num
                                        Train_Limit -= Num
                                        Back = 1
                                        break

                                    else :
                                        Text_Formatting ( 88, ( 88 * ' ' ) + '    You aren\'t able to train that many more Units. You can train ' + str( Train_Limit ) + ' more Units. ' )
                                        
                            except :
                                Unknown_Input ( )

                    else :
                        Text_Formatting ( 88, '    You dont have any ' + MT_Name + ' units available for training. ' )

                elif Type == 'Back' :
                    break

                else :
                    Unknown_Input ( )
                       
        elif Train == H_Name :

            while True :

                if Train_Limit == 0 :
                    break

                if Back == 1 :
                    Text_Formatting ( 88, ( 88 * ' ' ) + '    You may still train Units. ' )
                    break
                
                Text_Formatting ( 88, ( 88 * ' ' ) +  '   To train a previously Untrained Unit                     type | New  ' + ( ( 88 - len('   To train a previously Untrained Unit                     type | New  ') ) * ' ' ) + ( 88 * ' ' ) +\
                                                      '   To train a Basic Unit                                    type | Basic' + ( ( 88 - len('   To train a Basic Unit                                    type | Basic') ) * ' ' ) + ( 88 * ' ' ) +\
                                                      '   To train a Specialized unit into a commander             type | Spec ' + ( ( 88 - len('   To train a Specialized unit into a commander             type | Spec ') ) * ' ' ) + ( 88 * ' ' ) +\
                                                      '   Or to go back                                            type | Back ' + ( ( 88 - len('   Or to go back                                            type | Back ') ) * ' ' ) ) 

                Type = User_Input ( random.choice( ID ) )
                    
                if Type == 'New' :

                    if CC > 0 :

                        Text_Formatting ( 88, ( 88 * ' ' ) + '    How many ' + CC_Name + ' units would you like to send to the ' + H_Name + ' for training? ' )

                        while True :

                            if Train_Limit == 0 :
                                break

                            if Back == 1 :
                                break
                            
                            try :

                                Num = int( User_Input ( random.choice( ID ) ) )

                                if Num > CC :
                                    Text_Formatting ( 88, ( 88 * ' ' ) + '    You dont have that many ' + CC_Name + ' units available for training. ' )

                                else :
                                    if Train_Limit >= Num :
                                        CC -= Num
                                        H_CCTrain += Num
                                        Train_Limit -= Num
                                        Back = 1
                                        break

                                    else :
                                        Text_Formatting ( 88, ( 88 * ' ' ) + '    You aren\'t able to train that many more Units. You can train ' + str( Train_Limit ) + ' more Units. ' )
                                        
                            except :
                                Unknown_Input ( )

                    else :
                        Text_Formatting ( 88, ( 88 * ' ' ) + '    You dont have any ' + CC_Name + ' units available for training. ' )
                        

                elif Type == 'Basic' :

                    Text_Formatting ( 88, ( 88 * ' ' ) + '    Would you like to send a ' + SO_Name + ' unit or a ' + IT_Name + ' unit?         ' + SO_Name + ' | ' + IT_Name )

                    Basic = User_Input ( random.choice( ID ) )

                    if Basic == SO_Name :

                        if SO > 0 :

                            Text_Formatting ( 88, ( 88 * ' ' ) + '    How many ' + SO_Name + ' units would you like to send to the ' + H_Name + ' for training? ' )

                            while True :

                                if Train_Limit == 0 :
                                    break

                                if Back == 1 :
                                    break
                                
                                try :

                                    Num = int( User_Input ( random.choice( ID ) ) )

                                    if Num > SO :
                                        Text_Formatting ( 88, ( 88 * ' ' ) + '    You dont have that many ' + SO_Name + ' units available for training. ' )

                                    else :
                                        if Train_Limit >= Num :
                                            SO -= Num
                                            H_SOTrain += Num
                                            Train_Limit -= Num
                                            Back = 1
                                            break

                                        else :
                                            Text_Formatting ( 88, ( 88 * ' ' ) + '    You aren\'t able to train that many more Units. You can train ' + str( Train_Limit ) + ' more Units. ' )
                                            
                                except :
                                    Unknown_Input ( )

                        else :
                            Text_Formatting ( 88, '    You dont have any ' + SO_Name + ' available for training. ' )

                    elif Basic == IT_Name  :

                        if IT > 0 :

                            Text_Formatting ( 88, ( 88 * ' ' ) + '    How many ' + IT_Name + ' units would you like to send to the ' + H_Name + ' for training? ' )

                            while True :

                                if Train_Limit == 0 :
                                    break

                                if Back == 1 :
                                    break
                                
                                try :

                                    Num = int( User_Input ( random.choice( ID ) ) )

                                    if Num > IT :
                                        Text_Formatting ( 88, ( 88 * ' ' ) + '    You dont have that many ' + IT_Name + ' units available for training. ' )

                                    else :
                                        if Train_Limit >= Num :
                                            IT -= Num
                                            H_ITTrain += Num
                                            Train_Limit -= Num
                                            Back = 1
                                            break

                                        else :
                                            Text_Formatting ( 88, ( 88 * ' ' ) + '    You aren\'t able to train that many more Units. You can train ' + str( Train_Limit ) + ' more Units. ' )
                                            
                                except :
                                    Unknown_Input ( )

                        else :
                            Text_Formatting ( 88, '    You dont have any ' + IT_Name + ' units available for training. ' )

                    elif Basic == 'Back' :
                        break

                    else :
                        Unknown_Input ( )

                elif Type == 'Spec' :

                    if CT > 0 :

                        Text_Formatting ( 88, ( 88 * ' ' ) + '    How many ' + CT_Name + ' units would you like to send to the ' + H_Name + ' for training? ' )

                        while True :

                            if Train_Limit == 0 :
                                break

                            if Back == 1 :
                                break
                            
                            try :

                                Num = int( User_Input ( random.choice( ID ) ) )

                                if Num > CT :
                                    Text_Formatting ( 88, ( 88 * ' ' ) + '    You dont have that many ' + CT_Name + ' units available for training. ' )

                                else :
                                    if Train_Limit >= Num :
                                        CT -= Num
                                        H_CTTrain += Num
                                        Train_Limit -= Num
                                        Back = 1
                                        break

                                    else :
                                        Text_Formatting ( 88, ( 88 * ' ' ) + '    You aren\'t able to train that many more Units. You can train ' + str( Train_Limit ) + ' more Units. ' )
                                        
                            except :
                                Unknown_Input ( )

                    else :
                        Text_Formatting ( 88, '    You dont have any ' + CT_Name + ' units available for training. ' )

                elif Type == 'Back' :
                    break

                else :
                    Unknown_Input ( )

        elif Train == A_Name :

            while True :

                if Train_Limit == 0 :
                    break

                if Back == 1 :
                    Text_Formatting ( 88, ( 88 * ' ' ) + '    You may still train Units. ' )
                    break
                
                Text_Formatting ( 88, ( 88 * ' ' ) +  '   To train a previously Untrained Unit                     type | New  ' + ( ( 88 - len('   To train a previously Untrained Unit                     type | New  ') ) * ' ' ) + ( 88 * ' ' ) +\
                                                      '   To train a Basic Unit                                    type | Basic' + ( ( 88 - len('   To train a Basic Unit                                    type | Basic') ) * ' ' ) + ( 88 * ' ' ) +\
                                                      '   To train a Specialized unit into a commander             type | Spec ' + ( ( 88 - len('   To train a Specialized unit into a commander             type | Spec ') ) * ' ' ) + ( 88 * ' ' ) +\
                                                      '   Or to go back                                            type | Back ' + ( ( 88 - len('   Or to go back                                            type | Back ') ) * ' ' ) ) 

                Type = User_Input ( random.choice( ID ) )
                    
                if Type == 'New' :

                    if CC > 0 :

                        Text_Formatting ( 88, ( 88 * ' ' ) + '    How many ' + CC_Name + ' units would you like to send to the ' + A_Name + ' for training? ' )

                        while True :

                            if Train_Limit == 0 :
                                break

                            if Back == 1 :
                                break
                            
                            try :

                                Num = int( User_Input ( random.choice( ID ) ) )

                                if Num > CC :
                                    Text_Formatting ( 88, ( 88 * ' ' ) + '    You dont have that many ' + CC_Name + ' units available for training. ' )

                                else :
                                    if Train_Limit >= Num :
                                        CC -= Num
                                        A_CCTrain += Num
                                        Train_Limit -= Num
                                        Back = 1
                                        break

                                    else :
                                        Text_Formatting ( 88, ( 88 * ' ' ) + '    You aren\'t able to train that many more Units. You can train ' + str( Train_Limit ) + ' more Units. ' )
                                        
                            except :
                                Unknown_Input ( )

                    else :
                        Text_Formatting ( 88, ( 88 * ' ' ) + '    You dont have any ' + CC_Name + ' units available for training. ' )
                        

                elif Type == 'Basic' :

                    Text_Formatting ( 88, ( 88 * ' ' ) + '    Would you like to send a ' + SO_Name + ' unit or a ' + MD_Name + ' unit?         ' + SO_Name + ' | ' + MD_Name )

                    Basic = User_Input ( random.choice( ID ) )

                    if Basic == SO_Name :

                        if SO > 0 :

                            Text_Formatting ( 88, ( 88 * ' ' ) + '    How many ' + SO_Name + ' units would you like to send to the ' + A_Name + 's for training? ' )

                            while True :

                                if Train_Limit == 0 :
                                    break

                                if Back == 1 :
                                    break
                                
                                try :

                                    Num = int( User_Input ( random.choice( ID ) ) )

                                    if Num > SO :
                                        Text_Formatting ( 88, ( 88 * ' ' ) + '    You dont have that many ' + SO_Name + ' units available for training. ' )

                                    else :
                                        if Train_Limit >= Num :
                                            SO -= Num
                                            A_SOTrain += Num
                                            Train_Limit -= Num
                                            Back = 1
                                            break

                                        else :
                                            Text_Formatting ( 88, ( 88 * ' ' ) + '    You aren\'t able to train that many more Units. You can train ' + str( Train_Limit ) + ' more Units. ' )
                                            
                                except :
                                    Unknown_Input ( )

                        else :
                            Text_Formatting ( 88, '    You dont have any ' + SO_Name + ' available for training. ' )

                    elif Basic == MD_Name :

                        if MD > 0 :

                            Text_Formatting ( 88, ( 88 * ' ' ) + '    How many ' + MD_Name + ' units would you like to send to the ' + A_Name + ' for training? ' )

                            while True :

                                if Train_Limit == 0 :
                                    break

                                if Back == 1 :
                                    break
                                
                                try :

                                    Num = int( User_Input ( random.choice( ID ) ) )

                                    if Num > MD :
                                        Text_Formatting ( 88, ( 88 * ' ' ) + '    You dont have that many ' + MD_Name + ' units available for training. ' )

                                    else :
                                        if Train_Limit >= Num :
                                            MD -= Num
                                            A_MDTrain += Num
                                            Train_Limit -= Num
                                            Back = 1
                                            break

                                        else :
                                            Text_Formatting ( 88, ( 88 * ' ' ) + '    You aren\'t able to train that many more Units. You can train ' + str( Train_Limit ) + ' more Units. ' )
                                            
                                except :
                                    Unknown_Input ( )

                        else :
                            Text_Formatting ( 88, '    You dont have any ' + MD_Name + ' units available for training. ' )

                    elif Basic == 'Back' :
                        break

                    else :
                        Unknown_Input ( )

                elif Type == 'Spec' :

                    if CM > 0 :

                        Text_Formatting ( 88, ( 88 * ' ' ) + '    How many ' + CM_Name + ' units would you like to send to the ' + A_Name + ' for training? ' )

                        while True :

                            if Train_Limit == 0 :
                                break

                            if Back == 1 :
                                break
                            
                            try :

                                Num = int( User_Input ( random.choice( ID ) ) )

                                if Num > CM :
                                    Text_Formatting ( 88, ( 88 * ' ' ) + '    You dont have that many ' + CM_Name + ' units available for training. ' )

                                else :
                                    if Train_Limit >= Num :
                                        CM -= Num
                                        A_CMTrain += Num
                                        Train_Limit -= Num
                                        Back = 1
                                        break

                                    else :
                                        Text_Formatting ( 88, ( 88 * ' ' ) + '    You aren\'t able to train that many more Units. You can train ' + str( Train_Limit ) + ' more Units. ' )
                                        
                            except :
                                Unknown_Input ( )

                    else :
                        Text_Formatting ( 88, '    You dont have any ' + CM_Name + ' units available for training. ' )

                elif Type == 'Back' :
                    break

                else :
                    Unknown_Input ( )

        elif Train == 'Back' :
            if Train_Limit_Check == Train_Limit :
                return Actions
            else :
                Actions -= 1
                return Actions

        else :
            Unknown_Input ( ) 
    
#==================================================================================================
# RANDOM VARIATION #
#==================================================================================================

def Random_Variation ( x, c ) :

    Variation_List = []
    a = 0
    b = ( c + 1 )

    if c == 0 :

        return x

    else :
        
        for i in range( ( - c ), ( c + 1 ) ) :

            if a < b :
                a += 1
            else :
                a -= 1
                b = a

            for j in range( a ) :

                Variation_List.append( i )

        y = random.choice(Variation_List)

        return y + x

#==================================================================================================
# COMBAT OPTIONS #
#==================================================================================================

def Combat_Commitment ( ) :

    Text_Formatting (88, ( 88 * ' ' ) + '    Do you want to commit your Forces?                Yes | No ' )    

    while True :
        try :
            
            Commit = str( User_Input ( random.choice( ID ) ) )
            if Commit == 'Yes' :
                return Commit
    
            elif Commit == 'No' :
                return Commit
    
            else :
                Unknown_Input ( )

        except :
            continue

#==================================================================================================

def Retreat_Option ( Retreat ) :

    Text_Formatting (88, ( 88 * ' ' ) + '    Would you like to withdraw your forces?                Yes | No ' )
                      
    while True :
        try :
            
            Retreat = str( User_Input ( random.choice( ID ) ) )

            if Retreat == 'Yes' :
                Retreat_Commitment ( Retreat )
                return Retreat

            elif Retreat == 'No' :
                return Retreat
            
            else :
                Unknown_Input ( )

        except :
            continue

#==================================================================================================
        
def Retreat_Commitment ( Retreat ) :

    Text_Formatting (88, ( 88 * ' ' ) + '    Are you sure you\'d like to withdraw your forces?          Yes | No ' )
                      
    while True :
        try :
            
            Retreat = str( User_Input ( random.choice( ID ) ) )

            if Retreat == 'Yes' :
                return Retreat

            elif Retreat == 'No' :
                return Retreat
            
            else :
                Unknown_Input ( )

        except :
            continue

#==================================================================================================
        
def Cancel_Confirmation ( x ) :

    Text_Formatting (88, ( 88 * ' ' ) + '    Are you sure you\'d like to Cancel ' + x + '?                             Yes | No ' )
                      
    while True :
        try :
            
            Cancel = str( User_Input ( random.choice( ID ) ) )

            if Cancel == 'Yes' :
                return Cancel

            elif Cancel == 'No' :
                return Cancel
            
            else :
                Unknown_Input ( )

        except :
            continue

#==================================================================================================

def Deployment_Confirmation ( SO, MD, IT, CM, CT, MT, CO, Count, CH_Count ) : 

    global Requisitions, Subsistence

    Dtot = ( SO + MD + IT + CM + CT + MT + CO )
    Req_Cost = ( ( SO + MD + IT + CM + CT + MT + CO ) // 2 ) * ( Count + 1 )
    Sub_Cost = ( ( SO + MD + IT + CM + CT + MT + CO ) // 3 ) * ( Count )

    SOs, MDs, ITs, CMs, CTs, MTs, = '','','','','','',

    if SO > 1 :
        SOs = 's'
    elif SO == 0 :
        SOs = 's'
    if MD > 1 :
        MDs = 's'
    elif MD == 0 :
        MDs = 's'
    if IT > 1 :
        ITs = 's'
    elif IT == 0 :
        ITs = 's'
    if CM > 1 :
        CMs = 's'
    elif CM == 0 :
        CMs = 's'
    if CT > 1 :
        CTs = 's'
    elif CT == 0 :
        CTs = 's'
    if MT > 1 :
        MTs = 's'
    elif MT == 0 :
        MTs = 's'
    if CO == 1 :
        COs = ' to '
    elif CO == 0 :
        COs = ' not to '
        
    if Dtot < 1 :
        Text_Formatting ( 88, ( 88 * ' ' ) + '     You have not deployed any of your available forces. ' )
        User_Input ( random.choice( ID ) )
        return 'No'   

    if CH_Count > 0 :
            
        CH_Limit = CH_Count * 8
            
        if Dtot > CH_Limit :

            Text_Formatting ( 88, ( 88 * ' ' ) + '    You can\'t deploy more forces than your Choppers can transport. ' )
            return 'No'

    Text_Formatting ( 88, ( 88 * ' ' ) + '    You have selected the following forces for deployment: ' )
    Text_Formatting ( 88, \
      ( 88 * ' ' ) + '    ' + str( SO ) + ' ' + SO_Name + SOs + ( ( 88 - len( '    ' + str( SO ) + ' ' + SO_Name + SOs  ) ) * ' ' ) +
      ( 88 * ' ' ) + '    ' + str( MD ) + ' ' + MD_Name + MDs + ( ( 88 - len( '    ' + str( MD ) + ' ' + MD_Name + MDs  ) ) * ' ' ) +
      ( 88 * ' ' ) + '    ' + str( IT ) + ' ' + IT_Name + ITs + ( ( 88 - len( '    ' + str( IT ) + ' ' + IT_Name + ITs  ) ) * ' ' ) +
      ( 88 * ' ' ) + '    ' + str( CM ) + ' ' + CM_Name + CMs + ( ( 88 - len( '    ' + str( CM ) + ' ' + CM_Name + CMs  ) ) * ' ' ) +
      ( 88 * ' ' ) + '    ' + str( CT ) + ' ' + CT_Name + CTs + ( ( 88 - len( '    ' + str( CT ) + ' ' + CT_Name + CTs  ) ) * ' ' ) +
      ( 88 * ' ' ) + '    ' + str( MT ) + ' ' + MT_Name + MTs + ( ( 88 - len( '    ' + str( MT ) + ' ' + MT_Name + MTs  ) ) * ' ' ) +
      ( 88 * ' ' ) + '    You have chosen' + COs + 'deploy a ' + CO_Name + ( ( 88 - len( '    You have chosen' + COs + 'deploy a ' + CO_Name ) ) * ' ' ) )
                         
    Text_Formatting ( 88, ( 88 * ' ' ) + '    It will cost ' + str( Req_Cost ) + ' Requisitions and ' + str( Sub_Cost ) + ' Subsistence to deploy these forces. ' )

    while True :

        Text_Formatting ( 88, ( 88 * ' ' ) + '    Confirm Deployment of these forces?                 Yes | No | Cancel ' )
        Confirm = User_Input ( random.choice( ID ) ) 

        if Confirm == 'Yes' :
            Requisitions -= Req_Cost
            Subsistence -= Sub_Cost
            return 'Yes'
            break
        
        elif Confirm == 'No' :
            return 'No'
            break

        elif Confirm == 'Cancel' :
            return 'Cancel'
                            
                             
        else :
            Unknown_Input ( )
                
#==================================================================================================
# DEPLOYMENT NUMBERS #
#==================================================================================================
            
def Deployment_Numbers ( Count, CH_Count ) :

    global SO
    if CH_Count > 0 :
        CH_Limit = CH_Count * 8
        Text_Formatting ( 88, ( 88 * ' ' ) + '    The Choppers you\'ve deployed can transport ' + str( CH_Limit ) + ' of your troops for this operation. ' )
        User_Input ( random.choice( ID ) )
 
    if SO > 0 :

        Text_Formatting ( 88, ( 88 * ' ' ) + '    How many ' + SO_Name + 's would you like to deploy on this operation? ' )
        Text_Formatting ( 88, ( 88 * ' ' ) + '    You have ' + str( SO ) + ' ' + SO_Name + ' units available to Deploy. ' )
        
        while True :
            try :
                
                localSO = int( User_Input ( random.choice( ID ) ) )
                
                if localSO > SO :
                    
                    Not_Enough_Forces ( SO_Name )
                    
                else:
                    break
            
            except :
                Unknown_Input ( )

    else :
        localSO = 0

    #==================================================================================================

    global MD
    if MD > 0 :

        Text_Formatting ( 88, ( 88 * ' ' ) + '    How many ' + MD_Name + 's would you like to deploy on this operation? ' )
        Text_Formatting ( 88, ( 88 * ' ' ) + '    You have ' + str( MD ) + ' ' + MD_Name + ' units available to Deploy. ' )

        while True :
            try :
                
                localMD = int( User_Input ( random.choice( ID ) ) )
                
                if localMD > MD :
                    
                    Not_Enough_Forces ( MD_Name )
                    
                else:
                    break
            
            except :
                Unknown_Input ( )

    else :
        localMD = 0

    #==================================================================================================

    global IT
    if IT > 0 :

        Text_Formatting ( 88, ( 88 * ' ' ) + '    How many ' + IT_Name + 's would you like to deploy on this operation? ' )
        Text_Formatting ( 88, ( 88 * ' ' ) + '    You have ' + str( IT ) + ' ' + IT_Name + ' units available to Deploy. ' )
    
        while True :
            try :
                
                localIT = int( User_Input ( random.choice( ID ) ) )

                if localIT > IT :
                    
                    Not_Enough_Forces ( IT_Name )
                    
                else:
                    break
            
            except :
                Unknown_Input ( )

    else :
        localIT = 0
             
    #==================================================================================================

    global CM
    if CM > 0 :

        Text_Formatting ( 88, ( 88 * ' ' ) + '    How many ' + CM_Name + 's would you like to deploy on this operation? ' )
        Text_Formatting ( 88, ( 88 * ' ' ) + '    You have ' + str( CM ) + ' ' + CM_Name + ' units available to Deploy. ' )
    
        while True :
            try :
                
                localCM = int( User_Input ( random.choice( ID ) ) )

                if localCM > CM :
                    
                    Not_Enough_Forces ( CM_Name )
                    
                else:
                    break
            
            except :
                Unknown_Input ( )

    else :
        localCM = 0

    #==================================================================================================

    global CT
    if CT > 0 :

        Text_Formatting ( 88, ( 88 * ' ' ) + '    How many ' + CT_Name + 's would you like to deploy on this operation? ' )
        Text_Formatting ( 88, ( 88 * ' ' ) + '    You have ' + str( CT ) + ' ' + CT_Name + ' units available to Deploy. ' )
    
        while True :
            try :
                
                localCT = int( User_Input ( random.choice( ID ) ) )

                if localCT > CT :
                    
                    Not_Enough_Forces ( CT_Name )
                    
                else:
                    break
            
            except :
                Unknown_Input ( )

    else :
        localCT = 0


    #==================================================================================================

    global MT
    if MT > 0 :

        Text_Formatting ( 88, ( 88 * ' ' ) + '    How many ' + MT_Name + 's would you like to deploy on this operation? ' )
        Text_Formatting ( 88, ( 88 * ' ' ) + '    You have ' + str( MT ) + ' ' + MT_Name + ' units available to Deploy. ' )
    
        while True :
            try :
                
                localMT = int( User_Input ( random.choice( ID ) ) )

                if localMT > MT :
                    
                    Not_Enough_Forces ( MT_Name )
                    
                else:
                    break
            
            except :
                Unknown_Input ( )

    else :
        localMT = 0

    #==================================================================================================

    global CO
    if CO > 0 :
    
        Text_Formatting ( 88, ( 88 * ' ' ) + '    Would you like to send one ' + CO_Name + '?' )

        while True :
            try :

                localCO = str( User_Input ( random.choice( ID ) ) )
                
                if localCO == 'Yes' :
                    
                    if CO < 1 :
                        Not_Enough_Forces ( CO_Name )
                        continue
                    
                    else :
                        localCO = 1
                        break
                
                elif localCO == 'No' :
                    localCO = 0
                    break
                
                else:
                    Unknown_Input ( )
                    
            except :
                Unknown_Input ( )

    else :
        localCO = 0

    while True :
        
        Confirm = Deployment_Confirmation ( localSO, localMD, localIT, localCM, localCT, localMT, localCO, Count, CH_Count )

        if Confirm == 'Yes' :
            SO -= localSO
            MD -= localMD
            IT -= localIT
            CM -= localCM
            CT -= localCT
            MT -= localMT
            CO -= localCO
            return localSO, localMD, localIT, localCM, localCT, localMT, localCO, Count, CH_Count, Confirm
            break

        elif Confirm == 'No' :
            return localSO, localMD, localIT, localCM, localCT, localMT, localCO, Count, CH_Count, Confirm
            break

        elif Confirm == 'Cancel' :
            Cancel = Cancel_Confirmation ( 'force deployment' )
            if Cancel == 'Yes' :
                return localSO, localMD, localIT, localCM, localCT, localMT, localCO, Count, CH_Count, Confirm
                break

        else:
            Unknown_Input ( )
     
#==================================================================================================
# INPUT ERRORS #
#==================================================================================================
    
def Unknown_Input ( ) :

    Text_Formatting ( 88, ( 88 * ' ' ) + '    Unrecognized Input    ' )

#==================================================================================================

def Not_Enough_Forces ( x ) :

    Text_Formatting ( 88, ( 88 * ' ' ) + '    You dont have that many available ' + x + 's to deploy. ' )
    
#==================================================================================================
# COMBAT!!! #
#==================================================================================================
    
def Operation_Combat ( SO, MD, IT, CM, CT, MT, CO, ESO, EMD, EIT, ECM, ECT, EMT, ECO, First ) :
    
    #==================================================================================================
    # YOUR LOCAL COMBAT VARIABLES #
    #==================================================================================================

    Retreat = 'unsure'
    
    if CO == 1 :
        CO_Boost = 1.2
    else :
        CO_Boost = 1

    Medical_Strength = ( ( MD * 2 ) + CM + MT ) * CO_Boost
    Combat_Strength  = ( ( SO * 2 ) + CM + CT ) * CO_Boost
    Tech_Strength    = ( ( IT * 2 ) + CT + MT ) * CO_Boost

    if Combat_Strength != 0 :
        Combat_Bonus = round( ( ( 1 / ( Combat_Strength ** 0.25 ) ) * Combat_Strength * 0.05 ) * 100 )
    else :
        Combat_Bonus = 0

    if Medical_Strength != 0 :
        Revive_Chance = ( 1 / ( Medical_Strength ** 0.25 ) ) * Medical_Strength * 0.05 
        if Revive_Chance > 0.90 :
            Revive_Chance = 0.90
    else :
        Revive_Chance = 0
        
    R = round( Revive_Chance * 100 )
    Rn = round( ( 1 - Revive_Chance ) * 100 )
    Revive_Chance = []
    for i in range( R ) :
        Revive_Chance.append( 1 )
    for i in range( Rn ) :
        Revive_Chance.append( 0 )

    global Morale
    Morale_Boost = Morale / 10

    Forces_List = []
    for i in range( SO ) :
        Forces_List.append( 'Soldier' )
    for i in range( MD ) :
        Forces_List.append( 'Medic' )
    for i in range( IT ) :
        Forces_List.append( 'Technician' )
    for i in range( CM ) :
        Forces_List.append( 'Combat Medic' )
    for i in range( CT ) :
        Forces_List.append( 'Combat Technician' )
    for i in range( MT ) :
        Forces_List.append( 'Medical Technician' )
    SO, MD, IT, CM, CT, MT = 0,0,0,0,0,0

    #==================================================================================================
    # ENEMY LOCAL COMBAT VARIABLES #
    #==================================================================================================
    
    if ECO == 1 :
        ECO_Boost = 1.2
    else :
        ECO_Boost = 1

    EMedical_Strength = ( ( EMD * 2 ) + ECM + EMT ) * ECO_Boost
    ECombat_Strength  = ( ( ESO * 2 ) + ECM + ECT ) * ECO_Boost
    ETech_Strength    = ( ( EIT * 2 ) + ECT + EMT ) * ECO_Boost

    if ECombat_Strength != 0 :
        ECombat_Bonus = round( ( ( 1 / ( ECombat_Strength ** 0.25 ) ) * ECombat_Strength * 0.05 ) * 100 )
    else :
        ECombat_Bonus = 0
        
    if EMedical_Strength != 0 :
        ERevive_Chance = ( 1 / ( EMedical_Strength ** 0.25 ) ) * EMedical_Strength * 0.05 
        if ERevive_Chance > 0.90 :
            ERevive_Chance = 0.90
    else :
        ERevive_Chance = 0
        
    ER = round( ERevive_Chance * 100 )
    ERn = round( ( 1 - ERevive_Chance ) * 100 )
    ERevive_Chance = []
    for i in range( ER ) :
        ERevive_Chance.append( 1 )
    for i in range( ERn ) :
        ERevive_Chance.append( 0 )

    EForces_List = []
    for i in range( ESO ) :
        EForces_List.append( 'Soldier' )
    for i in range( EMD ) :
        EForces_List.append( 'Medic' )
    for i in range( EIT ) :
        EForces_List.append( 'Technician' )
    for i in range( ECM ) :
        EForces_List.append( 'Combat Medic' )
    for i in range( ECT ) :
        EForces_List.append( 'Combat Technician' )
    for i in range( EMT ) :
        EForces_List.append( 'Medical Technician' )
        
    #==================================================================================================

    Commit = Combat_Commitment ( )

    while True :
    
        if Commit == 'Yes' :

            Pre_Combat = len( Forces_List )
            
            if First == 1 :
                Att_Rev = Revive_Chance
                Def_Rev = ERevive_Chance
                Attacker = Forces_List
                Defender = EForces_List
                Att_Name = 'Your forces'
                Def_Name = 'The enemies forces'
                Att_Com_Bonus = Combat_Bonus
                Def_Com_Bonus = ECombat_Bonus
                
            else :
                Att_Rev = ERevive_Chance
                Def_Rev = Revive_Chance
                Attacker = EForces_List
                Defender = Forces_List
                Att_Name = 'The enemies forces'
                Def_Name = 'Your Forces'
                Att_Com_Bonus = ECombat_Bonus
                Def_Com_Bonus = Combat_Bonus

            Text_Formatting ( 88, '    Combat Event Log : ' )

            print( Dialogue_Box_Top ( ) )
            print('    |' + ( 90 * ' ' ) + '|' )
            
            while len( Attacker ) > 0 and len( Defender ) > 0 :

                for i in Attacker :
                    
                    for j in Defender :

                        i = 'Att Win'
                        j = 'Def Win'
                                            
                        Win_Chance_List = []
                        Att_Losses      = []
                        Def_Losses      = []

                               
                        for a in range( Att_Com_Bonus ) :
                            Win_Chance_List.append( i )
                        for a in range( Def_Com_Bonus ) :
                            Win_Chance_List.append( j )
                        
                        Win_Chance = random.choice( Win_Chance_List )
                        
                        if Win_Chance == 'Att Win' :
                            print('    |     ' + Def_Name + ' have suffered a casualty!' + ( 90 - len('     ' + Def_Name +' have suffered a casualty!') ) * ' ' + '|')
                            try :
                                Rev = random.choice(Def_Rev)
                            except :
                                Rev = 0
                            if Rev == 1 :
                                print('    |     But they have been revived!' + ( 90 - len('    But they have been revived!') ) * ' ' + '|')
                            else :
                                try :
                                    
                                    Death = random.choice( Defender )
                                    Defender.remove( Death )
                                    Def_Losses.append( Death )
                                    
                                    if Death == 'Medic' :
                                        for f in range( 6 ) :
                                            while 1 in Def_Rev :
                                                Def_Rev.remove( 1 )
                                                
                                    elif Death == 'Combat Medic' :
                                        for f in range( 3 ) :
                                            while 1 in Def_Rev :
                                                Def_Rev.remove( 1 )
                                                
                                    elif Death == 'Medical Technician' :
                                        for f in range( 3 ) :
                                            while 1 in Def_Rev :
                                                Def_Rev.remove( 1 )
                                                
                                    print('    |     A ' + Death + ' has been killed!' + ( 90 - len('     A ' + Death + ' has been killed!') ) * ' ' + '|')

                                except :
                                    None
                                    
                            print('    |' + ( 90 * ' ' ) + '|' )
                            
                        elif Win_Chance == 'Def Win' :
                            print('    |     ' + Att_Name + ' have suffered a casualty!' + ( 90 - len('     ' + Att_Name + ' have suffered a casualty!') ) * ' ' + '|')

                            try :
                                Rev = random.choice(Att_Rev)
                            except :
                                Rev = 0
                            if Rev == 1 :
                                print('    |     But they have been revived!' + ( 90 - len('     But they have been revived!') ) * ' ' + '|')
                            else :
                                try :
                                    
                                    Death = random.choice( Attacker )
                                    Attacker.remove( Death )
                                    Att_Losses.append( Death )
                                    
                                    if Death == 'Medic' :
                                        for f in range( 65 ) :
                                            while 1 in Att_Rev :
                                                Att_Rev.remove( 1 )
                                                
                                    elif Death == 'Combat Medic' :
                                        for f in range( 3 ) :
                                            while 1 in Att_Rev :
                                                Att_Rev.remove( 1 )
                                                
                                    elif Death == 'Medical Technician' :
                                        for f in range( 3 ) :
                                            while 1 in Att_Rev :
                                                Att_Rev.remove( 1 )
                                                    
                                    print('    |     A ' + Death + ' has been killed!' + ( 90 - len('     A ' + Death + ' has been killed!') ) * ' ' + '|')

                                except :
                                    None
                                    
                            print('    |' + ( 90 * ' ' ) + '|' )

    
            print( Dialogue_Box_Bottom ( ) )
    
            if First == 1 :

                Loss = Pre_Combat - len( Attacker )

                for i in Attacker : 
                    if i == 'Soldier' :
                        SO += 1
                    elif i == 'Medic' :
                        MD += 1
                    elif i == 'Technician' :
                        IT += 1
                    elif i == 'Combat Medic' :
                        CM += 1
                    elif i == 'Combat Technician' :
                        CT += 1
                    elif i == 'Medical Technician' :
                        MT += 1

                        
                print( Dialogue_Box_Top ( ) + '\n\
    |     ' + Att_Name + ' remaining: ' + str( len( Attacker ) ) + ( 90 - len('     ' + Att_Name + ' remaining: ' + str( len( Attacker ) ) ) ) * ' ' + '|\n'
  + Dialogue_Box_Bottom ( ) )
                print( Dialogue_Box_Top ( ) + '\n\
    |     ' + Def_Name + ' remaining: ' + str( len( Defender ) ) + ( 90 - len('     ' + Def_Name + ' remaining: ' + str( len( Defender ) ) ) ) * ' ' + '|\n'
  + Dialogue_Box_Bottom ( ) )
                
            else :

                Loss = Pre_Combat - len( Defender )             

                for i in Defender :
                    if i == 'Soldier' :
                        SO += 1
                    elif i == 'Medic' :
                        MD += 1
                    elif i == 'Technician' :
                        IT += 1
                    elif i == 'Combat Medic' :
                        CM += 1
                    elif i == 'Combat Technician' :
                        CT += 1
                    elif i == 'Medical Technician' :
                        MT += 1
                        
                print( Dialogue_Box_Top ( ) + '\n\
    |     ' + Def_Name + ' remaining: ' + str( len( Defender ) ) + ( 90 - len('     ' + Def_Name + ' remaining: ' + str( len( Defender ) ) ) ) * ' ' + '|\n'
  + Dialogue_Box_Bottom ( ) )
                print( Dialogue_Box_Top ( ) + '\n\
    |     ' + Att_Name + ' remaining: ' + str( len( Attacker ) ) + ( 90 - len('     ' + Att_Name + ' remaining: ' + str( len( Attacker ) ) ) ) * ' ' + '|\n'
  + Dialogue_Box_Bottom ( ) )

            Morale -= ( M_Loss * Loss )
            
            if SO + MD + IT + CM + CT + MT == 0 :

                Morale -= 10
                return 'Defeat', SO, MD, IT, CM, CT, MT, CO 
            else :
                Morale += 10
                return 'Victory', SO, MD, IT, CM, CT, MT, CO 
                
            
        elif Commit == 'No' :
            Retreat = Retreat_Option ( Retreat )
            
            if Retreat == 'Yes' :
                return SO, MD, IT, CM, CT, MT, CO
                break
            
            else :
                continue

#==================================================================================================
# GLOBAL PERSONEL VARIABLES UPDATER #
#==================================================================================================
            
def Post_Combat_Blues ( localSO, localMD, localIT, localCM, localCT, localMT, localCO ) :
    global SO, MD, IT, CM, CT, MT, CO
    SO += localSO
    MD += localMD
    IT += localIT
    CM += localCM
    CT += localCT
    MT += localMT
    CO += localCO

#==================================================================================================
# GAME LOSE CHECKS #
#==================================================================================================     

def Starvation ( ) :

    global  Morale, Requisitions, Subsistence, Discretion, \
            SO, MD, IT, CM, CT, MT, CC, \
            FW_Cost, CH_Cost, H, A, M_Loss,\
            B_CCTrain, B_MDTrain, B_ITTrain, B_MTTrain,\
            H_CCTrain, H_SOTrain, H_ITTrain, H_CTTrain,\
            A_CCTrain, A_SOTrain, A_MDTrain, A_CMTrain,\
            B_Teach, H_Teach, A_Teach, FARM_Work, FACT_Work, Pilot
    
    if Subsistence < 0 : 

        for i in range( abs( Subsistence // 3 ) ) :

            Death_List = []
            Subsistence += 1            
                        
            for i in range( SO ) :
                Death_List.append( SO_Name )

            for i in range( MD ) :
                Death_List.append( MD_Name )

            for i in range( IT ) :
                Death_List.append( IT_Name )

            for i in range( CM ) :
                Death_List.append( CM_Name )

            for i in range( CT ) :
                Death_List.append( CT_Name )

            for i in range( MT ) :
                Death_List.append( MT_Name )

            for i in range( CC ) :
                Death_List.append( CC_Name )

            for i in range( B_CCTrain ) :
                Death_List.append( CC_Name + ' in training at your ' + B_Name )

            for i in range( B_ITTrain ) :
                Death_List.append( IT_Name + ' in training at your ' + B_Name )

            for i in range( B_MDTrain ) :
                Death_List.append( MD_Name + ' in training at your ' + B_Name )

            for i in range( B_MTTrain ) :
                Death_List.append( MT_Name + ' in training at your ' + B_Name )

            for i in range( H_CCTrain ) :
                Death_List.append( CC_Name + ' in training at your ' + H_Name )

            for i in range( H_SOTrain ) :
                Death_List.append( SO_Name + ' in training at your ' + H_Name )

            for i in range( H_ITTrain ) :
                Death_List.append( IT_Name + ' in training at your ' + H_Name )

            for i in range( H_CTTrain ) :
                Death_List.append( CT_Name + ' in training at your ' + H_Name )

            for i in range( A_CCTrain ) :
                Death_List.append( CC_Name + ' in training at your ' + A_Name )

            for i in range( A_SOTrain ) :
                Death_List.append( SO_Name + ' in training at your ' + A_Name )

            for i in range( A_MDTrain ) :
                Death_List.append( MD_Name + ' in training at your ' + A_Name )

            for i in range( A_CMTrain ) :
                Death_List.append( CM_Name + ' in training at your ' + A_Name )

            for i in range( B_Teach ) :
                Death_List.append( SO_Name + ' acting as an instructor ' )

            for i in range( H_Teach ) :
                Death_List.append( MD_Name + ' acting as an instructor ' )

            for i in range( A_Teach ) :
                Death_List.append( IT_Name + ' acting as an instructor ' )

            for i in range( FARM_Work ) :
                Death_List.append( CC_Name + ' working a ' + FARM_Name )

            for i in range( FACT_Work ) :
                Death_List.append( CC_Name + ' working a ' + FACT_Name )

            for i in range( Pilot ) :
                Death_List.append( IT_Name + ' piloting a ' + CH_Name )

            if len( Death_List ) > 0:
                Death = random.choice( Death_List )
            
                Text_Formatting ( 88, ( 88 * ' ' ) + '    A ' + Death + ' starved to death. ' )
                Morale -= 1
                
                if Death == SO_Name :
                    SO -= 1

                if Death == MD_Name :
                    MD -= 1

                if Death == IT_Name :
                    IT -= 1

                if Death == CM_Name :
                    CM -= 1

                if Death == CT_Name :
                    CT -= 1

                if Death == MT_Name :
                    MT -= 1

                if Death == CC_Name :
                    CC -= 1

                if Death == CC_Name + ' in training at your ' + B_Name :
                    B_CCTrain -= 1

                if Death == IT_Name + ' in training at your ' + B_Name :
                    B_ITTrain -= 1

                if Death == MD_Name + ' in training at your ' + B_Name :
                    B_MDTrain -= 1

                if Death == MT_Name + ' in training at your ' + B_Name :
                    B_MTTrain -= 1

                if Death == CC_Name + ' in training at your ' + H_Name :
                    H_CCTrain -= 1

                if Death == SO_Name + ' in training at your ' + H_Name :
                    H_SOTrain -= 1

                if Death == IT_Name + ' in training at your ' + H_Name :
                    H_ITTrain -= 1

                if Death == CT_Name + ' in training at your ' + H_Name :
                    H_CTTrain -= 1

                if Death == CC_Name + ' in training at your ' + A_Name :
                    B_CCTrain -= 1

                if Death == SO_Name + ' in training at your ' + A_Name :
                    B_SOTrain -= 1

                if Death == MD_Name + ' in training at your ' + A_Name :
                    B_MDTrain -= 1

                if Death == CM_Name + ' in training at your ' + A_Name :
                    B_CMTrain -= 1

                if Death == SO_Name + ' acting as an instructor ' :
                    B_Teach -= 1

                if Death == MD_Name + ' acting as an instructor ' :
                    H_Teach -= 1

                if Death == IT_Name + ' acting as an instructor ' :
                    A_Teach -= 1

                if Death == CC_Name + ' working a ' + FARM_Name :
                    FARM_Work -= 1

                if Death == CC_Name + ' working a ' + FACT_Name :
                    FACT_Work -= 1

                if Death == IT_Name + ' piloting a ' + CH_Name :
                    Pilot -= 1

            else :
                return 'Lose'

        return 'Continue'

#==================================================================================================

def Make_Like_A_Tree ( ) :
    
    global  Morale, Requisitions, Subsistence, Discretion, \
            SO, MD, IT, CM, CT, MT, CC, \
            FW_Cost, CH_Cost, H, A, M_Loss,\
            B_CCTrain, B_MDTrain, B_ITTrain, B_MTTrain,\
            H_CCTrain, H_SOTrain, H_ITTrain, H_CTTrain,\
            A_CCTrain, A_SOTrain, A_MDTrain, A_CMTrain,\
            B_Teach, H_Teach, A_Teach, FARM_Work, FACT_Work, Pilot

    if Morale < 0 :

        for i in range( abs( Morale ) ) :

            Leave_List = []
            Morale += 1

            for i in range( SO ) :
                Leave_List.append( SO_Name )

            for i in range( MD ) :
                Leave_List.append( MD_Name )

            for i in range( IT ) :
                Leave_List.append( IT_Name )

            for i in range( CM ) :
                Leave_List.append( CM_Name )

            for i in range( CT ) :
                Leave_List.append( CT_Name )

            for i in range( MT ) :
                Leave_List.append( MT_Name )

            for i in range( CC ) :
                Leave_List.append( CC_Name )

            for i in range( B_CCTrain ) :
                Leave_List.append( CC_Name + ' in training at your ' + B_Name )

            for i in range( B_ITTrain ) :
                Leave_List.append( IT_Name + ' in training at your ' + B_Name )

            for i in range( B_MDTrain ) :
                Leave_List.append( MD_Name + ' in training at your ' + B_Name )

            for i in range( B_MTTrain ) :
                Leave_List.append( MT_Name + ' in training at your ' + B_Name )

            for i in range( H_CCTrain ) :
                Leave_List.append( CC_Name + ' in training at your ' + H_Name )

            for i in range( H_SOTrain ) :
                Leave_List.append( SO_Name + ' in training at your ' + H_Name )

            for i in range( H_ITTrain ) :
                Leave_List.append( IT_Name + ' in training at your ' + H_Name )

            for i in range( H_CTTrain ) :
                Leave_List.append( CT_Name + ' in training at your ' + H_Name )

            for i in range( A_CCTrain ) :
                Leave_List.append( CC_Name + ' in training at your ' + A_Name )

            for i in range( A_SOTrain ) :
                Leave_List.append( SO_Name + ' in training at your ' + A_Name )

            for i in range( A_MDTrain ) :
                Leave_List.append( MD_Name + ' in training at your ' + A_Name )

            for i in range( A_CMTrain ) :
                Leave_List.append( CM_Name + ' in training at your ' + A_Name )

            for i in range( B_Teach ) :
                Leave_List.append( SO_Name + ' acting as an instructor ' )

            for i in range( H_Teach ) :
                Leave_List.append( MD_Name + ' acting as an instructor ' )

            for i in range( A_Teach ) :
                Leave_List.append( IT_Name + ' acting as an instructor ' )

            for i in range( FARM_Work ) :
                Leave_List.append( CC_Name + ' working a ' + FARM_Name )

            for i in range( FACT_Work ) :
                Leave_List.append( CC_Name + ' working a ' + FACT_Name )

            for i in range( Pilot ) :
                Leave_List.append( IT_Name + ' piloting a ' + CH_Name )

            if len( Leave_List ) > 0:
                Leave = random.choice( Leave_List )

                Text_Formatting ( 88, ( 88 * ' ' ) + '    A ' + Leave + ' has deserted. ' )

                if Leave == SO_Name :
                    SO -= 1

                if Leave == MD_Name :
                    MD -= 1

                if Leave == IT_Name :
                    IT -= 1

                if Leave == CM_Name :
                    CM -= 1

                if Leave == CT_Name :
                    CT -= 1

                if Leave == MT_Name :
                    MT -= 1

                if Leave == CC_Name :
                    CC -= 1

                if Leave == CC_Name + ' in training at your ' + B_Name :
                    B_CCTrain -= 1

                if Leave == IT_Name + ' in training at your ' + B_Name :
                    B_ITTrain -= 1

                if Leave == MD_Name + ' in training at your ' + B_Name :
                    B_MDTrain -= 1

                if Leave == MT_Name + ' in training at your ' + B_Name :
                    B_MTTrain -= 1

                if Leave == CC_Name + ' in training at your ' + H_Name :
                    H_CCTrain -= 1

                if Leave == SO_Name + ' in training at your ' + H_Name :
                    H_SOTrain -= 1

                if Leave == IT_Name + ' in training at your ' + H_Name :
                    H_ITTrain -= 1

                if Leave == CT_Name + ' in training at your ' + H_Name :
                    H_CTTrain -= 1

                if Leave == CC_Name + ' in training at your ' + A_Name :
                    B_CCTrain -= 1

                if Leave == SO_Name + ' in training at your ' + A_Name :
                    B_SOTrain -= 1

                if Leave == MD_Name + ' in training at your ' + A_Name :
                    B_MDTrain -= 1

                if Leave == CM_Name + ' in training at your ' + A_Name :
                    B_CMTrain -= 1

                if Leave == SO_Name + ' acting as an instructor ' :
                    B_Teach -= 1

                if Leave == MD_Name + ' acting as an instructor ' :
                    H_Teach -= 1

                if Leave == IT_Name + ' acting as an instructor ' :
                    A_Teach -= 1

                if Leave == CC_Name + ' working a ' + FARM_Name :
                    FARM_Work -= 1

                if Leave == CC_Name + ' working a ' + FACT_Name :
                    FACT_Work -= 1

                if Leave == IT_Name + ' piloting a ' + CH_Name :
                    Pilot -= 1

            else :
                return 'Lose'

        return 'Continue'

#==================================================================================================
# OPERATION NAMING #
#==================================================================================================

def Operation_Name ( ) :

    while True :
        
        Text_Formatting ( 88, ( 88 * ' ' ) + '    What will you name this Operation? ' )

        NAME = User_Input ( random.choice( ID ) )

        if len( NAME ) > 35 :                    
            Text_Formatting ( 88, ( 88 * ' ' ) + '    The name you have entered is too long ' )
            
        elif len( NAME ) < 35 :

            if len( NAME ) < 1 :
                Text_Formatting ( 88, ( 88 * ' ' ) + '    You have not entered a name for this Operation ' )
            
            elif len( NAME ) > 0 :

                if len ( Op_Name_List ) == 0 :

                    Op_Name_List.append( NAME )
                    return NAME
                    break

                elif len ( Op_Name_List ) > 0 :

                    if NAME in Op_Name_List :

                        Text_Formatting ( 88, '    You have already use that name. ' )

                    else :
                        
                        Op_Name_List.append( NAME )
                        return NAME
                        break

#==================================================================================================
# ALL OPERATIONS #
#==================================================================================================

def Operation_Variation ( Op_Text1, Op_Text2, Op_Text_Com, Op_Text_Pac, Op_Text_Win, Op_Text_Lose, Delay, Delay_Var, ESO_Var, EMD_Var, EIT_Var, ECM_Var, ECT_Var, EMT_Var, ECO_Var, ESO, EMD, EIT, ECM, ECT, EMT, ECO, First, CC_Var, CC_Reward, Req_Var, Req_Reward, Sub_Var, Sub_Reward, Op_Number ) :

    global DAY
    
    Event_Day  = Random_Variation ( ( DAY + Delay ) , Delay_Var )
    if Event_Day < DAY :
        Event_Day = DAY
    ESO        = Random_Variation ( ESO, ESO_Var )
    if ESO < 0 :
        ESO = 0
    EMD        = Random_Variation ( EMD, EMD_Var )
    if EMD < 0 :
        EMD = 0
    EIT        = Random_Variation ( EIT, EIT_Var )
    if EIT < 0 :
        EIT = 0
    ECM        = Random_Variation ( ECM, ECM_Var )
    if ECM < 0 :
        ECM = 0
    ECT        = Random_Variation ( ECT, ECT_Var )
    if ECT < 0 :
        ECT = 0
    EMT        = Random_Variation ( EMT, EMT_Var )
    if EMT < 0 :
        EMT = 0
    ECO        = Random_Variation ( ECO, ECO_Var )
    if ECO < 0 :
        ECO = 0

    CC_Reward  = Random_Variation ( CC_Reward, CC_Var   )
    if CC_Reward < 0 :
        CC_Reward = 0
    Req_Reward = Random_Variation ( Req_Reward, Req_Var )
    if Req_Reward < 0 :
        Req_Reward = 0
    Sub_Reward = Random_Variation ( Sub_Reward, Sub_Var )
    if Sub_Reward < 0 :
        Sub_Reward = 0

    Op_Number  = Random_Variation ( Op_Number, 1000 ) 
    
    Operation_Prompt ( Op_Text1, Op_Text2, Op_Text_Com, Op_Text_Pac, Op_Text_Win, Op_Text_Lose, Event_Day, ESO, EMD, EIT, ECM, ECT, EMT, ECO, First, CC_Reward, Req_Reward, Sub_Reward, Op_Number )

#==================================================================================================

def Operation_Prompt ( Op_Text1, Op_Text2, Op_Text_Com, Op_Text_Pac, Op_Text_Win, Op_Text_Lose, Event_Day, ESO, EMD, EIT, ECM, ECT, EMT, ECO, First, CC_Reward, Req_Reward, Sub_Reward, Op_Number) :
    

    global CH, Requisitions, Discretion

    if len( Op_Text1 ) > 0 :
        Op_Text_Current = Op_Text1
    else :
        Op_Text_Current = 'A small force is roaming the ruins of the worlds nearby. ' 

    Text_Formatting ( 88, Op_Text_Current )
    User_Input ( random.choice( ID ) )
    
    Text_Formatting ( 88, Day_Format ( Event_Day - DAY ) )
    User_Input ( random.choice( ID ) )

    Text_Formatting ( 88, ( 88 * ' ' ) + '    Do you want to undertake this Operation?                   Deploy | Ignore ' )

    CH_Count = 0
    Choppers = 'No'

    while True :

        Choice = User_Input ( random.choice( ID ) )

        if Choice == 'Ignore' :
            
            break  

        elif Choice == 'Deploy' :

            NAME = Operation_Name ( )
            
            if Event_Day - DAY == 0 :

                break

            if Event_Day - DAY > 0 :

                if CH == 0 :

                    break

                elif CH > 0 :
                
                    Text_Formatting ( 88, '    This Operation is far enough out that your forces may utilize ' + CH_Name + 's to arrive immediately. It will '       +
                                      'cost 10 requisitions per ' + CH_Name + ' you send out on this Operation, and doing so will reduce your Discretion by an '     +
                                      'additional 5 points per ' + CH_Name + '. You currently have ' + str( Discretion ) + ' Discretion and ' + str( Requisitions )  +
                                      ' Requisitions to spare. Each ' + CH_Name + ' can deploy only 8 units, however deploying you forces via ' + CH_Name + ' will ' +
                                      'change your EDA to today. ' )

                    while True :

                        Text_Formatting ( 88, ( 88 * ' ' ) + '    Would you like to deploy your forces via ' + CH_Name + '?                Yes | No ' )
                        Choppers = User_Input ( random.choice( ID ) )

                        if Choppers == 'Yes' :
                            break

                        elif Choppers == 'No' :
                            CH_Count = 0
                            break

                        else :
                            Unknown_Input ( )

                    break 
                            
    if Choppers == 'Yes' :

        while True :
        
            try :

                Text_Formatting ( 88, ( 88 * ' ' ) + '    How many ' + CH_Name + 's would you like to deploy? ' )
                CH_Count = int( User_Input ( random.choice( ID ) ) )

                if CH_Count == 0 :
                    break

                elif CH_Count > CH :
                    Text_Formatting ( 88, ( 88 * ' ' ) + '    You do not have that many ' + CH_Name + 's available for deployment. ' )

                elif CH_Count * 10 > Requisitions :
                    Text_Formatting ( 88, ( 88 * ' ' ) + '    You do not have the available Requisitions to deploy that many ' + CH_Name + 's. ' )
                    
                else : 
                    CH -= CH_Count
                    Requisitions -= ( 10 * CH_Count )
                    Discretion -= ( 5 * CH_Count )
                    Event_Day = DAY
                    Count = 0
                    break

            except :
                Unknown_Input ( )
                    
    if Choice == 'Deploy' :

        Count = Event_Day - DAY

        while True :
            
            SO, MD, IT, CM, CT, MT, CO, Count, CH_Count, Confirm = Deployment_Numbers ( Count, CH_Count )
        
            if Confirm == 'Cancel' :
                break

            elif Confirm == 'Yes' :
                Act_Ops  [ Op_Number ] = lambda : Operation_Event ( Op_Text1, Op_Text2,  Op_Text_Com, Op_Text_Pac, Op_Text_Win, Op_Text_Lose, Event_Day, Count, ESO, EMD, EIT, ECM, ECT, EMT, ECO, First, CC_Reward, Req_Reward, Sub_Reward, NAME, SO, MD, IT, CM, CT, MT, CO, CH_Count, Op_Number) 
                Check_Ops[ Op_Number ] = lambda : Operation_Check ( Op_Text1, Event_Day, NAME, SO, MD, IT, CM, CT, MT, CO, Op_Number)
                break
    
#==================================================================================================

def Operation_Check ( Op_Text1, Event_Day, NAME, SO, MD, IT, CM, CT, MT, CO, Op_Number ) :

    Operation_GUI ( NAME, SO, MD, IT, CM, CT, MT, CO, Op_Text1, Event_Day)
    User_Input ( random.choice( ID ) )
    
#==================================================================================================

def Operation_RCheck ( Op_Text_Current, Return_Day, NAME, SO, MD, IT, CM, CT, MT, CO, Outcome, Op_Number ) :
    
    Operation_Return_GUI ( Op_Text_Current, Return_Day, NAME, SO, MD, IT, CM, CT, MT, CO, Outcome ) 
    User_Input ( random.choice( ID ) )

#==================================================================================================

def Operation_Return ( Op_Text_Current, Return_Day, NAME, SO, MD, IT, CM, CT, MT, CO, CH_Count, Outcome, Op_Number, CC_Reward, Req_Reward, Sub_Reward ) :

    global CH
    
    if Return_Day <= DAY :

        Operation_Return_GUI ( Op_Text_Current, Return_Day, NAME, SO, MD, IT, CM, CT, MT, CO, Outcome )

        User_Input ( random.choice( ID ) )

        Post_Combat_Blues ( SO, MD, IT, CM, CT, MT, CO )
        if Outcome == 'Victory' :
            Operation_Rewards ( CC_Reward, Req_Reward, Sub_Reward, NAME )
            CH += CH_Count
        
        Return_Ops    [ Op_Number ] = lambda: Do_Nothing ( )
        RCheck_Ops    [ Op_Number ] = lambda: Do_Nothing ( )
        
#==================================================================================================

def Operation_Event ( Op_Text1, Op_Text2,  Op_Text_Com, Op_Text_Pac, Op_Text_Win, Op_Text_Lose, Event_Day, Count, ESO, EMD, EIT, ECM, ECT, EMT, ECO, First, CC_Reward, Req_Reward, Sub_Reward, NAME, SO, MD, IT, CM, CT, MT, CO, CH_Count, Op_Number) :

    Op_Text_Current = Op_Text1
    Return_Day = DAY + Count
            
    if ( Event_Day - DAY ) == 0 :

        Operation_GUI ( NAME, SO, MD, IT, CM, CT, MT, CO, Op_Text_Current, Event_Day)
        
        User_Input ( random.choice( ID ) )

        if len( Op_Text2 ) > 0 :
            
            Op_Text_Current = Op_Text2
            
        else :
            Op_Text_Current = ( 88 * ' ' ) + '    Your forces have reported in at the rally point for Operation ' + str( NAME ) + '. '


        Text_Formatting ( 88, Op_Text_Current )
        User_Input ( random.choice( ID ) )
            
        if ( ESO + EMD + EIT + ECM + ECT + EMT + ECO ) > 0 :
    
            if len( Op_Text_Com ) > 0 :
                Op_Text_Current = Op_Text_Com

            else :
                Op_Text_Current = ( 88 * ' ' ) + '    There are enemy forces here! '

            Text_Formatting ( 88, Op_Text_Current )
            User_Input ( random.choice( ID ) )

            Outcome, SO, MD, IT, CM, CT, MT, CO  = Operation_Combat ( SO, MD, IT, CM, CT, MT, CO, ESO, EMD, EIT, ECM, ECT, EMT, ECO, First )

            if Outcome == 'Victory' :
                
                if len( Op_Text_Win ) > 0 :
                    Op_Text_Current = Op_Text_Win

                else :
                    Op_Text_Current = ( 88 * ' ' ) + '    Your forces are Victorious! They will return soon! '

                print( '\n\n\n\n\n' )

                for i in Victorious ( ) :
                    print( 30 * ' ' + i )
                    time.sleep(.02)

                print( '\n\n\n\n\n' )
                print( Dialogue_Box_Top ( ) )
                print( Dialogue_Box_Bottom ( ) )
            
                User_Input ( random.choice( ID ) )

                Text_Formatting ( 88, Op_Text_Current )
                User_Input ( random.choice( ID ) )

                RCheck_Ops[ Op_Number ] = lambda : Operation_RCheck  ( Op_Text_Current, Return_Day, NAME, SO, MD, IT, CM, CT, MT, CO, Outcome, Op_Number ) 
                Return_Ops[ Op_Number ] = lambda : Operation_Return  ( Op_Text_Current, Return_Day, NAME, SO, MD, IT, CM, CT, MT, CO, CH_Count, Outcome, Op_Number, CC_Reward, Req_Reward, Sub_Reward ) 

            elif Outcome == 'Defeat' :

                if len( Op_Text_Lose ) > 0 :
                    Op_Text_Current = Op_Text_Lose

                else :
                    Op_Text_Current = ( 88 * ' ' ) + '    Your forces have been Defeated! '

                print( '\n\n\n\n\n' )

                for i in Defeated ( ) :
                    print( 30 * ' ' + i )
                    time.sleep(.02)

                print( '\n\n\n\n\n' )
                print( Dialogue_Box_Top ( ) )
                print( Dialogue_Box_Bottom ( ) )

                User_Input ( random.choice( ID ) )

                Text_Formatting ( 88, Op_Text_Current )
                User_Input ( random.choice( ID ) )

        else :

            if len( Op_Text_Pac ) > 0 :
                Op_Text_Current = Op_Text_Pac

            else :
                Op_Text_Current = ( 88 * ' ' ) + '    There are no enemies in sight. '

            Outcome = 'Victory'
           
            Text_Formatting ( 88, Op_Text_Current )
            User_Input ( random.choice( ID ) )

            print( '\n\n\n\n\n' )

            for i in Victorious ( ) :
                print( 30 * ' ' + i )
                time.sleep(.02)

            print( '\n\n\n\n\n' )
            print( Dialogue_Box_Top ( ) )
            print( Dialogue_Box_Bottom ( ) )

            User_Input ( random.choice( ID ) )
            
            RCheck_Ops[ Op_Number ] = lambda : Operation_RCheck  ( Op_Text_Current, Return_Day, NAME, SO, MD, IT, CM, CT, MT, CO, Outcome, Op_Number ) 
            Return_Ops[ Op_Number ] = lambda : Operation_Return  ( Op_Text_Current, Return_Day, NAME, SO, MD, IT, CM, CT, MT, CO, CH_Count, Outcome, Op_Number, CC_Reward, Req_Reward, Sub_Reward )  

        Ops_History.append( lambda : Operation_History ( Op_Text_Current, Event_Day, NAME, SO, MD, IT, CM, CT, MT, CO, Outcome ) )
        Act_Ops      [ Op_Number ] = lambda: Do_Nothing ( )
        Check_Ops    [ Op_Number ] = lambda: Do_Nothing ( )
        
#==================================================================================================        

def Operation_Rewards ( CC_Reward, Req_Reward, Sub_Reward, NAME ) :

    global CC, Requisitions, Subsistence
    a,b,c = 's','s','s'
    CC += CC_Reward
    Requisitions += Req_Reward
    Subsistence  += Sub_Reward

    if CC_Reward == 1 :
        a = ''
    if Req_Reward == 1 :
        b = ''
    if Sub_Reward == 1 :
        c = ''

    Text_Formatting ( 88, '    Your forces have returned from Operation ' + NAME + ' with the following: ' )
    Text_Formatting ( 88, \
    ( 88 * ' ' ) + '    ' + str( CC_Reward ) + ' ' + CC_Name + a +       ( ( 88 - len( '    ' + str( CC_Reward ) + ' ' + CC_Name + a       ) ) * ' ' ) +\
    ( 88 * ' ' ) + '    ' + str( Req_Reward ) + ' Requisitions' + ( ( 88 - len( '    ' + str( Req_Reward ) + ' Requisitions' ) ) * ' ' ) +\
    ( 88 * ' ' ) + '    ' + str( Sub_Reward ) + ' Subsistence'  + ( ( 88 - len( '    ' + str( Sub_Reward ) + ' Subsistence'  ) ) * ' ' ) )
                  
    User_Input ( random.choice( ID ) )

#==================================================================================================

def Operation_History ( Op_Text_Current, Event_Day, NAME, SO, MD, IT, CM, CT, MT, CO, Outcome ) :

    Operation_Return_GUI ( Op_Text_Current, Event_Day, NAME, SO, MD, IT, CM, CT, MT, CO, Outcome ) 

#====================================================================================================================================================================================================
# FINAL CONFRONTATION #
#====================================================================================================================================================================================================       

def Final_Confrontation ( ) :

    Text_Formatting ( 88, ( 88 * ' ' ) + '    Day ' + str(DAY) + ' ha$s; c0m;`e3`T0o() O;{^%#@c_*l1o0$3!*# #* @* -`\', . *, _ . . .   ., `_ ,  . ' )
    User_Input ( random.choice( ID ) )

    Cascade ( '' )
    
    print( '@@@@@@@!@@@@@@@@@@@@@@@@@@@@!@@@@@@@@@@@@@@@@@@@@@@@@@@@@@!@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@!@@@@@@@@!' )
    print( '@@@@@!:!@@@@@@@@@@!@@@@@@@@!:@@@@!@@@@:@@@!@@@@@!@@@@@@@@! !!@@@@!@@@@!@@@@@@@@!@@@@!@@@@!: !@@@@@!:' )                                                                                                 
    print( '!@@@!: :!@@@@@@@@:  @@@@@@!: @@@ :@@@! @@@: @@@! @@@@@@@!:  :!@@@ @@@!  @@@@@@! !@@@ !@@@:  :!@@@!::' ) 
    print( '!@@@:   !@@@@@@@@  @@@@@@@@  @@@  @@@: @@@@ @@@: @@@@@@@@:   :@@@ @@@: @@@@@@@@ :@@@ :@@@:   !@@@: :' )
    print( ':@@!    :@@!       @@!  @@@  @@!  @@@  @@!@!@@@: @@!  @@@     @@! !@@  @@!  @@@ :@@!  @@@    :@@!   ' )
    print( ':!@!     !@!       !@!  @!@  !@!  @!@  !@!!@!@!  !@!  @!@     !@! @!!  !@!  @!@  !@!  @!@    :!@    ' )
    print( ' !!@     @!!!:!    @!@  !@!  @!@  !@!  @!@ !!@!  @!@  !@!      !@!@!   @!@  !@!  @!@  !@!     @!@   ' )
    print( ' !!!     !!!!!:    !@!  !!!  !@!  !!!  !@!  !!!  !@!  !!!       @!!!   !@!  !!!  !@!  !!!     !!!   ' )
    print( ' !!:     !!:       !!:  !!!  !!:  !!!  !!:  !!!  !!:  !!!       !!:    !!:  !!!  !!:  !!!           ' )
    print( ' :!:     :!:       :!:  !:!  :!:  !:!  :!:  !:!  :!:  !:!       :!:    :!:  !:!  :!:  !:!     :!:   ' )
    print( ' ::      ::       ::::: ::  ::::: ::   ::   ::   :::: ::        ::    ::::: ::  ::::: ::      ::    ' )
    print( ' :        :         : :  :    : :  :   ::    :   :: :  :         :      : :  :    : :  :      :::   ' )

    for i in range ( 6 ) :
        print ( )
        time.sleep(0.5)

    print( Dialogue_Box_Top ( ) )
    print( Dialogue_Box_Bottom ( ) )

    if DAY == 0 :
        Day_Var = 1
    else :
        Day_Var = 1 * ( DAY ** ( 1 / 5 ) ) 

    User_Input ( random.choice( ID ) )
    
    ESO        = round( 20 * Day_Var )
    EMD        = round( 8 * Day_Var )
    EIT        = round( 6 * Day_Var )
    ECM        = round( 4 * Day_Var )
    ECT        = round( 4 * Day_Var )
    EMT        = round( 4 * Day_Var )
    ECO        = 1
    
    First      = 0

#====================================================================================================================================================================================================
# SET OPERATION VARIABLES #
#====================================================================================================================================================================================================       

# Change 'Example' to anything you feel like
def Example_Operation_variables ( ) :

    # This is the Promp Text it should provide enough context that the player can make a resonable decision about what forces to send and how. 
    Op_Text1     = 'The Scans indicate a small amount of activity nearby, It\'s likely a small patrol, Chatter indicates maybe 5 personnel in total '
    # This is the Arrival Text mostly for additional flavour, go crazy.
    Op_Text2     = ''
    # This is the Combat Event Start Text, again it won't change much but will add interest to whatever event you are trying to create.
    Op_Text_Com  = ''
    # This is text for if there are no enemies in this mission. Available so you can create fetch Operations or just exploration style Operations.
    Op_Text_Pac  = ''
    # This is the text displayed on Operation Victory. Both this and the following text only display if there are enemies in the mission and combat actually occurs. 
    Op_Text_Win  = ''
    # This is the text displayed on Operation Defeat.
    Op_Text_Lose = ''


    # This is where you can set the number of enemies,
    # ESO is soldier type
    # EMD is Medic type
    # EIT is Technician type
    # ECM is Combat Medic type
    # EMT is Medical Technician type
    # ECO is Commander Type
    # These Variable should generally match the feel of the Operation established by the text above.
    ESO        = 3
    EMD        = 1
    EIT        = 1
    ECM        = 0
    ECT        = 0
    EMT        = 0
    ECO        = 0

    # Here you can set the amount by which the numbers above may be randomly varied when the operation is called
    # The Variation Function Will add or subtract a numnber in this range.
    # If this number is the same or larger then the unit type count set above there is a chance for there to be no unit of that type in the Operation.
    ESO_Var    = 2
    EMD_Var    = 1
    EIT_Var    = 0
    ECM_Var    = 0
    ECT_Var    = 0
    EMT_Var    = 0
    ECO_Var    = 0
    
    # This sets the Attack Initiative, 1 for Player 0 For enemy
    First      = 1

    # These set the days in the future and the varation amount of that number
    Delay      = 1
    Delay_Var  = 1

    # These variables determine the rewards upon victory, Civilians, Requisitions and Subsistence respectively 
    CC_Reward  = 3
    Req_Reward = 8
    Sub_Reward = 5
    
    # These will vary the above rewards in the same way as with the units
    CC_Var     = 2
    Req_Var    = 5
    Sub_Var    = 3

    # To Avoid Overwriting the operations in the game just make it a string of numbers 
    Op_Number  = 8431
    
    # Only alter the 'Short' part of this list name.
    # can be replaced with Short, Mid or Long
    # Keep in mind shorter ranges should yeild lesser rewards and take less time to arrive. and fro longer, more rewards and more Delay
    
    # Uncomment this to make sure it's added to the dictionary.
    # Short_Operations_List.append( lambda: Operation_Variation ( Op_Text1, Op_Text2, Op_Text_Com, Op_Text_Pac, Op_Text_Win, Op_Text_Lose, Delay, Delay_Var, ESO_Var, EMD_Var, EIT_Var, ECM_Var, ECT_Var, EMT_Var, ECO_Var, ESO, EMD, EIT, ECM, ECT, EMT, ECO, First, CC_Var, CC_Reward, Req_Var, Req_Reward, Sub_Var, Sub_Reward, Op_Number ) ) 

# Finally make sure this matches the function above and uncomment it so it initializes the variables in the dictionary.
# Example_Operation_variables ( )

#==================================================================================================

def BAA_Operation_variables ( ) :

    Op_Text1     = '   There’s a small depot nearby. It’s been under our watch since some survivors made it their supply rudimentary cache. \
It’s popping up again now because, to their great misfortune, these survivors were recently stumbled upon by patrolling NAM \
Forces and subsequently slaughtered. The supplies appear to have been left free for the taking. I understand if you want to \
avoid acting out the role of the vulture on the corpse of a dead world. But if you do decide to undertake this mission be \
cautious, there may be some unknown enemy forces remaining in the area.  '
    
    Op_Text2     = '   The target comes into view near the outskirts of a shelled out and crumbling city. The depot is old and \
mostly rusted ruin, half caved in, rafters of bent steel protruding like the ribs of rotting giant, gored over with \
blood-colored rust. There isn’t a soul in sight. No matter the seeming desolation, your forces approach with caution, on the \
lookout for any sign of hostiles, honing weapons on every leaf and scrap of garbage that ruffles in the light breeze. This \
better not be a waste of time. '
    
    Op_Text_Com  = '   Despite the quiet, your forces soon discover that they are not alone here. NAM seems to have left a \
surprise for any would be looters stumbling across this place. Guess that makes you a would-be looter. '
    
    Op_Text_Pac  = '   The approach to the Depot was at worst nerve-wracking, but your forces never spotted a single other person. \
The greatest danger was attempting to navigate the piles of jagged sheet metal and daggers of glass scattered over everything. '
    
    Op_Text_Win  = '   Fighting off NAMs combat drones nearly brought the whole place down. It groaned loud and ominous over\
the sound of each ricocheting bullet. But miraculously, the old structure held up but came away with even more holes then\
before punched into its corrugated sheet metal walls. After a time it proves easy enough to locate the hidden cache. One of the\
survivors had nearly clawed it from it\'s hiding place before NAMs combat drones had riddled the poor fool with holes. '
    
    Op_Text_Lose = 'NAMs little surprise seems to have worked. Your forces have died in the engagement. We won\'t be getting \
anything from that Depot after all. '
    
    ESO        = 0
    EMD        = 0
    EIT        = 0
    ECM        = 0
    ECT        = 0
    EMT        = 0
    ECO        = 0

    ESO_Var    = 2
    EMD_Var    = 0
    EIT_Var    = 0
    ECM_Var    = 0
    ECT_Var    = 0
    EMT_Var    = 0
    ECO_Var    = 0
    
    First      = 1

    Delay      = 3
    Delay_Var  = 1

    CC_Reward  = 0
    Req_Reward = 20
    Sub_Reward = 20
    
    CC_Var     = 1
    Req_Var    = 10
    Sub_Var    = 10

    Op_Number  = 4123
    
    Mid_Operations_List.append( lambda: Operation_Variation ( Op_Text1, Op_Text2, Op_Text_Com, Op_Text_Pac, Op_Text_Win, Op_Text_Lose, Delay, Delay_Var, ESO_Var, EMD_Var, EIT_Var, ECM_Var, ECT_Var, EMT_Var, ECO_Var, ESO, EMD, EIT, ECM, ECT, EMT, ECO, First, CC_Var, CC_Reward, Req_Var, Req_Reward, Sub_Var, Sub_Reward, Op_Number ) ) 

BAA_Operation_variables ( )

#==================================================================================================

def CAA_Operation_variables ( ) :

    Op_Text1     = '    A lone and lightly armored convoy pops up on radar. Three trucks, but it\'s not apparent if they\'re troop transport or supply, \
this could be a fucking loot pinata or a can of worms. What?! Hey, I\'ve been reading through lists of common phrases to sound more human, OKAY. \
Is it not working?   (;_; )   Well anyway, it\'s up to you if we hit the convoy. Could be a lot of trouble if these ARE troop transports, \
but we won\'t know unless we go ever there and shoot at them a whole bunch. '
    
    Op_Text2     = '    Fishtailing in the ice and mud the three trucks fight to get any solid footing in the runoff waterlogged canyon road. It seems like \
these fools might be ex-Nationals of some sort, remnants of a sovereign state militia from the old, dead, pre-NAM world. It\'s not clear what they\'re doing \
here. Maybe they have a base of some sort nearby. Let\'s hope not though; we don\'t need to deal with the reinforcements. Anyway, these guys aren\'t going\
anywhere fast but now\'s as good a time as any to see what they\'re driving around. Your forces are ready to go. '
    
    Op_Text_Com  = '    Opening fire, your forces shatter the windshields of each truck in the blink of an eye. Followed quickly my more blinking and\
then crying, as the smoke grenades that followed the opening barrage drive everyone out into the open. '
    
    Op_Text_Pac  = '    After hammering at the convoy for a few minutes before realizing nothing was coming of it, your forces cautiously approach the \
stalled trucks. Nobody shows, one of your ' + SO_Name + ' s pops the driver side doors, ready to shoot at the slightest movement or sign of life, \
but the cab is empty. All the vehicles are. Crazy as it sounds these were some old forgotten self-driving transports trying to desperately reroute to \
they\'re long dead destination after they collapsed all the highways in the war. '
    
    Op_Text_Win  = '    The echoes of the last gunshots fade down the cold canyon walls and are absorbed by the evergreens. The last enemy drops face first into \
the bloody mud, sinking halfway into it like a sad burial. All this death had better be worth it.  '
    
    Op_Text_Lose = '    The echoes of the last gunshots fade down the cold Canyon walls, absorbed by the evergreens as the last of your forces tumbles from the \
rocks and into the runoff stream, now running red with the blood of your troops. There could have been anything in those heavily guarded transports, but \
you\'ll never find out now. '
    
    ESO        = 2
    EMD        = 0
    EIT        = 1
    ECM        = 0
    ECT        = 0
    EMT        = 0
    ECO        = 0

    ESO_Var    = 4
    EMD_Var    = 1
    EIT_Var    = 1
    ECM_Var    = 0
    ECT_Var    = 0
    EMT_Var    = 0
    ECO_Var    = 0
    
    First      = 1

    Delay      = 0
    Delay_Var  = 1

    CC_Reward  = 0
    Req_Reward = 20
    Sub_Reward = 20
    
    CC_Var     = 5
    Req_Var    = 15
    Sub_Var    = 15

    Op_Number  = 8902
    
    Short_Operations_List.append( lambda: Operation_Variation ( Op_Text1, Op_Text2, Op_Text_Com, Op_Text_Pac, Op_Text_Win, Op_Text_Lose, Delay, Delay_Var, ESO_Var, EMD_Var, EIT_Var, ECM_Var, ECT_Var, EMT_Var, ECO_Var, ESO, EMD, EIT, ECM, ECT, EMT, ECO, First, CC_Var, CC_Reward, Req_Var, Req_Reward, Sub_Var, Sub_Reward, Op_Number ) ) 

CAA_Operation_variables ( )

#==================================================================================================

def DAA_Operation_variables ( ) :

    Op_Text1     = '    A lone and lightly armored convoy pops up on radar. Three trucks, but it\'s not apparent if they\'re troop transport or supply, \
this could be a fucking loot pinata or a can of worms. What?! Hey, I\'ve been reading through lists of common phrases to sound more human, OKAY. \
Is it not working?   (;_; )   Well anyway, it\'s up to you if we hit the convoy. Could be a lot of trouble if these ARE troop transports, \
but we won\'t know unless we go ever there and shoot at them a whole bunch. '
    
    Op_Text2     = '    Fishtailing in the ice and mud the three trucks fight to get any solid footing in the runoff waterlogged canyon road. It seems like \
these fools might be ex-Nationals of some sort, remnants of a sovereign state militia from the old, dead, pre-NAM world. It\'s not clear what they\'re doing \
here. Maybe they have a base of some sort nearby. Let\'s hope not though; we don\'t need to deal with the reinforcements. Anyway, these guys aren\'t going\
anywhere fast but now\'s as good a time as any to see what they\'re driving around. Your forces are ready to go. '
    
    Op_Text_Com  = '    Opening fire, your forces shatter the windshields of each truck in the blink of an eye. Followed quickly my more blinking and\
then crying, as the smoke grenades that followed the opening barrage drive everyone out into the open. '
    
    Op_Text_Pac  = '    After hammering at the convoy for a few minutes before realizing nothing was coming of it, your forces cautiously approach the \
stalled trucks. Nobody shows, one of your ' + SO_Name + ' s pops the driver side doors, ready to shoot at the slightest movement or sign of life, \
but the cab is empty. All the vehicles are. Crazy as it sounds these were some old forgotten self-driving transports trying to desperately reroute to \
they\'re long dead destination after they collapsed all the highways in the war. '
    
    Op_Text_Win  = '    The echoes of the last gunshots fade down the cold canyon walls and are absorbed by the evergreens. The last enemy drops face first into \
the bloody mud, sinking halfway into it like a sad burial. All this death had better be worth it.  '
    
    Op_Text_Lose = '    The echoes of the last gunshots fade down the cold Canyon walls, absorbed by the evergreens as the last of your forces tumbles from the \
rocks and into the runoff stream, now running red with the blood of your troops. There could have been anything in those heavily guarded transports, but \
you\'ll never find out now. '
    
    ESO        = 1
    EMD        = 0
    EIT        = 0
    ECM        = 0
    ECT        = 0
    EMT        = 0
    ECO        = 0

    ESO_Var    = 1
    EMD_Var    = 0
    EIT_Var    = 1
    ECM_Var    = 0
    ECT_Var    = 0
    EMT_Var    = 0
    ECO_Var    = 0
    
    First      = 1

    Delay      = 0
    Delay_Var  = 1

    CC_Reward  = 0
    Req_Reward = 14
    Sub_Reward = 12
    
    CC_Var     = 0
    Req_Var    = 8
    Sub_Var    = 6

    Op_Number  = 8902
    
    Short_Operations_List.append( lambda: Operation_Variation ( Op_Text1, Op_Text2, Op_Text_Com, Op_Text_Pac, Op_Text_Win, Op_Text_Lose, Delay, Delay_Var, ESO_Var, EMD_Var, EIT_Var, ECM_Var, ECT_Var, EMT_Var, ECO_Var, ESO, EMD, EIT, ECM, ECT, EMT, ECO, First, CC_Var, CC_Reward, Req_Var, Req_Reward, Sub_Var, Sub_Reward, Op_Number ) ) 

DAA_Operation_variables ( )

#==================================================================================================

def EAA_Operation_variables ( ) :

    Op_Text1     = '    The static coming through the loudspeaker is broken only occasionally by the sounds of gunfire and screams buried throughout the white noise.  \
There is a significant operating force in what seems like a massive scale conflict.  It\'s far away but at the site of a considerable military Installation. \
Whoever wins whatever going on right now will be weakened and vulnerable. We can take them out and claim whatever it is that\'s spurred all this fighting. \
Or you could leave it alone watch your resources dwindle away instead. '
    
    Op_Text2     = '    The shell of the installation rises above ground in shallow ridges of concrete running in long,  orderly rows over the flat graveled area. \
The grounds of this old military installation are a graveyard now. As the result of a child\'s toy box scattered across the floor, bloody and mangled bodies are \
everywhere, still freshly decaying from the battle a few earlier. The smell of sun-baked rotting flesh and vacated bowels is enough to cause to reconsider \
whatever we might find here. There is nobody alive in sight. The grounds are ghostly quiet the only sound is the crunch of gravel.  '
    
    Op_Text_Com  = ''
    
    Op_Text_Pac  = ''
    
    Op_Text_Win  = ''
    
    Op_Text_Lose = ''
    
    ESO        = 16
    EMD        = 4
    EIT        = 4
    ECM        = 2
    ECT        = 1
    EMT        = 2
    ECO        = 1

    ESO_Var    = 7
    EMD_Var    = 3
    EIT_Var    = 1
    ECM_Var    = 1
    ECT_Var    = 0
    EMT_Var    = 2
    ECO_Var    = 1
    
    First      = 1

    Delay      = 7
    Delay_Var  = 2

    CC_Reward  = 24
    Req_Reward = 63
    Sub_Reward = 24
    
    CC_Var     = 8
    Req_Var    = 26
    Sub_Var    = 17

    Op_Number  = 2484
    
    Long_Operations_List.append( lambda: Operation_Variation ( Op_Text1, Op_Text2, Op_Text_Com, Op_Text_Pac, Op_Text_Win, Op_Text_Lose, Delay, Delay_Var, ESO_Var, EMD_Var, EIT_Var, ECM_Var, ECT_Var, EMT_Var, ECO_Var, ESO, EMD, EIT, ECM, ECT, EMT, ECO, First, CC_Var, CC_Reward, Req_Var, Req_Reward, Sub_Var, Sub_Reward, Op_Number ) ) 

EAA_Operation_variables ( )

#==================================================================================================

def FAA_Operation_variables ( ) :

    Op_Text1     = '    The scan picks up a faint signal originating from what seems to be the middle of nowhere. It\'s probably a trap, but then again, no it\'s probably a trap. '
    
    Op_Text2     = '    Your forces arrive at what is indeed the middle of nowhere. Not too far from where you\'ve been holed up but in the middle of a big dead field. \
It\'s immediately apparent that something has gone down here recently.  Bootprints and bike-tire tracks scar the otherwise pristine mud, and the little wheat that \
still grows here has been trampled and broken in places.  But the air is dead and stagnant smelling not unpleasantly of a natural rot. The soft buzz of nearby insects \
is the only sound. If this is a trap, it\'s a poor one.  '
    
    Op_Text_Com  = '    The source of the faint signal is apparent as soon as it comes within visual range.  A single Corpse, filthy with muck and blood, both drying and \
cracking in the heat of the sun.  You don\'t have more than a minute to assess the damage before the sound of revving motorbikes marks the beginning of an unwanted \
shootout. It seems this was a trap after all. '
    
    Op_Text_Pac  = '    The source of the faint signal is apparent as soon as it comes within visual range.  A single Corpse, filthy with muck and blood, both drying and \
cracking in the heat of the sun.  Tentatively tour forces pick over the damage. The poor soul seems to have been tangled in barb wire and dragged through the field \
behind a motorbike or two. There\'s not a lot left of him. A small transceiver, mostly buried in the mud, seems to be what has been broadcasting. There\'s nothing else \
else in sight. This might have been a waste of time all along. Just as you\'re forced grudgingly pack up to head back, they notice some intact storm shelter doors \
rising out the earth at the near the edge of the field. It isn\'t totally empty either. '
    
    Op_Text_Win  = '    The bikers came on fast, spaying muck and touting roughshod rifles. They were fast but there was only a few of them, and they were easy targets \
at any range on that open terrain. Each dropped one by one until there was only twisted metal and mangled chunks of corpses seeping oil and blood into the still water. \
Just as you\'re forced grudgingly pack up to head back, they notice some intact storm shelter doors rising out the earth at the near the edge of the field. It isn\'t totally empty either. '
    
    Op_Text_Lose = '    Whether this was trap or just bad timing wouldn\'t change the fact that the biker gang had the jump on your forces, they each ended up more or \
less like the first guy; Dragged through the swamp in nets of barbed wire. '
    
    ESO        = 3
    EMD        = 0
    EIT        = 0
    ECM        = 0
    ECT        = 0
    EMT        = 0
    ECO        = 0

    ESO_Var    = 3
    EMD_Var    = 0
    EIT_Var    = 1
    ECM_Var    = 0
    ECT_Var    = 0
    EMT_Var    = 0
    ECO_Var    = 0
    
    First      = 0

    Delay      = 0
    Delay_Var  = 1

    CC_Reward  = 2
    Req_Reward = 16
    Sub_Reward = 4
    
    CC_Var     = 2
    Req_Var    = 12
    Sub_Var    = 10

    Op_Number  = 5643
    
    Short_Operations_List.append( lambda: Operation_Variation ( Op_Text1, Op_Text2, Op_Text_Com, Op_Text_Pac, Op_Text_Win, Op_Text_Lose, Delay, Delay_Var, ESO_Var, EMD_Var, EIT_Var, ECM_Var, ECT_Var, EMT_Var, ECO_Var, ESO, EMD, EIT, ECM, ECT, EMT, ECO, First, CC_Var, CC_Reward, Req_Var, Req_Reward, Sub_Var, Sub_Reward, Op_Number ) ) 

FAA_Operation_variables ( )

#==================================================================================================

def GAA_Operation_variables ( ) :

    Op_Text1     = '    The scan picks up a faint signal originating from what seems to be the middle of nowhere. It\'s probably a trap, but then again, no it\'s probably a trap. '
    
    Op_Text2     = '    Your forces arrive at what is indeed the middle of nowhere. Not too far from where you\'ve been holed up but in the middle of a big dead field. \
It\'s immediately apparent that something has gone down here recently.  Bootprints and bike-tire tracks scar the otherwise pristine mud, and the little wheat that \
still grows here has been trampled and broken in places.  But the air is dead and stagnant smelling not unpleasantly of a natural rot. The soft buzz of nearby insects \
is the only sound. If this is a trap, it\'s a poor one.  '
    
    Op_Text_Com  = '    The source of the faint signal is apparent as soon as it comes within visual range.  A single Corpse, filthy with muck and blood, both drying and \
cracking in the heat of the sun.  You don\'t have more than a minute to assess the damage before the sound of revving motorbikes marks the beginning of an unwanted \
shootout. It seems this was a trap after all. '
    
    Op_Text_Pac  = '    The source of the faint signal is apparent as soon as it comes within visual range.  A single Corpse, filthy with muck and blood, both drying and \
cracking in the heat of the sun.  Tentatively tour forces pick over the damage. The poor soul seems to have been tangled in barb wire and dragged through the field \
behind a motorbike or two. There\'s not a lot left of him. A small transceiver, mostly buried in the mud, seems to be what has been broadcasting. There\'s nothing else \
else in sight. This might have been a waste of time all along. Just as you\'re forced grudgingly pack up to head back, they notice some intact storm shelter doors \
popping out the earth at the near the edge of the field. It isn\'t totally empty either. '
    
    Op_Text_Win  = ''
    
    Op_Text_Lose = ''
    
    ESO        = 0
    EMD        = 0
    EIT        = 0
    ECM        = 0
    ECT        = 0
    EMT        = 0
    ECO        = 0

    ESO_Var    = 0
    EMD_Var    = 0
    EIT_Var    = 0
    ECM_Var    = 0
    ECT_Var    = 0
    EMT_Var    = 0
    ECO_Var    = 0
    
    First      = 0

    Delay      = 0
    Delay_Var  = 1

    CC_Reward  = 0
    Req_Reward = 12
    Sub_Reward = 4
    
    CC_Var     = 1
    Req_Var    = 7
    Sub_Var    = 5

    Op_Number  = 5643
    
    Short_Operations_List.append( lambda: Operation_Variation ( Op_Text1, Op_Text2, Op_Text_Com, Op_Text_Pac, Op_Text_Win, Op_Text_Lose, Delay, Delay_Var, ESO_Var, EMD_Var, EIT_Var, ECM_Var, ECT_Var, EMT_Var, ECO_Var, ESO, EMD, EIT, ECM, ECT, EMT, ECO, First, CC_Var, CC_Reward, Req_Var, Req_Reward, Sub_Var, Sub_Reward, Op_Number ) ) 

GAA_Operation_variables ( )

#==================================================================================================

def HAA_Operation_variables ( ) :

    Op_Text1     = ''
    
    Op_Text2     = ''
    
    Op_Text_Com  = ''
    
    Op_Text_Pac  = ''
    
    Op_Text_Win  = ''
    
    Op_Text_Lose = ''
    
    ESO        = 0
    EMD        = 0
    EIT        = 0
    ECM        = 0
    ECT        = 0
    EMT        = 0
    ECO        = 0

    ESO_Var    = 0
    EMD_Var    = 0
    EIT_Var    = 0
    ECM_Var    = 0
    ECT_Var    = 0
    EMT_Var    = 0
    ECO_Var    = 0
    
    First      = 0

    Delay      = 0
    Delay_Var  = 0

    CC_Reward  = 0
    Req_Reward = 0
    Sub_Reward = 0
    
    CC_Var     = 0
    Req_Var    = 0
    Sub_Var    = 0

    Op_Number  = 1242
    
    #Short_Operations_List.append( lambda: Operation_Variation ( Op_Text1, Op_Text2, Op_Text_Com, Op_Text_Pac, Op_Text_Win, Op_Text_Lose, Delay, Delay_Var, ESO_Var, EMD_Var, EIT_Var, ECM_Var, ECT_Var, EMT_Var, ECO_Var, ESO, EMD, EIT, ECM, ECT, EMT, ECO, First, CC_Var, CC_Reward, Req_Var, Req_Reward, Sub_Var, Sub_Reward, Op_Number ) ) 

HAA_Operation_variables ( )

#==================================================================================================

def IAA_Operation_variables ( ) :

    Op_Text1     = ''
    
    Op_Text2     = ''
    
    Op_Text_Com  = ''
    
    Op_Text_Pac  = ''
    
    Op_Text_Win  = ''
    
    Op_Text_Lose = ''
    
    ESO        = 0
    EMD        = 0
    EIT        = 0
    ECM        = 0
    ECT        = 0
    EMT        = 0
    ECO        = 0

    ESO_Var    = 0
    EMD_Var    = 0
    EIT_Var    = 0
    ECM_Var    = 0
    ECT_Var    = 0
    EMT_Var    = 0
    ECO_Var    = 0
    
    First      = 0

    Delay      = 0
    Delay_Var  = 0

    CC_Reward  = 0
    Req_Reward = 0
    Sub_Reward = 0
    
    CC_Var     = 0
    Req_Var    = 0
    Sub_Var    = 0

    Op_Number  = 9872
    
    #Short_Operations_List.append( lambda: Operation_Variation ( Op_Text1, Op_Text2, Op_Text_Com, Op_Text_Pac, Op_Text_Win, Op_Text_Lose, Delay, Delay_Var, ESO_Var, EMD_Var, EIT_Var, ECM_Var, ECT_Var, EMT_Var, ECO_Var, ESO, EMD, EIT, ECM, ECT, EMT, ECO, First, CC_Var, CC_Reward, Req_Var, Req_Reward, Sub_Var, Sub_Reward, Op_Number ) ) 

IAA_Operation_variables ( )










Game_Cycle ( )

