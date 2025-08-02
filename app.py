from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

class JavaRandom:
    def __init__(self, seed):
        self.seed = (seed ^ 0x5DEECE66D) & ((1 << 48) - 1)

    def next(self, bits):
        self.seed = (self.seed * 0x5DEECE66D + 0xB) & ((1 << 48) - 1)
        return self.seed >> (48 - bits)

    def nextInt(self, n):
        if (n & -n) == n:
            return (n * self.next(31)) >> 31
        bits, val = self.next(31), 0
        while (val := bits % n) + (n - 1) - bits < 0:
            bits = self.next(31)
        return val

def is_bedrock(x, y, z, seed=0):
    if y > 4 and y < 123:
        return False
    rand_seed = x * 341873128712 + z * 132897987541 + seed
    rng = JavaRandom(rand_seed)
    return y < rng.nextInt(5) if y <= 4 else y > 255 - rng.nextInt(5)

@app.route('/')
def home():
    return render_template('chunk.html')

@app.route('/find_chunk', methods=['GET'])
def find_chunk():
    try:
        chunk_x = int(request.args.get('chunk_x'))
        chunk_z = int(request.args.get('chunk_z'))
        y = int(request.args.get('y', 0))
        grid = []

        base_x = chunk_x * 16
        base_z = chunk_z * 16

        for x_off in range(16):
            row = []
            for z_off in range(16):
                world_x = base_x + x_off
                world_z = base_z + z_off
                row.append(is_bedrock(world_x, y, world_z))
            grid.append(row)

        return jsonify({"chunk_x": chunk_x, "chunk_z": chunk_z, "y": y, "grid": grid})
    except (TypeError, ValueError):
        return jsonify({"error": "Invalid chunk coordinates"}), 400

if __name__ == '__main__':
    app.run(debug=True)
