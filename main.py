from pygame import *
font.init()

class Button():
    def __init__(self, text, window, x, y, width, height, colour):
        self.rect = rect.Rect(x, y, width, height)
        self.colour = colour
        self.window = window
        self.text = text
    def show(self):
        draw.rect(self.window, self.colour, self.rect)
        try:
            self.window.blit(self.textrender, (self.rect.x, self.rect.y))
        except:
            pass
    def click(self, function):
        global istheturnofx
        if i.type == MOUSEBUTTONDOWN and i.button == 1:
            x, y = i.pos
            try:
                if self.rect.collidepoint(x, y):
                    function()
            except:
                pass
    def set_text(self):
        if istheturnofx:
            if self.text == None:
                self.text = 'X'
                self.textrender = font.SysFont('Arial', 150).render(self.text, True, (0, 0, 0))
                checkturn()
        else:
            if self.text == None:
                self.text = 'O'
                self.textrender = font.SysFont('Arial', 150).render(self.text, True, (0, 0, 0)) 
                checkturn()  

def checkturn():
    global istheturnofx
    if istheturnofx:
        istheturnofx = False
    else:
        istheturnofx = True        

def checkwin():
    global close
    global owon
    global xwon
    global tie
    global listofclicks
    listofclicks = []
    for i in listofrectangles:
        listofclicks.append(i.text)
    if check_win('X'):
        xwon = True
    if check_win('O'):
        owon = True
    if check_tie() and xwon == False and owon == False:
        tie = True
    if xwon or owon or tie:
        close = True

def check_win(letter):
    variable = False
    if listofclicks[0] == letter and listofclicks[1] == letter and listofclicks[2] == letter:
        variable = True
    if listofclicks[3] == letter and listofclicks[4] == letter and listofclicks[5] == letter:
        variable = True
    if listofclicks[6] == letter and listofclicks[7] == letter and listofclicks[8] == letter:
        variable = True
    if listofclicks[0] == letter and listofclicks[3] == letter and listofclicks[6] == letter:
        variable = True
    if listofclicks[1] == letter and listofclicks[4] == letter and listofclicks[7] == letter:
        variable = True
    if listofclicks[2] == letter and listofclicks[5] == letter and listofclicks[8] == letter:
        variable = True
    if listofclicks[0] == letter and listofclicks[4] == letter and listofclicks[8] == letter:
        variable = True
    if listofclicks[2] == letter and listofclicks[4] == letter and listofclicks[6] == letter:
        variable = True
    return variable

def check_tie():
    tie = True
    for i in listofclicks:
        if i == None:
            tie = False
            break
    return(tie)

closeall = False
while closeall != True:
    w = display.set_mode((1500, 750))
    display.set_caption('tic tac toe')
    listofrectangles = []
    x = 500
    y = 100
    owon = False
    xwon = False
    tie = False
    istheturnofx = True
    for i in range(3):
        for i in range(3):
            listofrectangles.append(Button(None, w, x, y, 150, 150, (0, 0, 255)))
            x += 200
        y += 200
        x = 500
    clock = time.Clock()
    close = False
    while close != True:
        w.fill((255, 255, 255))
        for i in event.get():
            if i.type == QUIT:
                close = True
                closeall = True
            for j in listofrectangles:
                j.click(j.set_text)
        if closeall:
            close = True
        for j in listofrectangles:
            j.show()
        checkwin()
        display.update()
        clock.tick(60)
    close = False
    while close != True:
        w.fill((255, 255, 255))      
        if closeall:
            close = True
        for i in event.get():
            if i.type == QUIT:
                close = True
                closeall = True
            if i.type == KEYDOWN:
                if i.key == K_1:
                    close = True
        if xwon:
            w.blit(font.SysFont('Arial', 100).render('X wins! (1-try again)', True, (0, 255, 0)), (500, 200))
        if owon:
            w.blit(font.SysFont('Arial', 100).render('O wins! (1-try again)', True, (0, 255, 0)), (500, 200))
        if tie:
            w.blit(font.SysFont('Arial', 100).render("It's a tie! (1-try again)", True, (0, 255, 0)), (500, 200))            
        display.update()
        clock.tick(60)