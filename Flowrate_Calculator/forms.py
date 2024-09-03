from django import forms

class CalculationForm(forms.Form):
    t = forms.FloatField(label='Time (days)')
    THTC = forms.FloatField(label='Temperature (kelvin)')
    FADin = forms.FloatField(label='Input flow of the Liquid (litres/day)')

    # Optional constants with default values
    SADin = forms.FloatField(label='Initial substrate concentration (gram/litre)', initial=4)
    XADin = forms.FloatField(label='Initial biomass concentration (gram/litre)', initial=2)
    μADmax = forms.FloatField(label='Maximum specific growth rate (hour⁻¹))', initial=0.35)
    D = forms.FloatField(label='Dilution rate (hour⁻¹)', initial=0.029)
    Kd = forms.FloatField(label='Micro-organisms’ detachment rate (hour⁻¹)', initial=0.02)
    Ks = forms.FloatField(label='Substrate-liquid interface’s mass transfer coefficient (gram/litre)', initial=150)
    KI = forms.FloatField(label='Factor inhibition (gram/litre)', initial=0.5)
    Yx = forms.FloatField(label='New cell production ratio', initial=0.82)
    Ksx = forms.FloatField(label='Substrate’s degradation rate for micro-organism growth (gram/gram)', initial=0.983)
    Kmx = forms.FloatField(label='Substrate’s degradation rate for micro-organism maintenance (gram/gram)', initial=0.4)
    Ys = forms.FloatField(label='Coefficient production', initial=4.35)
    YCH4 = forms.FloatField(label='CH₄ production coefficient', initial=0.27)
    YCO2 = forms.FloatField(label='CO₂ production coefficient', initial=0.4)
    YH2 = forms.FloatField(label='H₂ production coefficient', initial=0.03)
    YNH3 = forms.FloatField(label='NH₃ production coefficient', initial=0.01)
    Ta = forms.FloatField(label='HTC activation temperature (kelvin)', initial=473)
    A = forms.FloatField(label='Pre-exponential factor', initial=1)
    αs = forms.FloatField(label='Stoichiometric coefficient for hydro char in reaction', initial=1)

    SHTC0 = forms.FloatField(label='Solid product initial mass at HTC inlet (grams)', initial=0)
    CO20 = forms.FloatField(label='CO₂ initial concentration at AD inlet (grams/litre)', initial=0)
    NH30 = forms.FloatField(label='NH₃ initial concentration at AD inlet (grams/litre)', initial=0)
    H20 = forms.FloatField(label='H₂ initial concentration at AD inlet (grams/litre)', initial=0)
    ZAD0 = forms.FloatField(label='Methane initial concentration at AD inlet (grams/litre)', initial=0)
    XAD0 = forms.FloatField(label='Biomass initial concentration at AD inlet (grams/litre)', initial=0)
    SAD0 = forms.FloatField(label='Substrate initial concentration at inlet (grams/litre)', initial=0)
