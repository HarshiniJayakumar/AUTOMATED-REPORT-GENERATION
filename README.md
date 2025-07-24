# AUTOMATED-REPORT-GENERATION

COMPANY: CODTECH IT SOLUTIONS

NAME: HARSHINI J

INTERN ID: CT04DG2834

DOMAIN: PYTHON PROGRAMMING

DURATION: 4 WEEKS

MENTOR: NEELA SANTOSH

DESCRIPTION

For this task, I choose a project called **“Sales Agent Performance Report Generator”**.It takes sales data from a CSV file, make a understandable PDF report. The libraries used in this project are tkinter, csv, collections, matplotlib, reportlab, reportlab.platypus, reportlab.lib.units and reportlab.lib.colors .To make user-friendly, I used Python’s tkinter library to create a simple file selection window.  Users could just click and choose their CSV file. I used Python’s built-in csv module to read the data. Each row in the file contained details like the agent’s name, region, their sales amount, and performance level. I made sure to clean the data by removing extra spaces and checking for rows that had all four required fields. This initial stage helped ensure that the rest of the report would be accurate and based on clean, structured data. 

Once the data was ready, I moved on analyzing the data. I understand how to group and summarize information using Python. I used the collections module, which made it really easy to organize the sales figures. I calculated average sales for each agent and each region using defaultdict, which allowed me to group their sales numbers. Then I used Counter to count how many agents were marked as Excellent,Good, or other performance levels. This part of the project was really interesting, because I could really see the numbers coming together in a meaningful way. Instead of just looking at raw data, I was able to pull out patterns and insights, useful for business. 

After analyzing the data, I wanted to make it easier to understand by adding visual charts. Visual chart makes the users to understand about the data easily.I used the matplotlib library to create three types of charts: a bar chart that showed the average sales by region, a pie chart that showed the breakdown of performance levels and scatter chart about average sales by agent. These visuals helped turn plain numbers into something more engaging and easy to interpret. The charts also added in the PDF report. While creating these charts I learned how to choose the right type of visualization for different kinds of information. These small touches made the report not just informative, but also visually appealing and easier for someone to review quickly. 

The final part was turning all this into a well-structured PDF report. I used the ReportLab library to create a multi-page document that included the data table, the summary analysis, and the charts. I want the report should be professional , so I spent time making the report with headers, page numbers, and neatly styled tables. I used tools like TableStyle for formatting the tables and drawImage to insert the charts. I also paid attention to spacing and layout. Everything fit nicely on the pages. By the end, the report felt is generated successfully . The report might looks like a real sales meeting or performance review. This project taught me how to take raw data and turn it into something useful and presentable. More importantly, it showed me how different Python libraries can work together to build something practical and polished from start to finish.



#OUTPUT

#View the pdf report

[Sales_Report.pdf](https://github.com/user-attachments/files/21216089/Sales_Report.pdf)




