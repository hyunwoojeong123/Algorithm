function solution(needs, r) {
  let answer = 0;
  const N = needs.length;
  const M = needs[0].length;
  const bupums = [];
  for(let i = 0; i < M; i++) {
      bupums.push(i);
  }
  
  function getCombinations(arr,selectNumber) {
      const results = [];
      if (selectNumber === 1) return arr.map((value) => [value]);
      arr.forEach((fixed, index, origin) => {
          const rest = origin.slice(index + 1);
          const combinations = getCombinations(rest, selectNumber - 1);
          const attached = combinations.map((combination) => [fixed, ...combination]); 
          results.push(...attached); 
      });

      return results; // 결과 담긴 results return
  }
  const pos_combs = getCombinations(bupums,r);
  pos_combs.forEach((pos_comb) => {
      const boughted = Array.from({length: 16}, () => 0);
      pos_comb.forEach((p) => {
          boughted[p] = 1;
      })
      let cnt = 0;
      for(let i = 0; i < N; i++) {
          let can_make = true;
          for(let j = 0; j < M; j++) {
              if (needs[i][j] === 1 && !boughted[j]) {
                  can_make = false;
                  break;
              }
          }
          if(can_make) {
              cnt += 1;
          }
      }
      if(cnt > answer) {
          answer = cnt;
      }
  })
  
  return answer;
}