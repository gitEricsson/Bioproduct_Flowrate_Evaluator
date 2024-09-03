from django.shortcuts import render
from .forms import CalculationForm
import math
import numpy as np
import matplotlib.pyplot as plt
import io
import urllib, base64

def calculate_values(t, THTC, FADin, μADmax, D, Kd, Ks, KI, Yx, Ksx, Kmx, Ys, YCH4, YCO2, YH2, YNH3, Ta, A, αs, SADin, XADin, SHTC0, CO20, NH30, H20, ZAD0, XAD0, SAD0):
    # Constants and Formulas
    FAD = FADin
    
    B = (1 / Yx) + Ksx + Kmx + (1 / Ys) * (YCH4 + YCO2 + YH2 + YNH3)
    
    μAD = μADmax / (1 + (Ks / SADin) + (SADin / KI))
    
    XAD = ((D * XADin) / (D + μAD - Kd)) + (XAD0 - (D * XADin) / (D + μAD - Kd)) * math.exp(-(D + μAD - Kd) * t)
    
    SHTC = ((αs * A * math.exp(-Ta / THTC) * XAD * FAD * t ** 2) / 2) + SHTC0
    
    SAD = SADin - (XAD * μAD * B / D) + (SAD0 - SADin + ((XAD * μAD * B) / D)) * math.exp(-D * t)
    
    ZAD = YCH4 * μAD * XAD * t + ZAD0
    
    CO2 = YCO2 * μAD * XAD * t + CO20
    
    H2 = YH2 * μAD * XAD * t + H20
    
    NH3 = YNH3 * μAD * XAD * t + NH30
    
    MXADout = XAD * FAD * t
    MSADout = SAD * FAD * t
    MZADCH4 = ZAD * FAD * t
    MCO2 = CO2 * FAD * t
    MH2 = H2 * FAD * t
    MNH3 = NH3 * FAD * t

    return {
        'SHTCout': SHTC,
        'XADout': XAD,
        'SADout': SAD,
        'ZADCH4': ZAD,
        'CO2': CO2,
        'H2': H2,
        'NH3': NH3,
        'MXADout':  MXADout,
        'MSADout': MSADout,
        'MZADCH4': MZADCH4,
        'MCO2': MCO2,
        'MH2': MH2,
        'MNH3': MNH3,
        'B': B,
        'μAD': μAD,
        'XAD': XAD,
        'SAD': SAD,
        'ZAD': ZAD,
        'FAD': FAD
    }

def calculator_view(request):
    if request.method == 'POST':
        form = CalculationForm(request.POST)
        if form.is_valid():
            # Get user inputs
            t = form.cleaned_data['t']
            THTC = form.cleaned_data['THTC']
            FADin = form.cleaned_data['FADin']

            # Get constants (either user-provided or defaults)
            μADmax = form.cleaned_data['μADmax']
            D = form.cleaned_data['D']
            Kd = form.cleaned_data['Kd']
            Ks = form.cleaned_data['Ks']
            KI = form.cleaned_data['KI']
            Yx = form.cleaned_data['Yx']
            Ksx = form.cleaned_data['Ksx']
            Kmx = form.cleaned_data['Kmx']
            Ys = form.cleaned_data['Ys']
            YCH4 = form.cleaned_data['YCH4']
            YCO2 = form.cleaned_data['YCO2']
            YH2 = form.cleaned_data['YH2']
            YNH3 = form.cleaned_data['YNH3']
            Ta = form.cleaned_data['Ta']
            A = form.cleaned_data['A']
            αs = form.cleaned_data['αs']
            SADin = form.cleaned_data['SADin']
            XADin = form.cleaned_data['XADin']
            SHTC0 = form.cleaned_data['SHTC0']
            CO20 = form.cleaned_data['CO20']
            NH30 = form.cleaned_data['NH30']
            H20 = form.cleaned_data['H20']
            ZAD0 = form.cleaned_data['ZAD0']
            XAD0 = form.cleaned_data['XAD0']
            SAD0 = form.cleaned_data['SAD0']                        
                        
            # Function to plot and save each graph
            def plot_to_uri(x, y, ylabel):
                plt.figure()
                plt.plot(x, y)
                plt.xlabel('Time (days)')
                plt.ylabel(ylabel)
                plt.title(f'{ylabel} vs Time')
                plt.grid(True)
                
                buf = io.BytesIO()
                plt.savefig(buf, format='png')
                buf.seek(0)
                
                string = base64.b64encode(buf.read())
                uri = urllib.parse.quote(string)
                # uri = string.decode('utf-8')
                return uri

            # Time values for plotting
            time_values = np.linspace(0, t, 100)
        
        
            # Perform the calculation            
            results = calculate_values(t, THTC, FADin, μADmax, D, Kd, Ks, KI, Yx, Ksx, Kmx, Ys, YCH4, YCO2, YH2, YNH3, Ta, A, αs, SADin, XADin, SHTC0, CO20, NH30, H20, ZAD0, XAD0, SAD0)

            FAD = results['FAD']
            
            B = results['B']
            
            μAD = results['μAD']
                                
            XAD = results['XAD']
            
            SAD = results['SAD']
            
            ZAD = results['ZAD']
            
            CO2 = results['CO2']
            
            H2 = results['H2']
            
            NH3 = results['NH3']
                        
                    
            # Generating individual plots
            SHTC_plot = plot_to_uri(time_values, [(((αs * A * math.exp(-Ta / THTC) * XAD * FAD * t_val ** 2) / 2) + SHTC0) + SHTC0 for t_val in time_values], 'SHTC')

            XAD_plot = plot_to_uri(time_values, [((D * XADin) / (D + μAD - Kd)) + (XAD0 - (D * XADin) / (D + μAD - Kd)) * math.exp(-(D + μAD - Kd) * t_val) for t_val in time_values], 'XAD')

            SAD_plot = plot_to_uri(time_values, [SADin - (XAD * μAD * B / D) + (SAD0 - SADin + ((XAD * μAD * B) / D)) * math.exp(-D * t_val) for t_val in time_values], 'SAD')

            ZAD_plot = plot_to_uri(time_values, [YCH4 * μAD * XAD * t_val + ZAD0 for t_val in time_values], 'ZAD')
            
            CO2_plot = plot_to_uri(time_values, [YCO2 * μAD * XAD * t_val + CO20 for t_val in time_values], 'CO2')
            
            H2_plot = plot_to_uri(time_values, [YH2 * μAD * XAD * t_val + H20 for t_val in time_values], 'H2')
            
            NH3_plot = plot_to_uri(time_values, [YNH3 * μAD * XAD * t_val + NH30 for t_val in time_values], 'NH3')
            
            MXAD_plot = plot_to_uri(time_values, [XAD * FADin * t_val for t_val in time_values], 'MXADout')
            
            MSADout_plot = plot_to_uri(time_values, [SAD * FADin * t_val for t_val in time_values], 'MSADout')
            
            MZADCH4_plot = plot_to_uri(time_values, [ZAD * FADin * t_val for t_val in time_values], 'MZADCH4')
            
            MCO2_plot = plot_to_uri(time_values, [CO2 * FADin * t_val for t_val in time_values], 'MCO2')
            
            MH2_plot = plot_to_uri(time_values, [H2 * FADin * t_val for t_val in time_values], 'MH2')
            
            MNH3_plot = plot_to_uri(time_values, [NH3 * FADin * t_val for t_val in time_values], 'MNH3')
            
            plot = {'SHTC_plot': SHTC_plot,
                'XAD_plot': XAD_plot,
                'SAD_plot': SAD_plot,
                'ZAD_plot': ZAD_plot,
                'CO2_plot': CO2_plot,
                'H2_plot': H2_plot,
                'NH3_plot': NH3_plot,
                'MXAD_plot': MXAD_plot,
                'MSADout_plot': MSADout_plot,
                'MZADCH4_plot': MZADCH4_plot,
                'MCO2_plot': MCO2_plot,
                'MH2_plot': MH2_plot,
                'MNH3_plot': MNH3_plot}
            
            
            def Merge(dict1, dict2):
                return(dict2.update(dict1))
            
            Merge(plot, results)
            
            return render(request, 'result.html', {'results': results})

    else:
        form = CalculationForm()

    return render(request, 'index.html', {'form': form})
