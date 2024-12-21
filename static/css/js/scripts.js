async function loadExercises() {
    const response = await fetch('/exercises');
    const exercises = await response.json();
    const tableBody = document.getElementById('exerciseTable').getElementsByTagName('tbody')[0];
    tableBody.innerHTML = '';
    exercises.forEach((exercise) => {
        const row = `<tr>
            <td>${exercise.id}</td>
            <td>${exercise.name}</td>
            <td>${exercise.repetitions}</td>
            <td>${exercise.weight ?? 'N/A'}</td>
            <td>${exercise.duration ?? 'N/A'} min</td>
            <td>${new Date(exercise.created_at).toLocaleString()}</td>
            <td>
                <button onclick="editExercise(${exercise.id})">Edit</button>
                <button onclick="deleteExercise(${exercise.id})">Delete</button>
            </td>
        </tr>`;
        tableBody.innerHTML += row;
    });
}

async function deleteExercise(id) {
    const confirmDelete = confirm('Are you sure you want to delete this exercise?');
    if (confirmDelete) {
        await fetch(`/delete-exercise/${id}`, { method: 'DELETE' });
        alert('Exercise deleted!');
        loadExercises();
    }
}

function editExercise(id) {
    const name = prompt('Enter new exercise name:');
    const repetitions = prompt('Enter new repetitions:');
    const weight = prompt('Enter new weight (optional):');
    const duration = prompt('Enter new duration (mins, optional):');

    fetch(`/edit-exercise/${id}`, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ name, repetitions, weight, duration })
    }).then(() => {
        alert('Exercise updated!');
        loadExercises();
    });
}

// Load data on page load
window.onload = loadExercises;
