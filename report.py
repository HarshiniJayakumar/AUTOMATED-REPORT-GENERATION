

from tkinter import Tk, filedialog
from fpdf import FPDF
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.platypus import Table, TableStyle
from reportlab.lib import colors
import matplotlib.pyplot as plt
from collections import Counter, defaultdict
from reportlab.platypus import Table, TableStyle
from reportlab.lib.units import inch
import csv

# -- File Picker for CSV --
def pick_file():
    root = Tk()
    root.withdraw() 
    return filedialog.askopenfilename(
        title="Select your Sales Performance CSV file",
        filetypes=[("CSV files", "*.csv")])

# -- Read CSV Data --
def read_data(filepath):
    records = []
    with open(filepath, newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        for i, row in enumerate(reader):
            if i == 0 and row[0].lower() in ['agent', 'name']:
                continue
            if len(row) == 4:
                z=[]
                for x in row:
                    z.append(x.strip())
                records.append(tuple(z))
                #records.append(tuple(x.strip() for x in row))
    return records

# -- Analyze Data --
def analyze_sales_data(data):
    agent_sales = defaultdict(list)
    region_sales = defaultdict(list)
    level_counts = Counter()
    for agent, region, sales, level in data:
        sale_val = float(sales)
        agent_sales[agent].append(sale_val)
        region_sales[region].append(sale_val)
        level_counts[level] += 1
    avg_agent_sales = {agent: sum(sales)/len(sales) for agent, sales in agent_sales.items()}
    avg_region_sales = {region: sum(sales)/len(sales) for region, sales in region_sales.items()}
    return avg_agent_sales, avg_region_sales, level_counts

# -- Charts --
def create_bar_chart(data, title):
    labels = list(data.keys())
    values = list(data.values())
    plt.figure(figsize=(7, 4))
    plt.bar(labels, values, color='lightgreen')
    plt.title(title)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.close()
    
def create_scatter_chart(data,title):
    x=list(data.keys())
    y=list(data.values())
    plt.figure(figsize=(10,4))
    plt.scatter(x,y)
    plt.title(title)
   

def create_pie_chart(data, title):
    labels = list(data.keys())
    sizes = list(data.values())
    plt.figure(figsize=(6, 4))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%')
    plt.title(title)
    plt.tight_layout()
    plt.close()

# -- PDF Report --
def generate_sales_pdf(data, avg_agent, avg_region, level_summary, filename):
    c = canvas.Canvas(filename, pagesize=A4)
    width, height = A4

    def draw_header_footer(page_num):
        c.setFont("Helvetica-Bold", 14)
        c.drawCentredString(width/2, height - 40, "Sales Agent Performance Report")
        c.setFont("Helvetica", 10)
        c.setFont("Helvetica-Oblique", 9)
        c.drawCentredString(width / 2, 10, f"Page {page_num}")

    page_num = 1
    draw_header_footer(page_num)


    table_data = [["Agent", "Region", "Sales", "Level"]] + list(data)
    table = Table(table_data, colWidths=[1.5*inch]*4)
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.darkblue),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.lightgrey),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ]))
    table.wrapOn(c, width, height)
    table_height = len(table_data) * 18
    table.drawOn(c, 50, height - 100 - table_height)

    c.showPage()
    page_num += 1
 
    draw_header_footer(page_num)
      

    y = height - 90
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, y, "Average Sales per Agent:"); y -= 16
    c.setFont("Helvetica", 10)
    for name, avg in avg_agent.items():
        c.drawString(60, y, f"{name}: {avg:.2f}"); y -= 14

    y -= 10
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, y, "Average Sales per Region:"); y -= 16
    c.setFont("Helvetica", 10)
    for region, avg in avg_region.items():
        c.drawString(60, y, f"{region}: {avg:.2f}"); y -= 14

    y -= 10
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, y, "Performance Level Summary:"); y -= 16
    c.setFont("Helvetica", 10)
    for level, count in level_summary.items():
        c.drawString(60, y, f"{level}: {count}"); y -= 14

    create_bar_chart(avg_region, "Avg. Sales by Region")
    create_pie_chart(level_summary, "Agent Level Distribution")
    create_scatter_chart(avg_agent,"Avg. Sales per Agent")
    print(f"✅ PDF saved: {filename}")

# -- Main Execution --
if __name__ == "__main__":
    print("Only csv file is accepted")
    print()
    path = pick_file()
    if not path:
        print("❌ No file selected.")
        exit()

    records = read_data(path)
    if not records:
        print("⚠️ No valid 4-column records found in CSV.")
    else:
        avg_agent, avg_region, level_summary = analyze_sales_data(records)
        generate_sales_pdf(records, avg_agent, avg_region, level_summary, "Sales_Report.pdf")
