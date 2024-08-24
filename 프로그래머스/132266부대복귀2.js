// 12월 10일: 이틀째 고민하는데 너무 어렵다. 다익스트라 문제: 한 점에서 여러 점까지의 최단 거리
// -1 리턴하는 문제의 경우 Infinity를 활용
// 역으로 출발점에서 각 부대원 까지의 거리를 구한다

function solution(n, roads, sources, destination) {
  const graph = new Array(n + 1).fill(null).map((_) => [])
  for (let [a, b] of roads) {
    graph[a].push(b)
    graph[b].push(a)
  }
  const visited = new Array(n + 1).fill(Infinity)

  const q = [destination]
  visited[destination] = 0
  while (q.length > 0) {
    const idx = q.shift()
    for (let newIdx of graph[idx]) {
      if (visited[idx] + 1 < visited[newIdx]) {
        visited[newIdx] = visited[idx] + 1
        q.push(newIdx)
      }
    }
  }

  return sources.map((v) => {
    if (visited[v] === Infinity) return -1
    else return visited[v]
  })
}

console.log(
  solution(
    5,
    [
      [1, 2],
      [1, 4],
      [2, 4],
      [2, 5],
      [4, 5],
    ],
    [1, 3, 5],
    5
  )
)
