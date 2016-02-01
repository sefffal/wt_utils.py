import IPython.display as display
import ipywidgets as widgets
import time
import threading
import matplotlib.pyplot as plt

__all_funcs = []

def animate(func, speed=2, **kwargs):

    name, steps = list(kwargs.items())[0]
          
    # Pause all other threads
    for fstate in __all_funcs:
        fstate['playing'] = False
        fstate['thrd'].join()
    
    delay_sec = 1/speed # in Hz -> seconds to wait if op were instantaneous
    
    state = {'func':func, 'playing':False, 'thrd':None}
    progress = widgets.FloatProgress(min=min(steps), max=max(steps), value=0)

    def updateProgress():
        val = steps[index]
        progress.value = val
    
    playing = False
    index = 0
    def someFunc():
        nonlocal index
        while True:
            if index == len(steps):
                index = 0
            start = time.time()
            with mutex:
                if not state['playing']:
                    break
                updateProgress()
                index += 1
            time.sleep( delay_sec * (time.time() - start))
        play.disabled = False
        pause.disabled = True

    mutex = threading.Semaphore(1)


    play = widgets.Button(description='▶')
    @play.on_click
    def event_handler(*args):
        nonlocal state
       
        # Pause all other threads
        for fstate in __all_funcs:
            fstate['playing'] = False
            fstate['thrd'].join()
        
        __all_funcs.append(state)
        state['playing'] = True
        pause.disabled = False
        play.disabled = True
        state['thrd'] = threading.Thread(target=someFunc)
        state['thrd'].start()


    pause = widgets.Button(description='Ⅱ')
    @pause.on_click
    def event_handler(*args):
        nonlocal state
        with mutex:
            state['playing'] = False
            pause.disabled = True
            play.disabled = False
        state['thrd'].join()
        updateProgress()
        __all_funcs.remove(state)
    pause.disabled = True


    reset = widgets.Button(description='↺')
    @reset.on_click
    def event_handler(*args):
        nonlocal index, state
        with mutex:
            index = 0
            if not state['playing']:
                updateProgress()

    h = widgets.HBox([play, pause, reset])


    def wrapper(**kwargs):
        func(**kwargs)
        plt.show();
        
    args = {name: progress}

    z = widgets.interactive(wrapper, **args)

    v = widgets.VBox([h, z])
    display.display(v);
    time.sleep(0.5)
    updateProgress();