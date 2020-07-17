
(function( $ ) {

    'use strict';

    /*
	Morris: Stacked
    */
    try {
        Morris.Bar({
            resize: true,
            element: 'morrisStacked',
            data: morrisStackedData,
            xkey: 'y',
            ykeys: ['a', 'b'],
            labels: ['Series A', 'Series B'],
            barColors: ['#0088cc', '#2baab1'],
            fillOpacity: 0.7,
            smooth: false,
            stacked: true,
            hideHover: true
        });
    }
    catch (e) {}


	/*
	Morris: Donut
    */
    try {
        Morris.Donut({
            resize: true,
            element: 'morrisDonut',
            data: morrisDonutData,
            colors: colorsData
        });
    }
    catch (e) {}


	/*
	Liquid Meter
    */
    try {
        $('#meter').liquidMeter({
            shape: 'circle',
            color: '#0088CC',
            background: '#F9F9F9',
            fontSize: '24px',
            fontWeight: '600',
            stroke: '#F2F2F2',
            textColor: '#333',
            liquidOpacity: 0.9,
            liquidPalette: ['#333'],
            speed: 3000,
            animate: !$.browser.mobile
        });
    }
    catch (e) {}

	/*
	Liquid Meter Dark
    */
   try {
        $('#meterDark').liquidMeter({
            shape: 'circle',
            color: '#0088CC',
            background: '#272A31',
            stroke: '#33363F',
            fontSize: '24px',
            fontWeight: '600',
            textColor: '#FFFFFF',
            liquidOpacity: 0.9,
            liquidPalette: ['#0088CC'],
            speed: 3000,
            animate: !$.browser.mobile
        });
    }
    catch (e) {}

}).apply( this, [ jQuery ]);