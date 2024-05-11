import json

# Load JSON data from file with explicit encoding
with open('scrapped_data.txt', 'r', encoding='utf-8') as file:
    json_data = file.read()

# Parse the JSON data
parsed_data = json.loads(json_data)

# Extract relevant information
courses_data = []

for row in parsed_data["datos"]:
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

# Convert the extracted data to JSON
json_output = json.dumps(courses_data)

# Print the JSON output
print(json_output)