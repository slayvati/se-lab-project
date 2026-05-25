fetch("/birthdays")
    .then(response => response.json())
    .then(data => {

        const container = document.getElementById("container")

        if (data.length === 0) {
            container.innerHTML = "<h2>No birthdays today</h2>"
        }

        data.forEach(person => {

            container.innerHTML += `
                <div class="card">
                    <img src="/static/images/${person.image}">
                    <h2>Happy Birthday ${person.name} 🎂</h2>
                </div>
            `
        })
    })