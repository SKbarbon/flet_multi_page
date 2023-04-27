from flet_sub_page import subPage
import flet
import random

def second_target (page:flet.Page): #? This is the target function of the second page.
    colors = ["blue", "pink", "black", "red", "green"]
    page.bgcolor = random.choice(colors)
    page.add(flet.Text("Hello new page!", color="white"))
    page.update()

def main (page:flet.Page):
    def start_new_page (e):
        p = subPage(target=second_target) #! This is the "subPage" class.
        p.start() #! This will run and start the second page.
    
    page.add(flet.ElevatedButton("start new page", on_click=start_new_page,))
    page.update()


if __name__ == "__main__": #? This is so important, there will be errors without it.
    flet.app(target=main)