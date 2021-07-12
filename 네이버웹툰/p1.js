function solution(k, rates) {
  var answer = 0;
  let money = k
  let N = rates.length
  function DFS(money,dollar,idx) {
      // console.log(money,dollar,idx)
      if(idx === N) {
          if(money > answer) {
              answer = money
          }
          return;
      }
      if(dollar === 0) {
          // 사는 경우와 안사는 경우
          DFS(money,dollar,idx+1)
          if(money >= rates[idx]) {
              DFS(money-rates[idx],1,idx+1)
          }
      }
      else {
          // 파는 경우와 안파는 경우
          DFS(money,dollar,idx+1)
          DFS(money+rates[idx],0,idx+1)
      }
  }
  DFS(money,0,0)
  return answer;
}

var arrNumber = new Array(); //배열선언

arrNumber[0] = 1;
arrNumber[1] = 2;
arrNumber[2] = 3;
arrNumber[3] = 4;
arrNumber[4] = 5;	

for(var i=0;i<5;i++){
    arrNumber[i]=i;
}
print(arrNumber)