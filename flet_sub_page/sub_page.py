from typing import Any
import flet
import multiprocessing
import concurrent.futures


#? The Sub Page function
def _s_ (sub_page_class):
    import flet
    import threading

    #? The_App
    def APP (page:flet.Page):
        if sub_page_class.controls != None:
            for con in sub_page_class.controls:
                page.add(con)
        if sub_page_class.page_props != None:
            for P in sub_page_class.page_props:
                if hasattr(page, P):
                    setattr(page, P, sub_page_class.page_props[P])
                    page.update()
        page.update()
        if sub_page_class.target != None:
            sub_page_class.target (page)
        page.update()
    
    flet.app(target=APP)



class subPage (object):
    def __init__ (self, controls=None, page_props=None, target=None):
        self.controls = controls
        self.page_props = page_props
        self.target = target
    
    def start (self):
        with concurrent.futures.ProcessPoolExecutor() as executor:
            # future = executor.submit(push_new_app)
            # future.result()
            multiprocessing.Process(target=_s_, args=[self]).start()