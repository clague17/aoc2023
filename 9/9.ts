import { Matrix, lusolve, matrix } from 'mathjs';
import fs from "fs";

function approximateTerm(x: number[], term: number) {
  // Given the column vector x for the system Ax = b and the term to approximate
  // This is hardcoded to degree 4 polynomials
  return x.reduce((acc, val, idx) => {
    return acc + val *  Math.pow(term, x.length - 1 - idx)
  }, 0)
}

async function geoApprox(points: Array<[number, number]>, ): Promise<number> {
  const degree = points.length - 1
// Create the matrix and vector for the system of equations
let A: Array<Array<number>> = [];
let b: Array<number> = [];

for (let [x, y] of points) {
    let row: number[] = [];
    for (let i = degree; i >= 0; i--) {
        row.push(Math.pow(x, i));
    }
    A.push(row);
    b.push(y);
}

// Solve the system of equations
let coefficients = lusolve(matrix(A), matrix(b));

return approximateTerm(coefficients.toArray() as number[], 6)
}

async function main() {
  let inputFile = fs.readFileSync('ex.txt', 'utf-8').split('\n');
  console.log('inputFile', inputFile.length)
  const num = (await Promise.all(inputFile.map((line) => {
    let points = line.split(' ').map((val, idx) => [idx, Number(val)] as [number, number]);
    return geoApprox(points);
  }))).reduce((a, b) => a + b, 0)
  console.log(num)
}

main()

/*
* So this works, but unsure why it doesn't work on the input. 
* Potentially because the LU decomposition breaks down if the matrix is singular, which I'm assuming it could be :/ 
*/ 

