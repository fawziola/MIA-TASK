import pygame
#initial setup
pygame.init()

HEIGHT=800
WIDTH=800

SCREEN=pygame.display.set_mode([WIDTH,HEIGHT])
pygame.display.set_caption('chess game')
font=pygame.font.Font('freesansbold.ttf',20)
big_FONT=pygame.font.Font('freesansbold.ttf',50)
timer=pygame.time.Clock()
fps=60
#game vaiables
white_pieces=['rook','knight','bishob','king','queen','bishob','knight','rook',
              'pawn','pawn','pawn','pawn','pawn','pawn','pawn','pawn']
white_locations=[(0,0),(1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(7,0)
                 ,(0,1),(1,1),(2,1),(3,1),(4,1),(5,1),(6,1),(7,1)]


black_pieces=['rook','knight','bishob','king','queen','bishob','knight','rook',
              'pawn','pawn','pawn','pawn','pawn','pawn','pawn','pawn']
black_locations=[(0,7),(1,7),(2,7),(3,7),(4,7),(5,7),(6,7),(7,7)
                 ,(0,6),(1,6),(2,6),(3,6),(4,6),(5,6),(6,6),(7,6)]
 
#turn varying 
turn_step=0
selection=1000
valid_moves=[]

#loading piece images
black_queen=pygame.image.load('D:/py/assets/images/black queen.png')
black_queen=pygame.transform.scale(black_queen,(80,80))

black_king=pygame.image.load('D:/py/assets/images/superhero.png')
black_king=pygame.transform.scale(black_king,(80,80))

black_bishob=pygame.image.load('D:/py/assets/images/black bishop.png')
black_bishob=pygame.transform.scale(black_bishob,(70,70))

black_knight=pygame.image.load('D:/py/assets/images/black knight.png')
black_knight=pygame.transform.scale(black_knight,(70,70))

black_rook=pygame.image.load('D:/py/assets/images/black rook.png')
black_rook=pygame.transform.scale(black_rook,(75,75))

black_pawn=pygame.image.load('D:/py/assets/images/black pawn.png')
black_pawn=pygame.transform.scale(black_pawn,(65,65))

white_queen=pygame.image.load('D:/py/assets/images/white queen.png')
white_queen=pygame.transform.scale(white_queen,(80,80))

white_king=pygame.image.load('D:/py/assets/images/white king.png')
white_king=pygame.transform.scale(white_king,(80,80))

white_bishob=pygame.image.load('D:/py/assets/images/white bishop.png')
white_bishob=pygame.transform.scale(white_bishob,(70,70))

white_knight=pygame.image.load('D:/py/assets/images/white knight.png')
white_knight=pygame.transform.scale(white_knight,(70,70))

white_rook=pygame.image.load('D:/py/assets/images/white rook.png')
white_rook=pygame.transform.scale(white_rook,(75,75))

white_pawn=pygame.image.load('D:/py/assets/images/white pawn.png')
white_pawn=pygame.transform.scale(white_pawn,(65,65))

white_images=[white_bishob,white_pawn,white_king,white_queen,white_rook,white_knight]
black_images=[black_bishob,black_pawn,black_king,black_queen,black_rook,black_knight]

piece_list=['bishob','pawn','king','queen','rook','knight' ]

#draw main game board
def draw_board():
    for i in range(32):
        col=i%4
        row=i//4
        if row%2==0:
            pygame.draw.rect(SCREEN,'white',[600-(col*200),row*100,100,100])
        else:
            pygame.draw.rect(SCREEN,'white',[700-(col*200),row*100,100,100])
    
#draw pieces into board
def draw_pieces():
    for i in range(len(white_pieces)):
        index=piece_list.index(white_pieces[i])
        if white_pieces[i]=='pawn':
            SCREEN.blit(white_pawn,(white_locations[i][0]*100+20, white_locations[i][1]*100+20))
        else:
            SCREEN.blit(white_images[index],(white_locations[i][0]*100+10, white_locations[i][1]*100+10))
        if turn_step < 2:
            if selection == i:
                pygame.draw.rect(SCREEN, 'red', [white_locations[i][0] * 100 + 1, white_locations[i][1] * 100 + 1,
                                                 100, 100], 2)
                
#check pieces valid options

def check_options():
     




    for i in range(len(black_pieces)):
        index=piece_list.index(black_pieces[i])
        if black_pieces[i]=='pawn':
            SCREEN.blit(black_pawn,(black_locations[i][0]*100+20, black_locations[i][1]*100+20))
        else:
            SCREEN.blit(black_images[index],(black_locations[i][0]*100+10, black_locations[i][1]*100+10))  
        if turn_step >= 2:
          if selection == i:
                pygame.draw.rect(SCREEN, 'blue', [black_locations[i][0] * 100 + 1, black_locations[i][1] * 100 + 1,
                                                  100, 100], 2)

#main game loop
run=True
while run:
    timer.tick(fps)
    SCREEN.fill('black')
    draw_board()
    draw_pieces()

#event handling
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
             run=False


        if event.type==pygame.MOUSEBUTTONDOWN and event.button==1:
            x_coord=event.pos[0]//100  
            y_coord=event.pos[0]//100  
            click_coords=(x_coord,y_coord)
            if turn_step<=1:
                if click_coords in white_locations:
                    selection=white_locations.index(click_coords)
                    if turn_step==0:
                        turn_step=1
                if click_coords in valid_moves and selection!=1000:
                    white_locations[selection]=click_coords
                    if click_coords in black_locations:
                        black_piece=black_locations.index(click_coords)
                        black_pieces.pop(black_piece)
                        black_locations.pop(black_piece)        
                    black_options=check_options(black_pieces,black_locations,'black')
                    white_options=check_options(white_pieces,white_locations,'white')
                    turn_step=2
                    selection=1000
                    valid_moves=[]
            if turn_step>1:
                if click_coords in black_locations_locations:
                    selection=black_locations.index(click_coords)
                    if turn_step==2:
                        turn_step=3 
                if click_coords in valid_moves and selection!=1000:
                    black_locations[selection]=click_coords
                    if click_coords in white_locations_locations:
                        white_piece=white_locations.index(click_coords)
                        white_pieces.pop(white_piece)
                        white_locations.pop(white_piece)        
                    black_options=check_options(black_pieces,black_locations,'black')
                    white_options=check_options(white_pieces,white_locations,'white')
                    turn_step=0
                    selection=1000
                    valid_moves=[]













    pygame.display.flip()

pygame.quit()

          
 