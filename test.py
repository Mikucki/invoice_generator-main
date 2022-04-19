from fpdf import FPDF

Date = input('Data wystawienia faktury?: ')
Service_Date = input('Data wykonania usługi?: ')
termin_płątności = input('Termin płatności?: ')

class Company:
    def __init__(self, name, adress, code, city, NIP):
        self.adress = adress
        self.code = code
        self.city = city
        self.NIP = NIP
        self.name = name


firma_1 = Company('Super cars', 'Kosciuszki 60', '81-187', 'Gdynia', 5740001454)
firma_2 = Company('Perfecta', 'Abrahama 5c/11', '81-258', 'Gdynia', 7855578547)        
     





class PDF(FPDF):
    def header(self):
        # Logo
        self.image('fox_face.png', 3, 3, 35)
        # font
        self.set_font('helvetica', 'B', 20)
        # Padding
        self.cell(80)
        # Title
        self.cell(30, 10, 'Invoice', border=1, align='C')




        
    
        # Line break
        self.ln(20)



def footer(self):
    self.set_y(-15)
    self.set_font('helvetica', 'I', 10)
    self.cell(0, 10, f'Page {self.page_no()}/{{nb}}', align='C')



    # Page footer
    def footer(self):
        # Set position of the footer
        self.set_y(-15)
        # set font
        self.set_font('helvetica', 'I', 8)
        # Page number
        self.cell(0, 10, f'Page {self.page_no()}/{{nb}}', align='C')

# Create a PDF object
pdf = PDF('P', 'mm', 'Letter')

# get total page numbers
pdf.alias_nb_pages()

# Set auto page break
pdf.set_auto_page_break(auto = True, margin = 15)

#Add Page
pdf.add_page()

# specify font

pdf.set_font('helvetica', '', 12)

# Add text
# w = width
# h = height
# txt = your text
# ln (0 False; 1 True - move cursor down to next line)
# border (0 False; 1 True - add border around cell)
pdf.cell(130)
pdf.cell(45, 0, 'Data wystawienia:')
pdf.cell(0, 0, f'{Date}', ln=True)

pdf.cell(130)
pdf.set_font('helvetica', '', 12)
pdf.cell(45, 10, 'Data wykonania: ')
pdf.cell(0, 10, f'{Service_Date}', ln=True)

pdf.cell(130)
pdf.set_font('helvetica', '', 12)
pdf.cell(45, 0, 'Termin platnosci: ', border=0)
pdf.cell(0, 0, f'{termin_płątności}', ln=True)

pdf.line(10, 50, 205, 50)


pdf.set_font('helvetica', '', 12)
pdf.cell(140, 30, 'Sprzedawca: ', ln=False, border=0)

pdf.set_font('helvetica', '', 12)
pdf.cell(0, 30, 'Nabywca: ', ln=True)

pdf.set_font('helvetica', 'B', 12)
pdf.cell(140, 5, str(firma_1.name), ln=0, border=0)
pdf.cell(10, 5, str(firma_2.name), ln=1, border=0)

pdf.set_font('helvetica', '', 12)
pdf.cell(140, 5, 'NIP: ' + str(firma_1.NIP), ln=0, border=0)
pdf.cell(10, 5, 'NIP: ' + str(firma_2.NIP), ln=1, border=0)

pdf.set_font('helvetica', '', 12)
pdf.cell(140, 5, str(firma_1.adress), ln=0)
pdf.cell(10, 5, str(firma_2.adress), ln=True)

pdf.set_font('helvetica', '', 12)
pdf.cell(140, 5, str(firma_1.city) + ', ' + str(firma_1.code), ln=False)

pdf.set_font('helvetica', '', 12)
pdf.cell(140, 5, str(firma_2.city) + ', ' + str(firma_2.code), ln=True)

pdf.cell(200, 20, '', border=0, ln=1)

pdf.set_font('helvetica', '', 10)
pdf.cell(10, 10, 'Lp', border=1, align='C')
pdf.cell(60, 10, 'Nazwa towaru lub uslugi', border=1, align='C')
pdf.cell(25, 10, 'Stawka VAT', border=1, align='C')
pdf.cell(25, 10, 'wartosc netto', border=1, align='C')
pdf.cell(25, 10, 'wartosc VAT', border=1, align='C')
pdf.cell(25, 10, 'wartosc brutto', border=1, align='C', ln=True)


ilosc_rzedow = int(input('ile zostalo wykonanych uslug? '))
<<<<<<< Updated upstrea


for pick in range(1, int(ilosc_rzedow) +1):
    pdf.cell(10, 20, f'{pick}', border=1, ln=0)


    usluga_pick = input('usługa nr ' + f'{pick}: ')
    pdf.cell(60, 20, usluga_pick, border=1, ln=0)


    stawka_vat = input(f'Stawka VAT do usługi - {usluga_pick}: ')
    if stawka_vat == '23%' or '23' or '0.23':
        pdf.cell(25 ,20, f'{stawka_vat}' + '%', border=1, ln=0)
    elif stawka_vat == '8%' or '8' or '0.08':
        pdf.cell(25 ,20, f'{stawka_vat}' + '%', border=1, ln=0)
    elif stawka_vat == '5%' or '5' or '0.05':
        pdf.cell(25 ,20, f'{stawka_vat}' + '%', border=1, ln=0)
    elif stawka_vat == 'zw' or 'zw':
        pdf.cell(25 ,20, f'{stawka_vat}', border=1, ln=0)
    elif stawka_vat == 'np' or 'np':
        pdf.cell(25 ,20, f'{stawka_vat}', border=1, ln=0)
    else:
        pdf.cell(25 ,20, 'zla stawka VAT', border=1, ln=0)

        
    wartosc_netto = float(input(f'Wartosc netto do {usluga_pick}: '))
    pdf.cell(25 ,20, f'{wartosc_netto}', border=1, ln=0)
    
=======
stawka_vat = float(input('Stawka VAT:'))
wartosc_netto = int(input('watrosc_netto: '))
wartosc_vat = int(wartosc_netto) * int(stawka_vat)
wartosc_brutto = int(wartosc_netto) + int(wartosc_vat)

for i in range(1, int(ilosc_rzedow) + 1):
    pdf.cell(10, 20, f'{i}', border=1, align='C', ln=0 )


for pick in range(1, int(ilosc_rzedow) + 1):
    usluga_pick = input('usługa nr ' + f'{pick} :')
    pdf.cell(60, 20, f'{pick}' + usluga_pick, border=1, align='C', ln=0)


for pick in range(1, int(ilosc_rzedow) + 1):
    vat_pick = float(input('Stawka VAT do uslugi nr: ' + f'{pick} :'))
    pdf.cell(25, 20, f'{pick}' + usluga_pick, border=1, align='C', ln=1)


>>>>>>> Stashed changes

    wartosc_vat = (float(stawka_vat) / 100) * float(wartosc_netto)
    pdf.cell(25 ,20, f'{wartosc_vat}' , border=1, ln=0)

    wartosc_brutto = (float(wartosc_netto) + float(wartosc_vat))
    pdf.cell(25 ,20, f'{round(wartosc_brutto)}' , border=1, ln=1)




pdf.output('pdf_2.pdf')
