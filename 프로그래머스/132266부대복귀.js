function solution(n, roads, sources, destination) {
  var answer = []
  for (let i = 0; i < sources.length; i++) {
    let distance = 0
    let queue = []
    queue.push(sources[i])
    // BFS 탐색
    while (true) {
      // 현재의 위치
      let cur = queue.shift()
      // 목적지에 도착한 경우
      if (cur === destination) break
      // roads를 탐색
      for (let j = 0; j < roads.length; j++) {
        // 방문 여부
        let visited = new Array(roads.length).fill(false)
        // let roads_cp = JSON.parse(JSON.stringify(roads))
        // 현재에서 이동할 길이 있는 경우
        if (roads[j][0] == cur) {
          queue.push([roads[j][1]])
        } else if (roads[j][1] == cur) {
          queue.push(roads[j][0])
        }
      }
      if (queue.length === 0) {
        distance = -1
        break
      }
      distance += 1
    }
    answer.push(distance)
  }
  return answer
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
