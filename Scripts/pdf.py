#!/usr/local/bin/python3
from uuid import uuid4
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.piecharts import Pie
from reportlab.lib.units import inch

fruit = {
  "elderberries": 1,
  "figs": 1,
  "apples": 2,
  "durians": 3,
  "bananas": 5,
  "cherries": 8,
  "grapes": 13
}

styles = getSampleStyleSheet()
report = SimpleDocTemplate("./reports/" + str(uuid4()) + ".pdf")

table_data = []
for fruitN, fruitV in fruit.items():
   table_data.append([fruitN, fruitV])

table_style = [('GRID', (0,0), (-1,-1), 1, colors.black)]

report_title = Paragraph("A Complete Inventory of My Fruit", styles["h2"])

report_table = Table(data=table_data, style=table_style, hAlign="LEFT")

report_pie = Pie(width=3*inch, height=3*inch)

report_pie.data = []

report_pie.labels = []

for fruit_name in sorted(fruit):
   report_pie.data.append(fruit[fruit_name])
   report_pie.labels.append(fruit_name)

report_chart = Drawing()
report_chart.add(report_pie)

report.build([report_title, report_table, report_chart])