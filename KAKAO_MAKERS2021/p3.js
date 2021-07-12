function solution(n, passenger, train) {
  let answer = [1,0];
  const start = 1;
  const link = Array.from({length:n+1}, () => Array.from({length:n+1}, () => false))
  train.forEach(([st,ed]) => {
      // console.log(st,ed);
      link[st][ed] = true;
      link[ed][st] = true;
  })
  // console.log(link);
  function find_path(start,end) {
      let visited = Array.from({length:n+1}, ()=>false);
      let q = []
      
      q.push([start,[start]]);
      visited[start] = true;
      while(q.length !== 0) {
          const obj = q.shift();
          const node = obj[0];
          const path = obj[1];
          // console.log('node,path:',node,path)
          if(node === end) {
              visited = [];
              return path;
          }
          for(let i = 1; i <= n; i++) {
              if(link[node][i] && !visited[i]) {
                  q.push([i,[...path,i]]);
                  visited[i] = true;
              }
          }
      }
  }
  for(let end = 2; end <= n; end++) {
      // 경로 구하기
      const path = find_path(start,end)
      // console.log('path:',path)
      let userCnt = 0;
      path.forEach((stop) => {
          userCnt += passenger[stop-1];
      })
      if(userCnt >= answer[1]) {
          answer = [end,userCnt];
      }
  }
  //[종착지,총 유저]
  return answer;
}