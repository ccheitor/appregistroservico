import pandas as pd
import streamlit as st
from datetime import datetime, timedelta
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors
import io
import base64

st.set_page_config(page_title="Ordem de Serviço", layout="wide")
st.title("Identificação de Serviço")

st.header("Serviço")
with st.container():

    col0, col1, col2, col3 = st.columns([1, 1, 1, 1])
    tipo_registro = col0.selectbox("Selecione o tipo", ["Pedido", "Orçamento"])
    numero_registro = col1.text_input("Nº do Registro")
    data_registro = col2.date_input("Data do Registro", value=datetime.now().date())
    
    if data_registro:
        validade_registro = data_registro + timedelta(days=3)
    else:
        validade_registro = datetime.now().date()
    
    col3.text_input(f"Validade do registro",disabled=True,value=validade_registro.strftime('%d/%m/%Y'))
    

st.header("Cliente")
with st.container():

    col1, col2 = st.columns([2, 1])
    nome_cliente = col1.text_input("Nome do Cliente")
    documento = col2.text_input("CPF/CNPJ")

    with st.expander("Dados adicionais do cliente"):

        col1, col2, col3 = st.columns([2, 1, 1])
        email = col1.text_input("E-mail")
        telefone = col2.text_input("Telefone (DDD + número)")
        cep = col3.text_input("CEP")
        dados_adicionais =  st.text_area(label="Dados Adicionais do Cliente",placeholder=
        """Ex: Endereço, CPF, Inscrição Estadual, etc.""")

st.header("Descricao do Pedido")
descricao =  st.text_area("Descrição")


df = pd.DataFrame(columns=["Material", "Quantidade", "Valor bruto", "Valor liquido"])

st.header("Itens do Pedido")
with st.container():
    edited_df = st.data_editor(df, num_rows="dynamic")

# Função para gerar PDF
def generate_pdf():
    # Criar buffer para o PDF
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=A4)
    story = []
    
    # Estilos
    styles = getSampleStyleSheet()
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=16,
        spaceAfter=30,
        alignment=1  # Centralizado
    )
    header_style = ParagraphStyle(
        'CustomHeader',
        parent=styles['Heading2'],
        fontSize=14,
        spaceAfter=20,
        spaceBefore=20
    )
    normal_style = styles['Normal']
    
    # Título principal
    story.append(Paragraph("IDENTIFICAÇÃO DE SERVIÇO", title_style))
    story.append(Spacer(1, 20))
    
    # Seção Serviço
    story.append(Paragraph("SERVIÇO", header_style))
    story.append(Paragraph(f"<b>Tipo:</b> {tipo_registro}", normal_style))
    story.append(Paragraph(f"<b>Nº do Registro:</b> {numero_registro}", normal_style))
    story.append(Paragraph(f"<b>Data do Registro:</b> {data_registro.strftime('%d/%m/%Y') if data_registro else 'N/A'}", normal_style))
    story.append(Paragraph(f"<b>Validade:</b> {validade_registro.strftime('%d/%m/%Y') if data_registro else 'N/A'}", normal_style))
    story.append(Spacer(1, 15))
    
    # Seção Cliente
    story.append(Paragraph("CLIENTE", header_style))
    story.append(Paragraph(f"<b>Nome:</b> {nome_cliente}", normal_style))
    story.append(Paragraph(f"<b>CPF/CNPJ:</b> {documento}", normal_style))
    if email:
        story.append(Paragraph(f"<b>E-mail:</b> {email}", normal_style))
    if telefone:
        story.append(Paragraph(f"<b>Telefone:</b> {telefone}", normal_style))
    if cep:
        story.append(Paragraph(f"<b>CEP:</b> {cep}", normal_style))
    if dados_adicionais:
        story.append(Paragraph(f"<b>Dados Adicionais:</b> {dados_adicionais}", normal_style))
    story.append(Spacer(1, 15))
    
    # Seção Descrição
    if descricao:
        story.append(Paragraph("DESCRIÇÃO DO PEDIDO", header_style))
        story.append(Paragraph(descricao, normal_style))
        story.append(Spacer(1, 15))
    
    # Seção Itens
    if not edited_df.empty and len(edited_df) > 0:
        story.append(Paragraph("ITENS DO PEDIDO", header_style))
        
        # Preparar dados da tabela
        table_data = [["Material", "Quantidade", "Valor Bruto", "Valor Líquido"]]
        for _, row in edited_df.iterrows():
            if pd.notna(row['Material']) and str(row['Material']).strip():
                table_data.append([
                    str(row['Material']),
                    str(row['Quantidade']) if pd.notna(row['Quantidade']) else '',
                    str(row['Valor bruto']) if pd.notna(row['Valor bruto']) else '',
                    str(row['Valor liquido']) if pd.notna(row['Valor liquido']) else ''
                ])
        
        if len(table_data) > 1:  # Se há dados além do cabeçalho
            table = Table(table_data, colWidths=[2*inch, 1*inch, 1.5*inch, 1.5*inch])
            table.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('FONTSIZE', (0, 0), (-1, 0), 12),
                ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                ('GRID', (0, 0), (-1, -1), 1, colors.black)
            ]))
            story.append(table)
    
    # Gerar PDF
    doc.build(story)
    buffer.seek(0)
    return buffer

# Botão de exportação para PDF
st.header("Exportar Documento")
col1, col2, col3 = st.columns([1, 1, 1])

with col2:
    if st.button("📄 Exportar para PDF", type="primary", use_container_width=True):
        if nome_cliente and numero_registro:  # Verificar se há dados básicos
            try:
                pdf_buffer = generate_pdf()
                
                # Criar link de download
                b64_pdf = base64.b64encode(pdf_buffer.getvalue()).decode()
                href = f'<a href="data:application/pdf;base64,{b64_pdf}" download="ordem_servico_{numero_registro}_{nome_cliente}.pdf">Clique aqui para baixar o PDF</a>'
                st.markdown(href, unsafe_allow_html=True)
                
                st.success("PDF gerado com sucesso! Clique no link acima para baixar.")
                
            except Exception as e:
                st.error(f"Erro ao gerar PDF: {str(e)}")
        else:
            st.warning("Por favor, preencha pelo menos o nome do cliente e número do registro antes de exportar.")