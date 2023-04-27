# flet_multi_page
until now, flet v0.6 does not support multi pages.
With this tool, you can start new pages on the same script without the need of creating new `app` class or new cmd process etc...


## install

```
pip install flet-multi-page
```

## little peek

![Screen Recording 2023-04-27 at 3 22 44 PM](https://user-images.githubusercontent.com/86029286/234861120-f2dcc22d-169c-4161-8e40-a20455250f99.GIF)

## usage
Its very simple, you just need to import the package and import the class `subPage`.
This is an example code:

```python
from flet_sub_page import subPage
import flet

def main (page:flet.Page):
    def start_new_page (e):
        p = subPage(controls=[flet.Text("Hello from the new page!!")], page_props={"bgcolor":"blue"})
        p.start()
    
    page.add(flet.ElevatedButton("start new page", on_click=start_new_page))
    page.update()


if __name__ == "__main__": #? This is so important, there will be errors without it.
    flet.app(target=main)
```

Or if you want a second `target` function for the page you can just add `target` argument like this:

```python
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
    
    page.add(flet.ElevatedButton("start new page", on_click=start_new_page))
    page.update()


if __name__ == "__main__": #? This is so important, there will be errors without it.
    flet.app(target=main)
```

## `subPage` properties
- `controls` argument (optional): You can add the controls you need directly to the new page.
- `page_props` argument (optional): You can add the page properties you want as dict.
- `target` argument (optional): You can set a target function to call for the new page, and get `page` class as an argument.
