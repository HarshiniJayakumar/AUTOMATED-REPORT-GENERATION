# AUTOMATED-REPORT-GENERATION

COMPANY: CODTECH IT SOLUTIONS

NAME: HARSHINI J

INTERN ID: CT04DG2834

DOMAIN: PYTHON PROGRAMMING

DURATION: 4 WEEKS

MENTOR: NEELA SANTOSH

DESCRIPTION

For this task,I choose to work with the project titled “Sales Agent Performance Report Generator”, which involved creating an automated system to analyze and generate PDF reports from CSV data using various tools and libraries in Python. The `tkinter` library was used to provide a simple graphical user interface . This library allows users to browse and select the input CSV file .The user no need to type file paths manually, making the tool user-friendly.  The built in 'csv' module in python was used, for reading and handling CSV data, which made it easy to extract, iterate, and clean data line by line. The data cleaning process involved removing unnecessary whitespace and validating that each row contained the required four fields: Agent, Region, Sales, and Performance Level. The `collections` module in python was used, specifically `defaultdict` and `Counter`, was used for performing the core data analysis. `defaultdict` allowed grouping of sales figures by agents and regions, while `Counter` efficiently tallied the number of agents at each performance level, such as Excellent, Good, or Average. For visual representation, the `matplotlib` library was instrumental in creating three types of charts: a bar chart that showed average sales across different regions, scatter chart that showed the average sales by each agent and a pie chart that visually represented the distribution of performance levels among agents. These charts were not only aesthetically informative but also essential in providing quick, visual insights into the dataset. Once the analysis and visualization were complete, the `ReportLab` library was used to create a professional-looking PDF report. This part of the project involved using `canvas` to create a multipage PDF, where I included a data table, summaries of average sales per agent and region, and embedded the charts as images. `ReportLab.platypus.Table` and `TableStyle` were particularly useful for rendering tabular data with styling such as grid lines, header backgrounds, and column alignment, ensuring the final PDF report was visually structured and easy to read. I also used `reportlab.lib.units.inch` to maintain consistency in element positioning, and `reportlab.lib.colors` to style the table and header sections attractively. In addition, page numbers and headers were dynamically generated to give the report a professional touch, simulating a real-world business document. The integration of all these libraries into one streamlined Python script allowed the application to function seamlessly, requiring minimal user input while producing a high-quality report. Each of these tools played a vital role: `tkinter` for user interaction, `csv` for file handling, `collections` for data analysis, `matplotlib` for visualization, and `ReportLab` for PDF generation. Working with this wide range of tools gave me a strong understanding of how different libraries can be combined to solve a real-world problem efficiently. More importantly, it taught me the value of choosing the right tool for each task and how to write clean, modular code that’s easy to extend or reuse. This project not only sharpened my technical abilities but also improved my confidence in designing and implementing practical software solutions using Python’s vast ecosystem of tools.

#OUTPUT

#View the pdf report

[Sales_Report.pdf](https://github.com/user-attachments/files/21216089/Sales_Report.pdf)




