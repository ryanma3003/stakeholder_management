

(function($) {
    /* "use strict" */
	
 var dlabChartlist = function(){
	
	var screenWidth = $(window).width();
    var json = JSON.parse(pie_ttis_json).map(i=>Number(i));
	
	
	var pieChart3 = function(){
		 var options = {
          series: json,
          chart: {
          type: 'donut',
		  height:230
        },
		dataLabels:{  
			enabled: false,
			// enabledOnSeries: json,
			// formatter: function (val, opts) {
			// 	return val
			// },
			// textAnchor: 'middle',
			// distributed: false,
			// offsetX: 0,
			// offsetY: 0,
			// style: {
			// 	fontSize: '14px',
			// 	fontFamily: 'Poppins, sans-serif',
			// 	fontWeight: 'bold',
			// 	colors: ['#fff'],
			// },
		},
		stroke: {
          width: 0,
        },
		colors:['#F6AD2E', 'var(--primary)', '#412EFF', '#f72b50', '#68e365'],
		legend: {
              position: 'bottom',
			  show:false
            },
        responsive: [{
          breakpoint: 768,
          options: {
           chart: {
			  height:200
			},
          }
        }]
        };

        var chart = new ApexCharts(document.querySelector("#pieChart3"), options);
        chart.render();
    
	}
	
	
 
	/* Function ============ */
		return {
			init:function(){
			},
			
			
			load:function(){
				pieChart3();
				
			},
			
			resize:function(){
			}
		}
	
	}();

	
		
	jQuery(window).on('load',function(){
		setTimeout(function(){
			dlabChartlist.load();
		}, 1000); 
		
	});

     

})(jQuery);