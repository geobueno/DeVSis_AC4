Highcharts.chart('container', {
    title: {
        text: ''
    },
    xAxis: {
        categories: ['Variável 1', 'Variável 2', 'Variável 3', 'Variável 4']
    },
    labels: {
        items: [{
            html: '',
            style: {
                left: '50px',
                top: '18px',
                color: (Highcharts.theme && Highcharts.theme.textColor) || 'black'
            }
        }]
    },
    series: [{
        type: 'column',
        name: 'Objeto A',
        data: [3, 2, 1, 3]
    }, {
        type: 'column',
        name: 'Objeto B',
        data: [2, 3, 5, 7]
    }, {
        type: 'column',
        name: 'Objeto C',
        data: [4, 3, 3, 9]
    }, {
        type: 'spline',
        name: 'Média',
        data: [3, 2.67, 3, 6.33],
        marker: {
            lineWidth: 2,
            lineColor: Highcharts.getOptions().colors[3],
            fillColor: 'white'
        }
    }, {
        type: 'pie',
        name: 'Total consumption',
        data: [{
            name: 'Maria',
            y: 13,
            color: Highcharts.getOptions().colors[0]
        }, {
            name: 'João',
            y: 23,
            color: Highcharts.getOptions().colors[1]
        }, {
            name: 'Pedro',
            y: 19,
            color: Highcharts.getOptions().colors[2]
        }],
        center: [100, 80],
        size: 100,
        showInLegend: false,
        dataLabels: {
            enabled: false
        }
    }]
});