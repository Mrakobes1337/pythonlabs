from guietta import _, Gui, Quit, normalized, ___, III, HS, VS
import megagay

gui = Gui(
    ["Выберите предмет", _                      , _                      ],
    [["Пиджак"]        , "Выбранный предмет:"   ,"Отсутствует"           ],
    [["Брюки"]         , "Введите количество"   , "__num__"              ],
    [["Костюм-тройка"] , "Итог"                 , "_"                    ],
    [_                 , _                      , ""                     ],
    [_                 , _                      , ["Сохранить результат"]]
)


@gui.auto
def edited(gui,*args):
    if gui.Отсутствует == "Отсутствует":
        return
    try:
        int(gui.num)
    except:
        gui._="_"
        return
    changed(gui)

@gui.auto
def change1(gui,*args):
    gui.Отсутствует = "Пиджак"
    edited(gui)
    
@gui.auto
def change2(gui,*args):
    gui.Отсутствует = "Брюки"
    edited(gui)
    
@gui.auto
def change3(gui,*args):
    gui.Отсутствует = "Костюм-тройка"
    edited(gui)

@gui.auto
def save(gui, *args):
    pass

def changed(gui):
    num=int(gui.num)
    z=str(gui.Отсутствует)
    obj=megagay.classes[z]().__dict__
    gui._=megagay.calc(obj)*num

gui.events(
    [_,_,_],
    [change1,_,_],
    [change2,_,('textEdited', edited)],
    [change3,_,_],
    [_,_,_],
    [_,_,save]
)

gui.run()

pass