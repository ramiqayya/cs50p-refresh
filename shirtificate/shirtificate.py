from fpdf import FPDF


name=input("Name:")
pdf=FPDF(orientation='Portrait', format='A4')
pdf.add_page()

pdf.set_auto_page_break(False)

pdf.set_font('helvetica','B',size=40)

pdf.set_text_color(0,0,0)

pdf.set_y(20)

pdf.cell(190, 30, 'CS50 Shirtificate', new_x="LMARGIN", new_y="NEXT", align='C')

pdf.set_y(60)

pdf.image("shirtificate.png",x='C',w=190)

pdf.set_font('helvetica','B',size=25)

pdf.set_text_color(255,255,255)
pdf.set_y(120)
pdf.cell(0,10,txt=f'{name} took CS50',new_x="LMARGIN", new_y="NEXT", align='C')


pdf.output("shirtificate.pdf")