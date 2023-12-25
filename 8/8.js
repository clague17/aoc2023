const fs = require('fs');

function parseInstructions(instructions) {
    let nodes = {};
    for (let line of instructions) {
        let [source, dest] = line.split(' = ');
        let [left, right] = dest.split(', ');
        nodes[source] = [left.slice(1), right.slice(0, right.length - 1)];
    }
    return nodes;
}

async function finder(node, graph, instructions) {
  let idx = 0;
  let iters = 1000000000;
  idx = 0
  while (idx < iters) {
    if (node[node.length - 1] === 'Z') {
        return idx;
    }
    switch (instructions[idx % instructions.length]) {
        case 'L':
            node = graph[node][0];
            break;
        case 'R':
            node = graph[node][1];
            break;
    }
    idx += 1;
  }
  return idx
}

async function main() {
    let inputFile = fs.readFileSync('input.txt', 'utf-8').split('\n');
    let instructions = inputFile[0].trim();
    let graph = parseInstructions(inputFile.slice(2));
    let frontier = Object.keys(graph).filter(x => x.slice(-1) === 'A');

    // Got this from https://stackoverflow.com/questions/31302054/how-to-find-the-least-common-multiple-of-a-range-of-numbers
    const gcd = (a, b) => b == 0 ? a : gcd (b, a % b)
    const lcm = (a, b) =>  a / gcd (a, b) * b
    const lcmAll = (ns) => ns .reduce (lcm, 1)

    const pathLengths = await Promise.all(frontier.map(async (node) => {
      return await finder(node, graph, instructions)
    }))
    return lcmAll(pathLengths)
    // Because the instructions are technically infinite repeating sequences, we can just find the LCM of the path lengths
    // to find the first time they all repeat. It is much much faster to do this numerically than it is to try traversing each one. 
    // I ended up writing the solution to part two in js, because of the perceived benefits in parallelism. However I learned that
    // js is single threaded, so tbd how much it actually ended up helping me :/ 
}

main().then(console.log);