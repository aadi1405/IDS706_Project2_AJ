# Project2_AJ - CUSTOMER ANALYSIS COMMAND LINE TOOL


Hello everyone! Welcome to my Project for IDS706

## Goal of the Project

- To build a Bash command-line tool that performs useful data preparation task such as truncating data, sorting it, cleaning data, or doing ETL. 
- To analyze a customer dataset that can help companies assess their customers and make improvements in their products accordingly.



## Useful command line commands - 
- ls : to list out all the files & folders in current space
- cat <file_name> : to view the contents of the file
- vi <file_name> : to edit the file
- cd <folder_name> : to change directory
- head <file_name> : to list first few entries
- tail <file_name> : to list last few entries
- head -n <number_of_entries_wanted> <file_name> : to list the specific number of entries from top of the file
- tail -n <number_of_entries_wanted> <file_name> : to list the specific number of entries from bottom of the file



## Useful Keyboard Shortcuts -
- arrow up/down key : to get the most recently typed commands
- Command + e : to go to end of line
- Tab : to autofill
- :wq : to save and exit editor
- escape + insert : to start inserting on the editor


## Flow Chart about the Customer Analysis System
![Blank diagram](https://user-images.githubusercontent.com/67281453/194789066-3857c207-c654-4298-ad67-42d5cfa0e04e.png)


Data Source : https://www.kaggle.com/code/aashidutt3/eda-student-study-performance/data 

## About the Dataset

People

ID: Customer's unique identifier
Year_Birth: Customer's birth year
Education: Customer's education level
Marital_Status: Customer's marital status
Income: Customer's yearly household income
Kidhome: Number of children in customer's household
Teenhome: Number of teenagers in customer's household
Dt_Customer: Date of customer's enrollment with the company
Recency: Number of days since customer's last purchase
Complain: 1 if the customer complained in the last 2 years, 0 otherwise

Products

MntWines: Amount spent on wine in last 2 years
MntFruits: Amount spent on fruits in last 2 years
MntMeatProducts: Amount spent on meat in last 2 years
MntFishProducts: Amount spent on fish in last 2 years
MntSweetProducts: Amount spent on sweets in last 2 years
MntGoldProds: Amount spent on gold in last 2 years

Promotion

NumDealsPurchases: Number of purchases made with a discount
AcceptedCmp1: 1 if customer accepted the offer in the 1st campaign, 0 otherwise
AcceptedCmp2: 1 if customer accepted the offer in the 2nd campaign, 0 otherwise
AcceptedCmp3: 1 if customer accepted the offer in the 3rd campaign, 0 otherwise
AcceptedCmp4: 1 if customer accepted the offer in the 4th campaign, 0 otherwise
AcceptedCmp5: 1 if customer accepted the offer in the 5th campaign, 0 otherwise
Response: 1 if customer accepted the offer in the last campaign, 0 otherwise

Place

NumWebPurchases: Number of purchases made through the company’s website
NumCatalogPurchases: Number of purchases made using a catalogue
NumStorePurchases: Number of purchases made directly in stores
NumWebVisitsMonth: Number of visits to company’s website in the last month


## Some of the function available in this project 
- [getinfo] To get details of the data set 
- [randomsample] To get fice random samples from the dataset
- [shape] To get the shape of the dataset
- [diffedu] To return the different cateogaries of education of the customers in the dataset
- [eduvalue(x,y)]  return the average amount spent on a particular class of product by a particular customer class based on education
- [describe] To describe the dataset
- [countforme] To count the total number of purchases made in a particular mode
 
## Useful Resources :
- http://omgenomics.com/bash-intro/
