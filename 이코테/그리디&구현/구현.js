// 풀이를 떠올리긴 쉽지만 소스코드로 옮기기 어려운 문제

function solution(N, moves) {
  let result = Array(N).fill(Array(N).fill(0))
  let position = [0, 0]
  for (ele of moves) {
    if ((ele === 'U') & (position[0] > 0)) {
      position[0] -= 1
    } else if ((ele === 'D') & (position[0] < N - 1)) {
      position[0] += 1
    } else if ((ele === 'R') & (position[1] < N - 1)) {
      position[1] += 1
    } else if ((ele === 'L') & (position[1] > 0)) {
      position[1] -= 1
    }
  }
  return position
}

console.log(solution(5, 'RRRUDD'))
