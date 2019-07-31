# Scrape Read Me

### Make sure you have these files in your directory/folder
-	better_reads.py
-	summary_scrape.py
-	more_detail_genre_scrape.py
### Must use the better_reads.py scraper 1st for the other two scraper .py files to work

### Open your text editor 
-	For each scrape iteration you need to specify the number, start and end
-	Each time you run the script make sure to change the number, start and end variable
o	IMPORTANT: I suggest lowering the number of start and end count. Sometimes the website will timeout and forces the script to end. Then you’ll have to re-scrape again.
o	Make sure to change the number variable each time you run the script. This ensures that the summary csv file doesn’t get overridden.

### From command prompt
-	Make sure you change to the directory where the files are located.
-	Type in python <file_name>.py and enter
o	If you see an error pop on the command. No worries, it just means the website couldn’t find the tag and I’ve either scraped another tag or appended a null value

After running the better_reads.py you should have a Better_Books_Ever.csv in the same directory as the other 3 py file

Rinse and repeat with the other two scrape py files.

