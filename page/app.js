document.addEventListener('DOMContentLoaded', (event) => {
    fetch('../output.json')
        .then(response => response.json())
        .then(data => {
            window.courseData = data; 
            displayCourses(data);
        })
        .catch(error => console.error('Error loading JSON data:', error));
});

function displayCourses(courses) {
    const tableBody = document.getElementById('coursesTable').getElementsByTagName('tbody')[0];
    tableBody.innerHTML = '';

    courses.forEach(course => {
        course.Horarios.forEach(schedule => {
            const row = tableBody.insertRow();
            row.insertCell(0).innerText = course.No;
            row.insertCell(1).innerText = course.Sigla;
            row.insertCell(2).innerText = course.Asignatura;
            row.insertCell(3).innerText = schedule.Docente;
            row.insertCell(4).innerText = schedule.Día;
            row.insertCell(5).innerText = schedule.Horas;
            row.insertCell(6).innerText = schedule.Aula;
        });
    });
}

function searchCourses() {
    const searchValue = document.getElementById('search').value.toLowerCase();
    const filteredCourses = window.courseData.filter(course => 
        course.Asignatura.toLowerCase().includes(searchValue) || 
        course.Sigla.toLowerCase().includes(searchValue)
    );
    displayCourses(filteredCourses);
}