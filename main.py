import flet as ft

def main(page: ft.Page):
    page.title = "Sistema fotovoltáico"
    #page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.adaptive = True
    page.scroll = "always"
    
    lmd_DC = ft.TextField(keyboard_type="NUMBER",label="Consumo medio de energía diario en DC (Wh)",value="", text_align=ft.TextAlign.RIGHT)
    lmd_AC = ft.TextField(keyboard_type="NUMBER",label="Consumo medio de energía diario en AC (Wh)",value="", text_align=ft.TextAlign.RIGHT)
    
 #Inversor
 
    inversor_eficiencia = ft.TextField(keyboard_type="NUMBER",label="Eficiencia del inversor",value="0.9", text_align=ft.TextAlign.RIGHT)

#Batería

    v_bat = ft.TextField(keyboard_type="NUMBER",label="Voltaje de la batería (V)",value="", text_align=ft.TextAlign.RIGHT)
    bateria_eficiencia = ft.TextField(keyboard_type="NUMBER",label="Eficiencia de la batería",value="0.95", text_align=ft.TextAlign.RIGHT)
    com_eficiencia = ft.TextField(keyboard_type="NUMBER",label="Eficiencia de conversión",value="1", text_align=ft.TextAlign.RIGHT)
    cns = ft.TextField(keyboard_type="NUMBER",label="Sistema de acumulación de baterías (Ah)",value="Calcular", text_align=ft.TextAlign.RIGHT)

#Localización

    #insolacion_difusa_critica = ft.TextField(keyboard_type="NUMBER",label="Insolación difusa crítica (Wh/m2/día)",value="1800", text_align=ft.TextAlign.RIGHT)
    pdc = ft.TextField(keyboard_type="NUMBER",label="Potencia de cargas en continua (W)",value="", text_align=ft.TextAlign.RIGHT)
    pac = ft.TextField(keyboard_type="NUMBER",label="Potencia de cargas en alterna (W)",value="", text_align=ft.TextAlign.RIGHT)
    lmd = ft.TextField(keyboard_type="NUMBER",label="Consumo medio de energía diario (Wh/día)",value="Calcular", text_align=ft.TextAlign.RIGHT)
    lmd_solar = ft.TextField(keyboard_type="NUMBER",label="Consumo medio de energía diario (Wh/día)",value="Calcular", text_align=ft.TextAlign.RIGHT)
    n = ft.TextField(keyboard_type="NUMBER",label="Número de días de autonomía",value="1", text_align=ft.TextAlign.RIGHT)
    pdmax = ft.TextField(keyboard_type="NUMBER",label="Profundidad de descarga estacional",value="0.5", text_align=ft.TextAlign.RIGHT)
    fct = ft.TextField(keyboard_type="NUMBER",label="Factor de corrección por temperatura",value="1", text_align=ft.TextAlign.RIGHT)
 
 #Panel solar
 
    v_mod = ft.TextField(keyboard_type="NUMBER",label="Voltaje del módulo",value="", text_align=ft.TextAlign.RIGHT)
    p_mpp = ft.TextField(keyboard_type="NUMBER",label="Potencia pico del módulo en condiciones STC",value="", text_align=ft.TextAlign.RIGHT)
    hps_crit = ft.TextField(keyboard_type="NUMBER",label="Horas pico de sol HPS (kW/m2/día)",value="", text_align=ft.TextAlign.RIGHT)
    pr = ft.TextField(keyboard_type="NUMBER",label="Factor global de funcionamiento del panel",value="", text_align=ft.TextAlign.RIGHT)
    imodsc = ft.TextField(keyboard_type="NUMBER",label="Corriente del módulo en condición de cortocircuito",value="", text_align=ft.TextAlign.RIGHT)
    
    nt = ft.TextField(keyboard_type="NUMBER",label="Número de módulos",value="", text_align=ft.TextAlign.RIGHT)
    nserie = ft.TextField(keyboard_type="NUMBER",label="Número de módulos en serie",value="", text_align=ft.TextAlign.RIGHT)
    nparalelo = ft.TextField(keyboard_type="NUMBER",label="Número de módulos en paralelo",value="", text_align=ft.TextAlign.RIGHT)                       

# Regulador

    n_inv = ft.TextField(keyboard_type="NUMBER",label="Rendimiento del inversor",value="0.95", text_align=ft.TextAlign.RIGHT)
    i_entrada = ft.TextField(keyboard_type="NUMBER",label="Corriente de entrada del regulador (A)",value="Calcular", text_align=ft.TextAlign.RIGHT)
    i_salida = ft.TextField(keyboard_type="NUMBER",label="Corriente de salida del regulador (A)",value="Calcular", text_align=ft.TextAlign.RIGHT)
    p_inv = ft.TextField(keyboard_type="NUMBER",label="Potencia del inversor (W)",value="Calcular", text_align=ft.TextAlign.RIGHT)

#Funciones matemáticas

    def f_lmd(e):
        lmd.value = str(round(float(lmd_DC.value) + float(lmd_AC.value)/float(inversor_eficiencia.value)/(float(bateria_eficiencia.value)*float(com_eficiencia.value)),3))
        lmd_solar.value = str(lmd.value)
        page.update()


    def f_numero_modulos(e):
        if round(float(lmd_solar.value)/(float(p_mpp.value)*float(hps_crit.value)*float(pr.value)),0)%2==0:
            numero_modulos = round(float(lmd_solar.value)/(float(p_mpp.value)*float(hps_crit.value)*float(pr.value)),0)
        else:
            numero_modulos = round(float(lmd_solar.value)/(float(p_mpp.value)*float(hps_crit.value)*float(pr.value)),0)+1
        nt.value = str(numero_modulos)
        nserie.value = str(round(float(v_bat.value)/float(v_mod.value),0))
        nparalelo.value = str(round(float(nt.value)/float(nserie.value),0))
        print(round(float(lmd_solar.value)/(float(p_mpp.value)*float(hps_crit.value)*float(pr.value)),0))
        page.update()

    def f_cn(e):
        cndw = float(lmd.value)/(float(pdmax.value)*float(fct.value))
        cnda = cndw/float(v_bat.value)
        cnew = float(lmd.value)*float(n.value)/(float(pdmax.value)*float(fct.value))
        cnea = cnew/float(v_bat.value)
        if cnda > cnea:
            cns.value = round(cnda,2)
        else:
            cns.value = round(cnea,2)
        page.update()

    def f_reg_v(e):
        i_entrada.value = 1.25*float(imodsc.value)*float(nparalelo.value)
        i_salida.value = 1.25*(float(pdc.value)+float(pac.value)/float(n_inv.value))/float(v_bat.value)
        p_inv.value = 1.2*(float(pac.value))
        page.update()

    page.appbar = ft.AppBar(
        leading=ft.Icon(ft.icons.SOLAR_POWER_SHARP),
        leading_width=40,
        title=ft.Text("Sistema fotovoltáico"),
        center_title=False,
        bgcolor=ft.colors.ORANGE_300,
    )

    page.add(
        ft.Column(
            [#ft.Text("Dimensionamiento de un sistema solar fotovoltáico", theme_style=ft.TextThemeStyle.DISPLAY_SMALL),
             ft.Text("Consumo estimado", theme_style=ft.TextThemeStyle.HEADLINE_SMALL),
             lmd_DC,
             lmd_AC,
             inversor_eficiencia,
             bateria_eficiencia,
             com_eficiencia,
             #insolacion_difusa_critica,
             ft.FilledButton(content=ft.Text("Consumo medio de energía diario (Wh/día)"),on_click=f_lmd),
             lmd,
             ft.Text("Dimensionamiento módulo solar", theme_style=ft.TextThemeStyle.HEADLINE_SMALL),
             lmd_solar,
             p_mpp,
             hps_crit,
             pr,
             v_bat,
             v_mod,
             ft.FilledButton(content=ft.Text("Número de módulos"),on_click=f_numero_modulos),
             nt,
             nserie,
             nparalelo,
             ft.Text("Dimensionamiento del acumulador de baterías", theme_style=ft.TextThemeStyle.HEADLINE_SMALL),
             pdmax,
             fct,
             n,
             ft.FilledButton(content=ft.Text("Sistema de acumulación de baterías"),on_click=f_cn),
             cns,
             ft.Text("Dimensionamiento del regulador", theme_style=ft.TextThemeStyle.HEADLINE_SMALL),
             imodsc,
             pdc,
             pac,
             n_inv,
             ft.FilledButton(content=ft.Text("Corrientes para el regulador de voltaje"),on_click=f_reg_v),
             i_entrada,
             i_salida,
             p_inv,
             #ft.Text("Factor de forma", theme_style=ft.TextThemeStyle.HEADLINE_SMALL),
             #ft.FilledButton(content=ft.Text("Factor de forma"),on_click=f_ff),
             ],alignment=ft.MainAxisAlignment.CENTER,
        ),     
    )

ft.app(main)
