#!/usr/bin/env python
# coding: utf-8

# In[61]:


#Global variables
import random
board =[" "]*10
player_marker=" "
cpu_marker=" "
info=0
game_status=1
board[0]="d"


# In[62]:


def input_player():
    global player_marker, cpu_marker
    player_marker=input("Enter if X/O?")
    player_marker=player_marker.upper()
    if(player_marker=="X"):
        cpu_marker="O"
    else:
        cpu_marker="X"


# In[63]:


def display_board():
    global board
    print(board[7]+" | "+board[8]+" | "+board[9])
    print("---------")
    print(board[4]+" | "+board[5]+" | "+board[6])
    print("---------")
    print(board[1]+" | "+board[2]+" | "+board[3])
    


# In[64]:


def input_info():
    global info, player_marker
    abc=1
    while(abc==1):
        print("Please enter your desired position in reference to the diagram given below")
        print("Example enter '3' if your desired position is rightmost cell in bottom row")
        print("")
        print("(7)"+" | "+"(8)"+" | "+"(9)")
        print("---------------")
        print("(4)"+" | "+"(5)"+" | "+"(6)")
        print("---------------")
        print("(1)"+" | "+"(2)"+" | "+"(3)")
        print("")
        info=int(input("Enter your desired position?"))
        if(board[info]!=" "):
            abc=1
        else: abc=0
    board[info]=player_marker


# In[65]:


def check():
    global board, player_marker, cpu_marker, game_status
    if(board[1]==board[2]==board[3]==player_marker or board[1]==board[2]==board[3]==cpu_marker):
        game_status=0
    elif(board[4]==board[5]==board[6]==player_marker or board[4]==board[5]==board[6]==cpu_marker):
        game_status=0
    elif(board[7]==board[8]==board[9]==player_marker or board[7]==board[8]==board[9]==cpu_marker):
        game_status=0
    elif(board[1]==board[4]==board[7]==player_marker or board[1]==board[4]==board[7]==cpu_marker):
        game_status=0
    elif(board[2]==board[5]==board[8]==player_marker or board[2]==board[5]==board[8]==cpu_marker):
        game_status=0
    elif(board[3]==board[6]==board[9]==player_marker or board[3]==board[6]==board[9]==cpu_marker):
        game_status=0
    elif(board[1]==board[5]==board[9]==player_marker or board[1]==board[5]==board[9]==cpu_marker):
        game_status=0
    elif(board[3]==board[5]==board[7]==player_marker or board[3]==board[5]==board[7]==cpu_marker):
        game_status=0


# In[66]:


def cpu_play():
    global board, cpu_marker
    i=0
    while(board[i]!=" "):
        i = random.randint(1,9)
    board[i]=cpu_marker


# In[67]:


input_player()
while(game_status==1):
    input_info()
    check()
    if(game_status==0):
        break
    cpu_play()
    check()
    if(game_status==0):
        break
    display_board()
    input("Press Enter to continue...")
display_board()
print("Game Over")


# In[ ]:




