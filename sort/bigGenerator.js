let generate = function (base) {
  let arr = []
  let size = 10**base
  for (let i = 0; i < size; i++) {
    arr.push(getRandomInt(1000))
  }
  
  return arr
}
function getRandomInt(max) {
  return Math.floor(Math.random() * max)
}

const _generate = generate;
export { _generate as generate };
