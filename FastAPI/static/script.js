document.addEventListener("DOMContentLoaded", () => {
  fetch("/api/data")
    .then((response) => response.json())
    .then((data) => {
      document.getElementById("result").textContent = data.message;
    })
    .catch((error) => {
      document.getElementById("result").textContent = "데이터 불러오기 실패";
      console.error(error);
    });
});

// Dom이 로드되면, 아래의 함수를 바로 실행해주세요. 이 함수는 fetch를 하게 되어있는데, api의 data를 호출하세용. 응답을 받은 다음에 그걸 json으로 변환하고, 나머지 작업을 해줘라~
