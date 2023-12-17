$(document).ready(function() {
    var canvasVelocimetro1 = document.getElementById('velocimetro1').getContext('2d');
    var canvasVelocimetro2 = document.getElementById('velocimetro2').getContext('2d');
    var canvasGrafico1 = document.getElementById('grafico1').getContext('2d');

    var commonOptions = {
        responsive: true,
        maintainAspectRatio: false
    };

    var lineChartOptions = {
        responsive: true,
        maintainAspectRatio: false,
        scales: {
            x: {
                display: true,
                title: {
                    display: true,
                    text: 'Días'
                }
            },
            y: {
                display: true,
                title: {
                    display: true,
                    text: 'Cantidad'
                }
            }
        }
    };

    var velocimetro1 = new Chart(canvasVelocimetro1, {
        type: 'doughnut',
        data: {
            datasets: [{
                data: [100],
                backgroundColor: 'lightgreen'
            }]
        },
        options: commonOptions
    });

    var velocimetro2 = new Chart(canvasVelocimetro2, {
        type: 'doughnut',
        data: {
            datasets: [{
                data: [50],
                backgroundColor: 'salmon'
            }]
        },
        options: commonOptions
    });

    var grafico1 = new Chart(canvasGrafico1, {
        type: 'line',
        data: {
            labels: ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes'],
            datasets: [{
                label: 'Time-lapse',
                data: [8, 10, 12, 14, 17],
                borderColor: 'lightblue',
                borderWidth: 1
            }]
        },
        options: lineChartOptions
    });

    window.grafico1 = grafico1;

    function obtenerCantidadModulos() {
        $.ajax({
            type: 'GET',
            url: '/api/cantidad_modulos/',
            success: function(data) {
                $('#cantidadModulos1').text(data.cantidad_encendidos);
                $('#cantidadModulos2').text(data.cantidad_apagados);
                actualizarGrafico(data.cantidad_encendidos, data.cantidad_apagados);
            },
            error: function(error) {
                console.error('Error al obtener la cantidad de módulos:', error);
            }
        });
    }

    obtenerCantidadModulos();
    setInterval(obtenerCantidadModulos, 10000);

    function actualizarGrafico(cantidadEncendidos, cantidadApagados) {
        var canvasGrafico = document.getElementById('grafico1').getContext('2d');
        
        var dataGrafico = {
            datasets: [{
                data: [cantidadEncendidos, cantidadApagados],
                backgroundColor: ['lightgreen', 'salmon']
            }],
            labels: ['Encendidos', 'Apagados']
        };

        var donutChartOptions = {
            responsive: true,
            maintainAspectRatio: false
        };

        if (window.grafico1) {
            window.grafico1.destroy();
        }
        window.grafico1 = new Chart(canvasGrafico, {
            type: 'doughnut',
            data: dataGrafico,
            options: donutChartOptions
        });
    }
});