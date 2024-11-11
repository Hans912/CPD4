import csv

def process_athlete_data(file_path):

   # Extracting athlete stats by year
   records = []

   # Extracting athlete races
   races = []           

   global athlete_name
   athlete_name = ""
   athlete_id = ""
   comments = ""

   with open(file_path, newline='', encoding='utf-8') as file:
      reader = csv.reader(file)
      data = list(reader)

      athlete_name = data[0][0]
      print(athlete_name)
      athlete_id = data[1][0]
      print(f"The athlete id for {athlete_name} is {athlete_id}")

      for row in data[5:-1]:
         if row[2]:
            records.append({"year": row[2], "sr": row[3]})
         else:
            races.append({
               "finish": row[1],
               "time": row[3],
               "meet": row[5],
               "url": row[6],
               "comments": row[7]
            })

   return {
      "name": athlete_name,
      "athlete_id": athlete_id,
      "season_records": records,
      "race_results": races,
      "comments": comments
   }    

def gen_athlete_page(data, outfile):
   # template 
   # Start building the HTML structure
   html_content = f'''<!DOCTYPE html>
   <html lang="en">
   <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
       <!-- Get your own FontAwesome ID -->
       <script src="https://kit.fontawesome.com/7703f3cfbe.js" crossorigin="anonymous"></script>

      <link rel="preconnect" href="https://fonts.googleapis.com">
      <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
      <link href="https://fonts.googleapis.com/css2?family=Andika:ital,wght@0,400;0,700;1,400;1,700&family=Jacques+Francois&family=Oxanium:wght@200..800&display=swap" rel="stylesheet">

      <link href="../dist/css/lightbox.css" rel="stylesheet">
      <link rel = "stylesheet" href = "../css/reset.css">
      <link rel = "stylesheet" href = "../css/style.css">
      

      <title>{data["name"]}</title>
   </head>
   <body>
   <div class="grid"> 
   <a class= "skip" href = "#main">Skip to Main Content</a>
      <header>
         <div class="logo"><h1>PROGRUN</h1></div>
         <nav class="top_nav">
            <ul class="top_link">
               <li id="home"><i class="fa-solid fa-house"></i> <a href="../index.html">Home Page</a></li>
               <li><a href="mens.html">Men's Team</a></li>
               <li><a href="womens.html">Women's Team</a></li>
            </ul>
         </nav>
      </header>
      <div>
         <section id="athlete_name">
            <!--Athlete would input headshot-->
            <h2>{data["name"]}</h2>
            <a href = "../images/profiles/{data["athlete_id"]}.jpg" target="_blank" data-lightbox="athlete" data-title="{data["name"]}" data-alt="Athlete headshot" aria-label="Athlete Headshot" id="light">
               <img src="../images/profiles/{data["athlete_id"]}.jpg" alt="Athlete headshot" width="200" id="prof_pic"> 
            </a>
         </section>
      </div>
         <main id = "main">
            <section id= "athlete-sr-table">
               <h3>Athlete's Seasonal Records (SR) per Year</h3>
                  <table>
                        <thead>
                           <tr>
                              <th> Year </th>
                              <th> Season Record (SR)</th>
                           </tr>
                        </thead>
                        <tbody>
                        '''
   
   for sr in data["season_records"]:
      sr_row = f'''
                     <tr>
                        <td>{sr["year"]}</td>
                        <td>{sr["sr"]}</td>
                     </tr>                  
               '''
      html_content += sr_row

   html_content += '''                   
                </tbody>
                  </table>
                     </section>


                        <section id="athlete-result-table">
                        <h3>Race Results</h3>
                           

                           <table id="athlete-table">
                              <thead>
                                 <tr>
                                    <th>Race</th>
                                    <th>Athlete Time</th>
                                    <th>Athlete Place</th>
                                    <th>Race Comments</th>
                                 </tr>
                              </thead>

                              <tbody>
                  '''

   # add each race as a row into the race table 
   for race in data["race_results"]:
      race_row = f'''
                                 <tr class="result-row">
                                    <td>
                                       <a href="{race["url"]}">{race["meet"]}</a>
                                    </td>
                                    <td>{race["time"]}</td>
                                    <td>{race["finish"]}</td>
                                    <td>{race["comments"]}</td>
                                 </tr>
      '''
      html_content += race_row

   html_content += '''
                              </tbody>

                        </table>
                     </section>
                     <section id = "gallery">
                     <h3>Gallery</h3>
                     <p><i class="fa-solid fa-person-digging"></i></i> Under construction :) <i class="fa-solid fa-person-digging"></i></p>
                     </section>
                     </main>
         <footer class="footer">
            <p>
            Skyline High School<br>
            <address>
            2552 North Maple Road<br>
            Ann Arbor, MI 48103<br>   
            <a href = "https://sites.google.com/aaps.k12.mi.us/skylinecrosscountry2021/home">XC Skyline Page</a><br>
            <a href = "https://www.instagram.com/a2skylinexc/">Follow us on Instagram <i class="fa-brands fa-instagram" aria-label="Instagram"></i></a>
         </footer>
      </div>
      <script src="../dist/js/lightbox-plus-jquery.js"></script>
      <script src="../js/replace.js"></script>
   </body>
   </html>
   '''

   with open(outfile, 'w') as output:
      output.write(html_content)

def generate_nav_links(folder_path):
    import os
    print(folder_path)
    """Generate the HTML structure for the nav section."""
    html_files = [f for f in os.listdir(folder_path) if f.endswith('.html')]
    
    nav_content = '<ul class="dropdown-content">\n'
    for file in html_files:
        file_name = file.replace('.html', '')
        nav_content += f'  <li><a href="mens_team/{file}">{file_name}</a></li>\n'
    nav_content += '</ul>\n'

    return nav_content

def update_index_html(index_file, folder_path):
    import re

    """Update index.html by adding or replacing the dropdown nav section."""
    with open(index_file, 'r') as file:
        content = file.read()

    # Remove any existing dropdown content
    content = re.sub(r'<ul class="dropdown-content">.*?</ul>\n', '', content, flags=re.DOTALL)

    # Generate the new dropdown content
    new_nav = generate_nav_links(folder_path)

    # Find the position where the new nav should go (after </button>)
    button_end_index = content.find('</button>')

    if button_end_index != -1:
        # Insert the new nav section right after the button
        updated_content = (
            content[:button_end_index + 9] +  # After </button>
            '\n' + new_nav + 
            content[button_end_index + 9:]
        )
    else:
        print("No <button> tag found in index.html. Dropdown not added.")
        return

    # Write the updated content back to index.html
    with open(index_file, 'w') as file:
        file.write(updated_content)

def main():

   import os
   import glob

   # Define the folder path
   folder_path = 'CPD3/mens_team/'
   # Get all csv files in the folder
   csv_files = glob.glob(os.path.join(folder_path, '*.csv'))
   print(csv_files)

   print("hello")
   # Extract just the file names (without the full path)
   csv_file_names = [os.path.basename(file) for file in csv_files]

   # Output the list of CSV file names
   print(csv_file_names)
   print("hello2")
   for file in csv_file_names:
      print(file)

      # read data from file
      athlete_data = process_athlete_data(folder_path+file)
      # using data to generate templated athlete page
      gen_athlete_page(athlete_data, folder_path+file.replace(".csv",".html").replace(" ", ""))

      # read data from file
      # athlete_data2 = process_athlete_data(filename2)
      # using data to generate templated athlete page
      # gen_athlete_page(athlete_data2, "enshu_kuan.html")


   # Define the folder path
   folder_path2 = 'CPD3/womens_team/'
   # Get all csv files in the folder
   csv_files2 = glob.glob(os.path.join(folder_path2, '*.csv'))

   # Extract just the file names (without the full path)
   csv_file_names2 = [os.path.basename(file2) for file2 in csv_files2]

   # Output the list of CSV file names
   print(csv_file_names2)
   for file2 in csv_file_names2:

      # read data from file
      athlete_data2 = process_athlete_data(folder_path2+file2)
      # using data to generate templated athlete page
      gen_athlete_page(athlete_data2, folder_path2+file.replace(".csv",".html").replace(" ", ""))

      # read data from file
      # athlete_data2 = process_athlete_data(filename2)
      # using data to generate templated athlete page
      # gen_athlete_page(athlete_data2, "enshu_kuan.html")
   print("hello3")
   update_index_html('CPD3/index.html', folder_path)

if __name__ == '__main__':
    main()
