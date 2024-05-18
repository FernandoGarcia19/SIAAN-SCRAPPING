import json
import os

def simplify_json(data):
    courses_data = []
    for row in data["datos"]:
        course_info = {}
        for column in row:
            column_name = column["nombreColumna"]
            column_content = column["contenidoCelda"][0]["contenido"] if column["contenidoCelda"] else ""
            course_info[column_name] = column_content

        # Extract and simplify the "Horarios" information
        horarios = course_info.pop("Horarios", {}).get("datos", [])
        schedule_info = []
        for horario in horarios:
            schedule_info.append({
                "Tipo Docente": horario[0]["contenidoCelda"][0]["contenido"],
                "Docente": horario[1]["contenidoCelda"][0]["contenido"],
                "Día": horario[2]["contenidoCelda"][0]["contenido"],
                "Horas": horario[3]["contenidoCelda"][0]["contenido"],
                "Aula": horario[4]["contenidoCelda"][0]["contenido"]
            })
        course_info["Horarios"] = schedule_info

        courses_data.append(course_info)
    return courses_data

# Directory containing the .txt files
directory = 'scrapped_data'

# List to hold all processed course data
all_courses_data = []

# Iterate through each file in the directory
for filename in os.listdir(directory):
    if filename.endswith('.txt'):
        filepath = os.path.join(directory, filename)
        with open(filepath, 'r', encoding='utf-8') as file:
            json_data = file.read()
            parsed_data = json.loads(json_data)
            simplified_data = simplify_json(parsed_data)
            all_courses_data.extend(simplified_data)

# Write the collected data to a single output file
with open('output.txt', 'w', encoding='utf-8') as outfile:
    json.dump(all_courses_data, outfile, ensure_ascii=False, indent=4)

print("All data has been processed and written to output.txt")