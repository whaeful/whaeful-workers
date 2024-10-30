#Imports
import flet as ft
import time

#Main Page
text_color = ft.colors.WHITE
text_size = 24
tech_dd = None
product_type_dd = None
def dashboard_page(page: ft.Page):
    global text_color,text_size,tech_dd,product_type_dd
#fonts
    page.fonts = {
        "Oswald": "Oswald.ttf",
        "Oxanium": "Oxanium.ttf",
        "Roboto": "Roboto.ttf",
        "Antipasto": "Antipasto.ttf",
        "Bringthatnoize": "Bringthatnoize.ttf",
        "Fiexus": "Fiexus.ttf",
        "Breamcatcher": "Breamcatcher.otf",
        "Turnb": "TURNB.ttf"

    }
    page.theme= ft.Theme(font_family="Oxanium")
    logo = ft.Container(
        content=ft.Image(
            src="whaeful.png",
            width=960,
            height=240
        ),
        alignment=ft.alignment.center,
        expand=True,
        scale=ft.transform.Scale(1.0),
        animate_scale=ft.animation.Animation(1000,ft.AnimationCurve.EASE_IN_OUT),
    )
    def logo_animation():
        page.window.full_screen=True
        logo.scale=ft.transform.Scale(1.2)
        page.update()
        time.sleep(0.5)
        logo.scale=ft.transform.Scale(1.0)
        page.update()
        
    def show_main_page():
        page.clean()

        def calculator(page: ft.Page):
    #Calculation variables
            coef_dict = {
                "Streetwear": {
                    "Shoes": {"margin": 1, "shipping": 32},
                    "T-Shirt": {"margin": 1, "shipping": 16},
                    "Jacket": {"margin": 1, "shipping": 32},
                    "Vest": {"margin": 1, "shipping": 32},
                    "Pants": {"margin": 1, "shipping": 16},
                    "Shorts": {"margin": 1, "shipping": 16},
                    "Backpack": {"margin": 1, "shipping": 16},
                    "Bag": {"margin": 1, "shipping": 16},
                    "Socks": {"margin": 1, "shipping": 16},
                    "Set": {"margin": 1, "shipping": 32},
                    "Longsleeve": {"margin": 1, "shipping": 16},
                    "Tracksuit": {"margin": 1, "shipping": 32},
                    "Ziphoodie": {"margin": 1, "shipping": 16},
                    "Hat": {"margin": 1, "shipping": 16},
                    "Gloves": {"margin": 1, "shipping": 16},
                },
                "Luxury": {
                    "Shoes": {"margin": 1.35, "shipping": 48},
                    "T-Shirt": {"margin": 1.35, "shipping": 16},
                    "Jacket": {"margin": 1.35, "shipping": 48},
                    "Vest": {"margin": 1.35, "shipping": 32},
                    "Pants": {"margin": 1.35, "shipping": 16},
                    "Shorts": {"margin": 1.35, "shipping": 16},
                    "Backpack": {"margin": 1.35, "shipping": 32},
                    "Bag": {"margin": 1.35, "shipping": 48},
                    "Socks": {"margin": 1.35, "shipping": 16},
                    "Set": {"margin": 1.35, "shipping": 32},
                    "Longsleeve": {"margin": 1.35, "shipping": 16},
                    "Tracksuit": {"margin": 1.35, "shipping": 32},
                    "Ziphoodie": {"margin": 1.35, "shipping": 16},
                    "Hat": {"margin": 1.35, "shipping": 16},
                    "Gloves": {"margin": 1.35, "shipping": 16},
                },
                "Technics": {
                    "Styler": {"margin": 1.5, "shipping": 32},
                    "Hairdryer": {"margin": 1.5, "shipping": 32},
                    "Airpods": {"margin": 1.5, "shipping": 16},
                    "Airpods Max": {"margin": 1.5, "shipping": 16},
                }
            }
            
    #Category dropdown
            type_dd= ft.Dropdown(
                label= "Category type",
                width= 180,
                border_radius=10,
                options=[
                    ft.dropdown.Option("Streetwear"),
                    ft.dropdown.Option("Luxury"),
                    ft.dropdown.Option("Technics"),
                ],
            )
    #Calculation function and function variables

            def get_coeficients():
                category = type_dd.value
                product = get_second_dd()
                if category in coef_dict and product in coef_dict[category]:
                    shipping_coef = coef_dict[category][product]["shipping"]
                    margin_coef = coef_dict[category][product]["margin"]
                    eprice = (float(yprice.value) + 40) / 7 
                    shipping = float(eprice + float(shipping_coef))
                    margin = 0.35 * float(margin_coef)
                    total = round(shipping+(shipping * margin)) - 0.01
                    return total
                else:
                    return 1.0
                
    #Calculate button
            def dd_button(e):
                if yprice.value:
                    total = get_coeficients()
                    t1.value =f"Product price: {total}"
                    t2.value =f"Put this price in shopify product adding page!"
                page.update()
            def dd_show(e):
                global tech_dd,product_type_dd

                input_elements.controls.clear()
                input_elements.controls.append(yprice)
                input_elements.controls.append(type_dd)

                if type_dd.value == "Technics":                
    #Technics type dropdown
                    tech_dd = ft.Dropdown(
                        label= "Technics type",
                        border_radius=10,
                        width=180,
                        options=[
                            ft.dropdown.Option("Styler"),
                            ft.dropdown.Option("Hairdryer"),
                            ft.dropdown.Option("Airpods"),
                            ft.dropdown.Option("Airpods Max"),
                        ],
                    )
                    input_elements.controls.append(tech_dd)
                else:
    #Product type dropdown
                    product_type_dd= ft.Dropdown(
                        label = "Product type",
                        width= 180,
                        border_radius=10,
                        options=[
                            ft.dropdown.Option("Shoes"),
                            ft.dropdown.Option("T-Shirt"),
                            ft.dropdown.Option("Jacket"),
                            ft.dropdown.Option("Vest"),
                            ft.dropdown.Option("Pants"),
                            ft.dropdown.Option("Shorts"),
                            ft.dropdown.Option("Backpack"),
                            ft.dropdown.Option("Bag"),
                            ft.dropdown.Option("Socks"),
                            ft.dropdown.Option("Set"),
                            ft.dropdown.Option("Longsleeve"),
                            ft.dropdown.Option("Tracksuit"),
                            ft.dropdown.Option("Ziphoodie"),
                            ft.dropdown.Option("Hats"),
                            ft.dropdown.Option("Gloves"),
                        ],
                    )
                    input_elements.controls.append(product_type_dd) 
                input_elements.controls.append(b)
                if tech_dd:
                    tech_dd.value = None
                if product_type_dd:
                    product_type_dd.value = None
                page.update()
            type_dd.on_change = dd_show

            def get_second_dd():
                return tech_dd.value if type_dd.value == "Technics" else product_type_dd.value        
            
            
            t1 =ft.Text(size=text_size)
            t2 =ft.Text(size=text_size)
            yprice = ft.TextField(
                label="Enter price in Yuan",
                border_width=2,
                border_radius= 10,
                keyboard_type=ft.KeyboardType.NUMBER
            )
            b = ft.ElevatedButton(
                text= "Calculate", 
                on_click= dd_button
            )
            input_elements=ft.Row(
                [
                    yprice,
                    type_dd,
                    b,
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                vertical_alignment=ft.MainAxisAlignment.CENTER
            )
            show_price=ft.Row(
                [
                    ft.Column(
                        [
                            t1,
                            t2,
                        ]
                    )

                ],
                alignment=ft.MainAxisAlignment.CENTER
            )
            return ft.Container(
                content=ft.Column(
                    [
                        input_elements,
                        show_price
                    ],
                    alignment=ft.alignment.top_left
                ),
                alignment=ft.alignment.top_left,
                expand=True
            )
    #Settings page
        #Theme selection
        def settings(page: ft.Page):
            def font_change(e):
                if font_dd.value == "Roboto":
                    page.theme= ft.Theme(font_family="Roboto")
                    page.update()
                elif font_dd.value == "Oxanium":
                    page.theme= ft.Theme(font_family="Oxanium")
                    page.update()
                elif font_dd.value == "Oswald":
                    page.theme= ft.Theme(font_family="Oswald")
                    page.update()
                elif font_dd.value == "Antipasto":
                    page.theme= ft.Theme(font_family="Antipasto")
                    page.update()
                elif font_dd.value == "Breamcatcher":
                    page.theme= ft.Theme(font_family="Breamcatcher")
                    page.update()
                elif font_dd.value == "Bringthatnoize":
                    page.theme= ft.Theme(font_family="Bringthatnoize")
                    page.update()
                elif font_dd.value == "Fiexus":
                    page.theme= ft.Theme(font_family="Fiexus")
                    page.update()
                elif font_dd.value == "Turnb":
                    page.theme= ft.Theme(font_family="Turnb")
                    page.update()

            font_dd= ft.Dropdown(
                border_radius=2,
                hint_text="Choose app font",
                width=150,
                value="Oxanium",
                options=[
                    ft.dropdown.Option("Roboto"),
                    ft.dropdown.Option("Oxanium"),
                    ft.dropdown.Option("Oswald"),
                    ft.dropdown.Option("Antipasto"),
                    ft.dropdown.Option("Breamcatcher"),
                    ft.dropdown.Option("Bringthatnoize"),
                    ft.dropdown.Option("Fiexus"),
                    ft.dropdown.Option("Turnb"),

                ],
                on_change=font_change
            )
            return ft.Container(
                content=ft.Column(
                    [
                        ft.Text("Font changing", size=text_size),
                        font_dd,
                        
                    ],
                    alignment=ft.alignment.top_left

                ),
                alignment=ft.alignment.top_left
            )
    #Dashboard navigation
        page.window.full_screen = True
        def navigate(e):
            index = menu_rail.selected_index
            main_container.clean()
            if index == 0: 
                page.window.full_screen = True
                main_container.clean()
                main_container.content = ft.Text(value = "Home",color=text_color,size=text_size)
                page.update()
            elif index == 1:
                page.window.full_screen = True
                main_container.clean()
                main_container.content = ft.Text(value = "Worklist",color=text_color,size=text_size)
                page.update()
            elif index == 2:
                page.window.full_screen = True
                main_container.clean()
                main_container.content=calculator(page)
                page.update()
            elif index == 3:
                page.window.full_screen = True
                main_container.clean()
                main_container.content = settings(page)
                page.update()
            elif index == 4:
                page.window.full_screen = True
                main_container.clean()
                main_container.content = ft.Text(value = "Help", color = text_color,size = text_size )
                page.update()

    #Dashboard menu rail 
        menu_rail = ft.NavigationRail(
            selected_index=0,
            label_type=ft.NavigationRailLabelType.ALL,
            extended=False,
            min_width=120,
            min_extended_width=220,
            group_alignment=0,
            destinations=[
                ft.NavigationRailDestination(
                    icon=ft.icons.HOME_OUTLINED, selected_icon=ft.icons.HOME_ROUNDED, label="Home"
                ),
                ft.NavigationRailDestination(
                    icon_content=ft.Icon(ft.icons.CHECKLIST_OUTLINED),
                    selected_icon_content=ft.Icon(ft.icons.CHECKLIST_ROUNDED),
                    label="Worklist",  
                ),
                ft.NavigationRailDestination(
                    icon_content=ft.Icon(ft.icons.CALCULATE_OUTLINED),
                    selected_icon_content=ft.Icon(ft.icons.CALCULATE_ROUNDED),
                    label="Calculations",
                ),
                ft.NavigationRailDestination(
                    icon_content=ft.Icon(ft.icons.SETTINGS_OUTLINED),
                    selected_icon_content=ft.Icon(ft.icons.SETTINGS_ROUNDED),
                    label="Settings",
                ),
                ft.NavigationRailDestination(
                    icon_content=ft.Icon(ft.icons.HELP_OUTLINE_ROUNDED),
                    selected_icon_content=ft.Icon(ft.icons.HELP_ROUNDED),
                    label="Help",
                ),
            ],
            on_change=navigate
        )        
        
    #Container for adding objects in page
        main_container = ft.Container(
            margin=10,
            padding=10,
            alignment=ft.alignment.center,
            border_radius=10,
            expand= True,
        )
                        
        page.add(
            ft.Row(
                [
                    menu_rail,
                    ft.VerticalDivider(width=1),
                    ft.Container(
                        content=main_container,
                        alignment=ft.alignment.center,
                        expand=True
                        
                    )
                    
                ],
                expand=True,
            )
        )

    page.add(logo)
    page.update()
    logo_animation()
    time.sleep(1)
    show_main_page()




            
                        
ft.app(target=dashboard_page)



