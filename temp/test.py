import openpyxl, os
from openpyxl.styles import Font, colors

os.chdir("D:\\Chapter 12 - Excel files")

wb = openpyxl.load_workbook("produce_sales_updated.xlsx")
sheet = wb.active

# italic_24_font = Font(size=24, italic=True, bold=True, color=colors.RED)

# sheet["A1"].font = italic_24_font
# sheet["D4"] = "=D2+D3"


# wb.save("produce_sales_updated.xlsx")


x = sheet["D4"].value
y = sheet["A1"].value
print(x, y)
