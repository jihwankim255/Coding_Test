function solution(msg) {
  var answer = []
  // 사전 초기화
  const alphabet = {}
  for (var i = 1; i <= 26; i++) {
    const char = String.fromCharCode('A'.charCodeAt(0) + i - 1)
    alphabet[i] = char
  }
  while (msg.length > 0) {
    // 사전에서 현재 입력과 일치하는 가장 긴 문자열을 찾는다
    let longest = msg
    let longIndex = 0

    for (const key in alphabet) {
      if (alphabet[key] === longest) {
        longIndex = key
        console
        break
      } else {
        longest = longest.slice(0, -1)
      }
    }

    // 색인 번호를 출력
    answer.push(longIndex)
    msg = msg.slice(longest.length)
    console.log('msg: ', msg)
    // 사전에 등록
    if (msg.length > 0) {
      alphabet[i] = longest + msg.slice(0, 1)
      i += 1
    }
  }
  return answer
}
console.log(solution('KAKAO'))
