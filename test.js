const Http = new XMLHttpRequest();
const url = "https://naver.com";

Http.open("GET",url)
// Http.send();
Http.onreadystatechange = (e) => {
	console.log(Http.responseText);
};