// 그리디 - 곱하기 혹은 더하기
// 코테로치면 레벨1 정답률 70% 정도?
// 그리디 문제는 쉽거나 논리력으로 풀수 있다. 준비 안해도 될듯
function solution(input) {
  let result = ''
  for (char of input) {
    if (result === '') {
      result += char
      continue
    }
    if (char <= '1' || result <= '1') {
      result = (parseInt(result) + parseInt(char)).toString()
    } else {
      result = (parseInt(result) * parseInt(char)).toString()
    }
  }

  return result
}

console.log(solution('02984'))
console.log(solution('567'))
