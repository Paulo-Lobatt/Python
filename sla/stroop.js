// array com as palavras do teste
var words = ["vermelho", "azul", "verde", "amarelo"];

// array com as cores das palavras
var colors = ["red", "blue", "green", "yellow"];

// variáveis do teste
var index = 0;
var errors = 0;
var startTime, endTime;

// elementos da página
var question = document.getElementById("question");
var answer = document.getElementById("answer");
var next = document.getElementById("next");

// função que exibe a próxima pergunta
function nextQuestion() {
	// exibe a pergunta atual
	question.innerHTML = "<span style='color:" + colors[index] + "'>" + words[index] + "</span>";

	// limpa a resposta anterior
	answer.value = "";

	// avança para a próxima pergunta
	index++;

	// verifica se o teste acabou
	if (index == words.length) {
		endTime = new Date().getTime();

		// exibe os resultados
		var time = (endTime - startTime) / 1000;
		alert("Teste de Stroop concluído em " + time + " segundos com " + errors + " erros.");

		// reinicia o teste
		index = 0;
		errors = 0;
		nextQuestion();
	}
}

// evento de clique no botão "Próxima"
next.addEventListener("click", function() {
	if (index == 0) {
		// inicia o teste
		startTime = new Date().getTime();
	}

	// verifica se a resposta está correta
	if (answer.value.toLowerCase() != words[index]) {
		errors++;
	}

	// exibe a próxima pergunta
	nextQuestion();
});
