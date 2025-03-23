import openpyxl

# Cargar Archivo 

wb = openpyxl.load_workbook("Reportes_Ventas.xlsx")

for sheet in wb.sheetnames:
    ws = wb[sheet]
    for col in ws.columns:
        max_length = 0
        col_letter = col[0].column_letter #letra de la columna
        for cell in col:
            try:
                if cell.value: 
                    max_length = max(max_length, len(str(cell.value)))
            except:
                pass
        ws.column_dimensions[col_letter].wisth = max_length + 2 # Ajuste del ancho
        
# Guardar cambios
wb.save("Reportes_Ventas.xlsx")