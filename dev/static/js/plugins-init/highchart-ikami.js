// console.log(str_tatakelola);
var spider_result = JSON.parse(spider_ikami_json).map(i=>Number(i));
// console.log(spider_result);

Highcharts.chart('highchart-radar-ikami', {

    chart: {
        polar: true
    },

    title: {
        text: 'IKAMI Chart'
    },

    pane: {
        startAngle: 0,
        endAngle: 360
    },

    xAxis: {
        tickInterval: 1,
        min: 0,
        max: 5,
        lineWidth: 0,
        labels: {
            formatter: function() {
            
                let label;
                switch (this.value) {
                case 0:
                    label = 'Tata Kelola';
                    break;
                case 1:
                    label = 'Pengelolaan Risiko';
                    break;
                case 2:
                    label = 'Kerangka Kerja Keamanan Informasi';
                    break;
                case 3:
                    label = 'Pengelolaan Aset';
                    break;
                case 4:
                    label = 'Teknologi dan Keamanan Informasi';
                    break;
                }
                
                return label;
            }
        }
    },

    yAxis: {
        min: 0,
        max: 150,
        tickInterval: 30,
       	gridLineInterpolation : 'polygon',
    },

    series: [{
        type: 'line',
        name: 'Score',
        data: spider_result
    }]
});