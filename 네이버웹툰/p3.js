const blocks = [
  [[0,0],[1,0],[2,0]],
  [[0,0],[0,1],[0,2]],
  [[0,0],[1,0],[1,1]],
  [[0,0],[1,0],[1,-1]],
  [[0,0],[0,1],[1,1]],
  [[0,0],[0,1],[1,0]],
  ]
function solution(block,board) {
var answer = -1;
let b = blocks[block]
let N = board.length

for(let j = 0; j < N; j++) {
// console.log('j는',j,'일때 검사')
// 떨궜을때 세로위치를 구하자
let garo = j
let sero = 0
for (let i = 0; i < N; i++) {
// console.log('i는',i,'일때')
let can = true
for(let k = 0; k < 3; k++){
  // console.log([each[0]+i,each[1]+j])
  let ii = b[k][0] + i
  let jj = b[k][1] + j
  // console.log(ii,jj)
  if(ii < 0 || ii >= N || jj < 0 || jj >= N || board[ii][jj] == 1){
      can = false;
      break;
  }
}
if(!can) {
  // console.log(i,j,'못 놓음')
  sero = i-1
  break
}
}
if(sero != -1) {
// console.log('세로가로',sero,garo)
b.forEach((each) => {
  let ii = each[0] + sero
  let jj = each[1] + garo
  // console.log(ii,jj)
  board[ii][jj] = 1
})
// console.log(board)
//몇줄 채워졋느지 검사
let cnt = 0
for(let iii = 0; iii < N; iii++) {
  let is_filled = true
  for(let jjj = 0; jjj < N; jjj++) {
      if(board[iii][jjj] == 0) {
          is_filled = false;
          break;
      }    
  }
  if(is_filled) {
      cnt += 1
  }
}
if(cnt > answer) {
  answer = cnt
}
b.forEach((each) => {
  let ii = each[0] + sero
  let jj = each[1] + garo
  board[ii][jj] = 0
})

}
}
return answer;
}