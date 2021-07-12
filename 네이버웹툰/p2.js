function solution(money, cost) {
  var answer = -1;
  // 1층부터 차례로 검사한다. 얼마나 연속적으로 지을 수 있는지,
  let N = cost.length;
  for(let i = 0; i < N; i++) {
      if(N-i <= answer) {
          break;
      }
      let don = money
      for(let j = i; j < N;j ++) {
          if(don >= cost[j]) {
              don -= cost[j]
          } else {
              if(j-i > answer) {
                  answer = j-i
              }
              break;
          }
      }
      
  }
  return answer;
}