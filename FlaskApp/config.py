import warnings; warnings.filterwarnings("ignore")

def get_prop_style(status):
    if status == 'green':
        color_text = 'DarkGreen;' 
        color_bg   = '#62d289;'
    else:
        color_text = 'White;'
        color_bg   = '#ac0c0c;'

    style = "\
        border-radius: 8px; \
        font-size: 50px; \
        line-height: 1.6em;\
        text-align: center;\
        background-clip: border-box;\
        -webkit-text-fill-color: inherit;\
        background-color: " + color_bg + \
        "color: " + color_text   
    return style

dict_default = {
    'placeholder_age' : 'Age',
    'prop_box_style'  : 'visibility: hidden'
}