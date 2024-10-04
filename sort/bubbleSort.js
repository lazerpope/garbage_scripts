import { generate } from "./bigGenerator.js"
let date_delta = new Date().getTime()
console.log('Bubble Sort')
let stepsList = []

let time_table = []
let repeat = 100
let base = 2

let toSort = []
for (let i = 0; i < repeat; i++) {
  toSort.push(generate(base))
}
console.log(`arr of 10^${base} generated ${repeat} times `);

function sort(arr) {
  //console.log(`Initial ${arr}`)
  let steps = 0
  let date_ob = new Date().getTime()

  let swapped
 
  do {
    swapped = false
    let end = arr.length - 1
    
    for (let i = 0; i < end; i++) {
      steps ++
      if (arr[i] > arr[i + 1]) {
        swapped = true
        let temp = arr[i]
        arr[i] = arr[i+1]
        arr[i+1]  =temp
      }
    }
    end--
  } while (swapped)

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