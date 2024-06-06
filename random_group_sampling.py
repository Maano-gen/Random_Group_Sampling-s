import random
import numpy as np

# Define the groups
group_A = [
    "A101", "A102", "A103", "A104", "A105", "A106",
    "A201", "A202", "A203", "A204", "A205", "A206",
    "A301", "A302", "A303", "A304", "A305", "A306",
    "A401", "A402", "A403", "A404", "A405", "A406",
    "A501", "A502", "A503", "A504", "A505", "A506",
    "A601", "A602", "A603", "A604", "A605", "A606",
    "A701", "A702", "A703", "A704", "A705", "A706"
]

group_B = [
    "B111", "B112", "B113", "B114", "B115", "B116",
    "B211", "B212", "B213", "B214", "B215", "B216",
    "B311", "B312", "B313", "B314", "B315", "B316",
    "B411", "B412", "B413", "B414", "B415", "B416",
    "B511", "B512", "B513", "B514", "B515", "B516",
    "B611", "B612", "B613", "B614", "B615", "B616",
    "B711", "B712", "B713", "B714", "B715", "B716"
]

group_C = [
    "C121", "C122", "C123", "C124", "C125", "C126",
    "C221", "C222", "C223", "C224", "C225", "C226",
    "C321", "C322", "C323", "C324", "C325", "C326",
    "C421", "C422", "C423", "C424", "C425", "C426",
    "C521", "C522", "C523", "C524", "C525", "C526",
    "C621", "C622", "C623", "C624", "C625", "C626",
    "C721", "C722", "C723", "C724", "C725", "C726"
]

# Combine all groups into one list
all_entries = group_A + group_B + group_C

# Randomize the combined list
random.shuffle(all_entries)

# Function to divide the entries into 'num_groups' random groups
def create_random_groups(entries, num_groups):
    final_groups = [[] for _ in range(num_groups)]
    for entry in entries:
        random_group_index = random.randrange(num_groups)
        final_groups[random_group_index].append(entry)
    return final_groups

# Number of groups
num_groups = 7

# Create the 7 random groups
final_groups = create_random_groups(all_entries, num_groups)

# Write the groups to a text file
with open("groups.txt", "w") as file:
    for i, group in enumerate(final_groups, start=1):
        file.write(f"Group {i}:\n")
        file.write("\n".join(group))
        file.write("\n\n")

# Statistics calculation function
def calculate_statistics(groups):
    statistics = []
    for group in groups:
        group_counts = len(group)
        statistics.append(group_counts)
    return statistics

# Calculate statistics for the groups
group_statistics = calculate_statistics(final_groups)

# Calculate mean, median, and standard deviation of counts
mean_counts = np.mean(group_statistics)
median_counts = np.median(group_statistics)
std_dev_counts = np.std(group_statistics)

# Print the results
print("Statistics for the 7 Random Groups based on Sample Counts:")
print(f"Mean counts: {mean_counts}")
print(f"Median counts: {median_counts}")
print(f"Standard deviation of counts: {std_dev_counts}")

# Generate HTML report
with open("final.html", "w") as html_file:
    html_file.write("<!DOCTYPE html>\n<html lang='en'>\n<head>\n<meta charset='UTF-8'>\n")
    html_file.write("<meta name='viewport' content='width=device-width, initial-scale=1.0'>\n")
    html_file.write("<title>Random Group Division Report</title>\n<style>\n")
    html_file.write("body {font-family: Arial, sans-serif;margin: 20px;}\n")
    html_file.write("h1 {text-align: center;}\n.report-section {margin-bottom: 30px;}\n")
    html_file.write(".code-block {background-color: #f5f5f5;padding: 10px;border-radius: 5px;overflow-x: auto;}\n")
    html_file.write("</style>\n</head>\n<body>\n<h1>Random Group Division Report</h1>\n")
    html_file.write("<div class='report-section'>\n<h2>Introduction</h2>\n<p>This report presents the process and results of dividing a total of 126 units/plants into 7 random groups. The units/plants are initially categorized into three groups labeled A, B, and C. The goal is to completely randomize these units/plants and distribute them evenly among the 7 groups.</p>\n</div>\n")
    html_file.write("<div class='report-section'>\n<h2>Code Explanation</h2>\n<p>The provided Python code performs the following tasks:</p>\n<ol>\n<li>Defines three groups labeled A, B, and C, each containing a certain number of units/plants.</li>\n<li>Combines all units/plants into a single list and shuffles them randomly.</li>\n<li>Divides the shuffled units/plants into 7 groups using a random distribution method.</li>\n<li>Calculates statistics such as mean, median, and standard deviation of the counts for each group.</li>\n<li>Writes the final groups into a text file named 'groups.txt'.</li>\n</ol>\n<p>The code utilizes Python's random module for shuffling and random distribution, as well as numpy for statistical calculations.</p>\n</div>\n")
    
    # Adding the groups to the report
    html_file.write("<div class='report-section'>\n<h2>Final Groups</h2>\n")
    for i, group in enumerate(final_groups, start=1):
        html_file.write(f"<h3>Group {i}:</h3>\n<ul>\n")
        for entry in group:
            html_file.write(f"<li>{entry}</li>\n")
        html_file.write("</ul>\n")
    html_file.write("</div>\n")

    # Adding the statistics to the report
    html_file.write("<div class='report-section'>\n<h2>Statistics</h2>\n<p>Statistics for the 7 Random Groups based on Sample Counts:</p>\n<ul>\n")
    html_file.write(f"<li>Mean counts: {mean_counts}</li>\n")
    html_file.write(f"<li>Median counts: {median_counts}</li>\n")
    html_file.write(f"<li>Standard deviation of counts: {std_dev_counts}</li>\n")
    html_file.write("</ul>\n</div>\n")

    html_file.write("<div class='report-section'>\n<h2>Code Implementation</h2>\n<div class='code-block'>\n<pre><code>")
    with open(__file__, 'r') as python_file:
        for line in python_file:
            html_file.write(line.replace('<', '<').replace('>', '>'))
    html_file.write("</code></pre>\n</div>\n</div>\n")
    html_file.write("</body>\n</html>")
