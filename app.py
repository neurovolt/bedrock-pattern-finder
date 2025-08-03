
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Java Random implementation
class JavaRandom:
    def __init__(self, seed):
        self.seed = (seed ^ 0x5DEECE66D) & ((1 << 48) - 1)

    def next(self, bits):
        self.seed = (self.seed * 0x5DEECE66D + 0xB) & ((1 << 48) - 1)
        return self.seed >> (48 - bits)

    def next_int(self, bound):
        if bound <= 0:
            raise ValueError("bound must be positive")
        if (bound & (bound - 1)) == 0:
            return (bound * self.next(31)) >> 31
        bits = self.next(31)
        val = bits % bound
        while bits - val + (bound - 1) < 0:
            bits = self.next(31)
            val = bits % bound
        return val

# Generate bedrock pattern for a chunk
def generate_bedrock(chunk_x, chunk_z, y=-60):
    pattern = [[0 for _ in range(16)] for _ in range(16)]
    seed = chunk_x * 341873128712 + chunk_z * 132897987541 + y
    for x in range(16):
        for z in range(16):
            rnd = JavaRandom(seed + x * x * 4987142 + x * 5947611 + z * z * 4392871 + z * 389711)
            if rnd.next_int(5) == 0:
                pattern[z][x] = 1  # bedrock
    return pattern

@app.route('/')
def index():
    return render_template('pattern.html')

@app.route('/find', methods=['POST'])
def find_chunk():
    data = request.json
    grid = data.get('grid')
    matches = []

    for cx in range(-1000, 1001):
        for cz in range(-1000, 1001):
            if generate_bedrock(cx, cz) == grid:
                matches.append({'x': cx, 'z': cz})

    return jsonify({'matches': matches})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
