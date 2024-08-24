function solution(n, computers) {
  var result = 0
  const visited = new Array(n).fill(false)

  for (let i = 0; i < computers.length; i++) {
    if (!visited[i]) {
      bfs(computers[i], i)
    }
  }
  function bfs(computer, i) {
    visited[i] = true
    const q = [computer]
    while (q.length > 0) {
      let v = q.shift()
      for (let j = 0; j < v.length; j++) {
        if ((i !== j) & (v[j] === 1) & !visited[j]) {
          q.push(computers[j])
          visited[j] = true
        }
      }
    }
    // visited 변경
    // result 증가
    result += 1
    //네트워크 수
  }

  return result
}

console.log(
  solution(3, [
    [1, 1, 0],
    [1, 1, 0],
    [0, 0, 1],
  ])
)
console.log(
  solution(3, [
    [1, 1, 0],
    [1, 1, 1],
    [0, 1, 1],
  ])
)

let aaa = [
  [1, 1, 0],
  [1, 1, 1],
  [1, 1, 1],
  [1, 1, 1],
  [1, 1, 1],
  [1, 1, 1],
  [0, 1, 1],
]
let bbb = aaa
aaa[0] = [9, 9, 9]

console.log(aaa)
console.log(bbb)
console.log(aaa == bbb)
