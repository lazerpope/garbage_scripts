import { generate } from "./bigGenerator.js"
let date_delta = new Date().getTime()
console.log("Selection Sort")
let stepsList = []

let time_table = []
let repeat = 100
let base = 2

console.log(`arr of 10^${base} generated ${repeat} times `)

let toSort = []
for (let i = 0; i < repeat; i++) {
  toSort.push(generate(base))
}

function sort(arr) {
  let steps = 0
  //console.log(`Initial ${arr}`)
  let date_ob = new Date().getTime()
  for (let i = 0; i < arr.length; i++) {
    let max = arr[i]
    let max_i = i
    for (let j = i + 1; j < arr.length; j++) {
      steps ++
      if (max > arr[j]) {
        max = arr[j]
        max_i = j
      }
    }
    ;[arr[i], arr[max_i]] = [arr[max_i], arr[i]]
  }
  stepsList.push(steps)
  time_table.push(new Date().getTime() - date_ob)
  //console.log(`Final ${arr}`)
}

for (let n = 0; n < repeat; n++) {
  sort(toSort[n])
}

let avg = time_table.reduce((a, b) => a + b) / time_table.length 
avg = (avg / 1000).toFixed(3)
console.log(`avg time is ${avg} s based on ${time_table.length} repeats`)
date_delta = ((new Date().getTime() - date_delta) / 1000).toFixed(3)
console.log(`whole process took ${date_delta} s `)
console.log(`sorting ${avg * repeat} s `)
console.log(`other ${date_delta - avg * repeat} s `)
let avgSteps = stepsList.reduce((a, b) => a + b) / stepsList.length 
console.log(`avg steps ${avgSteps}  `)