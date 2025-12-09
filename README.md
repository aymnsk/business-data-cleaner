# Business Automation Portfolio

Practical Python scripts for business automation, data processing, and workflow optimization.

## Projects

### 1. Business Data Cleaner
- Cleans messy CSV files (removes duplicates, standardizes formats, fixes dates)
- ETL pipeline ready
- Outputs to Excel with detailed logs

### 2. Outlook Attachment Automation (Proof of Concept)
- Automated email attachment downloading
- Configurable search criteria (sender, subject, date range)
- Error handling and logging
- Can be extended with win32com (Windows) or imaplib (cross-platform)

### 3. API Data Fetcher
- Bulk API processing with rate limiting
- CSV input/output
- Simulated for services like Zillow Zestimate, real estate data, etc.

## Use Cases
- Automate manual data entry tasks
- Clean and transform business data
- Integrate with external APIs
- Build internal tools for startups/small businesses

## Tech Stack
- Python (Pandas, logging, os)
- SQL (MySQL/PostgreSQL)
- Linux/Windows automation
- Git version control

## Quick Start
1. Clone repository
2. Install requirements: `pip install pandas`
3. Run any script: `python clean_data.py input.csv output.xlsx`
