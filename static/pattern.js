
const grid = document.getElementById('grid');
let cells = [];

for (let y = 0; y < 16; y++) {
    cells[y] = [];
    for (let x = 0; x < 16; x++) {
        const cell = document.createElement('div');
        cell.classList.add('cell');
        cell.dataset.x = x;
        cell.dataset.y = y;
        cell.addEventListener('click', () => {
            cell.classList.toggle('active');
        });
        grid.appendChild(cell);
        cells[y][x] = cell;
    }
}

function getGridData() {
    return cells.map(row => row.map(cell => cell.classList.contains('active') ? 1 : 0));
}

function clearGrid() {
    cells.forEach(row => row.forEach(cell => cell.classList.remove('active')));
}

function findChunk() {
    fetch('/find', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({grid: getGridData()})
    })
    .then(res => res.json())
    .then(data => {
        const output = document.getElementById('output');
        if (data.matches.length > 0) {
            output.textContent = "Matches found:\n" + data.matches.map(m => `Chunk X: ${m.x}, Z: ${m.z}`).join('\n');
        } else {
            output.textContent = "No matches found in range.";
        }
    });
}
