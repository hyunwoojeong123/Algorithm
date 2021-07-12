function solution(gift_cards, wants) {
  const N = gift_cards.length;
  let answer = N;
  let cnt = Array.from({length: 1000001}, () => 0);
  
  for(let i =0 ; i < N; i++) {
      let num = gift_cards[i];
      cnt[num] += 1;
  }
  for (let i = 0; i < N; i++) {
      let num = wants[i];
      if (cnt[num] > 0) {
          answer -= 1;
          cnt[num] -= 1;
      }
  }
  
  return answer;
}