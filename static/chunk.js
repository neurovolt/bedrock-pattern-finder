async function loadChunk() {
    let chunkX = document.getElementById('chunk_x').value;
    let chunkZ = document.getElementById('chunk_z').value;
    let y = document.getElementById('y').value;

    if (chunkX === "" || chunkZ === "") {
        alert("Please enter chunk X and Z!");
        return;
    }

    let res = await fetch(`/find_chunk?chunk_x=${chunkX}&chunk_z=${chunkZ}&y=${y}`);
    let data = await res.json();

    if (data.error) {
        alert("Error: " + data.error);
        return;
    }

    drawGrid(data.grid);
}

function drawGrid(grid) {
    let canvas = document.getElementById('canvas');
    let ctx = canvas.getContext('2d');
    let size = 20; // Each block = 20px

    ctx.clearRect(0, 0, canvas.width, canvas.height);

    for (let x = 0; x < 16; x++) {
        for (let z = 0; z < 16; z++) {
            ctx.fillStyle = grid[x][z] ? "#000" : "#ccc"; // Black = Bedrock
            ctx.fillRect(z * size, x * size, size, size);
            ctx.strokeStyle = "#222";
            ctx.strokeRect(z * size, x * size, size, size);
        }
    }
}
