import pyautogui

screenWidth, screenHeight = pyautogui.size() 

def game_screen():
    game_window = pyautogui.screenshot(region=(350, 1100, 100, 100))
    return game_window


def jump():
    pyautogui.press('space')

def obstacle(game_window):
     
    obstacle = game_window.getpixel((20, 20))
    if obstacle == (83, 83, 83):
        return True
    else:
        return False


if __name__ == "__main__":
    while True:
        game_window_play = game_screen()
 
        if obstacle(game_window_play):  
            jump()                                    


                   