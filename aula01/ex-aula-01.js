let matriz1 = [[],[],[]]

let matriz2 = [[],[],[]]

let matriz3 = [[],[],[]]

for (let row = 0; row < height; row++) {
  for (let column = 0; column < width; column++) {
    if(row == 0 || column == 0 || row == height - 1 || column == width - 1) {
      matriz1[row][column] = "*"
    } else (
      matriz1[row][column] = "#"
    )
  }
}

for (let row = 0; row < height; row++) {
  for (let column = 0; column < width; column++) {
    if(row == 0 || row == 2) {
      matriz2[row][column] = "%"
    } else (
      matriz2[row][column] = "*"
    )
  }
}

for (let row = 0; row < height; row++) {
  for (let column = 0; column < width; column++) {
    if(column == 0 || column == 3) {
      matriz3[row][column] = "*"
    } else (
      matriz3[row][column] = "1"
    )
  }
}

console.log(matriz1)
console.log(matriz2)
console.log(matriz3)