document.addEventListener('DOMContentLoaded', () => {
    const quizContainer = document.getElementById('quiz');
    const questionContainer = document.getElementById('question-container');
    const nextButton = document.getElementById('next-button');
    const resultsContainer = document.getElementById('results');
    const restartButton = document.getElementById('restart-button');

    let questions = [];
    let currentQuestionIndex = 0;
    let score = 0;

    // Cargar preguntas desde el servidor
    fetch('/get_questions')
        .then(response => response.json())
        .then(data => {
            questions = data;
            shuffleQuestions(); 
            showQuestion();
        });

    // Mezclar las preguntas y las opciones de cada pregunta
    function shuffleQuestions() {
        for (let i = questions.length - 1; i > 0; i--) {
            const j = Math.floor(Math.random() * (i + 1));
            [questions[i], questions[j]] = [questions[j], questions[i]];
        }
        questions.forEach(question => {
            shuffleOptions(question.options); // Mezclar las opciones de cada pregunta
        });
    }

    // Mezclar las opciones de una pregunta
    function shuffleOptions(options) {
        for (let i = options.length - 1; i > 0; i--) {
            const j = Math.floor(Math.random() * (i + 1));
            [options[i], options[j]] = [options[j], options[i]];
        }
    }

    // Mostrar la pregunta actual
    function showQuestion() {
        const question = questions[currentQuestionIndex];
        const options = question.options.map(option => `
            <div class="option" onclick="selectOption(this)">${option}</div>
        `).join('');

        questionContainer.innerHTML = `
            <div class="question slide-in">
                <h3>${question.question}</h3>
                <div class="options">${options}</div>
            </div>
        `;
        nextButton.classList.add('hidden'); // Ocultar el botón "Siguiente" inicialmente
    }

    // Manejar la selección de una opción
    window.selectOption = function(selectedOption) {
        const options = document.querySelectorAll('.option');
        options.forEach(opt => {
            opt.classList.remove('selected', 'correct', 'incorrect'); 
            opt.onclick = null; // Deshabilitar clics en las opciones
        });

        
        selectedOption.classList.add('selected');

        // Verificar si la opción seleccionada es correcta
        if (selectedOption.textContent === questions[currentQuestionIndex].answer) {
            selectedOption.classList.add('correct'); 
            score++;
        } else {
            selectedOption.classList.add('incorrect'); 
           
            options.forEach(opt => {
                if (opt.textContent === questions[currentQuestionIndex].answer) {
                    opt.classList.add('correct'); 
                }
            });
        }

        nextButton.classList.remove('hidden'); 
    };

    // Avanzar a la siguiente pregunta
    nextButton.addEventListener('click', () => {
        currentQuestionIndex++;
        if (currentQuestionIndex < questions.length) {
            showQuestion(); 
        } else {
            showResults(); 
        }
    });

    // Mostrar los resultados finales
    function showResults() {
        quizContainer.classList.add('hidden'); 
        resultsContainer.innerHTML = `Obtuviste ${score} de ${questions.length} respuestas correctas.`;
        resultsContainer.classList.remove('hidden');
        resultsContainer.classList.add('fade-in'); 
        restartButton.classList.remove('hidden'); 
    }

    // Función para reiniciar el quiz
    restartButton.addEventListener('click', () => {
        currentQuestionIndex = 0;
        score = 0;
        shuffleQuestions(); 
        quizContainer.classList.remove('hidden'); 
        resultsContainer.classList.add('hidden');
        restartButton.classList.add('hidden'); 
        showQuestion(); 
    });
});