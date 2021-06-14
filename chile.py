import requests
import pandas as pd 
import xml.etree.ElementTree as ET
import gspread 
from gspread_dataframe import set_with_dataframe


metrics = ['Number of deaths', 'Number of infant deaths', 'Number of under-five deaths', 'Mortality rate for 5-14 year-olds (probability of dying per 1000 children aged 5-14 years)', 'Adult mortality rate (probability of dying between 15 and 60 years per 1000 population)','Estimates of number of homicides', 'Crude suicide rates (per 100 000 population)', 'Mortality rate attributed to unintentional poisoning (per 100 000 population)', 'Number of deaths attributed to non-communicable diseases, by type of disease and sex', 'Estimated road traffic death rate (per 100 000 population)', 'Estimated number of road traffic deaths', 'Mean BMI (kg/m&#xb2;) (crude estimate)', 'Mean BMI (kg/m&#xb2;) (age-standardized estimate)', 'Prevalence of obesity among adults, BMI > 30 (age-standardized estimate) (%)', 'Prevalence of obesity among children and adolescents, BMI > +2 standard deviations above the median (crude estimate) (%)', 'Prevalence of overweight among adults, BMI &amp;GreaterEqual; 25 (age-standardized estimate) (%)', 'Prevalence of overweight among children and adolescents, BMI > +1 standard deviations above the median (crude estimate) (%)', 'Prevalence of underweight among adults, BMI < 18.5 (age-standardized estimate) (%)', 'Prevalence of thinness among children and adolescents, BMI &lt; -2 standard deviations below the median (crude estimate) (%)', 'Alcohol, recorded per capita (15+) consumption (in litres of pure alcohol)', 'Estimate of daily cigarette smoking prevalence (%)', 'Estimate of daily tobacco smoking prevalence (%)', 'Estimate of current cigarette smoking prevalence (%)', 'Estimate of current tobacco smoking prevalence (%)', 'Mean systolic blood pressure (crude estimate)', 'Mean fasting blood glucose (mmol/l) (crude estimate)', 'Mean Total Cholesterol (crude estimate)','Prevalence of overweight among adults, BMI &GreaterEqual; 25 (age-standardized estimate) (%)','Prevalence of obesity among adults, BMI &GreaterEqual; 30 (age-standardized estimate) (%)', 'Prevalence of thinness among children and adolescents, BMI < -2 ']
dict_data = {
    'COUNTRY': [],
    'YEAR': [],
    'GHO': [],
    'SEX': [],
    'GHECAUSES': [],
    'AGEGROUP': [],
    'Display': [], 
    'Numeric': [], 
    'Low': [], 
    'High': []
}


def read_root(root):
    for child in root:
        country = None
        gho = None
        sex = None 
        year = None 
        ghecauses = None
        agegroup = None
        display = None 
        numeric = None 
        low = None 
        high = None 
        for child2 in child:
            if child2.tag == "GHO":
                gho = child2.text
            elif child2.tag == "COUNTRY":
                country = child2.text
            elif child2.tag == "SEX":
                sex = child2.text
            elif child2.tag == "YEAR":
                year = child2.text
            elif child2.tag == "GHECAUSES":
                ghecauses = child2.text
            elif child2.tag == "AGEGROUP":
                agegroup = child2.text
            elif child2.tag == "Display":
                display = child2.text
            elif child2.tag == "Numeric":
                numeric = float(child2.text)
            elif child2.tag == "Low":
                low = float(child2.text)
            elif child2.tag == "High":
                high = float(child2.text)
        if gho in metrics:
            dict_data['GHO'].append(gho)
            dict_data['COUNTRY'].append(country)
            dict_data['SEX'].append(sex)
            dict_data['YEAR'].append(year)
            dict_data['GHECAUSES'].append(ghecauses)
            dict_data['AGEGROUP'].append(agegroup)
            dict_data['Display'].append(display)
            dict_data['Numeric'].append(numeric)
            dict_data['Low'].append(low)
            dict_data['High'].append(high)
    print("Se termino de agregar datos")
    return dict_data



if __name__ == '__main__':
    request_uno = requests.get('http://tarea-4.2021-1.tallerdeintegracion.cl/gho_CMR.xml').text
    print("Datos de Camerun procesados")
    root_uno = ET.XML(request_uno)
    read_root(root_uno)
    request_dos = requests.get('http://tarea-4.2021-1.tallerdeintegracion.cl/gho_ESP.xml').text
    print("Datos de España procesados")
    root_dos = ET.XML(request_dos)
    read_root(root_dos)
    request_tres = requests.get('http://tarea-4.2021-1.tallerdeintegracion.cl/gho_FRA.xml').text
    print("Datos de Francia procesados")
    root_tres = ET.XML(request_tres)
    read_root(root_tres)
    request_cuatro = requests.get('http://tarea-4.2021-1.tallerdeintegracion.cl/gho_BRA.xml').text
    print("Datos de Brasil procesados")
    root_cuatro = ET.XML(request_cuatro)
    read_root(root_cuatro)
    request_cinco = requests.get('http://tarea-4.2021-1.tallerdeintegracion.cl/gho_USA.xml').text
    print("Datos de USA procesados")
    root_cinco = ET.XML(request_cinco)
    read_root(root_cinco)
    request_seis = requests.get('http://tarea-4.2021-1.tallerdeintegracion.cl/gho_DEU.xml').text
    print("Datos de Alemania procesados")
    root_seis = ET.XML(request_seis)
    read_root(root_seis)

    df = pd.DataFrame(data=dict_data)
    print(df)

    gc = gspread.service_account(filename='taller-tarea-4-316707-7653144657a3.json')
    sh = gc.open_by_key('19Vej7hkNSJBw5J0sX8kqpmdz-koeQopyFwpv8LBnrGo')
    worksheet = sh.get_worksheet(0)
    worksheet.clear()
    set_with_dataframe(worksheet, df)
        
#chile_df = pd.DataFrame(data=chile_json)
#print(chile_df)
#set_with_dataframe(worksheet, df)'''

